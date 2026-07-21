# Proof

Choose a basis `f_1,...,f_r` of the row space and write

```text
lambda_i=sum_(j=1)^r c_(ij)f_j.
```

For `alpha=(alpha_i)`, the scaled rows form a trade exactly when

```text
sum_i alpha_i c_(ij)=0,
sum_i gamma_i alpha_i c_(ij)=0       for every j.   (1)
```

Let `M` be the `2r` by `t` matrix of `(1)`, and put `K=ker M`. The original
trade says that the all-one vector lies in `K`.

The `r` coefficient columns `(c_(ij))_i` are linearly independent and each
lies in

```text
ker (1;gamma_i)_(i=1,...,t),
```

a space of dimension `t-2`. Hence

```text
r<=t-2,                                             (2)
```

which is the lower bound in `(CA1)`.

On the other hand, `rank M<=2r`, so

```text
dim K>=t-2r.                                        (3)
```

If `t>=2r+2`, then `dim K>=2`. Intersect `K` with any coordinate hyperplane
`alpha_i=0`. The intersection has positive dimension, and therefore contains
a nonzero scaled subtrade omitting row `i`. A row-scaling circuit cannot have
such a subtrade. Thus `t<=2r+1`, proving `(CA1)`.

For the decomposition claim, take any nonzero scaling vector in `K`. If its
support is not minimal among nonzero vectors of `K`, choose a nonzero vector
on a strict sub-support and scale it to cancel one coordinate of the first
vector. This writes the first vector as a sum of two nonzero vectors in `K`,
both on smaller supports. Induction on support size decomposes it into
support-minimal vectors. Each resulting trade has row-space rank at most
`r`, so `(CA1)` applies with its actual rank. The uniform split-pencil
dependency excludes rank one. Hence a rank-two trade decomposes into
rank-two circuits, and `(CA1)` restricts their arities to four and five.

Now take rank two and a basis `F,G`. Equations `(1)` become

```text
sum_i alpha_i(c_i,d_i,gamma_i c_i,gamma_i d_i)=0.   (4)
```

This proves `(CA2)`, while `(CA3)` follows directly from

```text
c_i(gamma_i d_i)-d_i(gamma_i c_i)=0.
```

Circuit minimality says the column kernel in `(4)` is one-dimensional and
its generator has no zero coordinate. Since the all-one vector is already
in that kernel, the column rank is `t-1`. This is exactly `(CA4)`.

For `t=4`, the four Segre columns span one projective hyperplane. Its
equation has the form

```text
A c+B d+C gamma c+D gamma d=0.                      (5)
```

On writing the row parameter as `[c:d]`, `(5)` says

```text
[c:d]=[B+D gamma:-(A+C gamma)]
```

projectively, including the values at poles. Distinct row classes and
distinct slopes, supplied by the split-pencil dependency, rule out a common
zero of the two linear forms and make this fractional-linear map
nonconstant. Conversely,
the four columns on such a graph lie in `(5)`; rank three is precisely the
absence of a smaller scaling dependence.

For `t=5`, rank four means that the five points in projective three-space
have a unique dependence. Every four being independent makes every
coefficient in that dependence nonzero, and rescaling the five rows makes
the coefficients all one. This is the stated five-point Segre circuit.
These are coefficient-level equivalences for a fixed pair `F,G`; support
embedding and aggregate ownership have not been asserted. QED.
