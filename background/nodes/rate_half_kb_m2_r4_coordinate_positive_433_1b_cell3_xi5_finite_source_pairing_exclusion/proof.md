# Proof

The source endpoint theorem proves that every `xi=5` target must lie over one
of six compatible source points for its source sign. There are 24 such points
in total. At each point the missing product and squared sum satisfy

```text
m=bf,       s=(b+f)^2,
```

and guarded `b!=0` fixes `f=m/b` uniquely.

Put `u=df` and `v=ef`. Since `f!=0`, the six residual records after deleting
`bf` are

```text
q, q, -q, u, sigma_o v, sigma_c cf,      q=uv/f^2.
```

For each of the 15 canonical perfect matchings, substitute these records into
the three equations `F(x,y)=paired(x,y)=0`. The compact-kernel formula makes
each equation an explicit polynomial in `u,v` over the deployed field.

The primary census computes all three pairwise resultants in `v`. Every
resultant is nonzero. It selects the smallest degree/term profile; in all 1440
source/matching/lane subcases the selected resultant has degree eight in `u`.
Every deployed-field `u` root is enumerated exactly as a root of

```text
gcd(R(u),u^p-u).
```

At each root, all three original equations are specialized to univariate
polynomials in `v` and their nonzero gcd is computed. An all-zero
specialization is recorded unresolved, never discarded. Across the census
there are 2208 outer `u` roots. Every three-equation gcd is the constant one,
so there is no `v` root, target boundary, witness, or unresolved branch.

An independent compiler repeats the construction with the variables
reversed: all three pairwise resultants are taken in `u`, every deployed-field
`v` root is enumerated, and the original equations are specialized in `u`.
It again finds 2208 outer roots and zero inner roots, solutions, or unresolved
branches, with the same per-source root-count profile.

The 1440 checked subcases exhaust the six compatible source points in each of
the 240 raw source-sign/matching/lane cases. Therefore every raw `xi=5` case
is empty. QED.
