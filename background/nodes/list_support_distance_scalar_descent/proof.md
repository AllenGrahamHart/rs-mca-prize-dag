# Proof

Suppose an `E`-valued center `y` has distinct degree-`<k` polynomials
`f_1,...,f_L` agreeing with it on at least `a` coordinates. Put

```text
T_i={x in D:f_i(x)!=y(x)}.
```

Then `|T_i|<=t`. For `i!=j`, the agreement sets of `f_i` and `f_j` intersect
in at most `k-1` positions, because their difference is a nonzero polynomial
of degree below `k`. Taking complements gives

```text
|T_i triangle T_j|>=2a-2(k-1)=2g.                    (1)
```

There are `N_r` nonzero `F`-linear functionals `lambda:E->F` up to
multiplication by `F^*`. Exactly `H_r` projective functional classes kill any
fixed nonzero element of `E`.

Fix one such `lambda`, and partition `{1,...,L}` according to equality of
the projected polynomials `lambda(f_i)`. Let `M_lambda` be the number of
parts, and define

```text
Z_(i,lambda)={x in T_i:lambda(f_i(x)-y(x))=0}.
```

If `i,j` lie in one part, their projected error sets are equal. Thus every
point of `T_i triangle T_j` lies in `Z_(i,lambda) union Z_(j,lambda)`, and
`(1)` gives

```text
|Z_(i,lambda)|+|Z_(j,lambda)|>=2g.                   (2)
```

For a collision part of size `s>=2`, sum `(2)` over its unordered pairs.
Each killed-error count appears `s-1` times, so the part contributes at
least `gs`, and in particular at least `g(s-1)`. Summing the parts yields

```text
L-M_lambda <= (1/g) sum_i |Z_(i,lambda)|.            (3)
```

Every nonzero error incidence is killed by exactly `H_r` projective
functionals, and there are at most `Lt` error incidences. Summing `(3)` over
all projective functionals gives

```text
sum_lambda (L-M_lambda)<=LtH_r/g.                    (4)
```

Under `(SD1)`, the right side of `(4)` is strictly smaller than `N_r`.
Therefore some `lambda` has `M_lambda=L`; all projected polynomials are
distinct. Since `D subset F` and `lambda` is `F`-linear,

```text
lambda(f_i(x))=sum_j lambda(f_(i,j))x^j,
```

so every projection is a degree-`<k` polynomial over `F`. Projection also
preserves each agreement coordinate. The projected center consequently has
`L` distinct base-field codewords at agreement at least `a`. This proves the
forward implication in `(SD2)`. Scalar inclusion `F subset E` proves the
reverse implication.

Finally,

```text
qH_r=(q^r-q)/(q-1)<(q^r-1)/(q-1)=N_r,
```

so `(SD3)` implies `(SD1)`. Direct substitution gives `(SD4)` and the stated
floor identity. QED.
