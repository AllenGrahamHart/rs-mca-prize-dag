# Proof

The maximal-row field-degree collapse leaves exactly `e=1` and `e=2`. In
both cases the evaluation-domain condition `2^41 | q-1` gives

```text
4 | q-1,
```

so `gcd(4,q-1)=4`. This proves that `(MCS2)` is the fourth-power subgroup
test in every branch.

If `e=1`, then `q=p`. The characteristic is not three because
`q>=3*2^128`. Thus `p` is either one or two modulo three. Accordingly
`gcd(3,p-1)` is three in the first residue class and one in the second.

If `e=2`, then `q=p^2` and again `p!=3`. Fermat's congruence modulo three
gives

```text
p^2=1 mod 3,
```

so `gcd(3,q-1)=3`. This proves `(MCS1)` and the cubic activation table.

The finite-field multiplicative group is cyclic. Its cube and fourth-power
subgroups are the kernels of exponentiation by `(q-1)/gcd(3,q-1)` and
`(q-1)/gcd(4,q-1)`, respectively. The coupled-norm dependency therefore
specializes exactly to `(MCS2)--(MCS3)`, while retaining its exact coupling
in every branch.

Finally, a descent from `F_(p^2)` to `F_p` changes the multiplicative group
in which a character is evaluated. Nothing above identifies those two
subgroup tests, so the stated descent warning is necessary. QED.
