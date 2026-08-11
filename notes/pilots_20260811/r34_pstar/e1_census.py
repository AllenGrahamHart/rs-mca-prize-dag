"""r34_pstar E1: the p* spectrum of pencils at wide cells.

Conventions (matching background/nodes/rate_half_ca_hankel_split_pencil_equivalence):
  D subset F_q, |D| = n, k, R = n-k, 1 <= r <= R, rho = R-r.
  A pencil is a pair of syndrome vectors y0, y1 in F_q^R.
  (The syndrome map e |-> (sum_x e(x) v_x x^m)_{m<R} is a rank-R matrix
   (v_x x^m), hence SURJECTIVE onto F_q^R, so an arbitrary pair y0,y1 is
   realised by an actual received pair.  No v_x is needed below.)
  M_i(y) = (y_{s+j})_{0<=s<R-i, 0<=j<=i}   ((R-i) x (i+1))
  Ann(V)_i = ker[M_i(y0); M_i(y1)],  p* = min{ i : Ann(V)_i != 0 }
  K_0 = Ann(V)_r,   h_r = rank[M_r(y0);M_r(y1)] = r+1-dim K_0
  D_r(D) = monic squarefree degree-r polys with all roots in D
  column-far  <=>  K_0 cap D_r(D) = empty
Stdlib only.  Run under tools/ramguard.
"""
import sys, random
from itertools import combinations


def rank_mod(rows, ncols, q):
    rows = [r[:] for r in rows]
    nr = len(rows)
    row = 0
    for c in range(ncols):
        piv = -1
        for t in range(row, nr):
            if rows[t][c]:
                piv = t
                break
        if piv < 0:
            continue
        rows[row], rows[piv] = rows[piv], rows[row]
        inv = pow(rows[row][c], q - 2, q)
        rows[row] = [(v * inv) % q for v in rows[row]]
        pr = rows[row]
        for t in range(nr):
            if t != row and rows[t][c]:
                f = rows[t][c]
                rt = rows[t]
                rows[t] = [(rt[j] - f * pr[j]) % q for j in range(ncols)]
        row += 1
        if row == nr:
            break
    return row


def nullspace(rows, ncols, q):
    """Return a basis of the nullspace of the given matrix over F_q."""
    rows = [r[:] for r in rows]
    nr = len(rows)
    piv_cols = []
    row = 0
    for c in range(ncols):
        piv = -1
        for t in range(row, nr):
            if rows[t][c]:
                piv = t
                break
        if piv < 0:
            continue
        rows[row], rows[piv] = rows[piv], rows[row]
        inv = pow(rows[row][c], q - 2, q)
        rows[row] = [(v * inv) % q for v in rows[row]]
        pr = rows[row]
        for t in range(nr):
            if t != row and rows[t][c]:
                f = rows[t][c]
                rt = rows[t]
                rows[t] = [(rt[j] - f * pr[j]) % q for j in range(ncols)]
        piv_cols.append(c)
        row += 1
        if row == nr:
            break
    free = [c for c in range(ncols) if c not in piv_cols]
    basis = []
    for fc in free:
        v = [0] * ncols
        v[fc] = 1
        for i, pc in enumerate(piv_cols):
            v[pc] = (-rows[i][fc]) % q
        basis.append(v)
    return basis


def stack(y0, y1, i, R, q):
    rows = []
    for t in range(R - i):
        rows.append([y0[t + j] for j in range(i + 1)])
    for t in range(R - i):
        rows.append([y1[t + j] for j in range(i + 1)])
    return rows


def pstar(y0, y1, R, q, cap):
    """min i<=cap with Ann(V)_i != 0; returns cap+1 if none."""
    for i in range(0, cap + 1):
        if rank_mod(stack(y0, y1, i, R, q), i + 1, q) < i + 1:
            return i
    return cap + 1


def ann_nonzero_at(y0, y1, i, R, q):
    return rank_mod(stack(y0, y1, i, R, q), i + 1, q) < i + 1


def pgen(y, R, q, cap):
    """min i<=cap with ker M_i(y) != 0 (low apolar degree of one slope)."""
    for i in range(0, cap + 1):
        rows = [[y[t + j] for j in range(i + 1)] for t in range(R - i)]
        if rank_mod(rows, i + 1, q) < i + 1:
            return i
    return cap + 1


def poly_mul(a, b, q):
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                out[i + j] = (out[i + j] + ai * bj) % q
    return out


def poly_from_roots(roots, q):
    p = [1]
    for rt in roots:
        p = poly_mul(p, [(-rt) % q, 1], q)
    return p


def poly_gcd(a, b, q):
    a = a[:]
    b = b[:]
    while True:
        while a and a[-1] == 0:
            a.pop()
        while b and b[-1] == 0:
            b.pop()
        if not a:
            return b
        if not b:
            break
        if len(a) < len(b):
            a, b = b, a
        inv = pow(b[-1], q - 2, q)
        shift = len(a) - len(b)
        f = a[-1] * inv % q
        for i in range(len(b)):
            a[shift + i] = (a[shift + i] - f * b[i]) % q
    while a and a[-1] == 0:
        a.pop()
    return a


def build_Dr(D, r, q):
    return [poly_from_roots(c, q) for c in combinations(D, r)]


def in_kernel(sig, y, R, r, q):
    for t in range(R - r):
        s = 0
        for j in range(r + 1):
            s += y[t + j] * sig[j]
        if s % q:
            return False
    return True


def column_far(y0, y1, Dr, R, r, q):
    for sig in Dr:
        if in_kernel(sig, y0, R, r, q) and in_kernel(sig, y1, R, r, q):
            return False
    return True


def bad_slopes(y0, y1, Dr, R, r, q):
    T = 0
    for g in range(q):
        y = [(y0[m] + g * y1[m]) % q for m in range(R)]
        for sig in Dr:
            if in_kernel(sig, y, R, r, q):
                T += 1
                break
    return T


CELLS = [
    # name, q, n, k, r   (D = {0..n-1})
    ("W1_round33", 13, 11, 3, 6),
    ("W2_round33", 11, 10, 2, 6),
    ("S1_sep", 11, 11, 1, 8),
    ("S2_sep", 13, 13, 1, 10),
    ("S3_sep", 17, 17, 1, 13),
    ("L1_lb1", 11, 7, 2, 3),
]


def main():
    seed = 20260811
    random.seed(seed)
    out = open(sys.argv[1], "w")

    def emit(s):
        out.write(s + "\n")
        out.flush()
        print(s)

    emit("# r34_pstar E1 -- p* spectrum census   seed=%d" % seed)
    emit("# cell : q n k r R rho  2rho  ceil(R/2)  generic p*=ceil(2R/3)  4rho<R?")
    for (name, q, n, k, r) in CELLS:
        R = n - k
        rho = R - r
        emit("%-11s q=%2d n=%2d k=%d r=%2d R=%2d rho=%d 2rho=%d ceilR2=%d "
             "gen_p*=%d sep(4rho<R)=%s"
             % (name, q, n, k, r, R, rho, 2 * rho, -(-R // 2), -(-2 * R // 3),
                4 * rho < R))
    emit("")

    NA = int(sys.argv[2]) if len(sys.argv) > 2 else 20000
    NB = int(sys.argv[3]) if len(sys.argv) > 3 else 1500

    for (name, q, n, k, r) in CELLS:
        R = n - k
        rho = R - r
        D = list(range(n))
        na = NA if R <= 12 else max(2000, NA // 8)
        hist = {}
        for _ in range(na):
            y0 = [random.randrange(q) for _ in range(R)]
            y1 = [random.randrange(q) for _ in range(R)]
            ps = pstar(y0, y1, R, q, r)
            hist[ps] = hist.get(ps, 0) + 1
        emit("[A] %s  p* spectrum over %d uniform random pencils (p*=%d means >r)"
             % (name, na, r + 1))
        for kk in sorted(hist):
            emit("     p*=%2d : %6d  (%.5f)" % (kk, hist[kk], hist[kk] / na))
        modal = max(hist, key=lambda z: hist[z])
        emit("     modal p*=%d ; predicted generic ceil(2R/3)=%d ; MATCH=%s"
             % (modal, -(-2 * R // 3), modal == -(-2 * R // 3)))
        emit("     min p* over sample = %d ; #{p* <= floor(R/2)=%d} = %d ; "
             "#{p* <= 2rho=%d} = %d"
             % (min(hist), R // 2, sum(v for kk, v in hist.items() if kk <= R // 2),
                2 * rho, sum(v for kk, v in hist.items() if kk <= 2 * rho)))
        out.flush()

    emit("")
    # Part B: joint p* / column-far / dim K_0 / gcd(K_0)
    for (name, q, n, k, r) in CELLS:
        R = n - k
        rho = R - r
        D = list(range(n))
        Dr = build_Dr(D, r, q)
        nb = NB if len(Dr) <= 1000 else max(300, NB // 5)
        cnt_far = 0
        joint = {}
        dimK = {}
        gcdmatch = 0
        for _ in range(nb):
            y0 = [random.randrange(q) for _ in range(R)]
            y1 = [random.randrange(q) for _ in range(R)]
            far = column_far(y0, y1, Dr, R, r, q)
            ps = pstar(y0, y1, R, q, r)
            hr = rank_mod(stack(y0, y1, r, R, q), r + 1, q)
            dk = r + 1 - hr
            if far:
                cnt_far += 1
                joint[ps] = joint.get(ps, 0) + 1
                dimK[dk] = dimK.get(dk, 0) + 1
                if dk > 0:
                    ns = nullspace(stack(y0, y1, r, R, q), r + 1, q)
                    g = ns[0]
                    for v in ns[1:]:
                        g = poly_gcd(g, v, q)
                    if ps <= r and len(g) - 1 == ps:
                        gcdmatch += 1
        emit("[B] %s  |D_r(D)|=%d  %d samples : column-far %d (%.4f)"
             % (name, len(Dr), nb, cnt_far, cnt_far / nb))
        emit("     p* spectrum RESTRICTED TO COLUMN-FAR: %s"
             % (" ".join("%d:%d" % (kk, joint[kk]) for kk in sorted(joint))))
        emit("     dim K_0 spectrum (column-far): %s"
             % (" ".join("%d:%d" % (kk, dimK[kk]) for kk in sorted(dimK))))
        emit("     #{column-far, dimK_0>0, deg gcd(K_0) == p*} = %d" % gcdmatch)
        emit("     predicted r+1-2rho = %d ; r+1-rho = %d"
             % (r + 1 - 2 * rho, r + 1 - rho))
        out.flush()

    emit("")
    # Part D: LB1 cell -- p* conditioned on dim K_0 = 0
    name, q, n, k, r = ("L1_lb1", 11, 7, 2, 3)
    R = n - k
    D = list(range(n))
    Dr = build_Dr(D, r, q)
    c0 = {}
    cpos = {}
    far0 = 0
    tot0 = 0
    for _ in range(4000):
        y0 = [random.randrange(q) for _ in range(R)]
        y1 = [random.randrange(q) for _ in range(R)]
        hr = rank_mod(stack(y0, y1, r, R, q), r + 1, q)
        dk = r + 1 - hr
        ps = pstar(y0, y1, R, q, r)
        if dk == 0:
            tot0 += 1
            c0[ps] = c0.get(ps, 0) + 1
            if column_far(y0, y1, Dr, R, r, q):
                far0 += 1
        else:
            cpos[ps] = cpos.get(ps, 0) + 1
    emit("[D] LB1 cell (n=7,k=2,r=3,q=11) R=%d r=%d : 4000 pencils" % (R, r))
    emit("     dim K_0 = 0 : %d of 4000 ; of those column-far %d" % (tot0, far0))
    emit("     p* | dimK_0=0 : %s   (p*=%d means > r)"
         % (" ".join("%d:%d" % (kk, c0[kk]) for kk in sorted(c0)), r + 1))
    emit("     p* | dimK_0>0 : %s"
         % (" ".join("%d:%d" % (kk, cpos[kk]) for kk in sorted(cpos))))
    emit("     TAUTOLOGY CHECK dim K_0 = 0 <=> p* > r : violations = %d"
         % (sum(v for kk, v in c0.items() if kk <= r)
            + sum(v for kk, v in cpos.items() if kk > r)))
    out.close()


if __name__ == "__main__":
    main()
