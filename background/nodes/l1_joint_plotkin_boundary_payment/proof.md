# Proof - L1 joint Plotkin-boundary payment

For two distinct contributors, the joint cross-determinant theorem gives

```text
|D_P intersect D_Q|+|R_P intersect R_Q|<=r.             (1)
```

Every set in `(PK2)` has the same size

```text
|A_P|=d+u=r+ell.                                        (2)
```

Because the core and background are disjoint, `(1)--(2)` imply

```text
|A_P triangle A_Q|
 =2(|A_P|-|A_P intersect A_Q|)
 >=2(r+ell-r)=2ell,                                     (3)
```

which proves `(PK3)`.

Embed every subset `A` of the `V`-point universe as its sign vector
`z_A in {+1,-1}^V`. Equation `(3)` gives

```text
<z_A,z_A'>=V-2|A triangle A'|<=V-4ell<=0               (4)
```

under `(PK4)`.

We use the following elementary Rankin lemma: at most `2V` nonzero vectors in
`R^V` can have pairwise nonpositive inner products. To prove it, repeatedly
remove an inclusion-minimal positive dependence

```text
sum_(i in I) lambda_i z_i=0,       lambda_i>0.
```

Every vector outside `I` is orthogonal to every vector in `I`, because the
inner product with the displayed sum is zero while all its summands are
nonpositive. Minimality makes the block span have dimension `|I|-1`.
After all such blocks are removed, the residual vectors are independent: a
mixed-sign dependence would split into two positive dependences, since the
inner product of its positive and negative sides is both a squared norm and
nonpositive. If there are `t` removed blocks, their spans and the residual
span are mutually orthogonal, so

```text
m<=V+t<=2V,                                             (5)
```

because each block consumes at least one dimension. Equations `(4)--(5)`
prove `(PK5)`.

At fixed `p<=P`, there are at most `2^M(P+1)n^P` exact petal-support patterns
and at most `n` defect degrees. Multiplying by `(PK5)` and using
`2^M<=n^(1/c_0)` proves `(PK6)`.

For an official source,

```text
(r-1)N+r=Mell+b.                                       (6)
```

Substituting `N=((Mell+b-r)/(r-1))` into `(PK7)` and multiplying by `r-1`
gives `(PK8)`. Replacing `b` by `ell-g` gives `(PK9)`. Since `g>=1`, the
left side of `(PK9)` must be positive, yielding `M>=3(r-1)`. The final
first-scale statement is direct substitution.
