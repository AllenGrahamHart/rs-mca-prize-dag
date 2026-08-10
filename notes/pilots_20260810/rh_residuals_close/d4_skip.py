#!/usr/bin/env python3
"""d2_sunflower.py -- list_profile_bound (round 29).

Validates T1 (sunflower rigidity), the per-line slope cap M_LINE,
T3 (Fisher sub-stratum) and T4 (one-line threshold) at the scaled cell
(n_s, k_s, q) = (8, 4, 17), by explicit enumeration of bad slopes and
their agreement sets for column-far received pairs.

Every claim checked here is an ASSERTION of my own proof; a single
counterexample refutes it and is reported first.
"""
import itertools
import random

q = 17
n = 8
k = 4

# multiplicative subgroup of order n in F_q^*
g = None
for cand in range(2, q):
    seen, x = set(), 1
    for _ in range(q - 1):
        x = x * cand % q
        seen.add(x)
    if len(seen) == q - 1:
        g = cand
        break
zeta = pow(g, (q - 1) // n, q)
D = []
x = 1
for _ in range(n):
    D.append(x)
    x = x * zeta % q
assert len(set(D)) == n, D
inv = [0] + [pow(i, q - 2, q) for i in range(1, q)]

SUBS = {}


def build(a):
    """for each a-subset S: (positions, leading-coeff functional, lagrange basis)"""
    out = []
    for S in itertools.combinations(range(n), a):
        # interpolate degree <= a-1 through points (D[i], y_i), i in S
        basis = []
        for i in S:
            # lagrange poly l_i, coefficients low->high, degree a-1
            coef = [1]
            den = 1
            for j in S:
                if j == i:
                    continue
                den = den * (D[i] - D[j]) % q
                new = [0] * (len(coef) + 1)
                for d, c in enumerate(coef):
                    new[d + 1] = (new[d + 1] + c) % q
                    new[d] = (new[d] - c * D[j]) % q
                coef = new
            di = inv[den % q]
            basis.append([c * di % q for c in coef])
        # BUGFIX (self-caught): the interpolant has degree <= a-1; a codeword
        # needs EVERY coefficient of X^k .. X^{a-1} to vanish, i.e. a-k
        # functionals, not just the leading one.
        lead = [[b[d] for b in basis] for d in range(k, a)]
        out.append((S, lead, basis))
    return out


def _drops(word, S, lead):
    for row in lead:
        s = 0
        for t, i in enumerate(S):
            if word[i]:
                s += row[t] * word[i]
        if s % q:
            return False
    return True


def codewords_at(word, a):
    """all deg<k codewords agreeing with `word` on >= a positions, plus their
    agreement sets.  a > k-1 so each is determined by any a-subset."""
    found = {}
    for S, lead, basis in SUBS[a]:
        if not _drops(word, S, lead):
            continue
        poly = [0] * a
        for t, i in enumerate(S):
            v = word[i]
            if v:
                b = basis[t]
                for d in range(a):
                    poly[d] = (poly[d] + v * b[d]) % q
        assert all(poly[d] == 0 for d in range(k, a)), poly
        key = tuple(poly[:k])
        if key not in found:
            ev = [0] * n
            for idx in range(n):
                acc = 0
                for d in range(k - 1, -1, -1):
                    acc = (acc * D[idx] + key[d]) % q
                ev[idx] = acc
            found[key] = frozenset(i for i in range(n) if ev[i] == word[i])
    return found


def column_far(y1, y2, a):
    for S, lead, basis in SUBS[a]:
        if _drops(y1, S, lead) and _drops(y2, S, lead):
            return False
    return True


def analyse(y1, y2, a):
    """returns (M, records) or None if not column-far"""
    if not column_far(y1, y2, a):
        return None
    slopes = {}
    for lam in range(q):
        w = [(y1[i] + lam * y2[i]) % q for i in range(n)]
        cw = codewords_at(w, a)
        if cw:
            key = min(cw)            # deterministic witness choice
            slopes[lam] = (key, cw[key])
    return slopes


# --- rh_residuals_close (round 32) D4 INSTRUMENTATION, added to a byte-identical
# --- scratch copy of notes/pilots_20260810/list_profile_bound/d2_sunflower.py
# --- (md5 b0273c8a365fea7ce93575c2a734aca5).  No original logic is altered:
# --- only counters are added.
STAT = {a: dict(total=0, skip_M=0, reached=0, guard_pass=0, guard_fail=0,
                fired=0, thetas={}, slack=[]) for a in (5, 6, 7)}


def check(slopes, a, log):
    """T1 + M_LINE on one configuration"""
    r = n - a
    lam_list = sorted(slopes)
    M = len(lam_list)
    STAT[a]["total"] += 1
    if M < 2:
        STAT[a]["skip_M"] += 1
        return M
    lines = {}
    for i in range(M):
        for j in range(i + 1, M):
            lu, mu = lam_list[i], lam_list[j]
            cl, cm = slopes[lu][0], slopes[mu][0]
            d = inv[(lu - mu) % q]
            v = tuple((cl[t] - cm[t]) * d % q for t in range(k))
            u = tuple((cl[t] - lu * v[t]) % q for t in range(k))
            lines.setdefault((u, v), set()).update([lu, mu])
    for (u, v), lam_set in lines.items():
        # E_P = jointly explained set of the code pair (u,v)
        def ev(p, x):
            acc = 0
            for d in range(k - 1, -1, -1):
                acc = (acc * x + p[d]) % q
            return acc
        E = frozenset(i for i in range(n)
                      if ev(u, D[i]) == y1G[i] and ev(v, D[i]) == y2G[i])
        e = len(E)
        # T1(a): E_P == A_lam cap A_mu for every pair on the line
        for lu, mu in itertools.combinations(sorted(lam_set), 2):
            inter = slopes[lu][1] & slopes[mu][1]
            if inter != E:
                log.append(("T1a-FAIL", u, v, lu, mu, sorted(inter), sorted(E)))
        # T1(b): E_P subset A_lam ; T1(c): petals pairwise disjoint
        pets = []
        for lu in sorted(lam_set):
            A = slopes[lu][1]
            if not E <= A:
                log.append(("T1b-FAIL", u, v, lu))
            pets.append(A - E)
        for i in range(len(pets)):
            for j in range(i + 1, len(pets)):
                if pets[i] & pets[j]:
                    log.append(("T1c-FAIL", u, v))
        # M_LINE : m <= 1 + r/(a-e)   and   2a-n <= e <= a-1
        m = len(lam_set)
        if not (2 * a - n <= e <= a - 1):
            log.append(("Erange-FAIL", u, v, e))
        if a - e <= 0 or m > 1 + r / (a - e):
            log.append(("MLINE-FAIL", u, v, m, e, 1 + r / max(a - e, 1)))
    # T3 Fisher sub-stratum
    theta = 0
    for lu, mu in itertools.combinations(lam_list, 2):
        theta = max(theta, len(slopes[lu][1] & slopes[mu][1]))
    STAT[a]["reached"] += 1
    STAT[a]["thetas"][theta] = STAT[a]["thetas"].get(theta, 0) + 1
    if theta * n < a * a:
        bound = (a - theta) / (a * a / n - theta)
        STAT[a]["guard_pass"] += 1
        STAT[a]["slack"].append((M, theta, round(bound, 4)))
        if M > bound + 1e-9:
            STAT[a]["fired"] += 1
            log.append(("T3-FAIL", M, theta, bound))
    else:
        STAT[a]["guard_fail"] += 1
    return M


for a in (5, 6, 7):
    SUBS[a] = build(a)

print("=" * 72)
print("cell (n,k,q) = (%d,%d,%d)   D = %s" % (n, k, q, D))
print("=" * 72)

random.seed(20260810)
log = []
per_a = {5: 0, 6: 0, 7: 0}
best = {5: (0, None), 6: (0, None), 7: (0, None)}
tested = {5: 0, 6: 0, 7: 0}

cands = []
for _ in range(4000):
    cands.append(([random.randrange(q) for _ in range(n)],
                  [random.randrange(q) for _ in range(n)]))
# targeted: build pairs from my own line construction (core E, code pair (u,v))
for _ in range(4000):
    a0 = 5
    E = random.sample(range(n), a0 - 1)
    u = [random.randrange(q) for _ in range(k)]
    v = [random.randrange(q) for _ in range(k)]

    def ev(p, x):
        acc = 0
        for d in range(k - 1, -1, -1):
            acc = (acc * x + p[d]) % q
        return acc
    y1 = [random.randrange(q) for _ in range(n)]
    y2 = [random.randrange(q) for _ in range(n)]
    for i in E:
        y1[i] = ev(u, D[i])
        y2[i] = ev(v, D[i])
    lam = random.randrange(1, q)
    rest = [i for i in range(n) if i not in E]
    for i in rest[:2]:
        y2[i] = (ev(v, D[i]) + random.randrange(1, q)) % q
        y1[i] = (ev(u, D[i]) - lam * (y2[i] - ev(v, D[i]))) % q
    cands.append((y1, y2))

for y1, y2 in cands:
    for a in (5, 6, 7):
        y1G, y2G = y1, y2
        sl = analyse(y1, y2, a)
        if sl is None:
            continue
        tested[a] += 1
        sub = []
        M = check(sl, a, sub)
        if sub:
            log.extend([(a,) + row for row in sub])
            per_a[a] += len(sub)
        if M > best[a][0]:
            best[a] = (M, (list(y1), list(y2)))

print()
print("column-far pairs examined: %s" % tested)
print("max bad-slope count observed (lower bound on B_CAFAR at this cell):")
for a in (5, 6, 7):
    print("   a=%d (sigma=%d, r=%d):  M_max = %d   [n-a+1 = %d]"
          % (a, a - k, n - a, best[a][0], n - a + 1))
print()
print("T1/M_LINE/T3 violations: %d   per a: %s" % (len(log), per_a))
for row in log[:12]:
    print("   ", row)
print()
print("T4 one-line threshold at this cell: a >= ceil((2n+k)/3) = %d"
      % -(-(2 * n + k) // 3))
print("   at a=7 the theorem forces M <= n-a+1 = %d ; observed max = %d"
      % (n - 7 + 1, best[7][0]))
print("=" * 72)

# ---------------- D4: the T3-guard skip fraction ----------------
print()
print("=" * 72)
print("D4  T3-GUARD SKIP FRACTION  (guard: theta*n < a*a)")
print("=" * 72)
tot = sum(STAT[a]["total"] for a in (5, 6, 7))
app = sum(STAT[a]["guard_pass"] for a in (5, 6, 7))
print("  total column-far configurations              : %d" % tot)
print("  T3 test ACTUALLY APPLIED (guard passed)      : %d" % app)
print("  T3 test SKIPPED                              : %d" % (tot - app))
print("  SKIP FRACTION                                : %d/%d = %.6f"
      % (tot - app, tot, (tot - app) / tot))
print("  APPLIED FRACTION                             : %.6f" % (app / tot))
print()
print("   a   total   skipped(M<2)   reached   guard_pass   guard_fail   fired"
      "   a*a/n")
for a in (5, 6, 7):
    s = STAT[a]
    print("  %2d  %6d  %12d  %8d  %11d  %11d  %6d   %.4f"
          % (a, s["total"], s["skip_M"], s["reached"], s["guard_pass"],
             s["guard_fail"], s["fired"], a * a / n))
print()
for a in (5, 6, 7):
    s = STAT[a]
    print("  a=%d theta histogram (over configurations that reached the guard): %s"
          % (a, dict(sorted(s["thetas"].items()))))
print()
print("  MINIMUM POSSIBLE theta: two agreement sets of size >= a inside [n]")
print("  intersect in >= 2a-n points, so theta >= 2a-n always:")
for a in (5, 6, 7):
    print("    a=%d : theta >= %d ; guard needs theta <= %d ; window size %d"
          % (a, 2 * a - n, -(-(a * a) // n) - 1 if (a * a) % n else a * a // n - 1,
             max(0, (-(-(a * a) // n) - 1 if (a * a) % n else a * a // n - 1)
                 - (2 * a - n) + 1)))
print()
print("  For the configurations where the test WAS applied, (M, theta, bound):")
for a in (5, 6, 7):
    s = STAT[a]
    if not s["slack"]:
        print("    a=%d : none" % a)
        continue
    dist = {}
    for (M, th, b) in s["slack"]:
        dist[(M, th, b)] = dist.get((M, th, b), 0) + 1
    print("    a=%d : %d applications, distinct (M,theta,bound) = %s"
          % (a, len(s["slack"]), dict(sorted(dist.items()))))
    worst = min(b - M for (M, th, b) in s["slack"])
    print("       tightest margin bound-M = %.4f  (test fires iff < 0)" % worst)
print("=" * 72)
