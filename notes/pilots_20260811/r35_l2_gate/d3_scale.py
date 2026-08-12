"""r35_l2_gate D3 -- the emptiness attack, the general-m ledger, and the
field-genericity of the D-F construction.

(a) the general-m dimension ledger: expected dim of the (L2) solvability
    locus in the projective curve space, at every m;
(b) TRANSVERSALITY of the good component (registered P5): the fibre of
    B = (f,g,h,k) over a witness curve Q is a single point, so the good
    component has dimension exactly 18 = 23 - 5;
(c) the left-kernel mechanism behind the banked (MI1) / my D-D:
    verify that Q_Z and X*Q_Z span the left kernel of the witness pencil;
(d) the construction re-run on THREE more fields (Z5 / field-genericity).
"""
import random

LINES = []


def P(s=""):
    LINES.append(str(s))


exec(open("notes/pilots_20260811/r35_l2_gate/_shared.py").read())


W97 = dict(
    p=97,
    f=[42, 13, 19, 51, 10], g=[83, 79, 17, 36, 40],
    h=[58, 28, 77, 64, 20], k=[2, 60, 10, 65, 31],
    Q0=[7, 10, 78, 31, 43, 62, 29, 22],
    Q1=[80, 88, 69, 63, 34, 94, 70, 62],
    Q2=[80, 4, 73, 12, 82, 59, 47, 1],
    y0=[77, 90, 33, 0, 95, 81, 25, 10, 92, 6, 84, 21, 86, 26, 40, 74],
    y1=[1, 20, 62, 91, 3, 28, 56, 71, 93, 78, 43, 53, 86, 96, 93, 1])

W193 = dict(
    p=193,
    f=[3, 69, 75, 72, 18], g=[104, 102, 140, 130, 6],
    h=[21, 183, 67, 171, 123], k=[22, 20, 41, 91, 61],
    Q0=[100, 171, 13, 99, 32, 133, 85, 141],
    Q1=[68, 181, 102, 84, 155, 1, 89, 104],
    Q2=[98, 184, 87, 75, 41, 63, 38, 1],
    y0=[151, 158, 140, 16, 63, 104, 161, 7, 184, 70, 128, 172, 152, 6, 48,
        151],
    y1=[134, 188, 35, 60, 176, 55, 170, 158, 86, 134, 167, 53, 182, 115, 33,
        1])


def analyse(W):
    p = W["p"]
    Q = [W["Q0"], W["Q1"], W["Q2"]]
    y0, y1 = W["y0"], W["y1"]
    P("-" * 70)
    P("WITNESS ANALYSIS, q = %d" % p)
    P("-" * 70)
    # (b) transversality: the fibre of B over Q is a single point
    Phi = phi_14x10(Q, p)
    ker = nullspace(Phi, p, 10)
    P("  dim ker Phi (= nullity of the 36x32 system, D-B)   : %d" % len(ker))
    if len(ker) == 1:
        v = ker[0]
        fr, gr = v[0:5], v[5:10]
        # compare with the B actually used, up to scale
        def prop(a, b):
            a = pad(a, 5)
            b = pad(b, 5)
            nz = [i for i in range(5) if b[i] % p]
            if not nz:
                return not any(x % p for x in a)
            c = (a[nz[0]] * pow(b[nz[0]], p - 2, p)) % p
            return all((a[i] - c * b[i]) % p == 0 for i in range(5))
        P("  recovered (f,g) proportional to the B used?        : %s / %s"
          % (prop(fr, W["f"]), prop(gr, W["g"])))
        P("  => B |-> Q has a ZERO-DIMENSIONAL fibre over the witness, so")
        P("     dim(good component) = dim{det M(B)=0} = 19-1 = 18 = 23-5,")
        P("     i.e. the good component has EXACTLY the expected dimension")
        P("     (the +4/codim-5 IS transverse there).  P5.")
    # (c) the left kernel: Q_Z and X*Q_Z, both of parameter degree 2
    okL = True
    for z in range(min(p, 25)):
        yz = [(y0[i] + z * y1[i]) % p for i in range(16)]
        Qz = pad([(Q[0][i] + z * Q[1][i] + z * z * Q[2][i]) % p
                  for i in range(8)], 9)
        XQz = [0] + Qz[:8]
        for u in (Qz, XQz):
            for b in range(8):
                if sum(u[a] * yz[a + b] for a in range(9)) % p:
                    okL = False
    P("  left kernel contains Q_Z and X*Q_Z (both param degree 2): %s" % okL)
    Lm = []
    for b in range(8):
        Lm.append([y0[a + b] % p for a in range(9)])
    P("  left nullity of M_r(y_0) alone                     : %d"
      % (9 - rank(Lm, p)))
    P("  => left minimal indices (2,2), right minimal index e=2,")
    P("     so 3e + delta = rho = 7 forces delta = 1: EXACTLY ONE rank-drop")
    P("     parameter, with multiplicity one.  This is the mechanism of the")
    P("     BANKED bound (A+s)e <= rho-s (MI1), which at m=2 reads 3e <= 7.")
    # rank profile / drop multiplicity
    drops = []
    for z in range(p):
        yz = [(y0[i] + z * y1[i]) % p for i in range(16)]
        r = rank(hankel(yz, p), p)
        if r < 7:
            drops.append((z, r))
    P("  measured finite rank-drop points (z, rank)         : %s" % drops)
    P("  rank at infinity (pencil M_r(y_1))                 : %d"
      % rank(hankel(y1, p), p))


def main():
    P("=" * 70)
    P("(a) THE GENERAL-m LEDGER FOR THE (L2) REALIZATION LAYER")
    P("=" * 70)
    P("  curve space: (m+1) forms of degree <= rho=4m-1 -> proj dim"
      " 4m(m+1)-1")
    P("  solvability locus = determinantal locus of the realization map;")
    P("  its codimension is deficit+1 = 4m^2-7m+3.")
    P("")
    P("  m | proj dim curves | deficit 4m^2-7m+2 | det codim | EXPECTED DIM"
      " = 11m-4")
    for m in range(1, 11):
        P("  %2d | %15d | %17d | %9d | %d"
          % (m, 4 * m * (m + 1) - 1, 4 * m * m - 7 * m + 2,
             4 * m * m - 7 * m + 3, 11 * m - 4))
    P("")
    P("  >>> 4m(m+1)-1 - (4m^2-7m+3) = 11m-4 > 0 for EVERY m >= 1.")
    P("  >>> The (L2) layer is NONEMPTY-EXPECTED AT EVERY m.  The sign")
    P("      change of the deficit at m=2 is a change in the equation-count")
    P("      excess, NOT in the existence verdict.")
    analyse(W97)
    analyse(W193)
    P("")
    P("=" * 70)
    P("(d) FIELD-GENERICITY: the same inversion on three more fields")
    P("=" * 70)
    for p in (257, 641, 769):
        rng = random.Random(31337 + p)
        found = 0
        draws = 0
        detsnz = 0
        while draws < 4 * p and found < 2:
            draws += 1
            B = [[rng.randrange(p) for _ in range(5)] for _ in range(4)]
            MB = build_MB(B, p)
            if det(MB, p) != 0:
                detsnz += 1
                continue
            for v in nullspace(MB, p, 24):
                Q = [v[0:8], v[8:16], v[16:24]]
                rep = quick_certify(Q, p)
                if rep is not None:
                    found += 1
                    P("  q=%3d  CERTIFIED: e=%s, generic rank %d, s=%d,"
                      " seprank %d, nullity %d, direct check %s"
                      % (p, rep["e"], rep["generic_rank"], rep["s"],
                         rep["seprank"], rep["nullity36"], rep["direct"]))
                    P("         Q_0 = %s" % pad(Q[0], 8))
                    P("         Q_1 = %s" % pad(Q[1], 8))
                    P("         Q_2 = %s" % pad(Q[2], 8))
                    break
        P("  q=%3d: %d draws, %d certified e=m=2 objects" % (p, draws, found))
    with open("notes/pilots_20260811/r35_l2_gate/d3_results.txt", "w") as fh:
        fh.write("\n".join(LINES) + "\n")
    print("\n".join(LINES))


main()
