# Proof - L1 affine split-pencil cross-determinant uniqueness

Because the two points have the same partial support pattern, on every
`x in S_i` one has

```text
W_0(x)=c_iF_0(x),       W_1(x)=c_iF_1(x).
```

Therefore `Delta(x)=0` on `S_i`.

Now take `x in V_i`. Equality of the missing-equation syndromes says

```text
W_0(x)-c_iF_0(x)=W_1(x)-c_iF_1(x).                    (1)
```

The cross determinant need not vanish there, but `L_(V_i)` divides `J`, so
`J Delta` does. Thus `J Delta` vanishes at every point of

```text
T_i=S_i disjoint_union V_i
```

for every `i`. The petals are pairwise disjoint, so their monic locators are
pairwise coprime. This proves the divisibility in `(CD4)`. The degree bound is
immediate from

```text
deg Delta<=deg W_0+deg F_1<=2d,       deg J=v.         (2)
```

Under `(CD5)`, the divisor in `(CD4)` has degree `t ell` strictly greater
than the degree of `J Delta`. Hence `J Delta=0`, and the polynomial ring is a
domain, so `Delta=0`.

The identity `W_0F_1=W_1F_0` and `gcd(F_0,W_0)=1` imply `F_0|F_1`. Both are
monic of degree `d`, so `F_0=F_1`; the cross identity then gives `W_0=W_1`.
This proves singleton uniqueness.

On the L1 branch, dense holes are terms in the polarized entropy, so
`v<=p`. Condition `(CD6)` implies `(CD5)`. A nonsingleton cell must therefore
satisfy `t ell<=2d+v<=2d+p`, giving the upper bound in `(CD7)`. The lower
bound is the already-proved threshold inequality

```text
d<=t ell+p-1.                                           (3)
```

Finally, if `d=m ell+eta`, then `(CD8)` gives

```text
t ell>=(2m+1)ell
       >2m ell+2eta+p
       =2d+p,
```

so `(CD6)` applies. The polynomial per-chart count follows by multiplying
the singleton cell bound by the compiler's polynomial number of exact support
patterns, syndromes, and defect degrees.
