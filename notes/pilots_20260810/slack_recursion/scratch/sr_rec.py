#!/usr/bin/env python3
"""sr_rec: D1 — is the PARITY RECURSION real?

Re-implementation of the round-28 char-0 antipodal enumerator (validated
against its banked totals 6 / 46 / 1974) with extra bookkeeping:

For the EVEN parity class (S = {2u : u in ch}, ch subset of [0,K)) write, at
level M = n/2 with rho = omega^2 of order K,

    X'' = sum_{u in ch, u even} sigma_u rho^{u/2}
    Y'' = sum_{u in ch, u odd}  sigma_u rho^{(u-1)/2}

The odd (omega-)component of E is omega * X'' * Y'', and the target equation
E - omega_T = c splits as

    (REC-BOX)  X'' * Y'' = sum_j d_{2j+1} rho^j,  d in {-1,0,1}^K.

REC-STRONG (the round-28 one-line note, taken literally) would say the RHS is
0, forcing ch into one level-M parity class and iterating the stratum ceiling.
This script tests REC-STRONG directly (does any CONTRIBUTING node have ch
meeting both parities?) and measures BOXFRAC = the fraction of enumerated
nodes passing the REC-BOX necessary test (the achievable pruning factor).
"""
import json, sys
from math import comb


def run(n, verbose=False):
    M = n // 2
    K = M // 2
    m = M - 1
    KH = K // 2

    def mulw(vec, e, sg, mod):
        out = [0] * mod
        for i, ci in enumerate(vec):
            if not ci:
                continue
            j = i + e
            s = sg
            while j >= mod:
                j -= mod
                s = -s
            out[j] += s * ci
        return out

    total = 0
    stratum = {}
    mixed_contrib = 0
    mixed_examples = []
    pure_contrib = 0
    nodes = 0
    box_pass = 0
    contrib_nodes = 0
    for cls in (0, 1):
        stack = [(0, [0] * K, [0] * K, 0, ())]
        while stack:
            u, P, E, s, ch = stack.pop()
            if u == K:
                if cls == 0:
                    nodes += 1
                    # REC-BOX test on this node (independent of whether it contributes)
                    if K >= 2 and KH >= 1:
                        Xp = [0] * KH
                        Yp = [0] * KH
                        for idx, uu in enumerate(ch):
                            sg = 1
                        # signs are not carried in ch; recomputed below at leaves
                if s % 2 == 0:
                    continue
                h = (m - s) // 2
                if h < 0:
                    continue
                Ee = mulw(E, 1, 1, K) if cls else E
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
                add = 2 * comb(A, r)
                total += add
                stratum[s] = stratum.get(s, 0) + add
                if cls == 0:
                    contrib_nodes += 1
                    ev = [x for x in ch if x % 2 == 0]
                    od = [x for x in ch if x % 2 == 1]
                    if ev and od:
                        mixed_contrib += 1
                        if len(mixed_examples) < 6:
                            mixed_examples.append(dict(ch=list(ch), s=s,
                                                       add=add,
                                                       even_part=ev, odd_part=od))
                    else:
                        pure_contrib += 1
                continue
            stack.append((u + 1, P, E, s, ch))
            sgs = (1,) if s == 0 else (1, -1)
            for sg in sgs:
                P2 = list(P)
                j, ss = u, sg
                while j >= K:
                    j -= K
                    ss = -ss
                P2[j] += ss
                inc = mulw(P, u, sg, K)
                E2 = [E[i] + inc[i] for i in range(K)]
                stack.append((u + 1, P2, E2, s + 1, ch + ((u, sg),) if False
                              else ch + (u,)))
    return dict(n=n, M=M, K=K, m=m, ANTIPODAL_exact=total,
                per_stratum={str(k): v for k, v in sorted(stratum.items())},
                PLATEAU=comb(M - 1, M // 2),
                contributing_nodes_evenclass=contrib_nodes,
                REC_STRONG_counterexamples=mixed_contrib,
                pure_parity_contributors=pure_contrib,
                REC_STRONG_verdict=("REFUTED" if mixed_contrib else "consistent"),
                mixed_examples=mixed_examples)


def boxfrac(n):
    """BOXFRAC over the even-class enumeration: fraction of (ch,sigma) nodes
    whose X''*Y'' lies in the {-1,0,1} box (the REC-BOX necessary test)."""
    M = n // 2
    K = M // 2
    KH = K // 2
    if KH < 1:
        return None
    tot = 0
    ok = 0
    # enumerate sigma-signed subsets of [0,K) with the first sign fixed
    stack = [(0, (), ())]
    out = []
    def rec(u, ev, od):
        nonlocal tot, ok
        if u == K:
            tot += 1
            X = [0] * KH
            Y = [0] * KH
            for (v, sg) in ev:
                X[v] += sg
            for (w, sg) in od:
                Y[w] += sg
            if not any(X) or not any(Y):
                ok += 1          # one parity class: product 0, trivially in box
                return
            Z = [0] * KH
            for i, xi in enumerate(X):
                if not xi:
                    continue
                for j, yj in enumerate(Y):
                    if not yj:
                        continue
                    k2 = i + j
                    s = xi * yj
                    while k2 >= KH:
                        k2 -= KH
                        s = -s
                    Z[k2] += s
            if all(-1 <= z <= 1 for z in Z):
                ok += 1
            return
        rec(u + 1, ev, od)
        for sg in (1, -1):
            if u % 2 == 0:
                rec(u + 1, ev + ((u // 2, sg),), od)
            else:
                rec(u + 1, ev, od + (((u - 1) // 2, sg),))
    sys.setrecursionlimit(10000)
    rec(0, (), ())
    return dict(n=n, K=K, nodes=tot, box_pass=ok, BOXFRAC=ok / tot,
                prune_factor=tot / ok if ok else None)


if __name__ == "__main__":
    ns = [int(x) for x in sys.argv[1].split(",")]
    out = sys.argv[2] if len(sys.argv) > 2 else None
    res = []
    for n in ns:
        r = run(n)
        r["boxfrac"] = boxfrac(n)
        res.append(r)
        print(json.dumps(r), flush=True)
        if out:
            with open(out, "w") as f:
                json.dump(res, f, indent=1)
