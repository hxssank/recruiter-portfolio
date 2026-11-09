import hashlib
import importlib.util
import json
from pathlib import Path
from xml.etree import ElementTree as ET

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "export_model", ROOT / "scripts/export_model.py"
)
EXPORT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(EXPORT)


def test_child_origin_rotates_in_parent_frame():
    robot = ET.fromstring("""<robot>
      <link name="base"/><link name="arm"/><link name="hand"/>
      <joint name="hand" type="fixed">
        <parent link="arm"/><child link="hand"/><origin xyz="1 0 0"/>
      </joint>
      <joint name="arm" type="fixed">
        <parent link="base"/><child link="arm"/>
        <origin xyz="2 3 4" rpy="0 0 1.5707963267948966"/>
      </joint>
    </robot>""")
    transforms = EXPORT.link_transforms(robot)
    np.testing.assert_allclose(transforms["hand"][:3, 3], [2, 4, 4])


def test_cyclic_link_graph_fails():
    robot = ET.fromstring("""<robot>
      <link name="a"/><link name="b"/>
      <joint><parent link="a"/><child link="b"/></joint>
      <joint><parent link="b"/><child link="a"/></joint>
    </robot>""")
    with pytest.raises(ValueError, match="cycle"):
        EXPORT.link_transforms(robot)


def test_export_matches_sources_and_contains_finite_geometry():
    model = json.loads((ROOT / "preview/assets/model.json").read_text())
    assert (
        model["sourceSha256"]
        == hashlib.sha256((ROOT / model["source"]).read_bytes()).hexdigest()
    )
    assert len(model["meshes"]) == 45
    assert model["triangles"] < 100_000
    assert model["originalTriangles"] > model["triangles"]
    for mesh in model["meshes"]:
        assert (
            mesh["sha256"]
            == hashlib.sha256((ROOT / mesh["source"]).read_bytes()).hexdigest()
        )
        positions = np.array(mesh["positions"]).reshape(-1, 3)
        normals = np.array(mesh["normals"]).reshape(-1, 3)
        assert positions.shape == normals.shape
        assert len(positions) % 3 == 0
        assert np.isfinite(positions).all() and np.isfinite(normals).all()
        np.testing.assert_allclose(np.linalg.norm(normals, axis=1), 1, atol=2e-5)
    height = model["bounds"]["max"][2] - model["bounds"]["min"][2]
    assert 0.52 < height < 0.55
