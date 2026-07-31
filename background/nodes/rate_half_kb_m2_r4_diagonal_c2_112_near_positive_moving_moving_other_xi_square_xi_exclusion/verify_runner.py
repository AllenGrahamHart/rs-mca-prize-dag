#!/usr/bin/env python3
"""Hash-pinned shard dispatcher for the other-xi square-xi certificate."""
import hashlib
import runpy
import shutil
import sys
import tempfile
from pathlib import Path

NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
DATA = NODE / "data"
NOTES = ROOT / "critical/nodes/rate_half_band_closure/notes"
HELPERS = {
    "shared": NOTES / "kb_c2_112_near_moving_template_probe.py",
    "source": NOTES / "kb_c2_112_near_moving_other_probe.py",
    "components": NOTES / "kb_c2_112_near_moving_other_cached_eliminate.py",
    "pairs": NOTES / "kb_c2_112_near_moving_other_cached_pairs.py",
    "classify": NOTES / "kb_c2_112_near_moving_other_cached_classify.py",
    "audit": NOTES / "kb_c2_112_near_moving_other_square_xi_audit.py",
}
EXPECTED_HELPERS = {
    "shared": "deb385db95bf5737a7eef419af359714829c19b5a92a63d087f0fc3451afd32c",
    "source": "80ff089f61471daf1299641fcd59e9c8a9be40163a8f678a6cc4e497f13e62b3",
    "components": "70951412e8238aa7997c5d08b8b268aed0e6e0dfc5cf800a448011472a5295b1",
    "pairs": "ef1d943cf078505c5573d73821318d00ca7e82bfeae8827848565cbe45f1f38d",
    "classify": "f2b1863dcde5a4fed8505ccfcbea96382d9cdaacc9434dbb39724d3443739202",
    "audit": "5915c95e5ab60e40fe6657c0ca95d1c4371daf54eaa259f917be4dd961dd198e",
}
EXPECTED_DATA = {
    "kb_c2_112_other_square-xi_c_components.json": "788df956cfb0e7826dfb2d8a2aae6d95fde30abebccb94837c197169655a033b",
    "kb_c2_112_other_square-xi_c_cores.json": "3dbb0d1a141fab677b21c53aa4ecf0ce539a2e6b979749ca2d9d7bb6e7d3d70a",
    "kb_c2_112_other_square-xi_d_components.json": "f96ba23d6c50c0268728a8fa35ba2f3e9a9cf0428423f6575e208f85916b77b9",
    "kb_c2_112_other_square-xi_d_cores.json": "93f1eec3a2dbda194a1d361ecef918c73b3e5c8d7891bfa4a401143938226cd0",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_hashes() -> None:
    for key, path in HELPERS.items():
        if sha(path) != EXPECTED_HELPERS[key]:
            raise RuntimeError(f"helper hash: {key}")
    for name, expected in EXPECTED_DATA.items():
        if sha(DATA / name) != expected:
            raise RuntimeError(f"data hash: {name}")


def source(root: str) -> None:
    check_hashes()
    with tempfile.TemporaryDirectory() as directory:
        temporary = Path(directory)
        sys.argv = [
            str(HELPERS["source"]), "square-xi", f"cache-{root}",
            "--cache-dir", str(temporary),
        ]
        runpy.run_path(str(HELPERS["source"]), run_name="__main__")
        name = f"kb_c2_112_other_square-xi_{root}_cores.json"
        if (temporary / name).read_bytes() != (DATA / name).read_bytes():
            raise RuntimeError(f"source checkpoint: {root}")
    print(f"KB_C2_112_NEAR_MOVING_OTHER_SQUARE_XI_SOURCE_{root.upper()}_PRIMARY_PASS")


def components(root: str) -> None:
    check_hashes()
    with tempfile.TemporaryDirectory() as directory:
        temporary = Path(directory)
        core_name = f"kb_c2_112_other_square-xi_{root}_cores.json"
        shutil.copyfile(DATA / core_name, temporary / core_name)
        sys.argv = [
            str(HELPERS["components"]), "square-xi", root,
            "cache-components", "--cache-dir", str(temporary),
        ]
        runpy.run_path(str(HELPERS["components"]), run_name="__main__")
        name = f"kb_c2_112_other_square-xi_{root}_components.json"
        if (temporary / name).read_bytes() != (DATA / name).read_bytes():
            raise RuntimeError(f"component checkpoint: {root}")
    print(f"KB_C2_112_NEAR_MOVING_OTHER_SQUARE_XI_COMPONENTS_{root.upper()}_PRIMARY_PASS")


def pair(left: int, right: int) -> None:
    check_hashes()
    sys.argv = [
        str(HELPERS["pairs"]), "square-xi", str(left), str(right),
        "--cache-dir", str(DATA), "--prove",
    ]
    runpy.run_path(str(HELPERS["pairs"]), run_name="__main__")


def classify(index: int) -> None:
    check_hashes()
    sys.argv = [
        str(HELPERS["classify"]), "square-xi", str(index),
        "--cache-dir", str(DATA),
    ]
    runpy.run_path(str(HELPERS["classify"]), run_name="__main__")
    print(f"KB_C2_112_NEAR_MOVING_OTHER_SQUARE_XI_CLASSIFY_{index}_PRIMARY_PASS")


def audit(mode: str) -> None:
    check_hashes()
    sys.argv = [
        str(HELPERS["audit"]), mode, "--data-dir", str(DATA),
    ]
    runpy.run_path(str(HELPERS["audit"]), run_name="__main__")


if __name__ == "__main__":
    check_hashes()
    print("KB_C2_112_NEAR_MOVING_OTHER_SQUARE_XI_DISPATCH_PASS")
