# Proof

The exact residual formula in the dependency gives `(ILB2)`. At the lowest
intermediate degree it gives `t=2`, and the dependency already proves the
degree-eighteen contradiction.

Increase `v` by `ell>=1`. Then `h` decreases by `ell`, so

```text
t=2+3ell>=5.                                         (1)
```

Write `delta_4` and `tau_t` for the nonzero leading coefficients of `D` and
`T`. The leading coefficient of `A` is

```text
4(t+3r)delta_4 tau_t.                                (2)
```

It is nonzero. In positive characteristic `p>d`, the factor four is a unit
and

```text
0<t+3r<=4r+1<d<p;                                   (3)
```

the characteristic-zero case is immediate. Therefore `deg A=t+4`.

The two terms of `J` have degrees `3t+12` and `7t`. Since `t>=5`,
`7t>3t+12`; the coefficient `27 tau_t^7` is nonzero. Thus `deg J=7t`.

By `(ILB4)`, a survivor has `v<=deg J=7t`. Substitute `(ILB2)`:

```text
v<=7(3v-2r+4)
  ==> 10v>=7r-14.                                    (4)
```

For `r=2^37-1`, the least integer satisfying `(4)` is

```text
ceil((7r-14)/10)=96,207,267,429.                     (5)
```

The floor is `(2^38-4)/3=91,625,968,980`, so every degree through one below
`(5)` is excluded. Their number is

```text
96,207,267,429-91,625,968,980=4,581,298,449.
```

This proves `(ILB6)--(ILB7)` and the stated scope. QED.
