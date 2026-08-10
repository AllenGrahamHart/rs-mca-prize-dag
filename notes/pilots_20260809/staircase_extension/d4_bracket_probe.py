"""D4: independent check of the razor-row bracket claims.

(i) Is B_ca^far really FREE at razor rows?  Derive an explicit q-free
    cap from the PROVED (ERC2)/(MI2) machinery at radius r and compare
    it with B* = floor(q/2^128).
(ii) Bracket arithmetic and the deep-radius geometry of the two ends.

The cap used here is the node's own (ERC2):
    T <= floor(((N-s)e + rho - A e)/(rho - s)),  (A+s)e <= rho-s,
with A = R+1-2rho and the pencil shape forcing rho <= min(R-r, r+1).
Maximising over the admissible (rho, s, e) is a tiny exact search when
the radius is deep, because rho <= R-r is then small.

Stdlib only.  Run under tools/ramguard.
"""


def say(s=""):
    print(str(s), flush=True)


n = 2 ** 41
k = 2 ** 40
R = n - k
N = n


def erc2(rho, s, e):
    A = R + 1 - 2 * rho
    d = rho - s
    if d <= 0 or A < 1 or (A + s) * e > d:
        return None
    return ((N - s) * e + rho - A * e) // d


def cap_at_radius(r, grid=400):
    """max of the (ERC2) bound over admissible (rho,s,e) at radius r.

    rho <= rho_hi = min(R-r, r+1) (the pencil is (R-r) x (r+1) and the
    branch is deficient).  In e the bound is monotone, so only e=0 and
    e=e_max matter.  In rho it is monotone increasing (both rho and
    N/A(rho) increase), which the sampled grid re-checks.
    """
    rho_hi = min(R - r, r + 1)
    cands = {1, rho_hi}
    for i in range(1, grid):
        cands.add(max(1, rho_hi * i // grid))
    best, arg = 0, None
    seq = []
    for rho in sorted(cands):
        loc = 0
        locarg = None
        # e = 0: the PROVED fixed-kernel branch gives T <= rho (the
        # (ERC1)/(ERC2) incidence chain assumes e >= 1 and must NOT be
        # evaluated at e = 0).
        A0 = R + 1 - 2 * rho
        if A0 >= 1:
            loc, locarg = rho, (rho, 0, 0)
        for s in range(0, min(rho, 4)):
            d = rho - s
            A = R + 1 - 2 * rho
            if A < 1:
                continue
            emax = d // (A + s)
            if emax < 1:
                continue
            v = erc2(rho, s, emax)
            if v is not None and v > loc:
                loc, locarg = v, (rho, s, emax)
        seq.append(loc)
        if loc > best:
            best, arg = loc, locarg
    mono = all(seq[i] <= seq[i + 1] for i in range(len(seq) - 1))
    return best, arg, mono


say("=== D4(i): is B_ca^far free at razor rows? ===")
say("radius r      rho_hi=min(R-r,r+1)  (ERC2) cap    argmax (rho,s,e)")
tests = [R // 2, R // 2 + 1, R - 2 ** 39, R - 2 ** 38, R - 2 ** 36,
         R - 2 ** 34, R - 2 ** 30, R - 2 ** 20, R - 100, R - 2]
for r in tests:
    if r >= R:
        continue
    cap, arg, mono = cap_at_radius(r)
    a = n - r
    say("r=%-14d %-20d %-13d %s mono=%s  (a = n-r = %d = k+%d)"
        % (r, min(R - r, r + 1), cap, arg, mono, a, a - k))
say()
say("Bracket ends:")
lo = k + 2 ** 34
hi = 3 * n // 4
for a, name in ((lo, "k+2^34  (RH-AC-lo)"), (hi, "3n/4    (RH-AC-hi)")):
    r = n - a
    cap, arg, mono = cap_at_radius(r)
    say("  a=%-14d %-20s r=n-a=%-14d far-CA cap=%d (rho,s,e)=%s mono=%s"
        % (a, name, r, cap, arg, mono))
say()
say("B* = floor(q/2^128) at the razor rows:")
for e2 in (167, 168, 169, 170, 175, 200, 256):
    q = 2 ** e2
    say("  q=2^%-4d B*=2^%-4d" % (e2, (q // 2 ** 128).bit_length() - 1))
say()
say("=> far-CA freeness threshold: the cap at the LOW bracket end is")
capl, _, _ = cap_at_radius(n - lo)
capr, _, _ = cap_at_radius(n - hi)
say("   %d at a=k+2^34 and %d at a=3n/4;" % (capl, capr))
say("   B* exceeds both as soon as q >= %d * 2^128 ~ 2^%.2f"
    % (max(capl, capr), 128 + max(capl, capr).bit_length() - 1))
say("   (razor rows have q >= 2^169, B* >= 2^41 — free with margin 2^%d)"
    % (41 - max(capl, capr).bit_length() + 1))
say()
say("=== D4(ii): bracket arithmetic ===")
say("k+2^34 = %d ; 3n/4 = %d ; width = %d" % (lo, hi, hi - lo))
say("sigma bracket = [2^34, 2^39] ; width = %d" % (2 ** 39 - 2 ** 34))
say("3n/4 corresponds to radius r = n/4 = 2^39 = R/2 = EXACTLY half distance")
say("k+2^34 corresponds to radius r = R-2^34 = %d (deep)" % (R - 2 ** 34))
say("closing {2^39,2^39+1} moves the determined q-axis from 2^167 to "
    "2^167+2^129: relative 2^-38")
say("=== END ===")
