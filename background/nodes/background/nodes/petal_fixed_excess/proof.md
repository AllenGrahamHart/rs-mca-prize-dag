# proof: petal_fixed_excess

- **status:** PROVED (fixed-excess polynomial bound; excess→∞ escape remains open,
  flagged)
- **closure:** proof

## Statement (this node)

Bound the **full-petal extras** at each **fixed cofactor excess** `e = d - ell <= c`.
Claim: in the generated-field window (`q = poly(n)`), the number of non-planted
full-petal listed codewords with touched-petal set `I` (`t = |I| >= 3`), petal
size `ell`, and core defect `d` with `d - ell <= c` (and `d` below the top defect
`(t-1)ell`) is

```
#extras(I, d)  <=  q^{d - ell + 1}  =  q^{e+1}  =  n^{O(c)}  =  poly(n),      (P)
```

i.e. **polynomial in `n` with an exponent depending only on the fixed excess `c`,
not on `n`**. This closes the *fixed-excess* layers of the full-petal branch (the
`e <= 6` layers delivered as finite enumerations); the *unbounded* excess
`e -> infinity` escape is a different, open problem, flagged in §4.

## 1. Banked lemmas (PROVED, from the L1 full-list quotient proof program)

- **Lemma 8 (Full-Petal Rank Certificate, PROVED).** Fix `I` (`t = |I|`), and
  `ell <= d <= (t-1)ell`. With the CRT operator `R_{I,d} : V_d -> F_q[X]_{<t ell}`,
  `R_{I,d}(F) = c_i F mod L_{T_i}` for `i in I`, and `pi_{>d}` extracting
  coefficients of degrees `d+1,...,t ell - 1`, put `K_{I,d} = ker(pi_{>d} R_{I,d})`.
  Then the full-petal listed codewords with exact touched set `I` and defect `d`
  **inject** into `{ L_D : D subset C, |D| = d } cap K_{I,d}`, so with
  `r_{I,d} = rank(pi_{>d} R_{I,d})`,
  ```
  #extras(I,d)  <=  |K_{I,d}|  =  q^{dim K_{I,d}}  =  q^{d + 1 - r_{I,d}}.     (L8)
  ```
- **Lemma 13 (High Rank Below Top Defect, PROVED).** For `t >= 3` and
  `ell <= d < (t-1)ell`,
  ```
  r_{I,d}  >=  ell,   equivalently   dim K_{I,d} = d + 1 - r_{I,d}  <=  d - ell + 1.  (L13)
  ```

Both are PROVED in `l1_full_list_quotient_proof_program.md` and re-verified on
toys here (§Verifier).

## 2. The fixed-excess polynomial bound [complete]

Let the excess be fixed, `e = d - ell <= c`, with `d` below the top defect
`(t-1)ell` (automatic once `c < (t-2)ell`, the operative large-petal regime — see
§3). Combine (L8) and (L13):

```
#extras(I,d)  <=  q^{d + 1 - r_{I,d}}   [L8]
              <=  q^{d - ell + 1}        [L13:  r_{I,d} >= ell]
              =   q^{e + 1}
              <=  q^{c + 1}.                                                   (2.1)
```

**Generated-field window.** The L1 program operates with `q = q_gen = poly(n)`
(the generated field; Lemma 8's own "Consequences": *"Since `q = poly(n)` in the
generated-field window..."*). Writing `q <= n^{a}` for a fixed constant `a`,

```
#extras(I,d)  <=  q^{c+1}  <=  n^{a(c+1)}  =  poly(n),                         (2.2)
```

with exponent `a(c+1)` depending **only** on the fixed excess `c` — this is
exactly claim (P). ∎(per (I,d))

**Summing over layers.** At fixed excess `e <= c`, a full-petal configuration is
specified by its touched set `I` (a `t`-subset of the petal index set) and its
defect `d = ell + e`. In the sunflower census the number of admissible `(I, d)`
with `e <= c` is itself `poly(n)` (the touched sets and defect layers are
poly-many in the relevant enumeration; each `d` is one of the `c+1` values
`ell,...,ell+c`). Hence the **total** full-petal extra count at fixed excess is a
`poly(n)`-fold sum of `poly(n)` terms, i.e. `poly(n)`. ∎

## 3. Why "fixed excess" is exactly the hypothesis that makes this work

Lemma 13's rank floor `r_{I,d} >= ell` holds strictly **below the top defect**
`d < (t-1)ell`. At the extreme top defect `d = (t-1)ell` the floor degrades (rank
drops, `dim K` exceeds `d-ell+1`) — verified in the toy table below, where the
`d = (t-1)ell` rows are the only ones violating (L13). But the top defect has
excess `e = (t-1)ell - ell = (t-2)ell`, which **grows with `ell`** and is therefore
*not* a fixed-excess-`<= c` layer once `ell` is large (`c < (t-2)ell`). So the
fixed-excess regime `e <= c` lives safely inside Lemma 13's valid range, and (P)
holds there. This is the precise sense in which bounding the excess rescues the
bound: it keeps `d` away from the top defect where the rank certificate is weak.

## 4. Honest scope — and the boundary with the open escape

- **Proved here (P):** at *fixed* excess `e <= c`, `#extras <= q^{e+1} = poly(n)`.
  The layers `e <= 6` are finite and were enumerated exactly; the bound is
  polynomial with a lower cutoff at the minimal defect `d = ell` (`e = 0`, first
  nonempty layer — Lemma 9), matching the "poly lower-cutoff growth rows"
  delivered in the enumeration.
- **Non-vacuous.** The layers are genuinely populated: explicit non-planted
  full-petal witnesses exist at `e = 2` (`ell=3, t=3, p=1009`) and `e = 5`
  (`ell=3, t=5, p=1009`) — so (P) bounds a real, nonzero family, it does not
  merely assert emptiness.
- **OPEN (flagged, not claimed):** the `e = d - ell -> infinity` escape. There
  `q^{e+1}` is super-polynomial, and a poly bound needs the *strong* rank floor
  `r_{I,d} >= d - O(1)` (kernel dim `= O(log n / log q)`), which Lemma 13 does not
  give. This is Theorem 21/B11's residual frontier and remains conjectural.
- **ROUTE-CUT (do not re-attempt):** the tempting exact-rank formula
  `r_{I,d} = min(d+1, t ell - d - 1)` — which would force the kernel *trivial*
  (zero extras) up to `d ~ t ell / 2` — is **false in general** (refuted by
  adversarial search: isolated prime coincidences, and a structural round-robin
  order-`ell`-coset family with `t` odd where the rank drops below the formula for
  every scalar). Crucially, **the fixed-excess bound (P) does not use this false
  formula**: it uses only the *weak* proved floor `r_{I,d} >= ell` (L13). The
  triviality question (whether the poly-bounded family is in fact empty) stays
  open; (P) bounds it either way.

## Verifier

`verify.py` (stdlib, exact `F_q` polynomial + CRT + rank, <5s): builds the CRT
operator `R_{I,d}` on toy sunflowers, computes `r_{I,d}` and `dim K_{I,d}`, and
asserts (a) Lemma 13 `r_{I,d} >= ell` and `dim K_{I,d} <= d-ell+1` for every layer
`ell <= d < (t-1)ell`; (b) that the resulting count bound `q^{d-ell+1}` is
`poly(n)` at fixed excess in the `q = poly(n)` window (a numeric check of the
exponent); (c) that the sole violations of (L13) occur exactly at the top defect
`d = (t-1)ell` (excess `(t-2)ell`, outside fixed-`c`); (d) the witness layers
`e in {2, 5}` lie below the top defect. All PASS. (The independent existence
witnesses are reproduced by the banked
`verify_l1_full_petal_growing_defect_witnesses.py`.)
