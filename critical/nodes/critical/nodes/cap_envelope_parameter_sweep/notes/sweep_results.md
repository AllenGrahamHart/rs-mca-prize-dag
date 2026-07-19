# cap_envelope_parameter_sweep — results

Compute node. Single process, exact big-integer arithmetic; every reported point
is re-derived deterministically by `verify_sweep.py` (all PASS). No git, no
dag.json edits.

## The lemma and its hypotheses (checked, not extrapolated)

Floor used: **cor:extension-pole-quotient-remainder-floor**
(`rs-mca-l1/tex/cs25_cap_v12.tex` ~line 542), whose list size comes from
**lem:quotient-remainder-prefix** / **lem:heaviest-prefix-locator-floor**
(~line 734/841), certificate-free ("box") level:

> `L := ceil( M_{c,m,s} / |B|^{w_c(s, A0-k-1)} )`, `M_{c,m,s}=C(N,m)·C(n-mc,s)`,
> `w_c(0,σ)=floor(σ/c)` for full-fiber supports; trigger `L>(q-b)/k`.

Its hypotheses (lem:quotient-remainder-prefix, verbatim conditions):
`B⊆F`, `D⊆B^×` a multiplicative coset of order `n`; `K<n`; `c|n`, `N=n/c`;
`A0=mc+s`, `0≤s<c`, `0≤m≤N`, `A0≥K`; **and if `s>0`, `mc+s≤n`.**
Extension-valuedness adds `B⊊F`, `D⊆B`, `|D|≥2` (cor line 497).

**KEY FINDING — no scale coupling.** Every hypothesis is on `(c,m,s,A0)` alone.
There is NO condition tying `c` to the ambient box, to `N_ρ`, or to `q`. The
`s>0` side-condition `mc+s≤n` is the only "box-like" constraint, and it is
**vacuous at full fiber `s=0`** — the regime the sweep uses. The printed
`N_ρ=1024` is a *declared convenience* (statement.md), not a lemma hypothesis.
So the floor is valid at every 2-power scale `c|n`; the sweep is legitimate.

Model (all conservative, direction verified):
- `n=2^41`, `q<2^256`. Full fiber `s=0`, `m=k/c+d`, `A0=mc=k+dc`,
  `σ=A0-k-1=dc-1`, `w=w_c(0,σ)=floor((dc-1)/c)=d-1`.
- Box charge: a proper subfield has `|B|<q<2^256`, so `|B|^w<2^{256w}` and
  `log2 L = log2 C(N,m) - 256 w` is a valid lower bound on `L`. (A proper
  subfield in fact has `b<2^128`; charging 256 is doubly conservative — the true
  `L` is larger, so all gains below are lower bounds.)
- Trigger (task iv): `log2 L > 256 - log2 k`, i.e. exact big-int
  `C(N,m) > 2^{256 d - e}` with `e=log2 k`. Since `(q-n)/k<q/k<2^{256-e}` and
  `q-n≥q-b`, this is stronger than the corollary's own `L>(q-b)/k`, so both the
  CA floor and the genuinely-extension-valued witness fire.
- Grid step: `2^-9` at 1/4 and 1/8, `2^-10` at 1/16 (confirmed vs
  corridor_window_cleanup / corridor_ledger; template 1/8 boundary = `2^-9`).
- Gain: absolute `d·c/n = d/N`; total grid steps `= d·2^{step}/N`;
  **net gain** (beyond the printed 1-step `N_ρ` reserve) `= d·2^{step}/N - 1`.
  The template's reported 0.0625 = (17·2^9/2^13) − 1 fixes this convention.

Method per rate: `c` over 2-power divisors of `gcd(n,k)=k` (so `k/c` integral);
`d=1,2,…`; `w=d-1`; exact `log2 C(N,m)`; trigger; if triggered, net gain.
`f(d)=log2 C(N,m0+d)−256d+e` is strictly decreasing (marginal entropy
`log2((1-ρ)/ρ)<256`), so `d_max` is the last triggering `d` per `c`; net is
maximized over `(c,d)`.

## Results (each row: exact big-int trigger + maximality of d; see verify_sweep.py)

### rate 1/8 (k=2^38) — recheck / OPTIMAL point
The template `d=17 @ c=2^28` (net **0.0625**, 180-bit trigger margin) reproduces
exactly, but is **NOT** maximal. Sweeping all `c`:
- maximal verified point: **c=2^21, d=2251, N=2^20** → **net 0.099121** (=203/2048),
  trigger margin 28.5 bits, d maximal.
- true supremum `2·H(1/8)/(1−H'(1/8)/256)−1 ≈ 0.09912`, approached from finer `c`
  (e.g. c=2^11 gives 0.099122); the `c=2^21` point is the largest exactly
  big-int-verifiable optimum. **Required X_acl(1/8) = 0.023 → MET, margin +0.076.**
  (1/8's own requirement was already met by the template; the optimum improves it.)

### rate 1/4 (k=2^39)
- maximal verified point: **c=2^25, d=209, N=2^16** → **net 0.632812** (=81/128),
  trigger margin 23.5 bits, d maximal (equivalent ties at c=2^24 d=418, c=2^23 d=836).
- **Required: task 0.318 → MET, margin +0.315;  ledger X_acl(1/4)=0.367 → MET, margin +0.266.**

### rate 1/16 (k=2^37)
- maximal verified point: **c=2^28, d=11, N=2^13** → **net 0.375000** (=3/8),
  trigger margin 21.1 bits, d maximal (tie at c=2^27 d=22).
- **Required: 0.304 → MET, margin +0.071.**  (task 0.304 = ledger X_acl(1/16).)

| rate | best (c, d) | N | net gain (steps) | required | margin | binding |
|------|-------------|---|------------------|----------|--------|---------|
| 1/4  | (2^25, 209) | 2^16 | 0.632812 = 81/128 | 0.318 / 0.367 | +0.315 / +0.266 | entropy⇄box |
| 1/8  | (2^21, 2251)| 2^20 | 0.099121 = 203/2048 | 0.023 | +0.076 | entropy⇄box |
| 1/16 | (2^28, 11)  | 2^13 | 0.375000 = 3/8 | 0.304 | +0.071 | entropy⇄box |

## Verdict (pre-registered interpretation)

Gains **≥ required at BOTH 1/4 and 1/16** (and 1/8): **the whole corridor family
closes by parameter optimization.** No lemma hypothesis fails at finer scales —
the floor's validity is scale-free in `c` and the `s=0` full-fiber choice retires
the only box-like side-condition. The binding constraint everywhere is the benign
**entropy-vs-box tradeoff**: each extra fiber (`d→d+1`) buys `~log2((1−ρ)/ρ)` bits
of `C(N,m)` entropy but is charged 256 box bits, so
`net → 2^{step}·H(ρ)/(256−H'(ρ)) − 1` (≈ 0.633 / 0.099 / 0.370 at 1/4 / 1/8 / 1/16,
matching corridor_window_cleanup's recovered figures). The wave-1 corridor widths
were measured against the lazy `N_ρ=1024` cap.

Falsifier (lemma conditions failing at every scale finer than `N_ρ`): **not
triggered** — conditions hold at all swept scales.
