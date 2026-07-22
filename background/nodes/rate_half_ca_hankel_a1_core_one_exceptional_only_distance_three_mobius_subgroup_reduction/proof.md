# Proof

The `e` disjoint pairs supply `2e=2^39-2` ordered solutions of `(MSR1)` in
`H x H`.

Suppose first that `alpha gamma!=0`. The polynomial

```text
P(x,y)=beta xy+alpha(x+y)-gamma
```

is absolutely irreducible by `alpha^2+beta gamma!=0`, has bidegree `(1,1)`,
has `P(0,0)!=0`, and has `deg P(x,0)=1`. The subgroup-curve estimate quoted
in `source.md` therefore gives

```text
#{(x,y) in H^2:P(x,y)=0}<=32 N^(2/3).                (1)
```

Its size hypotheses hold because `100<N` and
`N<p^(3/4)/3` follows from `p>2^167`. But

```text
32 N^(2/3)<2^33<2^39-2=2e,                          (2)
```

contradicting the matching.

Now let `gamma=0` and `alpha!=0`. If `beta!=0`, inversion preserves `H`,
and division of `(MSR1)` by `xy` gives

```text
x^(-1)+y^(-1)=-beta/alpha!=0.                       (3)
```

In the variables `u=x^(-1),v=y^(-1)`, this is the absolutely irreducible
bidegree-`(1,1)` polynomial `alpha(u+v)+beta`, whose constant term is
nonzero. The same subgroup-curve theorem therefore gives the bound `(1)`,
again smaller than `2e`. Hence `beta=0`, and `(MSR1)` becomes `x+y=0`,
which is `(MSR2)`.

Finally let `alpha=0`. Nonsingularity in `(MSR1)` forces
`beta gamma!=0`, and the equation is `xy=gamma/beta`. Since it has a
solution in `H x H`, the constant `c=gamma/beta` lies in `H`. This is
`(MSR3)` and exhausts all cases. QED.
