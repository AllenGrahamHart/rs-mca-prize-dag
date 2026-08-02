# Pilot report: WCL count bounds — the lattice route decided (Opus 5, 2026-08-02)

Coordinator note: condensed persistence of the subagent's report (full
detail in results/); audit in FABLE_AUDIT.md. 25/25 verifier replayed.

## VERDICTS: F1 not fired (no slot closes). F2 FIRED (the gap = one
named constant). F3 FIRED decisively (the lever is structurally wrong).

**The formalization (LAT0-LAT6, proved + certified):** relation
lattices ARE ideal lattices (det = q^o exactly); the normalized first
minimum kappa(I) = lambda_1^2 / N(I)^{2/h} satisfies kappa >= 1 —
WHICH IS EXACTLY THE BANKED AM-GM FENCE; det^{2/h} = q^{1/128}
ell-independently (the 256:1 ratio again); slot (ell,w) closes iff
kappa . q^{1/128} > w. kappa = 1 is TIGHT (the C1 flat polynomials at
w in {1,2,3,7} give kappa = 1 exactly, at every h — LAT5): the fence
and the first-minimum bound are ONE inequality.

**F3, two independent kills:** (1) THE MINIMA LAW (LAT1, theorem):
negacyclic shift is a free isometry, so lambda_1 = ... = lambda_h for
EVERY relation lattice — Minkowski's second theorem degenerates to his
first; there is no second-minimum information. (2) THE 256-BIT CAP:
the banked engineered witness (weight-6, order-512, Norm = 2.q0 with
q0 a 256-bit prime, v_2(q0-1) = 9 — recomputed from scratch, exact
match) gives an official-shape lattice with kappa <= 1.507, while
every open slot needs kappa in [3.97, 8.73] over the official range
(q_min = 3.2^41+1 is the HARDEST case; quoting only q ~ 2^256
understates the deficit by ~214 bits). **No v_2-blind bound can close
any open slot; the lever must see v_2(q-1) >= 41, which lattice
geometry cannot.** Ball-counting proves emptiness only through
lambda_1 (i.e. through the fence); Cauchy-Schwarz is circular; LAT2's
orbit granularity (counts are 0 or >= 2h) buys 9-11 bits of a 255-400
bit gap.

**CORRECTION OF RECORD (on the dli_norm_gate report):** the closing
"Minkowski second minimum" lever was posed in RESULTANT_GATE_SUMMARY
for the M-BOUND (multiplicity M_L <= 13.29), where it is sound once
restated over the RING action (Z[zeta]-independent short vectors force
q^ell | gcd of norms — the banked resultant gate); pointed at the
ZERO-EVENT slots it is structurally wrong. What closes slots is
v_2-AWARE: the sparse-certificate route (dli_wcl_extended_six_slot...)
— confirmed from a second direction; extend the standing planning line
to "not lattice/count bounds either."

**Census validation (third independent code path — q-ary basis + LLL
+ exact certification + exact Fincke-Pohst):** all banked censuses
reproduced identically (2N=16 all 11; 2N=32 ell=1 w<=5; ell=2 full
table, + fills in w=6 = {97}).

**The minima law measured (1593 certified lattices):** kappa
concentrated ~1.7 at h=16 (1.4x the Gaussian heuristic — ideal
lattices are MORE isotropic than random: the shift symmetry forbids
anomalously short directions); worst case degrades with sample size
(min 1.044 -> 1.116); kappa = 1 attained. The censuses support a
TYPICAL bound, not the uniform one F2 needs. The lambda_1^2 > w
relaxation is essentially lossless in the official regime w << h
(false-positive rate 1/1522 at w=5, h=16).

**Named cheap falsification experiment:** engineer a weight-5
order-512 relation with a 256-bit prime factor == 1 mod 512
(maxnorm(256,5) = 2^289.5 leaves 33 bits; typical norms 2^190 — a
large-deviation search). Success drops the cap to ~1.25 and kills the
route's last residue ((1,5)/(1,6) at the production window).

**Doubling (LAT6):** iota(L) (+) x.iota(L) <= L^(2h) with index
exactly q^o — census monotonicity; the minima side of the C1
embedding.

**Caveats:** exhaustive to h <= 16; official statements = proved
lemmas + the banked witness; the 1.507 cap is h=256/ell=1; conditional
fences at w >= 8 ride the probed maxnorm (flagged per-row);
ell > 1 measurement thin; process catch recorded (a composite prime
in a hand list was caught BY the orbit invariant — retained as a
soundness detector).
