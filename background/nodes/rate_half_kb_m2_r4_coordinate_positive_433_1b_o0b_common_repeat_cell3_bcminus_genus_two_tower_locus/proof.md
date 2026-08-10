# Proof

Substitute `t=epsilon_1 epsilon_2 r^2` into the three compact equations.
Their exact common polynomial factor is `r^2`, which is excluded by the
inherited guard. Let the three primitive quotients be `f_0,f_1,f_2`.

For every one of the four root-sign rows, exact standard-basis reduction
after saturation by the complete inherited guard proves both containments

```text
<f_0,f_1,f_2> = <F(b,c), R_epsilon(r,b,c)>,
```

where `R_epsilon` is the second equation in the statement. Concretely, all
three `f_j` reduce to zero modulo the right-hand ideal, while `F` and
`R_epsilon` reduce to zero modulo the left-hand ideal. Both saturated ideals
have dimension one. Thus the equations are necessary and sufficient, not
merely consequences of the compact system.

For the geometric form, set

```text
x=(b+1)/(b-1),  y=(c+1)/(c-1),  q=x/y.
```

The guard makes every displayed denominator nonzero. Clearing denominators
in `F` and substituting `x=qy` gives

```text
8 y^3 (D(q)y^2-N(q)).
```

The guard also has `y != 0`, proving the displayed quadratic model. Its
degree-six hyperelliptic polynomial is

```text
N(q)D(q)=q^6+8q^5+14q^4+12q^3+25q^2+4q.
```

Its integer discriminant is `-2^32*13`, whose residue modulo
`2130706433` is `1694498843`, hence nonzero. The polynomial is squarefree;
the standard genus formula for a squarefree degree-six hyperelliptic model
gives genus two. Finally, division of `R_epsilon` by the guarded factor
`bc-1` gives the quadratic equation for `r`. QED.
