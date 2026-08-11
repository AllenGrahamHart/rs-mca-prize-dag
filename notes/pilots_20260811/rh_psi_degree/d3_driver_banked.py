# ===================================================================
# ROUND-32 DRIVER (rh_fr_algebraic).  Everything above this line is a
# byte-identical scratch copy of notes/pilots_20260810/rh_type2_stratum/
# d3_census.py lines 1-345 (the round-31 decoder: BM + Vandermonde +
# nullspace + analyse()).  Only the driver below is new.
#
# QUESTION: for a REALIZABLE pencil, what is max_gamma |S_gamma ^ W|
# when W is the CANONICAL joint support W* = S_g u S_h of a pair
# MINIMISING the union (a* = min pair union), versus the planted W?
# ===================================================================

FR = dict(cells=0, pencils=0, canon=0,
          ov_ok=0, ov_bad=0, fib_ok=0, fib_bad=0, c2_ok=0, c2_bad=0,
          fr_ok=0, fr_bad=0, t1hist={}, xmax_planted=[], xmax_canon=[],
          astar=[], pairwise_bad=0, need_ok=0, need_bad=0)


def fibres(Wsorted, vg, vh):
    """mu: W -> P^1 for the representation pair (vg,vh):  z_g = vg + g*vh.
    x is killed by the finite slope -vg[x]/vh[x] when vh[x] != 0, else by
    the slope 'inf' (which is vh's own zero set inside W)."""
    mu = {}
    for x in Wsorted:
        b = vh.get(x, 0)
        if b == 0:
            mu[x] = "inf"
        else:
            mu[x] = (-vg.get(x, 0)) * inv(b) % q
    n = {}
    for x in Wsorted:
        n[mu[x]] = n.get(mu[x], 0) + 1
    return mu, n


def canonical_pass(recs0):
    """recs0: supported-slope records of ANY basis of the pencil.
    Re-runs the analysis in the basis (v_g, v_h) of a MINIMISING pair."""
    n = len(recs0)
    if n < 3:
        return None
    best, bestpair = None, None
    for i in range(n):
        for k in range(i + 1, n):
            u = len(recs0[i]["S"] | recs0[k]["S"])
            if best is None or u < best:
                best, bestpair = u, (i, k)
    i, k = bestpair
    vg, vh = recs0[i]["v"], recs0[k]["v"]
    W, recs = analyse(vg, vh)
    if len(W) != best:
        return None
    return best, W, recs, vg, vh


def fr_record(a_planted, W0, recs0):
    FR["pencils"] += 1
    if recs0:
        FR["xmax_planted"].append(max(len(rc["S"] & set(W0)) for rc in recs0))
    out = canonical_pass(recs0)
    if out is None:
        return
    astar, W, recs, vg, vh = out
    FR["canon"] += 1
    FR["astar"].append(astar)
    Wset = set(W)
    T = len(recs)
    t1 = sum(1 for rc in recs if rc["typ"] == 1)
    FR["t1hist"][t1] = FR["t1hist"].get(t1, 0) + 1
    mu, nfib = fibres(W, vg, vh)
    # (FIB) identity: the fibres partition W
    if sum(nfib.values()) == astar:
        FR["fib_ok"] += 1
    else:
        FR["fib_bad"] += 1
    xmax = 0
    for rc in recs:
        X = len(rc["S"] & Wset)
        xmax = max(xmax, X)
        # (C2) spend inequality for this W
        if rc["typ"] == 2:
            if rc["p"] >= R1 - astar + rc["n_gam"]:
                FR["c2_ok"] += 1
            else:
                FR["c2_bad"] += 1
        # (OV+): for EVERY g != gamma in P^1,  n_g - |S ^ F_g| <= p_gamma
        me = rc["gam"] if rc["tag"] == "f" else "inf"
        for gslope, ng in nfib.items():
            if gslope == me:
                continue
            s = sum(1 for x in Wset if mu[x] == gslope and x in rc["S"])
            if ng - s <= rc["p"]:
                FR["ov_ok"] += 1
            else:
                FR["ov_bad"] += 1
        # (FR) chain: X <= |S^S_g| + |S^S_h| <= 2(2rho - a*)
        if rc["typ"] == 2 and X > 2 * (2 * rho - astar):
            FR["fr_bad"] += 1
        elif rc["typ"] == 2:
            FR["fr_ok"] += 1
    FR["xmax_canon"].append((astar, xmax, T, t1))
    # pairwise sanity: no supported pair beats a*
    for i in range(len(recs)):
        for k in range(i + 1, len(recs)):
            if len(recs[i]["S"] | recs[k]["S"]) < astar:
                FR["pairwise_bad"] += 1


def build_modeB(a, p):
    """round-31 MODE B: plant a third slope with |S_3 \\ W| = p."""
    S1, S2 = rand_supp_pair(a)
    Wset = S1 | S2
    outside = [x for x in D if x not in Wset]
    if p > len(outside):
        return None
    P = set(random.sample(outside, p))
    Z = sorted(Wset | P, key=lambda x: IDX[x])
    Mv = [[pow(x, i, q) for x in Z] for i in range(R)]
    ns = nullspace(Mv, len(Z))
    if not ns:
        return None
    co = [random.randrange(q) for _ in ns]
    kv = [0] * len(Z)
    for cc, bs in zip(co, ns):
        for i2 in range(len(Z)):
            kv[i2] = (kv[i2] + cc * bs[i2]) % q
    kap = {Z[i2]: kv[i2] for i2 in range(len(Z)) if kv[i2]}
    if not all(x in kap for x in P):
        return None
    inW = [x for x in Wset if x in kap]
    k3 = rho - p
    if k3 < 0 or k3 > len(inW):
        return None
    S3inW = set(random.sample(inW, k3))
    v1, v2 = {}, {}
    for src, dst in ((S1, v1), (S2, v2)):
        for x in src:
            if x in S3inW:
                dst[x] = random.randrange(1, q)
            elif x in kap:
                dst[x] = kap[x]
            else:
                return None
    return v1, v2


random.seed(20260810 + m * 1000 + q)
say("=" * 74)
say("D3 (round 32) FR CENSUS   m=%d q=%d   rho=%d N=%d R+1=%d" % (m, q, rho, N, R1))
say("   incidence bound 3m-3 = %d ;  target 2m = %d ;  2(m-1) = %d"
    % (3 * m - 3, 2 * m, 2 * (m - 1)))
say("=" * 74)
say()
say("PRE-REGISTERED (PREREG R4): P4.1 planted-W max |S^W| exceeds 2m and")
say("reaches rho-(R+1-a)=%d ; P4.2/P4.3 zero (OV+)/(FR) violations at the" % (rho - (R1 - (8 * m - 2))))
say("canonical W* ; P4.4 census cannot separate 2m from 3m-3 ; P4.5 T_1=2.")
say()

for a in (8 * m - 2, 6 * m):
    lo = max(1, R1 - a)
    for p in range(lo, rho + 1):
        made = 0
        for _ in range(NT * 8):
            if made >= NT:
                break
            b = build_modeB(a, p)
            if b is None:
                continue
            W0, recs0 = analyse(b[0], b[1])
            if len(W0) != a:
                continue
            made += 1
            fr_record(a, W0, recs0)
    say("  planted a=%-5d : pencils=%-5d canonical passes=%-5d" % (a, FR["pencils"], FR["canon"]))

say()
say("--- RESULTS ---")
xp = FR["xmax_planted"]
say("  planted W  : max |S_gamma ^ W| over %d pencils : max %s  mean %.3f"
    % (len(xp), max(xp) if xp else None, (sum(xp) / len(xp)) if xp else 0))
say("               vs 2m=%d : exceeded in %d / %d pencils"
    % (2 * m, sum(1 for v in xp if v > 2 * m), len(xp)))
say("               vs 3m-3=%d : exceeded in %d / %d pencils"
    % (3 * m - 3, sum(1 for v in xp if v > 3 * m - 3), len(xp)))
xc = FR["xmax_canon"]
if xc:
    say("  canonical W*: a* histogram %s" % sorted({v[0]: 0 for v in xc}))
    say("               max |S_gamma ^ W*| : max %d  mean %.3f"
        % (max(v[1] for v in xc), sum(v[1] for v in xc) / len(xc)))
    say("               vs 2m=%d : exceeded in %d / %d"
        % (2 * m, sum(1 for v in xc if v[1] > 2 * m), len(xc)))
    say("               vs 2(2rho-a*) (the theorem) : exceeded in %d / %d"
        % (sum(1 for v in xc if v[1] > 2 * (2 * rho - v[0])), len(xc)))
    say("               vs 3m-3=%d : exceeded in %d / %d"
        % (3 * m - 3, sum(1 for v in xc if v[1] > 3 * m - 3), len(xc)))
    tab = {}
    for astar, xmax, T, t1 in xc:
        d = tab.setdefault(astar, [0, 0, 0])
        d[0] += 1
        d[1] = max(d[1], xmax)
        d[2] = max(d[2], T)
    say("     a*     n    max X   maxT   2(2rho-a*)   2m   3m-3")
    for astar in sorted(tab):
        d = tab[astar]
        say("  %5d %5d %7d %6d %11d %5d %6d"
            % (astar, d[0], d[1], d[2], 2 * (2 * rho - astar), 2 * m, 3 * m - 3))
say("  T_1 histogram at W* : %s" % sorted(FR["t1hist"].items()))
say()
say("--- FALSIFIERS ---")
say("  (FIB) fibres partition W*        : OK %d  BAD %d" % (FR["fib_ok"], FR["fib_bad"]))
say("  (OV+) n_g - |S^F_g| <= p_gamma   : OK %d  BAD %d" % (FR["ov_ok"], FR["ov_bad"]))
say("  (C2)  p >= R+1-a*+n_gamma        : OK %d  BAD %d" % (FR["c2_ok"], FR["c2_bad"]))
say("  (FR)  X <= 2(2rho-a*)            : OK %d  BAD %d" % (FR["fr_ok"], FR["fr_bad"]))
say("  a* minimality violations         : %d" % FR["pairwise_bad"])
say("  (round-31 carried checks) GNF OK %d BAD %d ; w*_bad %d ; TR1' bad %d"
    % (STATS["gnf_ok"], STATS["gnf_bad"], STATS["wstar_bad"], STATS["tr1_bad"]))
say()
say("  max T over all pencils = %d   (rho+2 = %d)  -> (SAT3) UNTESTED: %s"
    % (STATS["maxT"], rho + 2, STATS["maxT"] < rho + 2))
say("=== END d3_frcensus m=%d q=%d ===" % (m, q))

sys.stdout.write("\n".join(OUT) + "\n")
