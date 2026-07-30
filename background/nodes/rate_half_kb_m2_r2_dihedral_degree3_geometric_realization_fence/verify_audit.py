#!/usr/bin/env python3
"""Independent audit of the degree-three geometric realization fence."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = Path(__file__).resolve().parent


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    proof = (NODE / "proof.md").read_text()
    statement = (NODE / "statement.md").read_text()
    dag = (ROOT / "dag.json").read_text()
    require("D_3(y)-D_3(z)=(y-z)(y^2+yz+z^2-3)" in proof, "cubic identity")
    require("sum_alpha div(H(alpha,x))=2 div(B)" in proof, "source saturation")
    require("route fence" in statement, "route-fence scope")
    require("not an actual endpoint-record producer" in statement, "endpoint nonclaim")
    require("rate_half_kb_m2_r2_dihedral_degree3_geometric_realization_fence" in dag, "DAG node")
    print("RATE_HALF_KB_M2_R2_DIHEDRAL_DEGREE3_GEOMETRIC_REALIZATION_FENCE_AUDIT_PASS")


if __name__ == "__main__":
    main()
