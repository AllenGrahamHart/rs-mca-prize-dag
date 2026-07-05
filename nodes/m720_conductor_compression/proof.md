# proof: m720 — compression REFUTED, REFINED height gate PROVED, still open (Pro T5, verified)

## Refined universal height gate (PROVED, VERIFIED — corrects the crude 291)
Via the formal square root F_R(t)=prod(1-xt)^{1/2}=sum a_m t^m (all conjugate roots on the
unit circle => |a_m|<=U_m=[t^m](sum_{r<=2h}|C(1/2,r)|t^r)^{2h}), every cleared obstruction
A_j=2^{4h-2}O_j has |sigma(A_j)| <= 2^{H_h}, H_h=(4h-2)+log2(max_j sum_{a+b=2h-j,max>h}U_a U_b).
VERIFIED table: H_7=43.57, H_13=86.29, H_19=129.10, H_20=136.24. So if a nonzero obstruction
lies in L with H_h[L:Q]<log2 p then p∤N(A_j) => no survivor (P4-HB). CORRECTION: my earlier
291-bit cite was too weak (2^290.7>2^250 can't close h=20 even over Q); the refined 136.24
is far sharper.

## STILL insufficient at Row-C (the gap)
Even refined, at p~2^250: h<=18 close at degree<=2, but h=19,20 close ONLY if [L:Q]=1;
over F_{p^2} (q~2^250 => char ~125 bits) h=19,20 CANNOT close even over Q (136.24>125).
So m720 needs, per row/window, EITHER (R2) a SURVIVOR-CONDITIONED descent: a nonzero
obstruction in a field L with H_h[L:Q]<log2 p (survivor-specific, not support-size — the
1024/7 degree-512 witness refutes support-size compression), OR (R3) the C2 certificate
gcd(p,D(n,h))=1, BLOCKED on the missing official Row-C primes + D(n,h) payload.
