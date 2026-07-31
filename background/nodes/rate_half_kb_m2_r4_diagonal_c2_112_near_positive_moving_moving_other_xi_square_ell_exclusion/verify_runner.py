#!/usr/bin/env python3
"""Hash-pinned shard dispatcher for the other-xi square-ell certificate."""
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
    "audit": NOTES / "kb_c2_112_near_moving_other_square_ell_audit.py",
}
EXPECTED_HELPERS = {
    "shared": "deb385db95bf5737a7eef419af359714829c19b5a92a63d087f0fc3451afd32c",
    "source": "ef0ddd499a403abdc34b5fa6e83cbb38a444672c6e8fac7d59ea865d12ec19d1",
    "components": "3500ab7b665436113cd4a3ad5afb6d35a644bfcbf2407b240b2a5aa799cd21d0",
    "pairs": "9b7b2f40d572d038669ac75ca370282557dca86f0b63f4510c59887d125a1bf7",
    "classify": "260b2431c04af60947232f8cd0c482ebbfc84440b40bf255b8b4a6b24f85e782",
    "audit": "ec65696d2fad3e6f00be07d4cd759926b71db29064f0519ba06989319ca176d0",
}
EXPECTED_DATA = {
    "kb_c2_112_other_square-ell_c_components.json": "5c229362d7c88352af1d131744a30583a7e468faa5b12ab216808b4ccc8370d0",
    "kb_c2_112_other_square-ell_c_cores.json": "24bc8bb80cbc071ce1da51921ae015f8e3219b71b65455221a3ec596d3d8368a",
    "kb_c2_112_other_square-ell_d_components.json": "c811f8aa8d778347e58e8cd1af1c2889157d93feff3995af8f1a70d100900e2c",
    "kb_c2_112_other_square-ell_d_cores.json": "2d21a12aad0701f8cd083654f2059427ff0c7d547bb8bbf75a6841b0a1407a2b",
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
            str(HELPERS["source"]), "square-ell", f"cache-{root}",
            "--cache-dir", str(temporary),
        ]
        runpy.run_path(str(HELPERS["source"]), run_name="__main__")
        name = f"kb_c2_112_other_square-ell_{root}_cores.json"
        if (temporary / name).read_bytes() != (DATA / name).read_bytes():
            raise RuntimeError(f"source checkpoint: {root}")
    print(f"KB_C2_112_NEAR_MOVING_OTHER_SQUARE_ELL_SOURCE_{root.upper()}_PRIMARY_PASS")


def components(root: str) -> None:
    check_hashes()
    with tempfile.TemporaryDirectory() as directory:
        temporary = Path(directory)
        core_name = f"kb_c2_112_other_square-ell_{root}_cores.json"
        shutil.copyfile(DATA / core_name, temporary / core_name)
        sys.argv = [
            str(HELPERS["components"]), "square-ell", root,
            "cache-components", "--cache-dir", str(temporary),
        ]
        runpy.run_path(str(HELPERS["components"]), run_name="__main__")
        name = f"kb_c2_112_other_square-ell_{root}_components.json"
        if (temporary / name).read_bytes() != (DATA / name).read_bytes():
            raise RuntimeError(f"component checkpoint: {root}")
    print(f"KB_C2_112_NEAR_MOVING_OTHER_SQUARE_ELL_COMPONENTS_{root.upper()}_PRIMARY_PASS")


def pair(left: int, right: int) -> None:
    check_hashes()
    sys.argv = [
        str(HELPERS["pairs"]), "square-ell", str(left), str(right),
        "--cache-dir", str(DATA), "--prove",
    ]
    runpy.run_path(str(HELPERS["pairs"]), run_name="__main__")


def classify(index: int) -> None:
    check_hashes()
    sys.argv = [
        str(HELPERS["classify"]), "square-ell", str(index),
        "--cache-dir", str(DATA),
    ]
    runpy.run_path(str(HELPERS["classify"]), run_name="__main__")
    print(f"KB_C2_112_NEAR_MOVING_OTHER_SQUARE_ELL_CLASSIFY_{index}_PRIMARY_PASS")


def audit(mode: str) -> None:
    check_hashes()
    sys.argv = [
        str(HELPERS["audit"]), mode, "--data-dir", str(DATA),
    ]
    runpy.run_path(str(HELPERS["audit"]), run_name="__main__")


if __name__ == "__main__":
    check_hashes()
    print("KB_C2_112_NEAR_MOVING_OTHER_SQUARE_ELL_DISPATCH_PASS")
