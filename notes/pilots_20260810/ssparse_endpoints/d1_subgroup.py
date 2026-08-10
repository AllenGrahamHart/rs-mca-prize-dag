"""D1 / P15 (S-SUBGROUP): the only route I can see that evades the rung
quantization inside the printed proof skeleton.

A = (j full H-cosets) u (u loose points of Q),  |H| = t | N,  N' = N/t,
m = jt + u = N/2 + d.  Then P_A(Y) = Ptilde(Y^t) E(Y), deg E = u, so for
i < min(t, d) the constrained low coefficient is a_i = ptilde_0 * e_i(E).
Hence the class of A is determined by (ptilde_0, X) where X = the loose
set, and

    #A       = C(N', j) * C(N - j t, u)
    #classes <= N' * C(N - j t, u)
    L        >= C(N', j) / N'          (a valid lower bound)

Reach is unchanged: sigma = (d+1)c - 1 = (d+1) n / N - 1.
Admissibility for the MCA floor: q/L < 2^128 with the k q/(q-n) < 2^82
slack absorbed, i.e. C(N',j)/N' > 2^128 at every q < 2^256, i.e.
    2^128 * C(N',j) > N' * 2^256   <=>   C(N',j) > N' * 2^128.
Exhaustive scan over N = 2^i, t = 2^l | N, d in [1,t], u = m mod t.
"""
import math

n = 1 << 41
k = 1 << 40
TARGET = (1 << 34) - 1

print("=== P15: exhaustive S-SUBGROUP scan ===")
print(f"{'N':>8} {'t':>6} {'d':>5} {'u':>4} {'Nprime':>7} {'j':>7} "
      f"{'reach':>13} {'margin_bits':>12} {'adm':>4}")
best = None
hits = []
for i in range(2, 25):                       # N = 4 .. 2^24
    N = 1 << i
    c = n // N
    if c > k:
        continue
    for l in range(0, i + 1):                # t = 2^l | N
        t = 1 << l
        Np = N // t
        if Np < 2:
            continue
        for d in range(1, t + 1):
            m = N // 2 + d
            if m > N - 1:
                continue
            u = m % t
            j = (m - u) // t
            if j < 1 or j > Np - 1:
                continue
            reach = (d + 1) * c - 1
            if reach < (1 << 32):            # far below target, skip printing
                continue
            # SELF-CORRECTION 2 (2026-08-10): the b_0 coset carries the prefix
            # T_0 and must be excluded from A, so j cosets are chosen from
            # N'-1, not N'.  Anchor: t=1 must reproduce the printed rung's
            # 114.6503-bit margin exactly.
            C = math.comb(Np - 1, j)
            # margin in bits of  2^128 * C  vs  N' * 2^256
            bl = C.bit_length()
            lgC = (bl - 60) + math.log2(C >> (bl - 60)) if bl > 60 else math.log2(C)
            margin = (128 + lgC) - (math.log2(Np) + 256)
            adm = margin > 0
            if adm:
                hits.append((reach, N, t, d, u, Np, j, margin))
            if reach >= TARGET and (t <= 8 or adm):
                print(f"{N:>8} {t:>6} {d:>5} {u:>4} {Np:>7} {j:>7} "
                      f"{reach:>13} {margin:>12.4f} {'YES' if adm else 'no':>4}")
print()
hits.sort(reverse=True)
if hits:
    reach, N, t, d, u, Np, j, margin = hits[0]
    print(f"MAX ADMISSIBLE S-SUBGROUP REACH = {reach} = 2^{math.log2(reach):.6f}")
    print(f"   at (N,t,d,u) = ({N},{t},{d},{u}), N'={Np}, j={j}, margin {margin:.4f} bits")
    print(f"   target to beat (current proved reach) 2^34-1 = {TARGET}")
    print(f"   P15 (no gain, exactly equal): {reach == TARGET}")
    print(f"   F1 FIRES: {reach > TARGET}")
    print()
    print("   top-8 admissible rungs of the S-SUBGROUP family:")
    for h in hits[:8]:
        print(f"     reach={h[0]:>13} (2^{math.log2(h[0]):.4f})  N={h[1]:<8} t={h[2]:<5} "
              f"d={h[3]:<4} u={h[4]:<3} N'={h[5]:<6} j={h[6]:<6} margin={h[7]:.3f}")
print()
print("=== closed-form ceiling check: with N' >= 256 forced, N = t*N' and d <= t ===")
for t in (1, 2, 4, 8, 16, 256):
    ceil_reach = (t + 1) * n // (256 * t) - 1
    print(f"   t={t:<5} reach ceiling = (t+1)n/(256t)-1 = {ceil_reach:>13} "
          f"(2^{math.log2(ceil_reach):.4f})   > 2^34-1: {ceil_reach > TARGET}")
