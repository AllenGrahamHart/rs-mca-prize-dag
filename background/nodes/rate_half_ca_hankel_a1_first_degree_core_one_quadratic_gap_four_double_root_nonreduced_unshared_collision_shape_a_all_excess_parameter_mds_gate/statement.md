# `A=1` shape-A all-excess parameter-MDS gate

- **status:** PROVED
- **closure:** exact `4e`-column global compatibility matrix for all
  off-line residual fibers
- **consumer:** `rate_half_band_crossing_location`

Retain shape A, with

```text
Gamma={3e off-line supported slopes},
(m,n)=((e-2),(3e-7)/2).                            (APG1)
```

For every `delta in Gamma`, retain the all-excess factorization and put

```text
D_delta(X)=A_delta(X)R_delta(X),
deg D_delta=n-a_delta,
C_delta(X)=zeta_delta H_delta(X)
              =sum_(h=0)^a_delta c_(delta,h)X^h.  (APG2)
```

Thus `C_delta` is nonzero, has degree `a_delta-q_delta`, and

```text
G(delta,X)=D_delta(X)C_delta(X).                   (APG3)
```

Write

```text
D_delta(X)=sum_j d_(delta,j)X^j,
L_Gamma(T)=product_(delta in Gamma)(T-delta).      (APG4)
```

Define a matrix `K_all` with columns `(delta,h)`,
`0<=h<=a_delta`, and rows `(i,l)`,

```text
0<=i<=n,       0<=l<=2e,

(K_all)_((i,l),(delta,h))
 =d_(delta,i-h) delta^l/L_Gamma'(delta),           (APG5)
```

where an out-of-range coefficient of `D_delta` is zero. Then the complete
off-line fibers come from one biform of bidegree at most `(m,n)` if and
only if

```text
K_all c=0.                                         (APG6)
```

For shape A the excess ledger gives

```text
sum_(delta in Gamma)a_delta=e,
# columns of K_all=sum_delta(a_delta+1)=4e.         (APG7)
```

On the official row this is exactly

```text
733007751852 columns,
100743818300944219985234 printed parity rows.      (APG8)
```

Shape A requires a kernel vector whose block `C_delta` is nonzero for every
`delta`; its block degree recovers

```text
q_delta=a_delta-deg C_delta.                       (APG9)
```

In the smallest `e=7` analogue, the cyclic degree table with fourteen
zero-excess and seven excess-one slopes gives a `120 x 28` matrix. It has
rank `28` over both `F_337` and `F_421`; fifty deterministic
degree-preserving switch trials in each field also have rank `28`.

## Scope

The finite probes are evidence only. The theorem does not prove `K_all`
has full column rank for every admissible incidence profile or on the
official row. It replaces all residual-polynomial choices by one exact
matrix and identifies block-nonvanishing as the realizability condition.
