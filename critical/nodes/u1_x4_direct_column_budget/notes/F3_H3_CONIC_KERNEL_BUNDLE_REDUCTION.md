# F3 h=3 conic kernel-bundle reduction

Status: PROVED GEOMETRIC REDUCTION / SLOPE ARITHMETIC, NOT `RC-RANK`.

This packet gives a sharper proof primitive for the official conic
codimension target.  It does not prove the needed splitting bound.

## Setup

Keep the notation of `F3_H3_CONIC_RATIONAL_CURVE_INTERFACE.md`, and put

```text
d = 2HM = 6H(B-1).
```

Let

```text
W = span{R_U^b1 R_V^b2 R_W^b3 R_Q^(M-b1-b2-b3) : 0 <= b_i < B}
    <= H0(P^1, O(d)).
```

The full conic span is exactly the image of

```text
H0(O(A-1)) tensor W -> H0(O(d+A-1)).
```

Assume the boxed base products have no common base point.  In the repaired
same-fiber conic chart this is supported by the pairwise-gcd guard for
`P_U,P_V,P_W,Q`; the general theorem should keep this as an explicit
degeneracy exclusion.

## Exact Formula

Let `r=dim W`, and let `M_W` be the kernel bundle of the evaluation map

```text
0 -> M_W -> W tensor O -> O(d) -> 0.
```

On `P^1`,

```text
M_W = direct sum_{i=1}^{r-1} O(-e_i)
```

with `sum_i e_i=d`.  Twisting by `O(A-1)` and taking cohomology gives

```text
codim image(H0(O(A-1)) tensor W -> H0(O(d+A-1)))
  = h1(M_W(A-1))
  = sum_i max(e_i - A, 0).
```

Therefore the official conic rank theorem is reduced to the splitting-excess
bound

```text
sum_i max(e_i - A, 0) <= 1847.
```

This is equivalent to the codimension target once the correct repaired
basepoint-free `W` is fixed.

## Official Slope Arithmetic

If the `B^3` boxed base products are independent, the kernel bundle has rank
`B^3-1`.  Its average splitting degree is then

```text
d / (B^3-1).
```

The replay verifies that for all official exact-profile rows

```text
ceil(d/(B^3-1)) <= A,
```

with the tight margin

```text
A - ceil(d/(B^3-1)) = 1320
```

at `s=13`.

This does not prove balanced splitting or independence of the boxed base
products.  It says that a balanced kernel-bundle theorem would give codimension
zero, hence would be stronger than the required `1847`-defect theorem.

## Role

The conic rank wall can now be attacked as a vector-bundle statement:

```text
prove that the repaired boxed product linear series W has kernel splitting
excess at most 1847 above the official A-window.
```

This avoids the false complete-series shortcut and gives a concrete reason why
the official dense boxes should be much easier than arbitrary boxes satisfying
only `H >= 6A`.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_conic_kernel_bundle_reduction.py
```

Expected digest:

```text
H3_CONIC_KERNEL_BUNDLE_REDUCTION_PASS
```
