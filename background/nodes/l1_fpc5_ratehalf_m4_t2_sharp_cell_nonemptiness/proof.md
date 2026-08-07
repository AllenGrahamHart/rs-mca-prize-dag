# Proof: finite sharp-cell nonemptiness

The certificate partitions `H_32` into a core of size `15`, a background of
size `1`, and four petals of size `4`. For each layout, touched pair, and
degree-five core locator `F=L_D`, it interpolates the unique degree-at-most-five
polynomials `W_1,W_2` corresponding to touched labels `(1,0)` and `(0,1)`.
The remaining equations on the second petal are linear in the label ratio
`lambda`:

```text
W_1(x)+lambda W_2(x)=lambda F(x).
```

The verifier solves this rank-one system exactly in `F_97`; it does not sample
`lambda`. It retains only `lambda notin {0,1}`, `W` nonzero on every missed
core point, and then chooses distinct nonzero labels on the untouched petals
outside their finite forbidden value sets. These conditions are exactly
petal fullness, exact core defect, and no untouched-petal agreements.

For every survivor define

```text
P=L_(C\D)W.
```

Then `deg P<16`. It vanishes on the ten retained core points and agrees with
the zero background value because `W` vanishes on the background. On a petal
`T_i`, cancellation of the nonzero retained-core locator shows

```text
P=c_iL_C       iff       W=c_iF.
```

Thus the retained tests give exactly the printed two full petals and no
other petal points. The agreement count is `10+1+4+4=19`, the list threshold.

The exhaustive deterministic loop gives (NE1). The independent node verifier
reconstructs seed `3`, checks (NE2), and evaluates its complete received word
point by point. QED.
