# Proof

Put `d=9` and `L=12`. Choose twelve distinct polynomials
`q_0,...,q_11` of degree below `d` whose affine span is the full
`d`-dimensional polynomial space. For example, take

```text
q_0=0,
q_i=X^(i-1)                         (1<=i<=9),
q_10=sum_(j=0)^8 X^j,
q_11=sum_(j=0)^8 (j+2)X^j.
```

Every difference `q_e-q_f` is a nonzero polynomial of degree at most `8`.
Consequently at most

```text
8*C(12,2)=528
```

carrier points make two of their values equal.

## Shared core and petals

Choose `J subset D` of size `K-9` containing all those bad carrier points,
and put

```text
L_J(X)=product_(x in J)(X-x),
a_e=L_J q_e,
b_e=1.
```

The `a_e` have degree below `K`; they span a `9`-dimensional code subspace,
and `1` is independent of that subspace because every `a_e` vanishes on
`J`.

Every point of `D\J` now has the twelve values `a_e(x)` pairwise distinct.
Partition part of `D\J` into twelve disjoint petals `P_e`, each of size

```text
m-1-(K-9)=w+8=67480.
```

The remaining set `R` has size

```text
n-(K-9)-12(w+8)=238825.
```

Define the received pair on `J union P_0 union ... union P_11` by

```text
r_1=1,
r_0=0 on J,
r_0=a_e on P_e.
```

Thus `H_e=J union P_e` is a componentwise agreement core for `(a_e,1)` and
has exact size `m-1`. Pairwise distinctness of the `a_e(x)` off `J` shows
that no other petal belongs to `H_e`.

## The extension-field avoidance ledger

On `R` put `r_1=0`. We choose values `t_x=r_0(x) in F` so that all

```text
gamma_(e,x)=t_x-a_e(x),    e in {0,...,11}, x in R,
```

are globally distinct. This can be done greedily. Within one coordinate the
twelve values are already distinct. After `j` coordinates have been chosen,
at most `12^2 j` values of `t_x` are forbidden by collisions with an old
slope. Even at the final step this is at most

```text
12^2(238825-1)=34390656 < p^6=|F|.
```

Hence the greedy choice exists.

For each `(e,x)` use slope `gamma_(e,x)`, explanation

```text
h_(e,x)=a_e+gamma_(e,x),
```

and support `S_(e,x)=H_e union {x}`. On `H_e`, the received pair equals
`(a_e,1)` coefficientwise. At `x`,

```text
r_0(x)+gamma r_1(x)=t_x=a_e(x)+gamma.
```

On a different remainder coordinate equality would repeat one of the
globally distinct slopes. On another petal it would require
`a_f(x)=a_e(x)`, which is excluded. Thus the complete agreement set is
exactly `S_(e,x)` and has size `m`.

## Actual badness, post-near status, and margin

If two degree-below-`K` codewords simultaneously explained `(r_0,r_1)` on
`S_(e,x)`, their restrictions to the `m-1>K` point core would force them to
be exactly `(a_e,1)`. At `x`, the second component is `0`, not `1`, so this
is impossible. Every record is therefore support-wise MCA-bad.

The selected direction minimizer is `b_e=1`. It agrees with `r_1` on all of
`H_e` and fails only at `x`; the same uniqueness argument excludes a
zero-mismatch direction codeword. Hence `theta=1` and the selected pair is
exactly `(a_e,1)`.

Suppose the slope word were within `w` of some codeword `c`. Then `c` would
agree with it on at least `n-w` coordinates. Its intersection with the exact
`m`-point agreement set of `h_(e,x)` has size at least

```text
(n-w)+m-n=m-w=K.
```

Two degree-below-`K` codewords agreeing on `K` points are equal. This would
give `c=h_(e,x)`, but that codeword agrees on exactly `m<n-w` points, a
contradiction. Thus every record is post-near.

## Exact ranks

Let `A=span{a_e-a_0}`. It has dimension `9`. Put

```text
c_0=r_0-a_0=r_0,
d_0=r_1-1.
```

The vector `c_0` is not in `A`: it vanishes on `H_0`, which has more than
`K-1` points, while it is nonzero on `P_1`. If
`d_0=a+lambda c_0` with `a in A`, restriction to `H_0` forces `a=0`, and
restriction to `P_1` forces `lambda=0`; this contradicts `d_0=-1` on `R`.
Therefore

```text
dim span(A,c_0,d_0)=9+2=11.
```

Every selected error is

```text
c_0-a_e+gamma_(e,x)d_0.
```

Two slopes for the same `e` recover `d_0`; subtracting its multiple then
recovers `c_0-a_e`. Hence the selected errors span the full displayed
`11`-space. Similarly, differences of explanations recover `1` and all
`a_e-a_0`, so their affine span has dimension `9+1=10`.

The twelve `a_e` are distinct, so the twelve pair lines are distinct. This
completes the construction.
