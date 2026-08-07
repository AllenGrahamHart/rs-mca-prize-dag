# Proof

Fix `z` and an `A`-subset `S` in the fiber over `z`. The leading term and the
next `t` coefficients cancel in

```text
P_S=U_z-Q_S,
```

so `deg(P_S)<A-t=K`. On every point of `S`, `Q_S` vanishes, hence `P_S=U_z`.
Conversely, if a polynomial `P` of degree `<K` agrees with `U_z` on at least
`A` points, then `U_z-P` is monic of degree `A` and has those `A` roots. It is
therefore their locator `Q_S`, whose first `t` coefficients equal `z`.
Distinct supports have distinct locators and hence distinct codewords. Since a
nonzero degree-`A` polynomial has at most `A` roots, every agreement is exact.
This proves the bijection.

For the characteristic qualification, put

```text
ell_S^*(T)=prod_(x in S)(1-xT)=1+c_1T+...+c_A T^A.
```

Its logarithmic derivative is

```text
(ell_S^*)'/ell_S^*=-sum_(j>=0) p_(j+1)(S) T^j.
```

Thus `p_1=...=p_t=0` if and only if `i c_i=0` for every `1<=i<=t`.
In characteristic `p`, this forces exactly the `c_i` with `p` not dividing
`i`; the `p`-multiple coordinates are not determined. Consequently the set of
all `t`-null subsets is not one full locator-prefix fiber once `t>=p`.

It remains to disprove an unqualified max-to-null shortcut. For
`D=F_17^*`, `A=9`, and `t=1`, the prefix is minus the subset sum. Let
`N(s)` count the `9`-subsets with sum `s`. Fourier inversion over `F_17`
uses

```text
prod_(x in F_17^*)(1+T omega^(lambda x))
  =(1+T^17)/(1+T)=1-T+...+T^16
```

for every nonzero `lambda`; its `T^9` coefficient is `-1`. Since
`binom(16,9)=11440`,

```text
N(0)=(11440-16)/17=672,
N(s)=(11440+1)/17=673  for s nonzero.
```

The null fiber is therefore not heaviest. A null-fiber theorem remains useful
evidence, but it cannot replace a maximum-prefix theorem without another
proved reduction. QED.
