# Alfred

Runtime validation and simulation experiments for a small humanoid robot, built on [ToddlerBot](https://github.com/hshi74/toddlerbot). Alfred's contribution here is a reviewable patch set, regression tests, and a URDF-to-browser geometry exporter. The upstream robot platform, mechanical models, and original software belong to the ToddlerBot contributors.

This repository is a robotics development project. It does not contain a demonstrated household robot, trained Alfred policy, or validated hardware build.

## What changed

| Area | Local contribution | How to inspect it |
| --- | --- | --- |
| Robot messages | Replaces network pickle with bounded JSON and typed-array payloads. Remote peers require an HMAC key. Receivers reject invalid fields, tampering, stale packets, and replayed messages. | `comm_utils.py` changes and `test_alfred_comms.py` in the patch |
| Motor interface | Defines signed register conversion, fixes client cleanup iteration, uses a boolean torque-selection mask, and validates motor names, shape, finite values, and configured limits before writes. | Dynamixel C++ changes, `real_world.py`, and `test_alfred_telemetry.py` |
| Policy launch | Selects fixed-base models before terrain generation, checks model layout, aligns diffusion checkpoint arguments, and loads robot-specific preparation motions. | Policy and simulation changes plus `test_alfred_policy_regressions.py` |
| Recording | Gives each recorder a separate session directory and publishes complete episode files atomically. Failed saves retain samples for retry. | `dataset_utils.py` and `test_alfred_dataset_logger.py` |
| Training configuration | Makes the default environment count equal batch size multiplied by minibatches. | `ppo_config.py`; this is an arithmetic correction, not a training result |
| Model export | Traverses URDF link transforms, reduces reference visual meshes, and exports geometry with source hashes. | [Exporter](scripts/export_model.py) and [tests](tests/test_model_export.py) |

All runtime changes are in [0001-runtime-validation.patch](patches/0001-runtime-validation.patch). [upstream.json](upstream.json) records the base commit, modified files, and patch checksum. The original personal planning documents and nested upstream checkout are not included.

## Reconstruct the source

Use Git and Python 3.12. Run these commands from the Alfred repository root:

```bash
git clone --filter=blob:none --no-checkout https://github.com/hshi74/toddlerbot.git references/toddlerbot
git -C references/toddlerbot checkout --detach e337f3b177b4b53abff70b31d1695a7b66cc6d2e
git -C references/toddlerbot apply --check ../../patches/0001-runtime-validation.patch
git -C references/toddlerbot apply ../../patches/0001-runtime-validation.patch
```

The pinned upstream tree contains about 1.2 GB of files before Git history. This repository stores the patch and exporter only.

The exact base matters. Applying the patch to a newer upstream checkout can fail or change behavior. `references/` is ignored so the complete upstream source does not become a second copy in this repository.

## Run the source regressions

Use a separate Python environment for the robotics tests. The test selection includes headless MuJoCo checks, fake motor controllers, a local authenticated socket exchange, and C++ sanitizer programs. It does not open robot serial ports or download learned checkpoints.

```bash
python -m venv .venv
.venv/bin/python -m pip install -r requirements-test.txt
cd references/toddlerbot
../../.venv/bin/python -m pytest -q tests/test_alfred_policy_regressions.py tests/test_run_policy.py tests/test_alfred_comms.py tests/test_alfred_telemetry.py tests/test_alfred_dataset_logger.py
```

Local verification on November 9, 2026 passed all 94 selected runtime tests in 44.82 seconds on macOS with Python 3.12.15. This includes the C++ sanitizer tests.

A C++ compiler is needed for the telemetry sanitizer tests. Pytest skips those tests if no compiler is available. The stand tests advance free-base and fixed-base simulations for 15 control steps, about 0.3 seconds. This is a regression check, not a standing-duration or balance qualification.

## Export the reference geometry

The exporter uses a different NumPy version from the upstream robotics stack. Create a separate environment from the Alfred root:

```bash
python -m venv .venv-model
.venv-model/bin/python -m pip install -r requirements-model.txt
.venv-model/bin/python scripts/export_model.py
.venv-model/bin/python -m pytest -q tests/test_model_export.py
```

The output is `preview/assets/model.json`. It contains reduced visual meshes at zero joint angles, link transforms, and source hashes. It is not a simulated standing pose, collision model, or fabrication-ready Alfred design. The verified export contains 45 meshes and 76,679 triangles; all three exporter tests passed. Generated geometry stays out of Git.

## Known boundaries

Both message peers must use the new protocol. HMAC authenticates messages but does not encrypt them. Episode writes are atomic only after saving; process failure can still lose an unsaved episode in memory.

Upstream motor startup still enables torque automatically. Independent arming, sensor readiness checks, stale-sensor rejection, bounded shutdown, and an independent stop mechanism remain open. No physical hardware, trained-policy inference, GPU training, 60-second standing gate, or household task has been validated by this project.

The [verification workflow](../../.github/workflows/alfred.yml) reconstructs the pinned source and runs the two test environments separately. A workflow definition is not itself a passing CI result.

## Attribution

ToddlerBot's MIT license and copyright notice for Haochen Shi are retained in [LICENSE](LICENSE). The patch modifies that upstream software. The URDF exporter uses ToddlerBot reference geometry only after the user fetches the pinned source.

[Recruiter portfolio](https://github.com/hxssank/recruiter-portfolio)
