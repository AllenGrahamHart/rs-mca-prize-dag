# Coordinator audit — L-A pencil rigidity pilot

**Auditor:** Fable, 2026-08-03. **Verdict: BANKED — refutation-as-
stated accepted; L-A' + D1-D3 adopted; ROUND 9 COMPLETE.**

Replay 30/30. Hand-checked: LEMMA R's reduction (values of g_a on
A_1 u A_2 determine the class; nonzero via mu vanishing on >= k+1
points); THEOREM 3's iterated X-shift (deg(uX - u') <= e < t forces
uX = u', so u constant); the C'-in-one-line corollary; W1's audit
trail (dim span{B_a} = 3 with V = 4 blocks — not a pencil — while
dim Ann = 1: the Z-escape is real); LEMMA D1's multiplicity count
(V = 4 zero-escape => each point in <= 1 complement => disjoint).

Adopted: L-A is FALSE as stated (V = 4, e >= 2) — but the heart never
needed it there: LEMMA D1 makes V = 4 disjoint hence point-counted,
and W1/W2 have charge >= 2 anyway (rank = 2m-1 >= 2V at V = 4). At
V >= 5 the repaired L-A' covers everything except the named residual
(1 <= dim G < e with Z != empty). The CONSUMER (V_0 <= n/2) is now
proved at V = 4, e <= 2, t = 2, and all disjoint systems; the single
remaining ray-side obligation is the OVERLAP SLIVER: overlapping
zero-escape systems at e >= 3, V >= 5 (which also inherits L-B's
residual via the adopted L-A => L-B chain).

ROUND-9 NET: the band heart's open surface is now (1) the RS
list-size terminus at tau = k + ceil(h/2) — the real problem,
positive target #1 species, codeword-pair side, and (2) the overlap
sliver (combinatorial, precisely named, toy-attackable). Everything
else on the ray side is proved or refuted-and-rerouted.

## Dated addendum (2026-08-03, F9 pilot): FB FIRED — the V >= 5
non-existence evidence is VOID (random partitions blind to a codim-4
condition; exhaustive fields too small for a 5th disjoint block); 18
explicit V >= 5 non-pencil-forcing fixtures exist (T2/T1 false). The
proved THEOREMS 1/2/3/5 + D1-D3 replay clean on all of them; the
"forces >= V-1 blocks" claim corrects to >= V-2-e. See
f9_pencil_forcing/.
