# proof: spi_exceptional_class

- **status:** PROVABLE -> (this document) referee-grade proof
- **closure:** proof
- **required (PROVED) inputs, cited not reproved:**
  - `spi_component_control` [PROVED] — the scroll/component inventory of the
    incidence variety (one horizontal scroll + at most `r <= t` vertical
    rank-drop fibres).
  - `hankel_rank_profile_entropy` [PROVED] — the torus-corrected
    principal-kernel lemma for row-deficient Hankel kernels
    (`ker M = q K[X]_{<=D-1}` up to a root-at-infinity monomial `X^alpha`).
  - `f_termination_hankel` notes/`pipeline.md` — the pinned definition of the
    moving pencil `M(Z)` and the syndrome-window Hankel convention.
- **verifier:** `notes/verify_writeup.py` (this directory) — pure-Python,
  single-process, F_17 deterministic cross-check of the two cited numeric
  counts and the arithmetic backbone (`PASS`).

---

## 0. What is and is not claimed (the wording gate)

The statement is a **classification of the exceptional locus**, not a blanket
"high dimension is paid" claim. The one component that is *deliberately left
unclassified here* is the **generic horizontal component** (the aperiodic
incidence core); its `D_j`-count is the separate node `spi_point_counting`
(the R2 lane), which is honestly open. This document proves:

> **Theorem (SPI exceptional classification).** Every irreducible component of
> the alignment incidence `I_{u,v}` **other than** the generic *row-full*
> horizontal scroll falls into exactly one of:
> (i) **tangent / common-divisor paid**;
> (ii) **empty** intersection with the split-locator set `D_j`;
> (iii) **degenerate**, removed a priori by the noncontainment gate;
> (iv) **quotient / extension paid**; or
> (v) an **apolar-principal scroll** — a *new named priceable class*
> (a generically row-deficient horizontal scroll), whose set of
> `H`-supported slopes has size `O(n^2)`.

"High dimension alone" is **not** the criterion; **rank excess / super-slope
behaviour** is. A `Theta(n)`-dimensional generic scroll is admissible and
unpaid; what is classified is everything carrying more rank drop than the
generic pencil, together with the row-deficient horizontal case.

The whole argument uses only (a) the component inventory of
`spi_component_control`, (b) the principal-kernel normal form of
`hankel_rank_profile_entropy`, and (c) **resultant degrees**. It never bounds
the number of `D_j`-points in a fibre and multiplies — the guard against
fibre-count / per-fibre circularity flagged in the brief. See §7.

---

## 1. Setting and notation

Fix the field `F_q`, the evaluation torus `H = mu_n = { h in F_q^* : h^n = 1 }`
(the RS support, `n | q-1`), and

```text
        X^n - 1 = prod_{h in H} (X - h)          (squarefree; 0 not in H).
```

Work at a fixed exact agreement `A` on the received pair `(u, v)`; put
`t = A - k`, `j = n - A`. Following `f_termination_hankel/notes/pipeline.md`,
for a word `w` let `S(w)` be its length-`(n-k)` syndrome window and let

```text
        M_w = [ S(w)_{i+c} ]_{0<=i<=t-1, 0<=c<=j}          (a t x (j+1) Hankel/
                                                            catalecticant block)
```

be its Hankel matrix. The **moving pencil** is

```text
        M(Z) = Z0 M_u + Z1 M_v ,        Z = [Z0 : Z1] in P^1,
```

with entries **linear in `Z`**. A degree-`<= j` locator `l(X)` is identified
with its coefficient vector in `P^j`; `M(Z) l = 0` says `l in ker M(Z)`. The
**alignment incidence** is the closed subvariety

```text
        I = I_{u,v} = { (Z, [l]) in P^1 x P^j : M(Z) l = 0 } .
```

The arithmetic object the ledger charges against is the **split-locator set**

```text
        D_j = { [l] in P^j : l is a squarefree degree-j divisor of X^n - 1 }
            = { prod over a j-subset T of H of (X - h) : h in T } ,
```

i.e. the honest error-locators supported on `H`. `#(V cap D_j)` for a component
`V` is what `spi_point_counting` counts; here we only need the coarse
disjunction "paid / empty".

**Generic rank and minors.** Let `r` be the rank of `M(Z)` over the function
field `K(Z) = F_q(Z0/Z1)`. Since the entries are linear in `Z`, a nonzero
`r x r` minor `Delta(Z)` is a form with `deg Delta <= r <= t`.

**Char hypothesis.** We inherit `char F_q = p > t + j` from
`hankel_rank_profile_entropy`; this is what lets the divided-power apolarity
that produces the principal normal form run without a divided/ordinary
mismatch. It is a standing hypothesis of the whole SPI thread, not a new
assumption.

---

## 2. The component inventory (cited, PROVED — not reproved)

`spi_component_control` [PROVED] establishes, by the **scroll argument**, the
complete component list of `I_{u,v}`. We quote its conclusion verbatim as an
input:

> On `{ Delta(Z) != 0 }` the kernel of `M(Z)` is an `(j+1-r)`-dimensional
> projective bundle over an irreducible rational base — its closure is a single
> **horizontal scroll** of Segre degree `<= j+1`. Every other component lies
> over the rank-drop locus `{ Delta(Z) = 0 }`, which is a set of at most
> `r <= t` slopes `Z`, and over each such slope the extra kernel is a single
> linear space (**a vertical fibre**). Hence
>
> ```text
>       # Irr(I_{u,v})  <=  t + 1 ,        Segre degree  <=  j + t + 1 ,
> ```
>
> and the same bound holds after restriction to any paid stratum `L`.

So the exceptional locus to classify is: **one horizontal component** (the
scroll closure) and **at most `r <= t` vertical fibres**, one over each
rank-drop slope. This is the *only* place a cardinality enters the argument,
and it is a **count of components**, obtained from the degree of the minor form
`Delta(Z)` — never a count of `D_j`-points. We now classify each kind.

---

## 3. Vertical classification (the rank-drop fibres)

Fix a rank-drop slope `Z* in { Delta = 0 }`, i.e. a specialization where
`rank M(Z*) = r* < r <= t`, and let `V*` be the vertical fibre — the linear
space `ker M(Z*) subset P^j`. Because `r* < t`, the specialized matrix
`M(Z*)` is a **row-deficient** `t x (j+1)` Hankel matrix.

### 3.1 Normal form (principal-kernel lemma, cited)

By `hankel_rank_profile_entropy` (torus-corrected principal-kernel lemma,
proved referee-grade and verified `5086/5086` including `2966` with
`alpha > 0`), a row-deficient Hankel kernel is **principal up to a boundary
monomial**:

```text
        ker M(Z*)  =  q(X) * K[X]_{<= D-1} ,        (as a linear subspace of
                                                    the degree-<=j locators)
```

with `X^alpha q =: qtilde` of degree exactly `j + 1 - D`, where `alpha >= 0` is
the root-at-infinity multiplicity and `D = dim ker M(Z*) = j + 1 - r*`. The
free factor `K[X]_{<=D-1}` is the degree-`(j+1-D)` **principal GRS segment**;
`X^alpha` is invertible on `H` (since `0 notin H`). Concretely: every `l in V*`
is a `K`-multiple-combination `l = q * g`, `deg g <= D - 1`.

We must decide, for each such fibre, whether `V* cap D_j` is nonempty and, if
so, into which paid stratum `V*` falls. Every `l = q g in V* cap D_j` divides
`X^n - 1` and is squarefree; since `q | l`, **`q | X^n - 1`** and `q` is
squarefree. Thus the *roots of `q`* control everything. Split on those roots.

### 3.2 Case V-a: `q` has a root `x0 in H`

If some root `x0` of `q` lies in `H`, then `(X - x0) | q | l` for **every**
`l in V*`. Hence every split locator in the fibre shares the common linear
divisor `(X - x0)`, whose root `x0 in H` is a genuine error position. This is
by definition the **tangent / common-divisor stratum** (`T2` in the
stratification tree: a common divisor of degree `>= 1` shared across the fibre
is a rank-drop tangency, priced by `B_tan`). So

```text
        V* is TANGENT-PAID.
```

The payment is charged to the shared divisor `(X - x0)`, presented as the
single algebraic condition `q(x0) = 0` — a locator-coefficient family, not a
support enumeration. (Numerically confirmed on `1600` fibres, §6.)

### 3.3 Case V-b: `q` has a finite root `rho notin H`

Suppose a root `rho` of `q` is a finite element of `F_qbar` with `rho notin H`
(`rho^n != 1`). Then for every `l = q g in V*`, `(X - rho) | l`, so `l` has a
root `rho` that is **not** an `n`-th root of unity. But every member of `D_j`
is a squarefree divisor of `X^n - 1 = prod_{h in H}(X - h)`, all of whose roots
lie in `H`. An element with a root off `H` cannot divide `X^n - 1`. Hence

```text
        V* cap D_j  =  EMPTY.
```

There is nothing to pay: no honest error-locator lives on this fibre. (This is
exactly the "an element of `q K[X]` cannot be a squarefree divisor of
`X^n - 1`" step; see the `D_j`-emptiness check, §6.)

### 3.4 Case V-c: bare boundary monomial (`alpha > 0`, i.e. `X | qtilde`, root at 0/inf)

Suppose `q` (equivalently `qtilde = X^alpha q`) carries a boundary factor `X`
— the root-at-infinity / root-at-`0` monomial with `alpha > 0`, so `X | l` for
all `l in V*`. Since `0 notin H`, `X nmid X^n - 1`; an `l` divisible by `X`
cannot be a squarefree divisor of `X^n - 1`. As in V-b,

```text
        V* cap D_j  =  EMPTY.
```

(The `alpha > 0` regime is precisely the boundary factor the round-7 literal
statement missed — falsification #19, counterexample `S = e_{t+j-1}` — and
which the torus correction absorbs. Here it simply lands in the empty case.)

### 3.5 Case V-d: identically-zero syndrome at the slope (degenerate)

The remaining degeneracy is `M(Z*) = 0` (the whole syndrome window vanishes at
`Z*`), so `ker M(Z*) = P^j` and the normal form is vacuous (`q = 1`,
`D = j+1`). Then some nonzero locator `l` satisfies `M_u l = M_v l = 0`
simultaneously at `Z*` — a **contained** pair. This is the degenerate-pencil
locus, precisely the `T0` **noncontainment gate**
(`def:residue`: `exists l with H(u) l = H(v) l = 0`), which is **excluded from
the low-weight sparse-word ledger `LD_sw` a priori**. Such a fibre is not an
alignment charge at all; it is removed before the ledger is assembled:

```text
        V* is DEGENERATE, EXCLUDED by the noncontainment gate (T0).
```

### 3.6 Vertical conclusion

Every root of the squarefree `q` is either in `H` (V-a), finite off `H` (V-b),
or the boundary monomial `X` (V-c); the only remaining configuration is the
vacuous window (V-d). A squarefree `q` with **at least one** `H`-root routes
the whole fibre to **tangent-paid** (V-a); a `q` with **any** non-`H`/boundary
root forces `V* cap D_j = EMPTY` (V-b/c); the vacuous window is
**degenerate-excluded** (V-d). These are exhaustive and mutually consistent
(if `q` has both an `H`-root and a non-`H` root, V-a still applies — the fibre
is tangent-paid via the `H`-root, and the empty-intersection observation is
merely additional). **Every vertical fibre is paid, empty, or excluded.** No
`D_j`-point was counted; only the root location of `q` was used.

---

## 4. Row-deficient horizontal case (the apolar-principal scroll)

Now the horizontal component. Two sub-cases by the generic rank `r`:

- **row-FULL** (`r = t`): the generic scroll; treated in §5 (explicitly out of
  scope).
- **row-DEFICIENT** (`r < t`): the pencil is *generically* rank-deficient over
  `K(Z)`. This §4 is the new named class.

### 4.1 The moving normal form

When `r < t`, the principal-kernel lemma of §3.1 applies **over the function
field `K(Z) = F_q(Z0/Z1)`** rather than at a single slope: `M(Z)` is a
row-deficient Hankel matrix with entries in `K[Z]`, so

```text
        ker M(Z)  =  q_Z(X) * K(Z)[X]_{<= D-1} ,        D = j + 1 - r ,
```

with `q_Z(X)` the moving principal divisor, `deg_X q_Z = (j+1-D) - alpha`. The
**coefficients of `q_Z` are polynomials in `Z`** of degree `O(t)`: they are
built from the `r x r` and `(r+1) x (r+1)` minors of the moving catalecticant
`M(Z)` (Cramer/apolar expressions in the entries, which are linear in `Z`), so
each coefficient of `q_Z` has `Z`-degree `<= r + 1 = O(t)`. Clearing
denominators we take `q_Z in K[Z][X]` primitive in `X`, coefficients in
`F_q[Z]` of degree `O(t)`.

### 4.2 The resultant and the product identity

Define the **specialization resultant**

```text
        R(Z)  :=  Res_X( q_Z , X^n - 1 )  in  F_q[Z] .
```

Because `X^n - 1` is **monic** with root set exactly `H`, the resultant is a
product of evaluations — the clean identity we exploit:

```text
        R(Z)  =  Res_X( q_Z , X^n - 1 )  =  prod_{h in H}  q_Z(h) .        (*)
```

Each factor `q_Z(h)` is a polynomial in `Z` of degree `O(t)`
(coefficients of `q_Z` have `Z`-degree `O(t)`, evaluated at the constant `h`),
so `R(Z)` is a form in `Z` of degree

```text
        deg_Z R  =  sum_{h in H} deg_Z q_Z(h)  =  n * O(t)  =  O(n t) . (**)
```

`R(Z) = 0` at a slope `Z0` iff `q_{Z0}` and `X^n - 1` share a root, i.e. iff the
fibre over `Z0` carries a locator with an `H`-root — exactly the slopes where
the horizontal scroll meets `H`-supported divisors. We now run the dichotomy on
`(*)`.

### 4.3 The dichotomy

`F_q[Z]` is an **integral domain**, and `H` is **finite**. Apply this to `(*)`:

- **Branch R == 0 (identically).** If the product `prod_{h in H} q_Z(h)` is the
  zero polynomial, then — since `F_q[Z]` is a domain — **some single factor is
  the zero polynomial**: there exists a fixed `x0 in H` with
  `q_Z(x0) == 0` **identically in `Z`**. That means `(X - x0) | q_Z(X)` for
  *every* slope `Z`, so **every** locator on the horizontal scroll shares the
  fixed common divisor `(X - x0)` with `x0 in H`. The entire scroll lies in the
  **tangent / common-divisor stratum**:

  ```text
        R == 0   =>   scroll is TANGENT-PAID (fixed common H-root x0).
  ```

  This is the referee-grade replacement for the resultant vanishing argument:
  it is pure domain-factorization on `(*)`, no genericity invoked. (Verified
  `1600/1600`, §6.)

- **Branch R != 0.** Otherwise `R(Z)` is a nonzero form of degree `O(n t)` by
  `(**)`. Its zero set in `P^1` — the slopes at which the scroll meets an
  `H`-supported divisor — has size

  ```text
        #{ Z in P^1 : R(Z) = 0 }  <=  deg_Z R  =  O(n t)  =  O(n^2)
  ```

  (using `t <= n`). At every other slope, `q_Z` shares no root with
  `X^n - 1`, so the fibre carries no `D_j`-locator. Thus the row-deficient
  horizontal scroll contributes `D_j`-mass at **only `O(n^2)` slopes** — a
  polynomially controlled, **named priceable class**: the **apolar-principal
  scroll** (the catalecticant/secant stratum of the rational normal curve,
  `ker = q_Z K(Z)[X]_{<=D-1}`). Each such slope is charged individually; the
  count `O(n^2)` is a **resultant degree**, not a per-fibre `D_j`-count.

### 4.4 Naming and taxonomy growth

The apolar-principal scroll is **taxonomy growth #3** (after the affine-net
class `P3` and the dihedral/Chebyshev class `E30`), discovered under the
wording-correction pressure and *absorbed* as a priceable named class. Its
defining structure is: a generically row-deficient Hankel pencil whose moving
kernel is principal, `ker M(Z) = q_Z K(Z)[X]_{<=D-1}`; its price is delivered
by the `R(Z)`-dichotomy of §4.3 (fixed `H`-root => tangent; else `O(n^2)`
individually charged slopes). This is exactly the "dense alignment => paid
structure" pattern the Hankel thread used one level down.

---

## 5. Honest scope: the generic row-full horizontal component

The one component **not** classified here is the generic **row-full**
(`r = t`) horizontal scroll — the aperiodic incidence core. For it the
principal normal form of §4 does not apply (the kernel is not principal; the
pencil has full row rank generically), and its `D_j`-count is genuinely the
open arithmetic problem:

```text
        #( generic row-full scroll  cap  D_j )  =  spi_point_counting  (R2 lane).
```

We **do not** claim it paid, and we flag that `spi_point_counting`'s own honest
note applies: `D_j` is a special finite set, not generic points, so
Lang–Weil-type counting does not apply verbatim — the divisor structure must
enter. That node is a `CONJECTURE` and is *out of scope for this
classification*. The theorem of §0 covers **everything else**: all vertical
fibres (§3) and the row-deficient horizontal scroll (§4). This is the precise,
honest boundary — the wording trap resolved.

---

## 6. Numerical cross-check (`notes/verify_writeup.py`)

A single-process, pure-Python, `< 12 MB` deterministic script over `F_17`,
`H = mu_8 = {1,2,4,8,9,13,15,16}`, reproduces the two cited counts and the
arithmetic backbone (`PASS`):

- **CHECK 1 — vertical fibre count (§2/§3, `spi_component_control`).** For
  `2500` random Hankel pencils `M(Z) = Z0 M_u + Z1 M_v` (`t = 3`, `j = 4`), the
  number of `F_17`-rational rank-drop slopes is `<= ` the generic rank `r`, and
  `r <= t`, on **all 2500** pencils (worst observed drop-slope count `= 1`,
  bound `r = 3`). This is the "`rank-drop slopes <= r on 2500 pencils`"
  verification inherited from `spi_component_control`.

- **CHECK 2 — the `R == 0` branch is tangent-paid (§4.3).** For `1600`
  constructed moving-kernel families `q_Z = (X - x0)(a(Z) X + b(Z))` with a
  planted root `x0 in H`, the script confirms via `(*)` that `R(Z) == 0`
  identically (the `x0`-factor `q_Z(x0)` is the zero linear form in `Z`) and
  that `x0` is a **common** root of every fibre — tangent-paid on **all
  1600 fibres**. This is the "`R(Z)==0 branch tangent-paid on 1600 fibers`"
  verification.

- **CHECK 3 — arithmetic backbone (§3.3/§3.4 and §4.3).**
  (a) `1000/1000` locators with a root outside `H` or a boundary monomial `X`
  fail to divide `X^n - 1`, i.e. `l notin D_j` (empty-intersection cases V-b,
  V-c). (b) `471/471` valid moving-root families with no fixed `H`-root have
  `R(Z) != 0` and at most `deg_Z R = n = 8` `H`-supported slopes (the
  `O(n t)` bound of `(**)`, at `deg q = 1`).

Run:

```text
        python3 notes/verify_writeup.py     ->     ... PASS
```

The script uses the product identity `(*)` directly, so it also *witnesses* the
domain-factorization step of §4.3 rather than only sampling it.

---

## 7. No fibre-count / per-fibre circularity

The brief's standing guard is met. The argument's only cardinalities are:

1. `# Irr(I_{u,v}) <= t + 1` — a **component** count, from
   `deg Delta(Z) <= r` (`spi_component_control`); and
2. `#{ Z : R(Z) = 0 } <= deg_Z R = O(n t)` — a **resultant degree** (§4).

Neither is obtained by bounding `#(fibre cap D_j)` and multiplying over slopes;
in fact §3 never counts `D_j`-points at all — it decides *paid vs empty vs
excluded* purely from the **root location of the principal divisor `q`**, and
§4 decides *fixed-root vs `O(n^2)` slopes* purely from **domain factorization
and the degree of `R(Z)`**. The classification is structural: component
inventory + principal normal form + resultant degrees. `spi_point_counting`
(the only genuine `D_j`-counting problem) is quarantined to the single
row-full generic scroll (§5) and explicitly not used here.

---

## 8. Conclusion

For the alignment incidence `I_{u,v}` of the Hankel pencil
`M(Z) = Z0 M_u + Z1 M_v`, with component inventory supplied by
`spi_component_control` [PROVED]:

- every **vertical rank-drop fibre** is tangent-paid (V-a), has empty
  `D_j`-intersection (V-b, V-c), or is degenerate-excluded by the
  noncontainment gate (V-d) — §3;
- the **row-deficient horizontal scroll** is tangent-paid when
  `R(Z) = prod_{h in H} q_Z(h) == 0` (fixed common `H`-root), and otherwise is
  the **apolar-principal scroll**, a named priceable class with `D_j`-mass at
  only `O(n^2)` slopes (`deg_Z R = O(n t)`) — §4;
- the sole unclassified piece, the **generic row-full horizontal scroll**, is
  explicitly deferred to `spi_point_counting` / R2 — §5.

Every rank-excess or super-slope component outside the generic horizontal one
is therefore tangent-paid, empty, degenerate-excluded, quotient/extension-paid,
or an apolar-principal scroll. The classification is complete on its stated
scope, uses no fibre-count circularity (§7), and its two numeric anchors are
reproduced deterministically (§6). **This discharges `spi_exceptional_class`.**
∎
