# L1 polynomial-led interior cells are deeper-Q curves

- **status:** PROVED
- **role:** reduce every below-cap polynomial-led exact interior cell to a
  curve of deeper locator-prefix fibers
- **consumer:** `l1_mixed_petal_amplification`

## Setup

Let `H subset B` have size `n`, let `Omega` be its locator, and fix
`m>k`, `w=m-k`, and

```text
1<=e<=k,       d=w+e.                                (DQ1)
```

Let `U in B[X]` be monic of degree `m+e`, with top nonleading coefficients
`z_1,...,z_d`.  If `(1,U)` is the minimal shifted-lattice vector, its profile
is the strict interior value `d_1=d+1=w+e+1`.

For an `m`-subset `T`, write

```text
L_T=X^m+a_1X^(m-1)+...+a_m.
```

Given `s=(a_1,...,a_e) in B^e`, define recursively the monic degree-`e`
polynomial

```text
R_s=X^e+r_1X^(e-1)+...+r_e
```

and the remaining locator prefix `a_(e+1),...,a_(e+w)` by

```text
r_j=z_j-sum_(l=0)^(j-1) r_l a_(j-l),       1<=j<=e,
a_j=z_j-sum_(l=1)^e r_l a_(j-l),           e<j<=e+w, (DQ2)
```

where `a_0=r_0=1`.  Let `theta_z(s)=(a_1,...,a_(e+w))`.

## Exact decomposition

The complete level-`m` shell has the disjoint decomposition

```text
Z_m(U)=sum_(s in B^e)
  #{T in Fib_(m,w+e)(theta_z(s)):
    gcd(R_s,Omega/L_T)=1}.                            (DQ3)
```

For every retained support, the codeword is uniquely

```text
P=U-L_T R_s,       deg P<k.                          (DQ4)
```

The curve `theta_z` is injective because its first `e` coordinates are `s`.
Thus the polynomial-led strict-interior exact cell is exactly a guarded
`|B|^e`-slice curve through distinct depth-`w+e` locator-Q fibers.  In
particular,

```text
Z_m(U)<=sum_s |Fib_(m,w+e)(theta_z(s))|
       <=|B|^e max_y |Fib_(m,w+e)(y)|.                (DQ5)
```

If a discrete deeper-Q theorem gives

```text
max_y |Fib(y)|<=kappa(1+binom(n,m)|B|^(-(w+e)))+E,
```

then this cell costs at most

```text
kappa(|B|^e+binom(n,m)|B|^(-w))+|B|^e E.             (DQ6)
```

## Scope

No deeper-Q max-fiber theorem or curve-occupancy improvement is proved.
The additive `|B|^e` term in `(DQ6)` is real under a max-times-number-of-
slices argument and may exceed a finite row budget.  Nonconstant minimal
vectors, `e>k`, quotient coalescing, and cross-level finite summation remain
open.
