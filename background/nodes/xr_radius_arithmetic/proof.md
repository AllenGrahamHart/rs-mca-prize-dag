# proof: xr_radius_arithmetic

- **status:** PROVED (exact arithmetic on named/pinned inputs)
- **closure:** proof

## Statement (this node)

Compute the **required ledger reach** `s*(rate)` — a number. The verdict
(correcting the premature "`s* = 1`" reading): under the pinned-ledger two-regime
model, **`s* = 1` never closes a corridor row**; every corridor edge needs the
**full reach `s* = t* - 1`**, where `t*` is the corridor edge (smallest window
with FM mean `<= B*`). The four-rate table is reproduced *exactly*. Structural
facts that survive: the ball profile `N_s = C(j,s) C(n-j,s)` (Vandermonde), the
distinct-slope plateau `= E[X]^2`, and the head domination by `s = 1`.

This is an arithmetic node: given the **named upstream inputs** (i) the FM scale
(banked Lemma FM1), (ii) the pinned pair-ledger `c(s,t) = min(s, t-1)`
(provenance external + Monte-Carlo, packaged as `xr_ledger_qpower`), and (iii)
the two-regime coverage model, the reach `s*` is *computed*. No new inequality is
proved here; the content is the correct number and the `s* = t*-1` identity.

## 1. Inputs (named, not re-derived)

- **FM scale (banked Lemma FM1, exact).** For a row `(n, k, q)` at exact
  agreement `A`, with `t = A - k`, `j = n - A`, the aligned-support mean is
  `E[X] = C(n, j)(1 - q^{-t}) q^{1-t} <= C(n, j) q^{1-t}`. Gate
  `B* = floor(q / 2^128)`, so `log2 B* = L - 128` with `L := log2 q`.
- **Pinned pair-ledger (input).** `c(s, t) = min(s, t-1)`: the per-pair
  correlation exponent at exchange distance `s` decays as `q^{-c(s,t)}`, reaching
  its maximum (the independence **plateau**) at `s = t - 1`. Pinned upstream
  (`xr_ledger_qpower`, an OPEN packaging slot — used here as a hypothesis, which
  is legitimate for a *computation* node: we compute `s*` **given** the ledger).
- **Prize convention.** `L = log2 q = 255.9` (the "`2^{255.9}`" prize row of the
  budget audit), `n = 2^41`, `k = rho n`.

## 2. The corridor edge `t*` [definition + exact computation]

The corridor edge is the smallest window at which the FM mean drops to the gate:

```
t* = min { t : E[X] <= B* }
   = min { t : log2 C(n, n-k-t) + (1 - t)L <= L - 128 }
   = min { t : t * L  >=  log2 C(n, n-k-t) + 128 }.                        (T*)
```

(The last line: `log2C + (1-t)L <= L-128  <=>  log2C - tL <= -128  <=>  tL >= log2C + 128`.)
`f(t) := tL - log2 C(n, n-k-t) - 128` is strictly increasing in `t` (the `tL`
term rises by `L` per step; `log2 C(n, n-k-t)` falls as `j = n-k-t` moves below
`n/2`), so `t*` is the unique integer crossing. Solving (T*) exactly (binary
search; `log2 C` via `lgamma`, whose `~2e-4`-bit accuracy is far finer than the
`~L = 256`-bit step of `f`, so the integer crossing is unambiguous):

```
rate    t*              s* = t* - 1
1/2     8,592,912,739   8,592,912,738
1/4     7,014,660,390   7,014,660,389
1/8     4,722,556,392   4,722,556,391
1/16    2,943,177,800   2,943,177,799
```

These reproduce the QX.14/QX.15 table (215/215 checks) **to the last digit** at
`L = 255.9` — verified below.

## 3. The reach identity `s* = t* - 1` [complete, given the model]

The pair-ledger `c(s,t) = min(s, t-1)` says the correlation between aligned events
across an exchange path of length `s` saturates at `s = t - 1`: for `s >= t-1`,
`c = t-1` (the independence plateau); for `s < t-1` the events are still
correlated at level `q^{-s}`. The **two-regime coverage model** closes a corridor
row iff the ledger reaches decorrelation across the whole row, i.e. the reach must
attain the plateau of the edge window `t*`:

```
s_L (reach to plateau at window t)  =  t - 1,        so at the edge:
s*  =  s_L(t*)  =  t* - 1.                                                  (S*)
```

Equivalently: the FM mean at the corridor edge is `E[X] ~ B*` (order 1 relative to
the gate), so a *partial* reach `s < t*-1` leaves a residual correlation
`q^{-s} > q^{-(t*-1)}` that the two-regime accounting cannot absorb — only the full
plateau reach `t*-1` decorrelates the edge. Hence `s* = t*-1`. ∎

**`s* = 1` never closes.** By (S*), `s* = t*-1 ~ 3e9`–`8.6e9` at every rate (§2),
so `s* >> 1`: single-exchange reach `s = 1` is short of the required plateau by
billions of exchange steps. The premature "`s* = 1`" reading is corrected: `s = 1`
merely **dominates the head** of the aligned-count distribution (the largest
single-distance shell), it does not *close* the corridor. ∎

## 4. Structural facts that survive [complete]

- **Ball profile.** The number of co-supports `T'` at exchange distance `s` from a
  fixed `j`-support `T` is
  ```
  N_s = C(j, s) C(n-j, s)                                                   (BP)
  ```
  (drop `s` of `T`'s `j` points: `C(j,s)`; add `s` of the `n-j` outside points:
  `C(n-j,s)`). Exact; verified exhaustively on toys below.
- **Vandermonde / plateau `= E[X]^2`.** Summing (BP),
  `sum_s N_s = sum_s C(j,s) C(n-j,s) = C(n, j)` (Chu–Vandermonde), the total
  co-support count. On the second-moment side, at plateau distances (`s >= t-1`)
  the pair decorrelates and the joint aligned count factorises to `E[X]^2`
  exactly — the "distinct-slope plateau `= E[X]^2` (Vandermonde)" fact. The
  variance is thus a sum over shells `N_s` weighted by the ledger correlation
  `q^{-min(s,t-1)}` (this is exactly the object of the companion node
  `averaged_xr`).
- **Head `s = 1`, bulk peak.** The `s=1` shell `N_1 = j(n-j)` is the head; a
  second bulk peak of size `~ j(n-j)/n` rides the plateau at a `q^{-1}` discount
  (reported, not load-bearing here).

## 5. Mitigations (reported context; not re-derived)

The full-reach requirement is why the residual-ledger conversion path is hard
(localised to the mid band `s in (t/15, t-1]`). Three mitigations from the ledger,
quoted as context: (a) the stripped exemplar `A = 265` (`t = 9`) needs only
`s* = 4` — small-`t` partial XR, exactly what prediction P2 uses; (b) at rates
`1/4, 1/8, 1/16` the corridor edges are moment-trivial (Markov) once the count is
stripped, so **the contentful reach is rate `1/2` only**; (c) the `n^3`-budget and
plateau-absorption mechanisms hand off with `~3` bits of margin at the rate-`1/2`
edge (the arithmetic shadow of `E[X] ~ B*`). These are *reported*; this node
proves only the reach numbers and the `s* = t*-1` identity.

## 6. Honesty note

Proved: the exact `t*/s*` table (§2), the identity `s* = t*-1` **given the pinned
ledger and two-regime model** (§3), and the exact combinatorial facts (BP),
Vandermonde (§4). The pair-ledger `c(s,t) = min(s,t-1)` is an *input* (packaged in
the still-open `xr_ledger_qpower` slot); this node does not prove it, it *computes
with* it — which is the node's stated scope ("a number, not a hope"). The
downstream difficulty (extending a residual ledger to full reach `t*-1`) is
explicitly flagged in the statement and is **not** claimed closed here.

## Verifier

`verify.py` (stdlib `math.lgamma`, <1s): (1) solves (T*) at `L = 255.9` and
asserts the four `t*` match `{8592912739, 7014660390, 4722556392, 2943177800}`
exactly, with `s* = t*-1`; (2) verifies `s* >> 1` (never `1`); (3) verifies the
ball profile (BP) exhaustively on toys and the Vandermonde identity
`sum_s N_s = C(n,j)`; (4) checks the plateau onset `c(s,t) = min(s,t-1)` reaches
its max at `s = t-1`. All PASS.
