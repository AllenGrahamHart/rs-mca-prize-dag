# F3 h=8 x83 parity reduction

Status: PROVED STRUCTURAL FILTER FOR THE NON-ANTIPODAL x83 CERTIFIER.

This packet adds a sound zero-cost filter to the remaining h=8 n=64
non-antipodal x83 support target.  It does not close the h=8 residual, but it
rules out a whole false subcase inside the certifier: a non-antipodal full-zero
support cannot have all high odd locator coefficients equal to zero.

## Statement

Let

```text
L(X)=X^16+c15 X^15+...+c0
```

be the locator of a 16-support in `mu_64`.  The x83 forced square root is the
unique monic degree-8 polynomial `S(X)` whose square matches the top nine
coefficients of `L(X)`.

If

```text
c15=c13=c11=c9=0,
```

then the odd coefficients of `S` are forced to vanish.  Therefore `S(X)^2` is
even.  If the support is x83 full-zero, the low obstruction equations

```text
coeff_i(S^2-L)=0,  i=1,3,5,7,
```

force

```text
c7=c5=c3=c1=0.
```

Thus `L(X)` is an even polynomial.  Since its roots are distinct elements of
`mu_64`, the root set is stable under `x -> -x`; equivalently, the support is
antipodal.

Contrapositive:

```text
Any non-antipodal x83 full-zero support has at least one nonzero coefficient
among c15,c13,c11,c9.
```

The symbolic proof only divides by `2`, so it is valid in every odd
characteristic used by the h=8 rows.

## Role In The Certifier

The remaining h=8 target is still the non-antipodal support certifier.  This
packet lets that certifier safely skip any non-antipodal support whose high odd
locator coefficients all vanish, because such a support cannot be x83
full-zero.

The companion `F3_H8_ODD_CHART_RECOVERY_COMPILER.md` uses the same
contrapositive as an open cover: the remaining non-antipodal reciprocal target
lies on one of the four odd charts `c15,c13,c11,c9`.

This is deliberately weaker than exponent-unit or reflection canonicalization.
Those shortcuts are already refuted by
`F3_H8_EXPONENT_UNIT_FALSIFIER.md`.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_x83_parity_reduction.py
```

Expected digest:

```text
H8_X83_PARITY_REDUCTION_PASS
```
