# L1 cofactor-depth budget cancellation and sparse-image fence

- **status:** PROVED
- **role:** account exactly for the cofactor union in the locator-prefix route
- **consumer:** `l1_mixed_petal_amplification`

## Setup

Use the notation of `l1_exact_shell_fixed_cofactor_prefix_transport`.  After
normalizing the received word modulo degree-below-`k` codewords, let
`h=deg U`.  For an exact agreement shell of size `a>k`, put

```text
w=a-k,       e=h-a.
```

This node concerns `0<=e<k`, where the fixed-cofactor locator-prefix depth is

```text
d=w+e<a.
```

Let `D_a` be the `binom(n,a)` monic degree-`a` divisors of the domain
locator, let `Phi_(a,d)` retain the first `d` nonleading locator
coefficients, and write

```text
B_(a,d) = max_z |D_a intersect Phi_(a,d)^(-1)(z)|,
L_(a,d) = |Phi_(a,d)(D_a)|.
```

## Exact cancellation

The fixed-cofactor transport and the `q^e` possible cofactors give

```text
|E_a(U)| <= q^e B_(a,d).                              (CD1)
```

Consequently an ambient-normalized locator-prefix estimate

```text
B_(a,d) <= K_amb binom(n,a)/q^d                      (CD2)
```

implies, with no cofactor loss,

```text
|E_a(U)| <= K_amb binom(n,a)/q^w.                    (CD3)
```

For an image-normalized estimate

```text
B_(a,d) <= K_img binom(n,a)/L_(a,d),                 (CD4)
```

the exact conclusion is instead

```text
|E_a(U)| <= K_img (q^d/L_(a,d)) binom(n,a)/q^w.      (CD5)
```

Thus `q^e` is canceled by the `e` additional prefix equations only at
ambient scale, or after paying the full-image factor `q^d/L_(a,d)`.  A
primitive Q theorem normalized solely by the attained image does not remove
that factor.

With integer ceilings, a per-cofactor estimate by
`K ceil(binomial(n,a)/q^d)` gives the safe bound

```text
|E_a(U)| < K (binom(n,a)/q^w + q^e).                 (CD6)
```

The additive `q^e` is the exact rounding/sparse-occupation obstruction.

## Deployed-row fence

Grande Finale v3 prints the active depth-`w` full-slice means and budgets.
Using its field orders gives the following exact route diagnosis.

| row | `ceil(binomial(n,a+)/q^w)` | first deeper ambient mean `<1` | first `e` with `q^e>B*` |
|---|---:|---:|---:|
| KoalaBear MCA | 57,198,030,366 | `e=2` | `e=2` |
| KoalaBear list | 65,065,153,468 | `e=2` | `e=2` |
| Mersenne-31 MCA | 1,752,700 | `e=1` | `e=1` |
| Mersenne-31 list | 1,993,678 | `e=1` | `e=1` |

For KoalaBear the depth-`w+1` ambient means lie strictly between `1` and
`27`, respectively `1` and `31`; depth `w+2` is already sparse.  For
Mersenne-31 depth `w+1` is already sparse.  Once `q^e>B*`, the raw union over
`q^e` potentially nonempty per-cofactor cells cannot by itself certify the row
budget even if every occupied deeper fiber is a singleton.  This is a route
fence, not a counterexample: a collective theorem may prove that very few
cofactor targets are occupied. More precisely,
`l1_cofactor_prefix_pade_graph_normal_form` proves that all possible targets
form one codimension-`w` graph, so the collective theorem is a split-divisor/
graph intersection estimate.

## Scope

The current upstream row-sharp Q target is posed at the active depth `w`; it
does not supply a theorem uniform in `(a,w+e)`.  The proved F2 ladder/tower
identity transfers the Fourier model to prime-power fields, not max-fiber
constants between prefix depths.  Therefore `(CD3)` is an exact conditional
interface, not a closure of L1. Divisor/Pade-section transversality and
target-sensitive control after effective-image collapse remain open. The
`e>=k` range has the same exact section representation in
`l1_full_locator_pade_section_all_cofactors`, but this cancellation theorem
does not bound it.
