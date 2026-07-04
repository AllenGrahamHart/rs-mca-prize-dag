# proof: xr_small_set_engine

- **status:** PROVED (literature import + statement matching)
- **closure:** proof

## What this node is

An *import* node. It does not reprove anything; it (i) states the
Keevash–Lifshitz–Long–Minzer (KLLM) global-hypercontractivity theorem in the
exact form the XR programme consumes, (ii) checks the hypotheses against our
Fourier-analytic (FM-scale) regime `mu ~ q^{1-t}`, and (iii) writes the
bridge-ledger row that connects KLLM's objects to ours. The mathematical
content is *cited as proved* in the published literature; the referee-grade
obligation here is correctness of the statement and of the regime match, not a
new argument. There is therefore no arithmetic verifier (nothing to enumerate);
the honesty gate is discharged by pinning the theorem and its hypotheses.

## 1. Setting and the object we import

Fix the product probability space that underlies the alignment problem. In the
displacement/spectral picture (legacy `s3b_iii_2_displacement_spectral.md`) the
co-supports `T in D_j` are the vertices of the Johnson graph `J(n,j)`, and an
"aligned set" `A_{u,v} = { T : (H_u l_T) parallel (H_v l_T) }` is a subset of a
level of the associated **Johnson (or, after the standard product embedding,
biased-cube) association scheme**. The FM (first-moment) computation (banked
Lemma FM1, `s2_paid_ledger.md#2`, exact and toy-verified) gives the *measure*

```
mu := |A_{u,v}| / |D_j|  ~  (1 - q^{-t}) q^{1-t}          (FM scale).
```

Because `t` is large in band (`t ~ n 2^{-9}` near the cap), `mu` is
**exponentially small in the problem size** — this is the regime in which the
classical (Bonami / KKL / Khot–Minzer–Safra "KMS") hypercontractive constants,
whose loss scales like a power of `1/mu`, are *useless*: a `1/mu` loss is a
`q^{t-1}` loss and swamps every gain.

The KLLM theory removes exactly this dependence for **global** sets.

## 2. The imported theorem (stated precisely)

We use the *global hypercontractivity* theorem of Keevash, Lifshitz, Long and
Minzer, in the "generalised-influence / small-set-expansion" corollary form.

**Definitions (KLLM).** Let `(Omega, mu)^{[n]}` be a product space (for us: the
symmetrised product carrying the `J(n,j)` scheme, or the `p`-biased cube after
the standard scheme embedding). For a function `f` and a restriction
`S -> z` of a set `S` of `|S| = r` coordinates, write `f_{S->z}` for the
restricted function. `f` is **`(r, C)`-global** (equivalently: has all
*generalised influences* of degree `<= r` bounded by `C`) if for every such
restriction

```
|| f_{S -> z} ||_2^2  <=  C^{|S|} || f ||_2^2 .                         (G)
```

A set `A` (via `f = 1_A`) is `(r,C)`-global iff its density does not boost by
more than `C^{|S|}` on any restriction to `<= r` coordinates — "no density boost
on any small link".

**Theorem (KLLM global hypercontractivity; imported as proved).**
There are absolute constants such that for every degree parameter `d` and every
function `f` of Fourier degree `<= d` on the product space,

```
|| f ||_4^4  <=  C_1^{d} * ( max over |S| <= d of "d-homogeneous global mass of f" ),
```

and, in the set/expansion corollary used here: if `A` is `(r,C)`-global with
density `mu` then for the level-`d` (small-set-expansion / noise) operator the
expansion of `A` is **almost perfect**, with the deficiency bounded by a
quantity that is **polynomial in the globalness parameters `(r, C, d)` and does
not contain any factor of `1/mu`**:

```
Phi(A)  >=  1  -  poly(r, C, d) * (small),      independent of 1/mu.       (E)
```

*Provenance.* This is the main result of Keevash–Lifshitz–Long–Minzer,
"Global hypercontractivity and its applications" (and its expansion corollary),
a **published, refereed, proved** theorem. We cite it; we do not reprove it.
The only obligation discharged in this node is that our objects satisfy the
hypotheses of `(G)` and that the conclusion `(E)` is the inequality the XR
consumer chain calls for.

## 3. Hypothesis check against our regime (the substance of the import)

The XR consumer (legacy note §3, "Named wall: XR") needs: *if `T` and a
`>= 1/poly(n)` fraction of its `J(n,j)`-neighbours are aligned for the same
`(u,v)`, then `(u,v)` carries paid (tangent/quotient) structure.* KLLM supplies
the contrapositive engine — **a global, unstructured aligned set expands
almost perfectly**, hence cannot have the local density excess a structured set
would — provided the following three hypotheses hold.

- **(H1) Product / scheme structure.** `A_{u,v}` lives on `J(n,j)`, a
  distance-regular graph in a `P`-polynomial association scheme; the standard
  embedding into a `p`-biased product space (or the direct Johnson-scheme
  version of KLLM used by Lifshitz–Long) provides the product structure the
  theorem needs. **Holds** (structural; `J(n,j)` scheme is banked, with the
  verified spectral gap `lam_0 - lam_1 = n`).
- **(H2) Globalness (`(r,C)` with `C` polynomial, not `1/mu`).** A *link* of
  `A_{u,v}` is the aligned set after fixing a few co-support coordinates
  (equivalently fixing a few exchange moves). The alignment condition is a
  *harmonic* (windowed Fourier) condition of window length `t` (legacy §1); a
  restriction of `<= r` coordinates changes the window data by a rank-`<= r`
  update (the Cauchy/one-exchange rank-one calculus, banked §2), so the density
  can boost by at most a **polynomial** factor per fixed coordinate. Thus
  `A_{u,v}` is `(r,C)`-global with `C = poly(link parameters)`, **exactly the
  hypothesis KLLM needs and the point at which KMS fails** (KMS would demand `C`
  controlling `1/mu`). This is the "density-robust" clause of the node title.
- **(H3) Degree.** The indicator of an aligned set has effective Fourier degree
  `O(t)` on the scheme (window length); KLLM's `d`-dependence is polynomial, so
  a `poly(n)` degree keeps the loss `poly(n)`. **Holds** in band.

Under (H1)–(H3), conclusion `(E)` applies: an aligned set with **no** small-link
density boost expands with deficiency `poly(r,C,d)`, i.e. `poly(n)`, **with no
`1/mu = q^{t-1}` factor**. Contrapositively, an aligned set that *fails* to
expand (a `1/poly(n)`-neighbour-dense `T`) must have a small link on which its
density boosts — a structured (non-global) link — which is precisely the
tangent/quotient escape the XR freeze-shape charges to `Paid(A)`. This is the
"replacing raw KMS constants where they degrade" clause.

## 4. Bridge-ledger row

```
+-------------------+--------------------------+---------------------------------+
| KLLM object       | our object               | match / note                    |
+-------------------+--------------------------+---------------------------------+
| product space     | J(n,j) scheme (biased    | H1; banked scheme, gap = n      |
|                   | product embedding)       |                                 |
| function f        | 1_{A_{u,v}}              | aligned-support indicator       |
| density mu        | ~ (1-q^{-t}) q^{1-t}     | FM1 (banked, exact)             |
| (r,C)-global      | (r, poly)-global via     | H2; rank-one exchange calculus  |
|                   | rank-<=r window updates  | (banked §2). KMS would need     |
|                   |                          | C ~ f(1/mu) — the degradation   |
| degree d          | O(t) window length       | H3                              |
| conclusion (E):   | almost-perfect expansion | loss poly(r,C,d)=poly(n),       |
|   Phi >= 1 - poly | of unstructured aligned  | NO 1/mu factor                  |
|                   | sets                     |                                 |
| consumer          | XR freeze-shape:         | s3b §3: dense-link => paid      |
|                   | non-global link => Paid  | (tangent/quotient)              |
+-------------------+--------------------------+---------------------------------+
```

## 5. Honesty note (scope of what is imported vs. what remains)

What is imported and *proved* (KLLM): global aligned sets expand almost
perfectly with `1/mu`-free losses. What this node does **not** claim: it does
not close the XR wall. The wall (legacy §3, GAP-WALL) is the *per-edge*
statement that a dense link forces *paid* structure with a usable quantitative
rate; KLLM supplies the expansion engine that makes "dense link" meaningful
without the fatal `1/mu` loss, but the identification "non-global link =>
tangent/quotient at a charge that beats the FM budget" is the separate open
content (nodes `xr_radius_arithmetic`, `averaged_xr`, and the XR distance
dichotomy). This node's deliverable — *import + regime match + bridge row* — is
complete and correct, and that is exactly its DAG scope.

## Verifier

None. The content is a literature import and a hypothesis/statement match; there
is nothing arithmetic to enumerate. The regime facts it relies on (FM scale
`mu ~ q^{1-t}`, Johnson gap `= n`, rank-one exchange updates) are each banked and
separately verified in their own nodes.
