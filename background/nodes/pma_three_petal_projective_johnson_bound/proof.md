# Proof - PMA three-petal projective Johnson bound

## 1. Pairwise root intersections

The mu-basis determinant identity gives

```text
F_pW_q-F_qW_p=kappa L_1L_2L_3,       kappa!=0.
```

The core is disjoint from the petals. Hence `F_p(x),F_q(x)` are not both zero
at any `x in C`.

Let two primitive pairs have a common core root `x`. Both nonzero vectors

```text
(u_i(x),v_i(x)),       i=1,2,
```

lie in the one-dimensional kernel of `(F_p(x),F_q(x))`. They are nonzero
because a simultaneous zero would make `X-x` divide both coefficient
polynomials. Therefore

```text
H_12(x)=u_1(x)v_2(x)-u_2(x)v_1(x)=0.
```

The polynomial `H_12` has degree at most

```text
r_u+r_v=e-1.
```

It is nonzero. If it vanished identically, the two rational pairs would be
proportional over `K(X)`. Primitivity over the PID `K[X]` then makes the
proportionality factor a unit, contrary to their being distinct projective
pairs. Thus `H_12` has at most `e-1` distinct roots, proving (PJ2).

## 2. The packing calculation

Let the root sets be `D_1,...,D_L`, each of size `d`, in an `N`-point core.
For `x in C`, let `m_x` be the number of sets containing `x`. Then

```text
sum_x m_x=Ld.
```

Cauchy-Schwarz and (PJ2) give

```text
sum_x binom(m_x,2)
 >= (L^2d^2/N-Ld)/2,

sum_x binom(m_x,2)
 = sum_(i<j)|D_i intersect D_j|
 <= binom(L,2)(e-1).
```

After multiplying by two and dividing by `L>0`,

```text
L(d^2/N-(e-1))<=d-(e-1).
```

If `J=d^2-N(e-1)>0`, multiplication by `N/J` proves (PJ4). The case `L=0`
is immediate.

## 3. Rate one quarter

In the upper branch `e-1=2d-3ell`. Hence

```text
J=d^2-N(2d-3ell)
 =(N-d)^2+N(3ell-N).                              (1)
```

At rate `1/4`, `M=4`,

```text
3k+1=4ell+b,       0<=b<ell,
N=k-1=(4ell+b-4)/3<3ell.
```

Both terms on the right of (1) are nonnegative and the second is positive,
so every upper cell satisfies the Johnson condition.

For one defect and touched triple, (PJ4) has numerator

```text
N(d-e+1)=N(3ell-d)<=3n^2
```

and positive integer denominator. There are four triples and at most `n`
defect degrees, giving at most `12n^3` upper contributors. The lower branch
has at most four projective candidates per defect and therefore at most `4n`.
For `n>=1`, their sum is at most `16n^3`, proving (PJ6).

## 4. Rate one half

At rate `1/2`, equation (SRC) with `M=4` gives

```text
N=k-1=4ell+b-2.
```

Substitute `d=2ell-a` and `e-1=2d-3ell=ell-2a` into `J`:

```text
J=(2ell-a)^2-(4ell+b-2)(ell-2a)
 =ell(4a-b+2)+a^2+2ab-4a.
```

Throughout the strict strip, `d<N`, so `J(d)` decreases as `d` increases.
Its smallest value is therefore at `d=2ell-1`, or `a=1`:

```text
J_min=(6-b)ell+2b-3.
```

This is positive for every `0<=b<=6`, proving the first rate-half claim.
If `J<=0`, necessarily `b>=7`. In that range the remainder

```text
a^2+2ab-4a=a(a+2b-4)
```

is positive. Therefore the coefficient `4a-b+2` must be negative, giving
`4a<=b-3`. This proves (PJ8).
