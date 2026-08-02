#!/usr/bin/env python3
"""Independent certificate verification: sympy resultant + Bareiss + descent."""
import json, os, sys
sys.path.insert(0, "/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260802/c1_norm_ladder/scripts")
from norm_core import norm_bareiss, norm_descent_py
from sympy import symbols, Poly, resultant, ZZ

def check(d):
    x = symbols('x')
    N = len(d)
    f = Poly(list(reversed(d)), x, domain=ZZ)
    m = Poly([1] + [0]*(N-1) + [1], x, domain=ZZ)
    return {"f": d, "N": N, "weight": sum(1 for c in d if c),
            "sympy_resultant": str(resultant(f, m)),
            "bareiss": str(norm_bareiss(d)),
            "descent": str(norm_descent_py(d))}

if __name__ == "__main__":
    out = []
    for path in sys.argv[1:]:
        rec = json.load(open(path))
        c = check(rec["argmax_f"])
        c["source"] = path
        c["claimed_max"] = rec.get("max_norm", rec.get("max_norm_exact"))
        c["all_agree"] = (c["sympy_resultant"] == c["bareiss"] == c["descent"]
                          == c["claimed_max"])
        out.append(c)
    print(json.dumps(out, indent=1))
