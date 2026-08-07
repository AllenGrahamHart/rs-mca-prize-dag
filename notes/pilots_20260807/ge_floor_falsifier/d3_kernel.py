#!/usr/bin/env python3
"""D3 -- GE-WEAK form (b) end to end at toy scale.

THE ELL-CONDITION SYSTEM, exactly.
K_p = {v in Z^{N'} : sum_x v_x zeta^x = 0 mod p}, zeta of order N', p = 1 mod N'.
Phi_{N'}(X) = X^h + 1 (h = N'/2), so the ONLY cyclotomic relations are the
antipodal ones e_a + e_{a+h}.  With FOLD(v)_j = v_j - v_{j+h}:

   v is in K_p                  <=>  FOLD(v)(zeta) = 0 mod p
   v is NON-cyclotomic          <=>  FOLD(v) != 0
   v ternary with support <= L  <=>  FOLD(v) in {-2,..,2}^h with ||.||_1 <= L
                                     (min cost to realise w_j is |w_j|)

So:  K_p HAS A NON-CYCLOTOMIC TERNARY VECTOR OF SUPPORT <= 2l'
     <=>  some w != 0 in the folded box with ||w||_1 <= 2l' has w(zeta) = 0 mod p
     <=>  p | Norm(w) for such a w  (p = 1 mod N' has residue degree 1).

Hence the EXACT universal threshold TIGHTEMPTY(N', L) computed by sweep.py:
every row prime above it is certified for free, by ONE inequality.
"""
import itertools
import json
import math
import sys

sys.path.insert(0, __file__.rsplit('/', 1)[0])
from gelib import tower_norm


def c4_replay():
    """Reproduce the banked C-4 toy anchor (lattice_cone_certificate ledger):
    N' = 16, p = 12289, w <= 6 -> 288 antipodal cyclotomic relations, ZERO
    non-cyclotomic."""
    N, h, p, L = 16, 8, 12289, 6
    # zeta of order 16 in F_p
    z = None
    for g in range(2, p):
        c = pow(g, (p - 1) // N, p)
        if pow(c, N // 2, p) != 1 and pow(c, N, p) == 1:
            z = c
            break
    assert z is not None and pow(z, N, p) == 1 and pow(z, N // 2, p) == p - 1
    pw = [pow(z, i, p) for i in range(N)]
    cyc = 0
    non = 0
    idx = range(N)
    for s in range(1, L + 1):
        for sup in itertools.combinations(idx, s):
            for sgn in itertools.product((-1, 1), repeat=s):
                val = 0
                for t, a in zip(sup, sgn):
                    val += a * pw[t]
                if val % p:
                    continue
                v = [0] * N
                for t, a in zip(sup, sgn):
                    v[t] = a
                w = [v[j] - v[j + h] for j in range(h)]
                if any(w):
                    non += 1
                else:
                    cyc += 1
    print("== C-4 REPLAY: N'=16, p=12289, support <= 6, zeta of order 16 ==")
    print("   cyclotomic (antipodal) kernel vectors : %d   (= %d up to global "
          "sign; banked C-4 says 288)" % (cyc, cyc // 2))
    print("   NON-cyclotomic kernel vectors         : %d   (banked C-4 says 0)"
          % non)
    # closed form check
    tot = sum(math.comb(h, j) * 2 ** j for j in range(1, L // 2 + 1))
    print("   closed form sum_j C(h,j) 2^j, j <= 3  : %d" % tot)


def boxcount(h, L):
    """#{w in {-2..2}^h : ||w||_1 <= L}, exact, by DP."""
    dp = [0] * (L + 1)
    dp[0] = 1
    for _ in range(h):
        nd = [0] * (L + 1)
        for s in range(L + 1):
            if not dp[s]:
                continue
            for a in (0, 1, 1, 2, 2):        # multiplicities: 0 once, +-1, +-2
                if s + a <= L:
                    nd[s + a] += dp[s]
        dp = nd
    return sum(dp)


def census(h):
    """Exhaustive bad-prime census: which p = 1 mod N' admit a non-cyclotomic
    ternary kernel vector at all?  (p bad  <=>  p | Norm(w), w != 0 in box.)"""
    N = 2 * h
    data = json.load(open(__file__.rsplit('/', 1)[0] + "/sweep_h%d.json" % h))
    pool = data["pool"]
    fp = data["fp"]
    bad = sorted(p for p in pool if fp[str(p)] == 1)
    assert all(p % N == 1 for p in bad)
    hi = data["tight"][2 * h]
    print("\n== BAD-PRIME CENSUS, N' = %d (EXHAUSTIVE over the whole folded "
          "box) ==" % N)
    print("   a prime p = 1 mod %d is BAD iff K_p contains a non-cyclotomic "
          "ternary vector" % N)
    print("   #BAD = %d ; largest BAD = %d = TIGHTEMPTY ; "
          "every p = 1 mod %d above it is FREE" % (len(bad), hi, N))

    def pi_mod(x):
        c = 0
        n = 1
        while True:
            n += N
            if n > x:
                return c
            ok = n > 1
            d = 3
            while d * d <= n:
                if n % d == 0:
                    ok = False
                    break
                d += 2
            if ok:
                c += 1

    print("   %-24s %-8s %-8s %-8s %-14s" %
          ("dyadic window", "#BAD", "#p=1modN'", "frac", "class-heuristic"))
    lo = 2
    while lo < hi * 2:
        hi2 = lo * 2
        nb = sum(1 for p in bad if lo <= p < hi2)
        npr = pi_mod(min(hi2 - 1, hi * 2)) - pi_mod(lo - 1)
        # class heuristic: E[#nonzero folded classes in K_p] = (5^h-1)/p
        mid = (lo + hi2) / 2.0
        heur = 1.0 - math.exp(-(5 ** h - 1) / mid)
        print("   [2^%-5.0f, 2^%-5.0f)      %-8d %-8d %-8s %-14.4f" %
              (math.log2(lo), math.log2(hi2), nb, npr,
               ("%.3f" % (nb / npr)) if npr else "-", heur))
        lo = hi2
    return bad


def main():
    c4_replay()
    for h in (4, 8):
        census(h)

    print("\n== D3 PRICING: certification cost as a function of (N', p, l') ==")
    print("MAXNORM(N') measured EXHAUSTIVELY: 144 = 12^2 (h=4), 614656 = 28^4 "
          "(h=8).")
    print("Pattern:  MAXNORM(h) = (4(h-1))^{h/2}   [PROVED at h=4,8; "
          "CONJECTURAL above]")
    print("%-5s %-7s %-16s %-16s %-16s" %
          ("h", "N'", "AMGM=(4h)^{h/2}", "(4(h-1))^{h/2}", "needed for p=2^250"))
    for h in (4, 8, 16, 32, 64):
        a = (h / 2.0) * math.log2(4 * h)
        b = (h / 2.0) * math.log2(4 * (h - 1))
        need = 250.0 / (h / 2.0)
        print("%-5d %-7d 2^%-14.3f 2^%-14.3f base 2^%-6.4f = %.1f"
              % (h, 2 * h, a, b, need, 2 ** need))
    print("At the prize cell h = 64: the norm instrument is non-vacuous only "
          "for log2 p > 255.269 (conjectural exact) / 255.456 (banked 253^32)"
          "; the row sits at 250.  Closing it needs base 224.6, not 252.")

    print("\n== D3/D4 SEARCH COST: full-radius exhaustion, two split models ==")
    print("%-5s %-7s %-20s %-20s %-20s" %
          ("h", "N'", "box 5^h", "weight-split MITM", "coord-split on FOLD"))
    for h in (4, 8, 16, 32, 64):
        N = 2 * h
        w = N                       # full radius 2l' = N'
        ws = math.log2(math.comb(N, w // 2)) + w / 2.0
        cs = (h / 2.0) * math.log2(5)
        print("%-5d %-7d 2^%-18.3f 2^%-18.3f 2^%-18.3f"
              % (h, N, h * math.log2(5), ws, cs))
    print("banked C-4 small-radius model C(N',w/2)*2^{w/2} at N'=128: "
          "w=12 -> 2^%.1f, w=14 -> 2^%.1f, w=16 -> 2^%.1f"
          % (math.log2(math.comb(128, 6)) + 6, math.log2(math.comb(128, 7)) + 7,
             math.log2(math.comb(128, 8)) + 8))
    # crossover
    for w in range(2, 129, 2):
        ws = math.log2(math.comb(128, w // 2)) + w / 2.0
        if ws > 32 * math.log2(5):
            print("crossover: the folded coordinate-split (2^%.3f) beats the "
                  "banked weight-split from w = %d upward" %
                  (32 * math.log2(5), w))
            break

    print("\n== BOXCOUNT(h, L) = #{w in box : ||w||_1 <= L} (exact DP) ==")
    for h in (8, 64):
        print("  h=%d: " % h + ", ".join(
            "L=%d:2^%.2f" % (L, math.log2(boxcount(h, L)))
            for L in (4, 8, 16, 32, 2 * h)))


if __name__ == "__main__":
    main()
