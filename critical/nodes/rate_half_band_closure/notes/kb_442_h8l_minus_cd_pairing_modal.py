#!/usr/bin/env python3
"""Bounded exact H8-L-minus / xi=cD pairing pilot on Modal.

Each shard tests one of the 15 residual perfect matchings after imposing the
forced product cD=1.  A UNIT result is exact over QQ.  NONUNIT and timeout
rows are retained as frontier data; neither is interpreted as a packet.
"""

from __future__ import annotations

import itertools
import json

import modal


app = modal.App("kb-442-h8l-minus-cd-pairing")
image = modal.Image.debian_slim(python_version="3.12").pip_install("sympy==1.13.3")


def matchings(items: tuple[int, ...]):
    if not items:
        yield ()
        return
    first = items[0]
    for index in range(1, len(items)):
        second = items[index]
        remainder = items[1:index] + items[index + 1:]
        for tail in matchings(remainder):
            yield ((first, second),) + tail


MATCHINGS = tuple(matchings(tuple(range(6))))


@app.function(image=image, cpu=1.0, memory=512, timeout=60)
def exact_pairing(payload: dict[str, int]) -> dict[str, object]:
    import resource
    import time

    import sympy as sp

    pairing_index = payload["pairing"]
    sigma = payload["sigma"]
    ell, b, e, f = sp.symbols("ell b e f")
    c = (b - 2) * (ell**3 - ell + 1)
    d = 1 / c
    relation = ell**4 + 1
    b_gate = b**2 - b*ell**3 + b*ell - b + 1

    # On H8-L,tau=-1 the common factor b+1 can be removed from the
    # cross-product involution coefficients.
    gamma = b + c
    alpha = -b*c*(b - 1)
    beta = b**2*c*(b + c)

    products = (c*e, sigma*d*e, d*f, -d*f, e*f, -e*f)
    equations = []
    for left, right in MATCHINGS[pairing_index]:
        y, z = products[left], products[right]
        rational = gamma*y*z - alpha*(y + z) - beta
        equations.append(sp.factor(sp.together(rational).as_numer_denom()[0]))

    started = time.monotonic()
    basis = sp.groebner(
        (relation, b_gate, *equations),
        f, e, b, ell,
        order="grevlex",
        method="f5b",
    )
    unit = len(basis.polys) == 1 and basis.polys[0].as_expr() == 1
    elapsed = time.monotonic() - started
    peak_kib = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return {
        "sigma": sigma,
        "pairing": pairing_index,
        "pairs": MATCHINGS[pairing_index],
        "status": "UNIT" if unit else "NONUNIT",
        "basis_size": len(basis.polys),
        "elapsed_seconds": round(elapsed, 3),
        "peak_kib": peak_kib,
        "basis_head": [str(poly.as_expr()) for poly in basis.polys[:3]],
    }


@app.local_entrypoint()
def main() -> None:
    payloads = [
        {"sigma": sigma, "pairing": pairing}
        for sigma in (-1, 1)
        for pairing in range(len(MATCHINGS))
    ]
    rows = []
    for payload, result in zip(
        payloads,
        exact_pairing.map(payloads, order_outputs=True, return_exceptions=True),
    ):
        if isinstance(result, BaseException):
            rows.append({
                **payload,
                "pairs": MATCHINGS[payload["pairing"]],
                "status": "ERROR",
                "error": f"{type(result).__name__}: {result}",
            })
        else:
            rows.append(result)
        print(json.dumps(rows[-1], sort_keys=True), flush=True)

    summary = {
        status: sum(row["status"] == status for row in rows)
        for status in ("UNIT", "NONUNIT", "ERROR")
    }
    print("KB_442_H8L_MINUS_CD_PAIRING_SUMMARY " + json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    raise SystemExit("run with: modal run kb_442_h8l_minus_cd_pairing_modal.py")
