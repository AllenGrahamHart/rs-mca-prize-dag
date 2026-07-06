# moment_trade_staircase proof

Let `B` be a block of roots and let

```text
L_B(X) = prod_{b in B} (X - b)
       = X^b - e_1(B) X^{b-1} + e_2(B) X^{b-2} - ...
```

If `e_1(B) = ... = e_t(B) = 0`, then the top `t` sub-leading coefficients of
`L_B` vanish. Thus replacing one such block by another `t`-moment-null block
does not change the top `t` coefficients of the full locator, provided the
blocks are inserted in the same residual tail.

More generally, for a disjoint family of `t`-moment-null blocks
`B_1, ..., B_R`, the locator of any union of selected blocks, multiplied by a
fixed tail locator, has top coefficients depending only on the fixed tail and
on the number and sizes of the selected blocks. In the equal-size staircase
case those data are fixed, so all selected locators share the top `t`
coefficients.

For Reed-Solomon exact-list counting, sharing the top `t` locator coefficients
is exactly the condition that the corresponding locator differences have
degree `< k`. Hence every such block family produces the same exact-list
staircase mechanism as the quotient and dihedral families. Symmetry is only a
special source of moment-nullity; the algebra uses only the vanishing elementary
symmetric functions.

The per-row question of whether primitive moment-null block families exist is
not part of this mechanism lemma; that is the role of
`x4b_moment_trade_exclusion`.
