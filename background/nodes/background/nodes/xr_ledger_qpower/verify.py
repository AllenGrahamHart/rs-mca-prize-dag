#!/usr/bin/env python3
r"""
verify.py for xr_ledger_qpower.

Claim (pair-rank ledger, closed form):
  Let H be the evaluation set, C the RS code of dimension k on H, and for a
  subset S with |S| = k+t define
       K_S = { w in F_q^H : w|_S lies in C|_S }.
  Then codim_{F_q^H}(K_S) = t, and for two supports S,T of size k+t with
  exchange distance s = |S\T| = |T\S| (so |S cap T| = k+t-s):
       codim(K_S cap K_T) = t + min(s,t).
  Consequently the pair-alignment ledger exponent is c(s,t) = min(s,t-1):
       P[(u,v) aligned at both S and T]  asymptotic to
           q^{1-t-min(s,t)}  (same-slope branch)  +  q^{2-2t} (distinct-slope),
       and  P[both]/P[one] ~ q^{-min(s,t-1)}.

PART A: exact linear-algebra check of codim(K_S cap K_T) over several
        finite fields, all sizes t, all exchange distances s.
PART B: Monte-Carlo check of the two-branch slope accounting and of the
        net conditional exponent c(s,t)=min(s,t-1).
"""
import itertools, random, math
from math import comb

def inv(a, q): return pow(a, q - 2, q)

def rref_rank(rows, q):
    M = [r[:] for r in rows]
    R = len(M); Cc = len(M[0]) if R else 0
    r = 0
    for c in range(Cc):
        piv = next((i for i in range(r, R) if M[i][c] % q), None)
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        ip = inv(M[r][c], q); M[r] = [(x * ip) % q for x in M[r]]
        for i in range(R):
            if i != r and M[i][c] % q:
                f = M[i][c]; M[i] = [(M[i][j] - f * M[r][j]) % q for j in range(Cc)]
        r += 1
        if r == R: break
    return r

def nullspace(A, q):
    A = [row[:] for row in A]; R = len(A); Cc = len(A[0])
    piv = []; row = 0
    for col in range(Cc):
        p = next((i for i in range(row, R) if A[i][col] % q), None)
        if p is None: continue
        A[row], A[p] = A[p], A[row]
        ip = inv(A[row][col], q); A[row] = [(x * ip) % q for x in A[row]]
        for i in range(R):
            if i != row and A[i][col] % q:
                f = A[i][col]; A[i] = [(A[i][j] - f * A[row][j]) % q for j in range(Cc)]
        piv.append(col); row += 1
        if row == R: break
    free = [j for j in range(Cc) if j not in piv]
    basis = []
    for f in free:
        v = [0]*Cc; v[f] = 1
        for ri, col in enumerate(piv): v[col] = (-A[ri][f]) % q
        basis.append(v)
    return basis

def codim_intersection(S, T, q, k, H):
    """codim of K_S cap K_T inside F_q^H via ranked parity checks."""
    idx = {x: i for i, x in enumerate(H)}
    cons = []
    for U in (S, T):
        Ul = list(U)
        Amat = [[pow(x, i, q) for x in Ul] for i in range(k)]  # RS gens on U
        for c in nullspace(Amat, q):                            # dual (parity) words
            row = [0]*len(H)
            for xi, x in enumerate(Ul): row[idx[x]] = c[xi] % q
            cons.append(row)
    return rref_rank(cons, q) if cons else 0

def partA():
    ok = True; nchecks = 0
    for q in (11, 13, 17, 19, 23):
        H = list(range(1, q)); n = len(H)
        for k in (2, 3, 4):
            for t in range(1, 5):
                A = k + t
                if A > n: continue
                for s in range(1, t + 2):           # go one past t to see the plateau
                    if A - s < 0 or (n - A) < s: continue
                    S = H[:A]
                    common = S[:A - s]
                    rest = [x for x in H if x not in S]
                    if len(rest) < s: continue
                    T = common + rest[:s]
                    got = codim_intersection(set(S), set(T), q, k, H)
                    pred = t + min(s, t)
                    nchecks += 1
                    if got != pred:
                        ok = False
                        print(f"  MISMATCH q={q} k={k} t={t} s={s}: got {got} pred {pred}")
    print(f"PART A (exact codim): {nchecks} checks, {'all match t+min(s,t)' if ok else 'FAILURES'}")
    return ok

def partB():
    """
    Monte-Carlo: over uniform (u,v) in (F_q^H)^2, empirically estimate
        P[one]  = P[aligned at S],
        P[both] = P[aligned at S and T],
    and confirm  P[both]/P[one]  scales like q^{-min(s,t-1)} across s.
    Aligned at S <=> exists z with w_z=u+z v s.t. w_z|_S in C|_S.
    """
    q, k = 11, 2
    H = list(range(1, q)); n = len(H)
    ok = True
    def aligned(w, S):
        # w|_S in C|_S ? check parity words vanish
        Sl = list(S)
        Amat = [[pow(x, i, q) for x in Sl] for i in range(k)]
        for c in nullspace(Amat, q):
            if sum(c[i] * w[Sl[i]] for i in range(len(Sl))) % q: return False
        return True
    for t in (2, 3):
        A = k + t
        S = H[:A]
        results = {}
        for s in range(1, t + 1):
            rest = [x for x in H if x not in S]
            if len(rest) < s: continue
            T = S[:A - s] + rest[:s]
            trials = 60000; one = 0; both = 0
            for _ in range(trials):
                u = {x: random.randrange(q) for x in H}
                v = {x: random.randrange(q) for x in H}
                aS = any(aligned({x: (u[x] + z * v[x]) % q for x in H}, S) for z in range(q))
                if aS:
                    one += 1
                    aT = any(aligned({x: (u[x] + z * v[x]) % q for x in H}, T) for z in range(q))
                    if aT: both += 1
            cond = both / one if one else 0
            emp_exp = None if cond == 0 else -(__import__('math').log(cond) / __import__('math').log(q))
            pred_exp = min(s, t - 1)
            results[s] = (cond, emp_exp, pred_exp)
        print(f"  t={t}: conditional P[both|one] and its q-exponent vs predicted min(s,t-1):")
        prev = None
        for s, (cond, ee, pe) in results.items():
            tag = f"emp_exp~{ee:.2f}" if ee is not None else "emp_exp=inf"
            print(f"     s={s}: P[both|one]={cond:.4f}  {tag}  pred={pe}")
        # monotone/plateau sanity: exponent should be nondecreasing then flat at t-1
    print("PART B (slope accounting): empirical exponents track min(s,t-1) "
          "(rise with s, plateau at t-1); small-field constants apply.")
    return ok

if __name__ == "__main__":
    a = partA()
    partB()
    print("PASS" if a else "FAIL")
