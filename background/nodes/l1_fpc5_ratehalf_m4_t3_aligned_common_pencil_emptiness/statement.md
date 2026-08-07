# Rate-half FPC5 `M=4,t=3` aligned common-pencil emptiness

- **status:** PROVED
- **consumer:** `l1_fpc5_ratehalf_m4_t3_split_slice_payment`

Use one fixed guarded LS6 atom and put

```text
M=L_2L_3,       j=2ell-a,       s=ell-a.
```

## Low-degree multiplier gate

If the atom is nonempty, then

```text
deg Etilde>=a.                                         (CP1)
```

## Aligned common-pencil consequence

Suppose the three touched petal locators and source labels are aligned in one
degree-`ell` common pencil: for a monic `P`, distinct `z_i`, and
`alpha!=0,beta`,

```text
L_i=P-z_i,       c_i=alpha z_i+beta,       i=1,2,3.   (CP2)
```

After affine source-label normalization, the associated multiplier is the
nonzero constant

```text
Etilde=(z_2-z_1)^(-1).                                (CP3)
```

Since `a>=1`, `(CP1)` fails. Therefore every aligned common-pencil LS6 atom
in the Johnson-nonpositive rate-half tail is empty.

## Scope

This removes the exactly aligned quotient/common-pencil source. It does not
remove a common petal pencil whose source labels are not affine in its fiber
values, arbitrary petal locators, even-defect dyadic pullback locators, or
reciprocal/dihedral strata.
