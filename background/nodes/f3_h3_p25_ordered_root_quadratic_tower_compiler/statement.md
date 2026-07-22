# H3 P25 ordered-root quadratic tower compiler

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_dsp8_correlation_bound` (evidence/router)
- **dependency:** `f3_h3_p25_quadratic_divisor_tower_compiler`

Let `n=2^s`, `p=1 mod n`, and `q=25`. A nonidentity product fiber with
`P(t)>=q` exists if and only if the following ordered-root quadratic system
has a geometric solution in characteristic `p`.

Choose `T`, inverses `tau,eta`, and for `1<=i<=q` choose `x_i,z_i,B_(i,0)`.
Impose

```text
T tau=1,       (T-1)eta=1,       x_i z_i=1,
B_(i,0)=(x_i-T)z_i.                                (ORT1)
```

Starting with `A_(i,0)=1-x_i`, introduce scalar towers

```text
A_(i,j+1)=A_(i,j)^2,
B_(i,j+1)=B_(i,j)^2,       0<=j<s,
A_(i,s)=B_(i,s)=1.                                 (ORT2)
```

Finally list the `M=binom(q,2)=300` differences `x_i-x_j`, multiply them by
a quadratic prefix product, and invert the final product. This enforces that
all `x_i` are distinct.

The complete system has

```text
2qs+q+M+3 =50s+328 variables,
2qs+2q+M+2=50s+352 equations,                      (ORT3)
```

all of total degree at most two. Across `13<=s<=41`, this is at most `2,378`
variables and `2,402` equations.

The presentation is smaller than the symmetric degree-25 divisor tower but
has `q!` ordered presentations of a generic fiber. That symmetry can dominate
a solver. This theorem is an exact alternative compiler, not a performance
claim, a completed Nullstellensatz certificate, or a DSP8 close.
