#!/usr/bin/env python3
"""ms_exact: exact char-0 count at the antipodal-pair-locator target, via the
PARITY THEOREM.  No field, no background, no enumeration of the full subset
space.

Setting: n = 2M, M = 2^r, zeta = primitive n-th root, omega = zeta^2 primitive
M-th root, K = M/2 = dim Z[omega] (min poly z^K + 1).  Subsets B of mu_n with
|B| = m = M - 1, decomposed as (S, sigma, T) over the M antipodal pairs, with
    e1 = P = sum_{j in S} sigma_j zeta^j
    e2 = E(S,sigma) - omega_T,   E = sum_{j<j' in S} sigma_j sigma_j' zeta^{j+j'}

PARITY THEOREM (proved here, verified below).  Write S = S_even u S_odd.  The
odd part of E (its Z[omega]-coefficient of zeta) equals  zeta * X * Y  with
    X = sum_{j in S_even} sigma_j omega^{j/2},  Y = sum_{j in S_odd} sigma_j omega^{(j-1)/2},
whose exponents both lie in [0, K) -- a Q-basis of Q(omega).  Hence X = 0 iff
S_even is empty and Y = 0 iff S_odd is empty, and since Z[omega] is a domain:

    E(S,sigma) lies in Z[omega]  <=>  S is contained in the even pairs
                                      or in the odd pairs.

Since omega_T is always in Z[omega], any target c in Z[omega] -- in particular
the antipodal-pair-locator targets c = omega^i (i.e. e2(B) = x^2, x in mu_n) --
receives contributions ONLY from such S.  Corollary: only strata
|S| = s <= K = n/4 contribute.

Prescribed-sum count with exclusion (closed form).  T is chosen pairwise:
d_i = [i in T] - [i+K in T] in {-1,0,1} determines omega_T = sum d_i omega^i
uniquely.  With forced indices required to be outside S,
    #{T} = C(A, (h - s')/2),  s' = |supp d|,  A = #{i : d_i = 0, both i, i+K free}
(zero unless every forced index is free, h >= s', h - s' even).

Cost: (3^K - 1)/2 nodes x O(K).  n=32 -> 3^8 = 6561; n=64 -> 3^16 = 43M.
"""
import json, sys
from math import comb


def run(n, verbose=False):
    M = n // 2
    K = M // 2
    m = M - 1
    assert M & (M - 1) == 0 and K >= 1, "M must be a power of two"

    def mul_omega_pow(vec, e, sg):
        """sg * omega^e * vec, in the basis omega^0..omega^{K-1} (omega^K = -1)."""
        out = [0] * K
        for i, ci in enumerate(vec):
            if not ci:
                continue
            j = i + e
            s = sg
            while j >= K:
                j -= K
                s = -s
            out[j] += s * ci
        return out

    total = 0
    stratum = {}
    # parity class 0 = even pairs S={2u}, class 1 = odd pairs S={2v+1}
    for cls in (0, 1):
        stack = [(0, [0] * K, [0] * K, 0, ())]  # (u, P, E, s, chosen U)
        while stack:
            u, P, E, s, ch = stack.pop()
            if u == K:
                if s % 2 == 0:
                    continue
                h = (m - s) // 2
                if h < 0:
                    continue
                # E for the odd class carries an extra factor omega
                Ee = mul_omega_pow(E, 1, 1) if cls else E
                # tau = Ee - c, c = omega^0 = 1
                tau = list(Ee)
                tau[0] -= 1
                ok = True
                sp = 0
                for t in tau:
                    if t < -1 or t > 1:
                        ok = False
                        break
                    if t:
                        sp += 1
                if not ok or sp > h or (h - sp) % 2:
                    continue
                S = set((2 * x) if cls == 0 else (2 * x + 1) for x in ch)
                A = 0
                good = True
                for i in range(K):
                    di = tau[i]
                    if di == 1:
                        if i in S:
                            good = False
                            break
                    elif di == -1:
                        if (i + K) in S:
                            good = False
                            break
                    else:
                        if (i not in S) and ((i + K) not in S):
                            A += 1
                if not good:
                    continue
                r = (h - sp) // 2
                if r > A:
                    continue
                add = 2 * comb(A, r)          # factor 2: sigma -> -sigma
                total += add
                stratum[s] = stratum.get(s, 0) + add
                continue
            stack.append((u + 1, P, E, s, ch))          # skip pair u
            sgs = (1,) if s == 0 else (1, -1)           # fix first sign: half
            for sg in sgs:
                P2 = list(P)
                # P2 += sg * omega^u
                j, ss = u, sg
                while j >= K:
                    j -= K
                    ss = -ss
                P2[j] += ss
                # E2 = E + sg*omega^u * P
                inc = mul_omega_pow(P, u, sg)
                E2 = [E[i] + inc[i] for i in range(K)]
                stack.append((u + 1, P2, E2, s + 1, ch + (u,)))
    return dict(n=n, M=M, K=K, m=m,
                ANTIPODAL_exact=total,
                per_stratum={str(k): v for k, v in sorted(stratum.items())},
                stratum_ceiling=K,
                PLATEAU=comb(M - 1, M // 2),
                STRAT1_closed_form=(M + 2) * comb(K - 1, K // 2 - 1) if K >= 2 else None)


if __name__ == "__main__":
    ns = [int(x) for x in sys.argv[1].split(",")]
    out = sys.argv[2] if len(sys.argv) > 2 else None
    res = []
    for n in ns:
        r = run(n)
        r["ratio_to_plateau"] = r["ANTIPODAL_exact"] / r["PLATEAU"]
        res.append(r)
        print(json.dumps(r))
        sys.stdout.flush()
        if out:
            with open(out, "w") as f:
                json.dump(res, f, indent=1)
