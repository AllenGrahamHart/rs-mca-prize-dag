# Proof

Write `A=(1-H)\{0}`. A product representation of `t` has

```text
a=1-x, b=1-y, x,y in H\{1},
(1-x)(1-y)=t.
```

Since `t` is nonzero, `x=1` cannot occur. Solving for `y` gives

```text
y = 1 - t/(1-x) = 1 + t/(x-1).
```

Thus choosing `x in H` whose image under the displayed inversion lies in `H`
is bijective with choosing `(a,b) in A^2` with `ab=t`. Hence
`P(t)=I_inv(t)`.

Similarly, a quotient representation has

```text
c=1-z, d=1-w, z,w in H\{1},
(1-w)/(1-z)=t.
```

Solving for `w` gives

```text
w = 1 - t(1-z) = 1 + t(z-1).
```

The affine intersection `I_aff(t)` also contains `(z,w)=(1,1)`. For `t!=0`,
if either coordinate equals `1`, the equation forces both to equal `1`.
Therefore this is the unique intersection point not corresponding to a valid
pair in `A^2`, proving `R(t)=I_aff(t)-1`.

Finally, if `R(t)>=1`, then `I_aff(t)>=2`. Under the proposed simultaneous
bound,

```text
P(t)=I_inv(t) <= 39-2 I_aff(t) <= 35.
```

This proves the reduction to the paired PGL2 intersection bound. No claim that
the constant 39 estimate itself has been proved is made here.

