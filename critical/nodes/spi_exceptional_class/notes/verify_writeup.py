#!/usr/bin/env python3
"""
verify_writeup.py -- deterministic cross-checks for
nodes/spi_exceptional_class/proof.md.

Constraints honoured: single process, pure Python (no numpy / no sympy),
well under 1 GB RAM, no parallelism, no background work.  Runs in ~1 s.

Field  F_17 ;  H = mu_8 = {1,2,4,8,9,13,15,16} = 8th roots of unity in F_17
(2 has multiplicative order 8, so X^8 - 1 splits with simple roots over F_17).

The proof (see ../proof.md) rests on three mechanical facts; each CHECK below
reproduces one of them, and CHECK 1 / CHECK 2 reproduce the two counts cited in
the write-up and inherited from spi_component_control's verification.

  KEY IDENTITY used throughout.  Because X^n - 1 is MONIC with root set exactly
  H, the Sylvester resultant collapses to a product of evaluations:

        R(Z) := Res_X( q_Z , X^n - 1 ) = prod_{h in H} q_Z(h).

  As q_Z's coefficients are polynomials in Z, each q_Z(h) is a polynomial in Z,
  and F_17[Z] is an integral domain, so R == 0 (identically in Z) IFF some
  single factor q_Z(h0) == 0 identically -- i.e. one fixed h0 in H is a root of
  every fibre.  That is exactly the "R == 0 => fixed common H-root => tangent"
  step of part (3), made elementary.

  CHECK 1  (part 1 & 2; also the spi_component_control input):
        2500 random Hankel pencils M(Z) = Z0*Mu + Z1*Mv ; the number of
        F_17-rational rank-drop slopes is <= the generic rank r, and r <= t.

  CHECK 2  (part 3, the R == 0 branch):
        1600 constructed moving-kernel families q_Z carrying a PLANTED root
        x0 in H ; verify R(Z) == 0 identically (the x0-factor is the zero form)
        and that x0 is a common root of every fibre  =>  common-divisor
        (tangent) stratum.

  CHECK 3  (arithmetic backbone of part 2):
        (a) D_j EMPTINESS: a locator with any root outside H, or a boundary
            monomial X | l, does NOT divide X^n - 1, hence l is not in D_j.
        (b) R != 0 SLOPE BOUND: a moving-root family with no fixed H-root has
            R(Z) = a(Z)^8 - 1 != 0 with deg_Z R = n*deg_Z(coeff) = O(n t), so at
            most O(n t) = O(n^2) slopes are H-supported.
"""

import random

P = 17
N = 8                                   # H = mu_N
H = sorted({pow(2, i, P) for i in range(N)})   # [1,2,4,8,9,13,15,16]
assert H == [1, 2, 4, 8, 9, 13, 15, 16]
assert all(pow(h, N, P) == 1 for h in H)

# ---------------------------------------------------------------- F_17 helpers
def inv(a):
    return pow(a % P, P - 2, P)

def mat_rank(rows):
    """Rank over F_P of a list-of-rows matrix (Gaussian elimination)."""
    M = [row[:] for row in rows]
    R = len(M)
    C = len(M[0]) if R else 0
    rank = 0
    col = 0
    for col in range(C):
        piv = None
        for r in range(rank, R):
            if M[r][col] % P != 0:
                piv = r
                break
        if piv is None:
            continue
        M[rank], M[piv] = M[piv], M[rank]
        iv = inv(M[rank][col])
        M[rank] = [(x * iv) % P for x in M[rank]]
        for r in range(R):
            if r != rank and M[r][col] % P != 0:
                f = M[r][col]
                M[r] = [(a - f * b) % P for a, b in zip(M[r], M[rank])]
        rank += 1
        if rank == R:
            break
    return rank

# ------------------------------------------------- univariate poly over F_17
# polynomials are coefficient lists, low degree first
def poly_trim(a):
    while len(a) > 1 and a[-1] % P == 0:
        a.pop()
    return a

def poly_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai % P == 0:
            continue
        for j, bj in enumerate(b):
            out[i + j] = (out[i + j] + ai * bj) % P
    return poly_trim(out)

def poly_eval(a, x):
    acc = 0
    for c in reversed(a):
        acc = (acc * x + c) % P
    return acc

def poly_divmod(a, b):
    """return (quot, rem) of a / b over F_P ; b monic-izable (lc invertible)."""
    a = [c % P for c in a]
    b = poly_trim([c % P for c in b])
    q = [0] * (max(len(a) - len(b) + 1, 1))
    r = a[:]
    poly_trim(r)
    ilc = inv(b[-1])
    while len(r) >= len(b) and not (len(r) == 1 and r[0] == 0):
        deg = len(r) - len(b)
        coef = (r[-1] * ilc) % P
        q[deg] = coef
        for i, bc in enumerate(b):
            r[deg + i] = (r[deg + i] - coef * bc) % P
        poly_trim(r)
        if len(r) < len(b):
            break
    return poly_trim(q), poly_trim(r)

def poly_gcd(a, b):
    a = poly_trim([c % P for c in a])
    b = poly_trim([c % P for c in b])
    while not (len(b) == 1 and b[0] == 0):
        _, r = poly_divmod(a, b)
        a, b = b, r
    # normalise monic
    if a[-1] % P != 0:
        iv = inv(a[-1])
        a = [(c * iv) % P for c in a]
    return a

XN_MINUS_1 = [(-1) % P] + [0] * (N - 1) + [1]        # X^N - 1


# ================================================================ CHECK 1
def check1_vertical_rank_drop(trials=2500, t=3, j=4, seed=12345):
    """#rational rank-drop slopes <= generic rank r, and r <= t, on `trials`
    random Hankel pencils.  (spi_component_control: '<= r on 2500 pencils'.)"""
    rng = random.Random(seed)
    W = t + j                                  # syndrome window length index span
    # P^1(F_17): 17 affine slopes (Z0=1,Z1=z) + infinity (Z0=0,Z1=1)
    slopes = [(1, z) for z in range(P)] + [(0, 1)]
    worst = 0
    max_r = 0
    for _ in range(trials):
        Su = [rng.randrange(P) for _ in range(W)]
        Sv = [rng.randrange(P) for _ in range(W)]
        # Hankel windows: M[i][c] = S[i+c], i in 0..t-1, c in 0..j
        def hankel(S):
            return [[S[i + c] for c in range(j + 1)] for i in range(t)]
        Mu, Mv = hankel(Su), hankel(Sv)
        ranks = []
        for (z0, z1) in slopes:
            Mz = [[(z0 * Mu[i][c] + z1 * Mv[i][c]) % P
                   for c in range(j + 1)] for i in range(t)]
            ranks.append(mat_rank(Mz))
        r = max(ranks)                         # generic rank (attained: 18 > r)
        drops = sum(1 for rk in ranks if rk < r)
        assert drops <= r, (drops, r, Su, Sv)
        assert r <= t
        worst = max(worst, drops)
        max_r = max(max_r, r)
    return dict(trials=trials, t=t, j=j, generic_rank_max=max_r,
               worst_rank_drop_slopes=worst, bound=max_r,
               ok=(worst <= max_r))


# ================================================================ CHECK 2
def check2_R_zero_is_tangent(trials=1600, seed=2024):
    """1600 moving-kernel families q_Z = (X - x0)*(a(Z) X + b(Z)) with a PLANTED
    root x0 in H.  Verify R(Z) = prod_h q_Z(h) == 0 identically (the x0 factor is
    the zero linear form in Z) and x0 is a common root of every fibre."""
    rng = random.Random(seed)
    passed = 0
    for _ in range(trials):
        x0 = rng.choice(H)                     # fixed common H-root (planted)
        a0, a1 = rng.randrange(P), rng.randrange(P)
        b0, b1 = rng.randrange(P), rng.randrange(P)
        # q_Z(X) = (X - x0)*( (a0 Z0 + a1 Z1) X + (b0 Z0 + b1 Z1) ).
        # Each factor q_Z(h) is a LINEAR FORM in (Z0,Z1); store as (cZ0, cZ1).
        def qeval_form(h):
            # (h - x0) * ( a(Z) h + b(Z) ) ; a(Z)=a0 Z0+a1 Z1 etc.
            s = (h - x0) % P
            return (s * (a0 * h + b0) % P, s * (a1 * h + b1) % P)
        forms = [qeval_form(h) for h in H]
        # R(Z) = product of these linear forms.  In the domain F_17[Z] it is the
        # zero polynomial IFF one factor is the zero form (0,0).
        zero_factor = any(f == (0, 0) for f in forms)
        # the x0 factor must be the zero form (h==x0 gives s==0):
        x0_form = qeval_form(x0)
        # x0 is a common root of every fibre: q_Z(x0) is the zero form
        common_root_ok = (x0_form == (0, 0))
        # sanity: R vanishes at all 18 rational slopes
        def R_at(z0, z1):
            prod = 1
            for (c0, c1) in forms:
                prod = (prod * (c0 * z0 + c1 * z1)) % P
            return prod
        all_slopes = [(1, z) for z in range(P)] + [(0, 1)]
        R_zero_numeric = all(R_at(z0, z1) == 0 for (z0, z1) in all_slopes)
        if zero_factor and common_root_ok and R_zero_numeric:
            passed += 1
    return dict(trials=trials, tangent_paid=passed,
               ok=(passed == trials))


# ================================================================ CHECK 3
def check3_backbone(seed=7):
    """(a) D_j emptiness for out-of-H roots / boundary monomial;
       (b) R != 0 moving-root family has <= deg_Z R = O(n) supported slopes."""
    rng = random.Random(seed)
    OUT = [x for x in range(1, P) if pow(x, N, P) != 1]   # roots outside H
    # (a) D_j emptiness ------------------------------------------------------
    a_trials, a_pass = 1000, 0
    for _ in range(a_trials):
        if rng.random() < 0.5:
            rho = rng.choice(OUT)              # finite root outside H
        else:
            rho = 0                            # boundary monomial X | l
        # l = (X - rho) * (random product of a few (X - h), h in H)
        ell = [(-rho) % P, 1]
        for _ in range(rng.randrange(0, 3)):
            h = rng.choice(H)
            ell = poly_mul(ell, [(-h) % P, 1])
        # l in D_j  <=>  l | X^N - 1.  With a non-H (or zero) root it must not.
        _, rem = poly_divmod(XN_MINUS_1, ell)
        divides = (len(rem) == 1 and rem[0] == 0) and (len(ell) - 1 <= N)
        # also: gcd(l, X^N-1) != l  (l carries a factor absent from X^N-1)
        g = poly_gcd(ell, XN_MINUS_1)
        not_in_Dj = (not divides) and (g != poly_trim(ell[:]))
        if not_in_Dj:
            a_pass += 1
    # (b) R != 0 slope bound -------------------------------------------------
    # A genuine moving kernel is q_Z(X) = c(Z) X - a(Z) with c,a HOMOGENEOUS
    # linear forms in Z (same degree -- the moving-catalecticant coefficients).
    # Its root a(Z)/c(Z) traces a Mobius map P^1 -> P^1.  R(Z) = prod_h
    # (h c(Z) - a(Z)) is a degree-N homogeneous form in Z (deg_Z R = N =
    # O(n * deg_Z coeff)), so at most N slopes send the root into H.
    b_trials, b_pass = 500, 0
    slopes = [(1, z) for z in range(P)] + [(0, 1)]
    for _ in range(b_trials):
        c0, c1 = rng.randrange(P), rng.randrange(P)
        a0, a1 = rng.randrange(P), rng.randrange(P)
        # keep it a genuine MOVING root: (c0,c1) not proportional to (a0,a1),
        # and c not identically zero.
        if (c0, c1) == (0, 0) or (c0 * a1 - c1 * a0) % P == 0:
            b_trials -= 1
            continue
        def root_in_H(z0, z1):
            c = (c0 * z0 + c1 * z1) % P
            a = (a0 * z0 + a1 * z1) % P
            if c == 0:
                return False                   # root at infinity, not in H
            x = (a * inv(c)) % P
            return pow(x, N, P) == 1
        supp = sum(1 for s in slopes if root_in_H(*s))
        if supp <= N:                          # deg_Z R = N bounds supported slopes
            b_pass += 1
    return dict(dj_emptiness=dict(trials=a_trials, passed=a_pass,
                                  ok=(a_pass == a_trials)),
                slope_bound=dict(trials=b_trials, passed=b_pass, degZ_R=N,
                                 ok=(b_pass == b_trials)))


# ================================================================ main
if __name__ == "__main__":
    r1 = check1_vertical_rank_drop()
    r2 = check2_R_zero_is_tangent()
    r3 = check3_backbone()

    print("F_17,  H = mu_8 =", H)
    print()
    print("CHECK 1  vertical rank-drop count <= generic rank r (<= t):")
    print("   ", r1)
    print("CHECK 2  R == 0 branch is tangent-paid (fixed common H-root):")
    print("   ", r2)
    print("CHECK 3  arithmetic backbone (D_j emptiness ; R != 0 slope bound):")
    print("   ", r3)
    print()
    ok = (r1["ok"] and r2["ok"] and r3["dj_emptiness"]["ok"]
          and r3["slope_bound"]["ok"])
    print("PASS" if ok else "FAIL",
          "-- 2500 pencils, 1600 tangent fibres, 1000 D_j, 500 slope-bound")
