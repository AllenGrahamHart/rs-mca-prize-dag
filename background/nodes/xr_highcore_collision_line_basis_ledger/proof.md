# Proof

Write `V=A-A`. For a collision line `ell`, choose two witnessing errors
`e,f` at distinct slopes and let `W=Z(e) intersect Z(f)`, where `Z(e)` is the
zero set of `e`. A coordinate function restricted to an affine line is
affine-linear. If it vanishes at the two distinct points `e,f`, it vanishes
on the whole line. Hence `W=W_ell` and `|W_ell|=k`.

We next compute the kernel of restriction `V->F^W`. The nonzero direction

```text
q=(e-f)/(gamma_e-gamma_f)
```

lies in that kernel and satisfies `Hq=y_1`. Conversely, let `z in V` vanish
on `W`. Since `H(V) subset <y_1>`, write `Hz=beta y_1`. Both `z` and `q` are
supported on `D\W`, a set of size `R`. If `beta=0`, then `z` is a kernel
word of weight at most `R`, so the distance hypothesis gives `z=0`. If
`beta!=0`, then `z-beta q` is such a kernel word, and hence is zero. Thus the
restriction kernel is exactly `<q>` and its rank is `s-1`. In particular
`b_ell>=1`.

Fix coordinates on `A`, so its errors are `e_*+Bx` with `B` of column rank
`s`. For every basis `J` counted by `b_ell`, the equations

```text
(e_*+Bx)|_J=0
```

have rank `s-1` and their solution set is exactly `ell`. Therefore one
`(s-1)`-subset `J` cannot be counted by two distinct collision lines.
Injecting all pairs `(ell,J)` into the `(s-1)`-subsets of `D` proves `(CLB1)`.

Let `m_ell` be the number of nonzero coordinate rows of `B` within `W_ell`.
Choose one basis of the rank-`s-1` row matroid there. Every nonloop row outside
that basis has a nonzero coefficient in its basis expansion, so replacing a
basis row with that row at a nonzero coefficient gives a new basis. Different
outside rows give different bases. Hence

```text
b_ell >= 1+(m_ell-(s-1)),
m_ell <= b_ell+s-2.                                      (4)
```

A loop row means that every direction in `V` is zero at that coordinate. As
`ell` vanishes there, the constant affine value is also zero, so every member
of `A` vanishes at every loop in `W_ell`. Removing those loops leaves a common
support chart consisting of `D\W_ell` plus the `m_ell` nonloops. Its size is
`R+m_ell`, proving `(CLB1b)`.

Every member on `ell` has at least

```text
n-r=k+h
```

zeros. Exactly `k` coordinate functions vanish identically on the line. Any
other coordinate function has at most one zero on `ell`, so the petal sets
`Z(e)\W_ell` are disjoint for distinct members of `P intersect ell`. Each has
size at least `h`, and all lie in the `R` coordinates outside `W_ell`. This
proves `(CLB2)`.

Finally, take all distinct basis-rich witness lines for `P_hi(B)`. They cover
`P_hi(B)`, each contains at most `L` members, and `(CLB1)` permits at most
`floor(C(n,s-1)/B)` such lines. This proves `(CLB3)`. Applying the argument to
one selected error above every slope can only reduce the object being counted.

For `(CLB4)`, choose a collision line attaining `b_*`. Its loop chart from
`(CLB1b)` contains the entire affine family and has size at most
`R+b_*+s-2`. Coordinate rows outside that chart are zero on all of `V`, so no
independent core minor can use them. The injection proving `(CLB1)` therefore
lands in the `(s-1)`-subsets of the smaller chart. Since every line has at
least `b_*` bases, `(CLB2)` gives exactly `(CLB4)`.

For `s=4`, if every witness line has at least `B` bases, `(CLB3)` pays the
whole high-core selector at the printed thresholds. Otherwise a line has
`b<B`, and `(CLB1b)` places the whole selector in excess at most
`b+2<=B+1`. Comparing this with the independently proved GRK depths gives the
rank-four row classifications in the statement. Applying the self-localized
bound `(CLB4)` removes three further endpoint basis values. No dichotomy
premise is introduced: the alternatives are exhaustive.
