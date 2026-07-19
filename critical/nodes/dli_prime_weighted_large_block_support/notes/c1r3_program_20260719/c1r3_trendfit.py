# c1r3 KILL-TREND evaluation (pre-registered: per-octave worst K'_r3, monotone
# across >=3 populated octaves AND log2-linear extrapolation crossing 4 (literal)
# / 1 (amber) before q = 2^32). Least-squares over all populated octaves, plus
# conservative secondary reads (last-two-octave slope; first-to-last chord).
import math
worsts = {  # octave -> (argmax q, worst K'_r3 float)
    22: (7340033, 0.307530076),
    23: (13631489, 0.448742388),
    24: (26214401, 0.591911586),
    26: (81788929, 1.008154437),
    27: (246415361, 1.024517293),
}
xs = [math.log2(q) for q, k in worsts.values()]
ys = [math.log2(k) for q, k in worsts.values()]
mono = all(b > a for a, b in zip([k for _, k in sorted(worsts.items())],
                                 [k for _, k in sorted(worsts.items())][1:] )) if False else \
       all(worsts[o2][1] > worsts[o1][1] for o1, o2 in zip(sorted(worsts), sorted(worsts)[1:]))
xb = sum(xs) / len(xs); yb = sum(ys) / len(ys)
sl = sum((x - xb) * (y - yb) for x, y in zip(xs, ys)) / sum((x - xb) ** 2 for x in xs)
y32 = yb + sl * (32 - xb)
xc4 = xb + (2 - yb) / sl        # log2 K' = 2  <=>  K' = 4
xc1 = xb + (0 - yb) / sl        # K' = 1
print(f"monotone increasing across {len(worsts)} populated octaves: {mono}")
print(f"LS fit: slope={sl:.4f} bits/octave; K'(2^32) pred = {2**y32:.3f}; "
      f"crosses 4 at log2(q)={xc4:.2f} ({'BEFORE' if xc4 < 32 else 'AFTER'} 2^32); "
      f"crosses 1 at log2(q)={xc1:.2f} ({'BEFORE' if xc1 < 32 else 'AFTER'} 2^32)")
s2 = (ys[-1] - ys[-2]) / (xs[-1] - xs[-2])
print(f"last-two-octave slope = {s2:.4f} bits/octave -> crossing 4 at log2(q)="
      f"{xs[-1] + (2 - ys[-1]) / s2:.1f}")
sc = (ys[-1] - ys[0]) / (xs[-1] - xs[0])
print(f"first-to-last chord slope = {sc:.4f} -> crossing 4 at log2(q)={xs[-1] + (2 - ys[-1]) / sc:.2f}")
# per-octave step slopes (deceleration display)
oct_sorted = sorted(worsts)
for o1, o2 in zip(oct_sorted, oct_sorted[1:]):
    (q1, k1), (q2, k2) = worsts[o1], worsts[o2]
    print(f"step {o1}->{o2}: slope {(math.log2(k2)-math.log2(k1))/(math.log2(q2)-math.log2(q1)):+.4f} bits/octave")
# amber exactness (from banked exact fractions)
a1 = (2766759940242725, 2744381056483328)
a2 = (1058880560632659, 1033540934303744)
print(f"amber exact: 81788929 K'={a1[0]}/{a1[1]} > 1: {a1[0] > a1[1]}; "
      f"246415361 K'={a2[0]}/{a2[1]} > 1: {a2[0] > a2[1]}")
print(f"iid baseline note: (E-1)/r -> (q-1)/q under iid fibers (=1); worst amber excess over iid = "
      f"{(1.024517293 - 1) * 100:.2f}%")
