# ===================================================================
# ROUND-33 DRIVER (rh_psi_degree).  Everything above this line is a
# byte-identical scratch copy of
#   notes/pilots_20260810/rh_fr_algebraic/d3_frcensus.py  lines 1-496
# whose own lines 1-345 are byte-identical to round 31's
#   notes/pilots_20260810/rh_type2_stratum/d3_census.py  lines 1-345
# (both diffs run clean this session).  Only this driver is new, and the
# RNG seed is round 32's, so the pencil ensemble is the SAME ensemble.
#
# NEW MEASURABLES (PREREG R0/R3), for every type-2 slope and both W's:
#   h_gamma  = the deg <= a-1 interpolant of  x |-> z_gamma(x) Q_gamma(x)
#              sigma'_W(x)   on W   (the shortened-code K'|_W coordinate;
#              round 32 D2.4)
#   Dh       = deg h_gamma                vs the (C2) cap d = a-(4m+2)
#   Rin      = #{x in W : h_gamma(x)=0}   (predicted = n + X - ov)
#   Rout     = roots of h_gamma outside W, WITH multiplicity
#   nonsplit = degree of the part of h_gamma with no root in F_q
#   ov       = |S_gamma ^ F_gamma|,  cancel = #{x in (W\F)^S : z_x = v_x}
# Falsifiable identities:
#   (JDEC)  d - Rin = o + j + cancel
#   (DEGSUM) Dh = Rin_mult + Rout + nonsplit
#   (AGG)   sum_{supported} X_gamma = sum_{x in W} d_x = a*m - def_in
# ===================================================================

Dset = set(D)
FOURM2 = 4 * m + 2


def poly_eval(c, x):
    r = 0
    for v in reversed(c):
        r = (r * x + v) % q
    return r


def interp_coeffs(nodes, vals):
    """monomial coefficients of the interpolant through (nodes, vals)."""
    n = len(nodes)
    dd = vals[:]
    for k in range(1, n):
        for i in range(n - 1, k - 1, -1):
            dd[i] = (dd[i] - dd[i - 1]) * inv(nodes[i] - nodes[i - k]) % q
    coeffs = [0] * n
    basis = [1] + [0] * (n - 1)
    deg = 0
    for i in range(n):
        if dd[i]:
            for t in range(deg + 1):
                coeffs[t] = (coeffs[t] + dd[i] * basis[t]) % q
        if i < n - 1:
            new = [0] * n
            for t in range(deg + 1):
                new[t + 1] = (new[t + 1] + basis[t]) % q
                new[t] = (new[t] - basis[t] * nodes[i]) % q
            basis = new
            deg += 1
    while len(coeffs) > 1 and coeffs[-1] == 0:
        coeffs.pop()
    return coeffs


def divide_out(c, r):
    n = len(c)
    b = [0] * (n - 1)
    b[n - 2] = c[n - 1]
    for i in range(n - 2, 0, -1):
        b[i - 1] = (c[i] + r * b[i]) % q
    return b


def split_roots(c):
    """multiplicity of every F_q root, plus the degree of the non-split part."""
    mult = {}
    cur = c[:]
    for x in range(q):
        while len(cur) > 1 and poly_eval(cur, x) == 0:
            cur = divide_out(cur, x)
            mult[x] = mult.get(x, 0) + 1
    return mult, len(cur) - 1


PSI = dict(slopes=0, jdec_ok=0, jdec_bad=0, degcap_ok=0, degcap_bad=0,
           rin_ok=0, rin_bad=0, degsum_ok=0, degsum_bad=0,
           agg_ok=0, agg_bad=0, defin=[], rows=[], full_deg=0,
           simple_ok=0, simple_bad=0, t2hist={}, ratio=[], maxT=0)


def psi_record(where, Wsorted, recs):
    """where in {'planted','canon'}"""
    Wset = set(Wsorted)
    a = len(Wsorted)
    dcap = a - FOURM2
    if dcap < 0:
        return
    sp = {x: sigma_prime(Wsorted, x) for x in Wsorted}
    # (AGG): sum over ALL supported slopes of |S ^ W|  vs  sum_{x in W} d_x
    dx = {x: 0 for x in Wsorted}
    sumX = 0
    for rc in recs:
        for x in rc["S"]:
            if x in dx:
                dx[x] += 1
                sumX += 1
    defin = a * m - sum(dx.values())
    if sumX == sum(dx.values()):
        PSI["agg_ok"] += 1
    else:
        PSI["agg_bad"] += 1
    PSI["defin"].append((where, defin, max(dx.values()) if dx else 0))
    PSI["maxT"] = max(PSI["maxT"], len(recs))
    t2 = [rc for rc in recs if rc["typ"] == 2]
    PSI["t2hist"][(where, len(t2))] = PSI["t2hist"].get((where, len(t2)), 0) + 1
    xs = []
    for rc in t2:
        S, z, v = rc["S"], rc["z"], rc["v"]
        X = len(S & Wset)
        u = len(S)
        o = rho - u
        n = a - len(z)
        ov = sum(1 for x in Wsorted if x in S and x not in z)
        cancel = sum(1 for x in Wsorted if x in S and x in z
                     and z[x] == v.get(x, 0))
        j = rc["j"]
        hv = []
        for x in Wsorted:
            Qx = 1
            for s in S:
                Qx = Qx * (x - s) % q
            hv.append(z.get(x, 0) * Qx % q * sp[x] % q)
        Dh = newton_degree(Wsorted, hv)
        Rin = sum(1 for t in hv if t == 0)
        coeffs = interp_coeffs(Wsorted, hv)
        mult, nonsplit = split_roots(coeffs)
        Rin_m = sum(k for x, k in mult.items() if x in Wset)
        Rout = sum(k for x, k in mult.items() if x not in Wset)
        RoutD = sum(k for x, k in mult.items() if x not in Wset and x in Dset)
        PSI["slopes"] += 1
        if Dh <= dcap:
            PSI["degcap_ok"] += 1
        else:
            PSI["degcap_bad"] += 1
        if Rin == n + X - ov:
            PSI["rin_ok"] += 1
        else:
            PSI["rin_bad"] += 1
        if dcap - Rin == o + j + cancel:
            PSI["jdec_ok"] += 1
        else:
            PSI["jdec_bad"] += 1
        if Dh == Rin_m + Rout + nonsplit:
            PSI["degsum_ok"] += 1
        else:
            PSI["degsum_bad"] += 1
        if Rin_m == Rin:
            PSI["simple_ok"] += 1
        else:
            PSI["simple_bad"] += 1
        if Dh == dcap:
            PSI["full_deg"] += 1
        PSI["rows"].append((where, a, X, n, o, j, cancel, ov, Dh, dcap,
                            Rin, Rin_m, Rout, RoutD, nonsplit, len(t2)))
        xs.append(X)
    if xs and where == "canon":
        PSI["ratio"].append((len(xs), max(xs), sum(xs) / len(xs), a))


random.seed(20260810 + m * 1000 + q)
say("=" * 74)
say("D3 (round 33, rh_psi_degree) PSI-DEGREE CENSUS   m=%d q=%d  rho=%d N=%d"
    % (m, q, rho, N))
say("  (C2) degree cap d = a-(4m+2);  target a/4;  mean over type-2 = ?")
say("  PRE-REGISTERED (R3): P3.1 (JDEC) 0 violations; P3.2 def_in=0 mostly;")
say("  P3.3 T_2 = 1 at the canonical W* so max/mean == 1 (ZERO POWER);")
say("  P3.4 Dh = d in >=85%; P3.5 all W-roots simple; P3.6 mean Rout < 2.")
say("=" * 74)
say()

for a in (8 * m - 2, 6 * m):
    lo = max(1, R1 - a)
    made_tot = 0
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
            made_tot += 1
            psi_record("planted", W0, recs0)
            out = canonical_pass(recs0)
            if out is not None:
                astar, Wc, recsc, vg, vh = out
                psi_record("canon", Wc, recsc)
    say("  planted a=%-5d : pencils=%d" % (a, made_tot))

say()
say("--- IDENTITY CHECKS (falsifiers; a single BAD kills the claim) ---")
say("  type-2 slopes measured        : %d" % PSI["slopes"])
say("  (C2) degree cap  Dh <= a-(4m+2): OK %d  BAD %d"
    % (PSI["degcap_ok"], PSI["degcap_bad"]))
say("  Rin = n + X - ov               : OK %d  BAD %d"
    % (PSI["rin_ok"], PSI["rin_bad"]))
say("  (JDEC) d - Rin = o + j + cancel: OK %d  BAD %d"
    % (PSI["jdec_ok"], PSI["jdec_bad"]))
say("  (DEGSUM) Dh = Rin_m+Rout+nonsp : OK %d  BAD %d"
    % (PSI["degsum_ok"], PSI["degsum_bad"]))
say("  every W-root of h simple       : OK %d  BAD %d"
    % (PSI["simple_ok"], PSI["simple_bad"]))
say("  (AGG) sum X = sum_{x in W} d_x : OK %d  BAD %d"
    % (PSI["agg_ok"], PSI["agg_bad"]))
say("  Dh == d exactly (full degree)  : %d / %d" % (PSI["full_deg"], PSI["slopes"]))
dfi = [t[1] for t in PSI["defin"]]
say("  def_in = a*m - sum d_x  : min %s max %s  zero in %d/%d ; max d_x = %s (e=%d)"
    % (min(dfi) if dfi else None, max(dfi) if dfi else None,
       sum(1 for t in dfi if t == 0), len(dfi),
       max([t[2] for t in PSI["defin"]] or [0]), e))
say()
say("--- T_2 (the max/mean question) ---")
for k in sorted(PSI["t2hist"]):
    say("  %-8s T_2 = %d : %d pencils" % (k[0], k[1], PSI["t2hist"][k]))
if PSI["ratio"]:
    mx = max(r[0] for r in PSI["ratio"])
    say("  canonical W*: max T_2 = %d  ->  max/mean = %s"
        % (mx, "1.000 IDENTICALLY (ZERO POWER)" if mx == 1 else "measurable"))
say()
say("--- THE ROOT COUNT OF h_gamma IN W (the mandate's quantity) ---")
say("  where     a  slopes  maxRin  meanRin  d=a-(4m+2)  ceil(a/4)  maxX  a/4  maxDh")
agg = {}
for r in PSI["rows"]:
    key = (r[0], r[1])
    d = agg.setdefault(key, [0, 0, 0, 0, 0, 0])
    d[0] += 1
    d[1] = max(d[1], r[10])
    d[2] += r[10]
    d[3] = max(d[3], r[2])
    d[4] = max(d[4], r[8])
    d[5] = max(d[5], r[9])
for key in sorted(agg):
    d = agg[key]
    a = key[1]
    say("  %-8s %4d %6d %7d %8.3f %11d %10d %5d %5.2f %6d"
        % (key[0], a, d[0], d[1], d[2] / d[0], a - FOURM2, -(-a // 4), d[3],
           a / 4.0, d[4]))
say()
say("--- THE STRATUM SPLIT BY j (is j=0 the X-MAXIMAL stratum?) ---")
say("  where     a   j  slopes  maxX  meanX  maxRin  max(o+j+cancel)  maxRout  maxn")
sp2 = {}
for r in PSI["rows"]:
    key = (r[0], r[1], min(r[5], 3))
    d = sp2.setdefault(key, [0, 0, 0, 0, 0, 0, 0])
    d[0] += 1
    d[1] = max(d[1], r[2])
    d[2] += r[2]
    d[3] = max(d[3], r[10])
    d[4] = max(d[4], r[4] + r[5] + r[6])
    d[5] = max(d[5], r[12])
    d[6] = max(d[6], r[3])
for key in sorted(sp2):
    d = sp2[key]
    say("  %-8s %4d %3s %7d %5d %6.3f %7d %16d %8d %5d"
        % (key[0], key[1], ("%d" % key[2]) if key[2] < 3 else ">=3",
           d[0], d[1], d[2] / d[0], d[3], d[4], d[5], d[6]))
say()
say("--- IS THE TARGET  X <= a/4  SATISFIED?  (4X <= a) ---")
say("  where     j      slopes   X>a/4   worst 4X/a   worst (X, a)")
vt = {}
for r in PSI["rows"]:
    key = (r[0], "j=0" if r[5] == 0 else "j>=1")
    d = vt.setdefault(key, [0, 0, 0.0, (0, 0)])
    d[0] += 1
    if 4 * r[2] > r[1]:
        d[1] += 1
    ratio = 4.0 * r[2] / r[1]
    if ratio > d[2]:
        d[2] = ratio
        d[3] = (r[2], r[1])
for key in sorted(vt):
    d = vt[key]
    say("  %-8s %-5s %8d %7d %12.4f   X=%d a=%d"
        % (key[0], key[1], d[0], d[1], d[2], d[3][0], d[3][1]))
say()
say("--- WHERE THE MISSING DEGREE GOES (R2.3) ---")
say("  Rout = roots of h outside W (with mult); RoutD = those inside D\\W;")
say("  nonsplit = degree with no F_q root.  Predicted: (d-Dh)+Rout+(Rin_m-Rin)")
say("  = o+j+cancel.")
say("  where     a   meanRout  maxRout  meanRoutD  mean nonsplit  mean(d-Dh)")
ag2 = {}
for r in PSI["rows"]:
    key = (r[0], r[1])
    d = ag2.setdefault(key, [0, 0, 0, 0, 0, 0])
    d[0] += 1
    d[1] += r[12]
    d[2] = max(d[2], r[12])
    d[3] += r[13]
    d[4] += r[14]
    d[5] += (r[9] - r[8])
for key in sorted(ag2):
    d = ag2[key]
    say("  %-8s %4d %10.3f %8d %10.3f %14.3f %11.3f"
        % (key[0], key[1], d[1] / d[0], d[2], d[3] / d[0], d[4] / d[0],
           d[5] / d[0]))
say()
say("  max T over pencils = %d  (rho+2 = %d) -> (SAT3) UNTESTED: %s"
    % (PSI["maxT"], rho + 2, PSI["maxT"] < rho + 2))
say("=== END d3_psi m=%d q=%d ===" % (m, q))

sys.stdout.write("\n".join(OUT) + "\n")
