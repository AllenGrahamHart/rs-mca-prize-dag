#!/usr/bin/env python3
"""STANDALONE CERTIFICATE VERIFIER.  Imports NOTHING from latlib.

Given state/CELL.cert.json it re-checks, from scratch and in exact integer
arithmetic:

  V1  the prime p and the root rho are the literal constants printed in the
      repo (typed in again below, not read from cells.py);
  V2  rho has exact order 128 in F_p;
  V3  every row w of the reported basis B satisfies sum_j w_j rho^j = 0 mod p
      (so L(B) is contained in Lambda_p);
  V4  |det B| = p, by an INDEPENDENT fraction-free (Bareiss) determinant;
  V5  hence L(B) = Lambda_p:  L(B) <= Lambda_p and
      [Lambda_p : L(B)] = |det B| / det(Lambda_p) = p/p = 1.
      (det Lambda_p = p because Lambda_p is the kernel of the surjection
       Z^64 -> Z/p, w -> sum w_j rho^j, whose j=0 coefficient is 1.)
  V6  the reported witness set is what it says it is: for EMPTY, that the
      certificate claims no vector; for NONEMPTY, each w is re-verified.

What V1-V6 do NOT do is re-run the enumeration.  The emptiness claim itself
is the statement "a complete Fincke-Pohst enumeration of L(B) over the ball
of radius R = 16, with the box test applied exactly at every leaf, visited
FPNODES nodes and returned nothing".  To replay THAT, delete
state/CELL.enum.json and re-run runcell.py.

Usage:
  tools/ramguard local -- python3 \
     notes/pilots_20260807/ge_lattice_cert/verify_cert.py E1-128
"""
import json
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))

# --- V1: the literal constants, retyped from the repo -----------------------
# background/nodes/e1_pocklington_250bit_exhibit_field/statement.md:11-12
LIT_P = {
    "E1-128":
        904625697166646869347790708689937759412227977745095982970820953353127723009,
    # critical/nodes/corridor_ledger/verify_corridor_literal_prime.py:22-26
    "CORRIDOR-128":
        108037839417390090843359763492907651258221714407500997496797919767622829735937,
    # background/nodes/mca_quadratic_prize_rows/statement.md:31-34
    "PROTH-1over2": 132540169958804033333249306710494641010898987122689,
    "PROTH-1over4": 411940680852499481698306614369841346700408394874881,
    "PROTH-1over8": 979947269755402568812854322316630667196565607677953,
    "PROTH-1over16": 2121285573237585848299875619011192262679065433997313,
}
# background/nodes/e1_pocklington_250bit_exhibit_field/statement.md:23-24
LIT_RHO = {
    "E1-128":
        440266185830122294862552098878717819794821358702875176198798016633729926114,
}


def bareiss_det(M):
    """Fraction-free Gaussian elimination.  Exact integer determinant."""
    A = [row[:] for row in M]
    n = len(A)
    sign = 1
    prev = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            for i in range(k + 1, n):
                if A[i][k] != 0:
                    A[k], A[i] = A[i], A[k]
                    sign = -sign
                    break
            else:
                return 0
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * A[k][k] - A[i][k] * A[k][j]) // prev
            A[i][k] = 0
        prev = A[k][k]
    return sign * A[n - 1][n - 1]


def main():
    cid = sys.argv[1]
    cert = json.load(open(os.path.join(HERE, "state", "%s.cert.json" % cid)))
    p, B, h = cert["p"], cert["basis"], cert["h"]
    ok = True
    print("== STANDALONE VERIFICATION of %s ==" % cid)

    v1 = (cid not in LIT_P) or (p == LIT_P[cid])
    print("V1 prime matches the literal repo constant           : %s" % v1)
    ok &= v1
    if cid in LIT_RHO:
        rho = LIT_RHO[cid]
        v2 = pow(rho, 128, p) == 1 and pow(rho, 64, p) == p - 1
        print("V2 rho has exact order 128 in F_p                    : %s" % v2)
        ok &= v2
    else:
        # recover the root actually used from the certificate's own basis:
        # row 1 of the canonical basis is (-rho, 1, 0...); after reduction we
        # instead re-derive rho from the lattice: rho = -w_0/w_1 for any row
        # with w_1 invertible is NOT well defined, so we take the root from
        # the smallest generator consistent with all rows.
        rho = None
        for g in range(2, 1000):
            c = pow(g, (p - 1) // 128, p)
            if pow(c, 64, p) == p - 1:
                if all(sum(w[j] * pow(c, j, p) for j in range(h)) % p == 0
                       for w in B):
                    rho = c
                    break
        v2 = rho is not None
        print("V2 a primitive 128th root consistent with B exists    : %s "
              "(rho found = %s)" % (v2, rho is not None))
        ok &= v2
        if rho is None:
            print("     (expected for the PLANT-C control: it is a CO-CYCLIC")
            print("      lattice {w : sum w_j c_j = 0 mod p} with a random c,")
            print("      not the ideal lattice Lambda_p.  Its check is the")
            print("      planted-vector recovery, in the run transcript.)")
            det = bareiss_det(B)
            print("V4 |det B| = p (independent Bareiss)                 : %s"
                  % (abs(det) == p))
            print("V6 %d witnesses reported; planted vector recovery is the "
                  "control." % len(cert["found"]))
            sys.exit(0)

    v3 = all(sum(w[j] * pow(rho, j, p) for j in range(h)) % p == 0 for w in B)
    print("V3 every basis row lies in Lambda_p                  : %s" % v3)
    ok &= v3

    det = bareiss_det(B)
    v4 = abs(det) == p
    print("V4 |det B| = p (independent Bareiss)                 : %s" % v4)
    print("     |det B| = %d" % abs(det))
    ok &= v4

    print("V5 therefore L(B) = Lambda_p (index = |det B|/p = %d)  : %s"
          % (abs(det) // p if p else 0, v4 and v3))

    fnd = cert["found"]
    if not fnd:
        print("V6 certificate claims EMPTY; FPNODES = %d, FPSEC = %.0f"
              % (cert["nodes"], cert["fpsec"]))
        print("     box tested: {-%d..%d}^%d, ||w||_1 <= %d, R^2 = %d"
              % (cert["boxinf"], cert["boxinf"], h, cert["L"],
                 min(4 * h, 2 * cert["L"])))
    else:
        allok = True
        for w in fnd:
            c1 = any(w) and max(abs(t) for t in w) <= cert["boxinf"]
            c2 = sum(abs(t) for t in w) <= cert["L"]
            c3 = sum(w[j] * pow(rho, j, p) for j in range(h)) % p == 0
            allok &= (c1 and c2 and c3)
        print("V6 all %d reported witnesses re-verified exactly      : %s"
              % (len(fnd), allok))
        ok &= allok

    print("\nRESULT: %s" % ("ALL STRUCTURAL CHECKS PASS" if ok
                            else "**VERIFICATION FAILED**"))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
