# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy==2.4.2", "trimesh==4.11.2", "fast-simplification==0.1.13"]
# ///
"""Export the reference URDF's zero pose as reduced browser geometry."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from xml.etree import ElementTree as ET

import numpy as np
import trimesh
from numpy.typing import NDArray

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path(
    "references/toddlerbot/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.urdf"
)


def origin_matrix(origin: ET.Element | None) -> NDArray[np.float64]:
    if origin is None:
        return np.eye(4)
    rpy = [float(value) for value in origin.get("rpy", "0 0 0").split()]
    result = trimesh.transformations.euler_matrix(*rpy, axes="sxyz")
    result[:3, 3] = [float(value) for value in origin.get("xyz", "0 0 0").split()]
    return result


def link_transforms(robot: ET.Element) -> dict[str, NDArray[np.float64]]:
    links = {element.attrib["name"] for element in robot.findall("link")}
    joints = list(robot.findall("joint"))
    children = {joint.find("child").attrib["link"] for joint in joints}
    transforms = {name: np.eye(4) for name in links - children}
    while joints:
        pending = []
        for joint in joints:
            parent = joint.find("parent").attrib["link"]
            child = joint.find("child").attrib["link"]
            if parent not in transforms:
                pending.append(joint)
                continue
            transforms[child] = transforms[parent] @ origin_matrix(joint.find("origin"))
        if len(pending) == len(joints):
            raise ValueError("URDF contains a cycle or an unresolved parent link")
        joints = pending
    if links != transforms.keys():
        raise ValueError("URDF link tree is incomplete")
    return transforms


def export_model() -> dict:
    urdf = ROOT / SOURCE
    robot = ET.parse(urdf).getroot()
    transforms = link_transforms(robot)
    materials = {}
    for material in robot.findall("material"):
        color = material.find("color")
        if color is not None:
            rgb = [float(x) for x in color.attrib["rgba"].split()[:3]]
            materials[material.attrib["name"]] = "#" + "".join(
                f"{round(channel * 255):02x}" for channel in rgb
            )
    meshes = []
    bounds = []
    source_count = 0
    for link in robot.findall("link"):
        for visual in link.findall("visual"):
            geometry = visual.find("geometry/mesh")
            if geometry is None:
                raise ValueError("Expected mesh geometry for every reference visual")
            source = urdf.parent / geometry.attrib["filename"]
            mesh = trimesh.load_mesh(source)
            source_count += len(mesh.faces)
            mesh = trimesh.Trimesh(
                vertices=np.round(mesh.vertices / 0.001) * 0.001,
                faces=mesh.faces,
            )
            mesh.update_faces(mesh.nondegenerate_faces())
            mesh.update_faces(mesh.unique_faces())
            mesh.remove_unreferenced_vertices()
            if len(mesh.faces) > 1200:
                mesh = mesh.simplify_quadric_decimation(face_count=1200, aggression=10)
                mesh.update_faces(mesh.nondegenerate_faces())
                mesh.remove_unreferenced_vertices()
            scale = [float(x) for x in geometry.get("scale", "1 1 1").split()]
            mesh.apply_scale(scale)
            mesh.apply_transform(
                transforms[link.attrib["name"]] @ origin_matrix(visual.find("origin"))
            )
            material = visual.find("material")
            material_name = material.get("name", "") if material is not None else ""
            meshes.append(
                {
                    "name": link.attrib["name"],
                    "source": str(source.relative_to(ROOT)),
                    "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                    "positions": np.round(
                        mesh.vertices[mesh.faces].reshape(-1), 6
                    ).tolist(),
                    "normals": np.round(
                        np.repeat(mesh.face_normals, 3, axis=0).reshape(-1), 5
                    ).tolist(),
                    "color": materials.get(material_name, "#b6c6ce"),
                }
            )
            bounds.append(mesh.bounds)
    return {
        "name": "ToddlerBot 2xc",
        "source": str(SOURCE),
        "sourceSha256": hashlib.sha256(urdf.read_bytes()).hexdigest(),
        "pose": "URDF zero joint angles",
        "units": "m",
        "upAxis": "z",
        "vertexGridMm": 1,
        "note": "Reduced reference visual geometry. This static pose is not a simulated standing result or an Alfred fabrication model.",
        "originalTriangles": source_count,
        "triangles": sum(len(mesh["positions"]) // 9 for mesh in meshes),
        "bounds": {
            "min": np.min([bound[0] for bound in bounds], axis=0).tolist(),
            "max": np.max([bound[1] for bound in bounds], axis=0).tolist(),
        },
        "meshes": meshes,
    }


if __name__ == "__main__":
    target = ROOT / "preview/assets/model.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    model = export_model()
    target.write_text(json.dumps(model, separators=(",", ":")) + "\n")
    print(
        f"Exported {len(model['meshes'])} meshes, {model['triangles']} triangles to {target}"
    )
