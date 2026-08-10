"""D2/D3 part 2: registered checks P4-P7 plus the R3/R4 arithmetic.

P4  the N=28 design 9-line under C (no linear algebra)
P5  the cyclotomic law under C1 (distinct root sets)
P6  the (AO1) closure scan over (m,a,O)
P7  the O-sensitivity at m=2, a=4m+2
R3  cyclotomic exclusion at official scale
R4  disjoint-support fence across m

Stdlib only.  Run under tools/ramguard.
"""


def say(s=""):
    print(str(s), flush=True)


def ao1(N, R, rho, e, a, O):
    """registered bound (AO1); None when a >= R+1 (type-2 term vacuous)."""
    if a <= rho:
        return None
    if a >= R + 1:
        return None
    t1 = min(e + 1, a // (a - rho), (a * e + O) // rho)
    t2 = ((N - a) * e) // (R + 1 - a)
    return t1 + t2


say("=== P4 : the N=28 q=29 design 9-line under characterization C ===")
tri = [(1, 2, 5), (3, 6, 7), (4, 16, 21), (9, 17, 23), (10, 19, 26),
       (11, 18, 27), (12, 13, 22), (14, 20, 28), (15, 24, 25)]
N, R, rho, e = 28, 14, 3, 1
allpts = set()
ok = True
for S in tri:
    if allpts & set(S):
        ok = False
    allpts |= set(S)
say("  9 triples pairwise disjoint : %s   |union| = %d of N = %d"
    % (ok, len(allpts), N))
say("  A = R+1-2rho = %d ; R4 needs A <= rho = %d  ->  %s"
    % (R + 1 - 2 * rho, rho, "SATISFIED" if R + 1 - 2 * rho <= rho else "VIOLATED"))
a = 2 * rho
say("  for any pair, a = |S_i u S_j| = %d ; type-2 lower bound"
    " |S\\W| >= R+1-a = %d, but |S| = rho = %d" % (a, R + 1 - a, rho))
say("  contradiction margin = %d ; so every third slope is neither type-1"
    " (disjointness) nor type-2  ->  T forced to 2, not 9."
    % (R + 1 - a - rho))
say("  round-27 measured Hankel nullity for this line = 0 (NOT realizable):"
    " C AGREES, with no linear algebra.")
say()

say("=== P5 : the cyclotomic law explained by C1 (injectivity) ===")
say("  row                    N    rho  e   design T  #distinct root sets"
    " = N/rho   C1 verdict     round-27 nullity")
ROWS = [("N=16 rho=4 e=2 r0=2", 17, 16, 4, 2, 8, 0),
        ("N=16 rho=4 e=4 r0=1", 17, 16, 4, 4, 16, 0),
        ("N=12 rho=3 e=1 r0=3", 13, 12, 3, 1, 4, 3),
        ("N=20 rho=5 e=1 r0=5", 41, 20, 5, 1, 4, 5),
        ("N=24 rho=6 e=2 r0=3", 73, 24, 6, 2, 8, 0),
        ("N=16 rho=4 e=2 r0=2", 97, 16, 4, 2, 8, 0),
        ("N=16 rho=4 e=2 r0=2", 113, 16, 4, 2, 8, 0)]
hits = 0
for (name, q, Nn, rr, ee, Td, nul) in ROWS:
    ncos = Nn // rr
    verdict = "repeats -> NOT column-far" if Td > ncos else "distinct -> allowed"
    pred0 = (Td > ncos)
    obs0 = (nul == 0)
    agree = (pred0 == obs0)
    hits += agree
    say("  %-21s %-4d %-4d %-3d %-9d %-19d %-26s %d   %s"
        % (name, Nn, rr, ee, Td, ncos, verdict, nul,
           "AGREE" if agree else "DISAGREE"))
say("  sign agreement: %d / %d rows" % (hits, len(ROWS)))
say()

say("=== R3 : cyclotomic exclusion at OFFICIAL scale (proof arithmetic) ===")
m = 2 ** 37
say("  A=1 half-distance profile: rho = 2^39 = %d, N = 2^41 = %d, R = 2^40"
    % (2 ** 39, 2 ** 41))
say("  rho | N : %s ; #distinct mu_rho-cosets = N/rho = %d"
    % ((2 ** 41) % (2 ** 39) == 0, 2 ** 41 // 2 ** 39))
say("  C1 => T <= 4 ; targets are rho+1 = %d and rho+2 = %d."
    % (2 ** 39 + 1, 2 ** 39 + 2))
say("  => the cyclotomic family CANNOT violate either budget. Margin = %d."
    % (2 ** 39 + 1 - 4))
say("  A=3 strict profile: rho = 4m-1 = %d, N = 16m = %d, rho | N ? %s"
    % (4 * m - 1, 16 * m, (16 * m) % (4 * m - 1) == 0))
say("  (gcd(4m-1,16m) = gcd(4m-1,4) * ... ; 4m-1 is odd and 4m-1 > 16m/2 for"
    " m>=1 is false, so check directly:) 16m mod (4m-1) = %d"
    % ((16 * m) % (4 * m - 1)))
say()

say("=== R4 : disjoint-support fence across the scale parameter ===")
say("   m   N=16m  rho=4m-1  T=rho+2  T*rho    N     T*rho<=N ?  A<=rho ?")
for mm in [1, 2, 3, 4, 5, 10]:
    Nn, rr = 16 * mm, 4 * mm - 1
    T = rr + 2
    say("  %-3d %-6d %-9d %-8d %-8d %-5d %-11s %s"
        % (mm, Nn, rr, T, T * rr, Nn, T * rr <= Nn, (8 * mm + 1 - 2 * rr) <= rr))
say("  => the fully-disjoint mechanism of the m=1 fence is arithmetically"
    " available ONLY at m=1.")
say()

say("=== P6 : (AO1) closure scan, strict A=3 endpoint (e=m, rho=4m-1) ===")
say("   m   O    closing a-window {a : (AO1) <= rho+1}          width")
summary = []
for mm in range(1, 41):
    Nn, Rr, rr, ee = 16 * mm, 8 * mm, 4 * mm - 1, mm
    for O in range(0, min(mm, 4)):
        good = [a for a in range(rr + 1, 2 * rr + 1)
                if (ao1(Nn, Rr, rr, ee, a, O) or 10 ** 9) <= rr + 1]
        if mm <= 8 or O == 0:
            lo = min(good) if good else None
            hi = max(good) if good else None
            say("  %-3d %-4d %-48s %d"
                % (mm, O, ("[%s..%s] (rho+1=%d, 4m+2=%d)" % (lo, hi, rr + 1, 4 * mm + 2))
                   if good else "EMPTY", len(good)))
        if O == 0:
            summary.append((mm, len(good), min(good) if good else None,
                            max(good) if good else None))
say()
say("  O=0 summary: m, width, a_min, a_max")
say("   widths over m in [2,40]: min=%d max=%d ; a_min-4m always = %s"
    % (min(s[1] for s in summary[1:]), max(s[1] for s in summary[1:]),
       sorted({s[2] - 4 * s[0] for s in summary[1:] if s[2] is not None})))
say("   m=1 width = %d (fence: must be 0)" % summary[0][1])
say()

say("=== P7 : O-sensitivity at m=2, a=4m+2=10 ===")
for O in range(0, 2):
    say("  m=2 a=10 O=%d : (AO1) = %s   (target rho+1 = 8, cap rho+2 = 9)"
        % (O, ao1(32, 16, 7, 2, 10, O)))
say()
say("=== END part 2 ===")
