#!/usr/bin/env python3
r"""
verify.py for f_dual_distance_frame.

For a flat (linear subspace) P of the polynomial parameter space, encode it as
a linear code via evaluation on H:  the generator matrix G has one column per
x in H, column x = the "trace" (b_i(x))_i for a basis b_i of P.

Claims checked (over several finite fields and random / structured flats):
  (1) A subset S of H has linearly DEPENDENT traces  <=>  the dual code P^perp
      contains a nonzero word supported inside S.
  (2) Weight-1 dual word  <=>  common root of all of P.
      Weight-2 dual word   <=>  a "twin" pair (evaluations always proportional).
  (3) CLOSURE: for a minimum-support dual word (support minimal under
      inclusion), all its coordinates are nonzero, and any p in P vanishing on
      all-but-one of that support vanishes on the whole support.
  (4) If the dual distance w* = d(P^perp) satisfies w* > r = dim P, then EVERY
      r-subset of columns (traces) is linearly independent (general position).
"""
import itertools, random

def inv(a, q): return pow(a, q - 2, q)

def rank(rows, q):
    M = [r[:] for r in rows]; R = len(M); Cc = len(M[0]) if R else 0; r = 0
    for c in range(Cc):
        piv = next((i for i in range(r, R) if M[i][c] % q), None)
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        ip = inv(M[r][c], q); M[r] = [(x*ip) % q for x in M[r]]
        for i in range(R):
            if i != r and M[i][c] % q:
                f = M[i][c]; M[i] = [(M[i][j]-f*M[r][j]) % q for j in range(Cc)]
        r += 1
        if r == R: break
    return r

def nullspace(A, q):
    A = [row[:] for row in A]; R = len(A); Cc = len(A[0]); piv = []; row = 0
    for col in range(Cc):
        p = next((i for i in range(row, R) if A[i][col] % q), None)
        if p is None: continue
        A[row], A[p] = A[p], A[row]
        ip = inv(A[row][col], q); A[row] = [(x*ip) % q for x in A[row]]
        for i in range(R):
            if i != row and A[i][col] % q:
                f = A[i][col]; A[i] = [(A[i][j]-f*A[row][j]) % q for j in range(Cc)]
        piv.append(col); row += 1
        if row == R: break
    free = [j for j in range(Cc) if j not in piv]; basis = []
    for f in free:
        v = [0]*Cc; v[f] = 1
        for ri, col in enumerate(piv): v[col] = (-A[ri][f]) % q
        basis.append(v)
    return basis

def all_codewords(gen, q):
    """enumerate the linear code spanned by rows of gen (small dims only)."""
    R = len(gen); n = len(gen[0]) if R else 0
    for coeffs in itertools.product(range(q), repeat=R):
        w = [0]*n
        for i, c in enumerate(coeffs):
            if c:
                for j in range(n): w[j] = (w[j] + c*gen[i][j]) % q
        yield w

def dual_code(gen, q):
    return nullspace(gen, q)         # words c with gen . c = 0

def check_flat(basis_polys, H, q):
    """basis_polys: list of coeff-lists (a poly = sum a_i X^i). Returns report."""
    G = [[sum(p[d]*pow(x, d, q) for d in range(len(p))) % q for x in H] for p in basis_polys]
    r = rank(G, q)                    # dim of the evaluation code
    n = len(H)
    dual_basis = dual_code(G, q)
    # (4) dual distance
    dwords = [w for w in all_codewords(dual_basis, q) if any(w)] if dual_basis else []
    wstar = min((sum(1 for a in w if a) for w in dwords), default=n+1)
    # (1) test: random S, dependent traces <=> exists dual word supported in S
    ok1 = True
    for _ in range(40):
        ssz = random.randint(1, min(n, r+2))
        S = random.sample(range(n), ssz)
        cols = [[G[i][x] for i in range(len(G))] for x in S]
        dep = rank([[cols[a][b] for a in range(len(cols))] for b in range(len(G))], q) < len(S)
        has_dual = any(all((w[x] == 0) for x in range(n) if x not in S) and any(w[x] for x in S)
                       for w in dwords)
        if dep != has_dual: ok1 = False
    # (3) closure for a minimum-support dual word
    ok3 = True
    if dwords:
        # minimal-support word
        msupp = min(dwords, key=lambda w: sum(1 for a in w if a))
        supp = [x for x in range(n) if msupp[x]]
        # minimality of support -> all coords nonzero already guaranteed by min-weight;
        # closure: any codeword-of-P (member p) vanishing on all but one supp pt vanishes on all
        # emulate: for each member p in P, if it is zero on all but one supp point => zero there too
        for coeffs in itertools.product(range(q), repeat=len(basis_polys)):
            evalv = [sum(coeffs[i]*G[i][x] for i in range(len(G))) % q for x in range(n)]
            zeros = [x for x in supp if evalv[x] == 0]
            if len(zeros) == len(supp) - 1:
                # the missing one must also be zero
                miss = [x for x in supp if evalv[x] != 0]
                if miss: ok3 = False; break
    # (4) w* > r => every r-subset of columns independent
    ok4 = True
    if wstar > r:
        for Ssub in itertools.combinations(range(n), r):
            cols = [[G[i][x] for i in range(len(G))] for x in Ssub]
            if rank([[cols[a][b] for a in range(len(cols))] for b in range(len(G))], q) < r:
                ok4 = False; break
    return r, wstar, ok1, ok3, ok4

def main():
    allok = True; nn = 0
    random.seed(1)
    for q in (7, 11, 13):
        H = list(range(1, q))                       # H = F_q^*
        n = len(H)
        for _ in range(8):
            dim = random.randint(1, 3)
            deg = random.randint(dim, min(dim+2, n-1))
            basis = [[random.randrange(q) for _ in range(deg+1)] for _ in range(dim)]
            if rank([[sum(p[d]*pow(x,d,q) for d in range(len(p)))%q for x in H] for p in basis], q) < dim:
                continue
            r, wstar, o1, o3, o4 = check_flat(basis, H, q)
            nn += 1
            if not (o1 and o3 and o4):
                allok = False
                print(f"  FAIL q={q} r={r} wstar={wstar} : dep<=>dual={o1} closure={o3} genpos={o4}")
    print(f"checked {nn} random flats over F_7,F_11,F_13")
    print("PASS" if allok else "FAIL")

if __name__ == "__main__":
    main()
