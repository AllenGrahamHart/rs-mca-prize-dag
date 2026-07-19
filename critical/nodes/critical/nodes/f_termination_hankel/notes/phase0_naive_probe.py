# Phase-0 gate: Hankel-kernel sparse-word support structure over F_p.
# Measures the two quantities Phase-1 scales: support DIAMETER and the
# support-lattice #closed-sets. Validates the object (rich, non-coset,
# low-diameter supports appear = E17 signature) before Modal scale-up.
import itertools, random
random.seed(1)
P = 17

def kernel_basis(rows, ncol):
    # rows: list of length-ncol vectors over F_P; return a basis of the right kernel
    M = [r[:] for r in rows]
    piv = {}
    r = 0
    for c in range(ncol):
        pr = next((i for i in range(r, len(M)) if M[i][c] % P), None)
        if pr is None: continue
        M[r], M[pr] = M[pr], M[r]
        inv = pow(M[r][c], P-2, P)
        M[r] = [(x*inv) % P for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] % P:
                f = M[i][c]; M[i] = [(a - f*b) % P for a,b in zip(M[i], M[r])]
        piv[c] = r; r += 1
    free = [c for c in range(ncol) if c not in piv]
    basis = []
    for fc in free:
        v = [0]*ncol; v[fc] = 1
        for c, rr in piv.items():
            v[c] = (-M[rr][fc]) % P
        basis.append(v)
    return basis

def min_weight_supports(basis, ncol, maxw=4):
    # exhaustively find minimal-weight nonzero kernel vectors' supports
    if not basis: return set()
    k = len(basis)
    sig = {}
    for coeffs in itertools.product(range(P), repeat=k):
        if not any(coeffs): continue
        v = [0]*ncol
        for c, b in zip(coeffs, basis):
            if c:
                for j in range(ncol): v[j] = (v[j] + c*b[j]) % P
        supp = tuple(j for j in range(ncol) if v[j])
        if 1 <= len(supp) <= maxw:
            sig[supp] = True
    # keep minimal supports (not containing a smaller found support)
    S = sorted(sig, key=len)
    minimal = []
    for s in S:
        ss = set(s)
        if not any(set(m) <= ss for m in minimal):
            minimal.append(s)
    return set(minimal)

def closed_sets(supports):
    # union-closure of the support family (+ empty set)
    L = {frozenset()}
    fam = [frozenset(s) for s in supports]
    changed = True
    cur = set(fam) | {frozenset()}
    while True:
        new = set(cur)
        for a in cur:
            for b in fam:
                new.add(a | b)
        if new == cur: break
        cur = new
    return cur

def hankel_census(n_seq, ncol, trials=4000):
    # Hankel matrix H[i][j] = s[i+j]; rows i=0..nrow-1, cols j=0..ncol-1
    nrow = n_seq - ncol
    diam_hist = {}; ncs_hist = {}; noncoset = 0; total_flats = 0; examples = []
    for _ in range(trials):
        s = [random.randrange(P) for _ in range(n_seq)]
        rows = [[s[i+j] for j in range(ncol)] for i in range(nrow)]
        basis = kernel_basis(rows, ncol)
        if not basis: continue
        supp = min_weight_supports(basis, ncol, maxw=4)
        supp = {t for t in supp if len(t) >= 2}   # weight>=2 (weight-1 = forced coords)
        if not supp: continue
        total_flats += 1
        for t in supp:
            d = max(t) - min(t)
            diam_hist[d] = diam_hist.get(d, 0) + 1
            # "coset/AP" heuristic: support is an arithmetic progression?
            if len(t) >= 2:
                diffs = {t[i+1]-t[i] for i in range(len(t)-1)}
                if len(diffs) > 1 and len(t) >= 3:
                    noncoset += 1
                elif len(t) == 2 and (t[1]-t[0]) not in (1,):
                    pass
        ncs = len(closed_sets(supp))
        ncs_hist[ncs] = ncs_hist.get(ncs, 0) + 1
        if len(examples) < 3 and any(len(t)>=2 for t in supp):
            examples.append((ncol, sorted(supp)))
    return dict(ncol=ncol, nseq=n_seq, flats=total_flats,
                diam=dict(sorted(diam_hist.items())),
                ncs=dict(sorted(ncs_hist.items())),
                max_diam=max(diam_hist) if diam_hist else None,
                max_ncs=max(ncs_hist) if ncs_hist else None,
                examples=examples)

for (nseq, ncol) in [(12,6),(16,8),(20,10)]:
    r = hankel_census(nseq, ncol, trials=3000)
    print(f"n_seq={nseq} ncol={ncol}: flats={r['flats']} "
          f"max_diam={r['max_diam']} max_#closed={r['max_ncs']}")
    print("   diam hist:", r['diam'])
    print("   #closed hist:", r['ncs'])
    print("   examples:", r['examples'][:2])
