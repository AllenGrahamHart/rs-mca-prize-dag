"""D2/D3 sparse side: EXACT S_sparse structure at scaled rows, and F_COLL --
the sharp scaled form of falsifier F2.

Setting (RH-SPLIT / rate_half_mca_sparse_layer_reduction): a sparse pair
(e1,e2) with support union E, |E| = e <= r = n_s - a, a = K + tau.
Facts derived here and verified by brute force at (n_s,q) = (8,17):

 (T) every TANGENT slope is MCA-bad (witness c = 0, agreement set
     (D\E) u {j} of size n_s-e+1 >= a, and both components are forced to
     the zero codeword there while (e1(j),e2(j)) != 0).  Hence
     S_sparse(a) >= min(r, q)  -- the tangent floor.
 (N) a NON-TANGENT MCA-bad slope needs an ambiguity codeword c != 0 with
     >= a-e roots in D\E, so c = h * P_Z with Z subset D\E, |Z| = a-e,
     deg h <= e-tau-1, and the defining system
        e1|_E + gamma e2|_E = h * P_Z|_E
     is LINEAR in (gamma, h): e equations, e-tau+1 unknowns.
     Projectively: the pencil U = span(e1,e2) must MEET the subspace
     V_Z = P_Z|_E * F[X]_{<e-tau}|_E, dim e-tau, codim tau in F^E.

 At the minimal support e = tau+1 (h constant, V_Z = <p_Z> a POINT of
 P^(e-1)), a bad slope exists for Z exactly when [p_Z] lies on the
 projective line P(U).  So
     F_COLL(n_s,q,tau) = max over E and over lines l of #{[p_Z] in l}
 is exactly the non-tangent sparse payload at minimal support -- the
 sharp scaled form of F2.  |Z| = a - e = K - 1 always.
"""
import math
from math import comb, isqrt
from itertools import combinations

import ffield as ff


def proj_norm(v, q):
    for x in v:
        if x:
            inv = pow(x, q - 2, q)
            return tuple((y * inv) % q for y in v)
    return None


def pz_points(n_s, K, q, tau, E_idx):
    """the locator point set { [p_Z] } in P^(e-1), e = tau+1, |Z| = K-1"""
    D = ff.subgroup(n_s, q)
    E = [D[i] for i in E_idx]
    out = [D[i] for i in range(n_s) if i not in E_idx]
    pts = set()
    for Z in combinations(out, K - 1):
        v = []
        for j in E:
            p = 1
            for x in Z:
                p = p * (j - x) % q
            v.append(p)
        pn = proj_norm(v, q)
        if pn is not None:
            pts.add(pn)
    return pts, comb(len(out), K - 1)


def max_collinear(pts, e, q):
    """max number of the given projective points on one projective line"""
    P = [list(p) for p in pts]
    if len(P) <= 2:
        return len(P)
    if e == 2:                       # P^1: every point is on 'the' line
        return len(P)
    lines = {}
    if e == 3:                       # P^2: line through 2 points = cross product
        for i in range(len(P)):
            ax, ay, az = P[i]
            for j in range(i + 1, len(P)):
                bx, by, bz = P[j]
                key = proj_norm(((ay * bz - az * by) % q,
                                 (az * bx - ax * bz) % q,
                                 (ax * by - ay * bx) % q), q)
                s = lines.setdefault(key, set())
                s.add(i)
                s.add(j)
    else:
        for i in range(len(P)):
            for j in range(i + 1, len(P)):
                key = ff.canon_subspace([P[i], P[j]], e, q)
                s = lines.setdefault(key, set())
                s.add(i)
                s.add(j)
    return max(len(s) for s in lines.values())


def rot_classes(n_s, e):
    seen, reps = set(), []
    for E in combinations(range(n_s), e):
        c = min(tuple(sorted((x + s) % n_s for x in E)) for s in range(n_s))
        if c not in seen:
            seen.add(c)
            reps.append(c)
    return reps


# ---------------------------------------------------------------- exact e=2
def sparse_e2(n_s, K, q, tau=1):
    """EXACT S_sparse contribution at e=2 (tau=1): the unique rank-2 config
    on 2 points is (1,0),(0,1) up to GL2, so the whole pencil is F^E and
    every Z with p_Z != 0 contributes the slope P_Z(j2)/P_Z(j1)."""
    a = K + tau
    D = ff.subgroup(n_s, q)
    best, arg = 0, None
    for E_idx in rot_classes(n_s, 2):
        j1, j2 = D[E_idx[0]], D[E_idx[1]]
        out = [D[i] for i in range(n_s) if i not in E_idx]
        sl = set()
        for Z in combinations(out, a - 2):
            p1 = p2 = 1
            for x in Z:
                p1 = p1 * (j1 - x) % q
                p2 = p2 * (j2 - x) % q
            if p1 == 0:
                continue
            sl.add(p2 * pow(p1, q - 2, q) % q)
        sl.add(0)                       # the tangent slope of this config
        if len(sl) > best:
            best, arg = len(sl), E_idx
    return best, arg


if __name__ == "__main__":
    print("=== tangent floor (T): S_sparse(a) >= min(r,q), r = n_s - a ===")
    for n_s in (8, 16):
        K = n_s // 2
        for tau in range(1, K):
            a = K + tau
            print(f"  n_s={n_s:<3} a=K+{tau:<2}={a:<3} r={n_s-a:<3} "
                  f"wedge(r<=tau, S<=r): {n_s-a <= tau}")
        print()

    print("=== EXACT S_sparse at e=2, tau=1 (q-independent cost), n_s=8,16 ===")
    print(f"{'n_s':>4} {'q':>10} {'log2q':>7} {'B_s':>8} {'#Z':>8} {'S_e2':>8} "
          f"{'>B_s?':>7} {'upper e-bound':>14}")
    for n_s in (8, 16):
        K = n_s // 2
        for q in (17, 41, 97, 257, 65537, 16777289):
            if (q - 1) % n_s:
                continue
            Bs = isqrt(q)
            v, arg = sparse_e2(n_s, K, q)
            nz = comb(n_s - 2, K - 1)
            ub = max(e + comb(n_s - e, K + 1 - e) for e in range(2, n_s - K))
            print(f"{n_s:>4} {q:>10} {math.log2(q):>7.2f} {Bs:>8} {nz:>8} {v:>8} "
                  f"{str(v > Bs):>7} {ub:>14}")
        print()

    print("=== F_COLL: max collinear locator points (sharp scaled F2), n_s=16 ===")
    print(f"{'n_s':>4} {'tau':>4} {'e':>3} {'q':>8} {'#Z':>7} {'#pts':>7} "
          f"{'F_COLL':>7} {'B_s':>7} {'fires?':>7}")
    for n_s in (16,):
        K = n_s // 2
        for tau in (2, 3):
            e = tau + 1
            for q in (17, 97, 65537):
                if (q - 1) % n_s:
                    continue
                Bs = isqrt(q)
                bestc, nz, npt = 0, 0, 0
                for E_idx in rot_classes(n_s, e)[:(3 if e == 3 else 2)]:
                    pts, nzz = pz_points(n_s, K, q, tau, E_idx)
                    c = max_collinear(pts, e, q)
                    if c > bestc:
                        bestc, nz, npt = c, nzz, len(pts)
                print(f"{n_s:>4} {tau:>4} {e:>3} {q:>8} {nz:>7} {npt:>7} "
                      f"{bestc:>7} {Bs:>7} {str(bestc > Bs):>7}")
