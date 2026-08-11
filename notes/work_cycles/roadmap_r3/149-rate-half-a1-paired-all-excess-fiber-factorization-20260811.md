# Cycle 149: rate-half `A=1` paired all-excess fiber factorization (2026-08-11)

## Residual minimum-word polynomial

For an arbitrary off-line slope, the center difference is a nonzero RS
codeword supported inside a set of size `d_min+a_delta`. Factoring its
forced `k-1-a_delta` zeros leaves a nonzero polynomial `H_delta` with
degree at most `a_delta`.

Keeping this polynomial in the source calculation extends the prior
zero-excess theorem to every off-line slope:

```text
Qbar(delta,X)=chi A_delta B_delta R_delta,
G(delta,X)=zeta A_delta H_delta R_delta.
```

Consequently

```text
n-deg_X G(delta,X)=a_delta-deg H_delta,
gcd_X(Qbar_delta,G_delta)=A_delta R_delta.
```

Every padded-heavy factor is therefore present even on positive-excess
fibers. The absence of an extra outside-support gcd is exact: at
`x in S_delta\U`, both endpoint codewords and their line equal `f(x)`, so
`g_delta(x)=-e_delta(x)!=0`, forcing `H_delta(x)!=0`.

## Universal first jet

At an actual-support root, the same retained actual-error term gives

```text
G_t/Q_t-G_X/Q_X
 =(x-s_0)v_x L_U0'(x)e_delta(x)/Lambda(delta) !=0.
```

Thus all actual-support intersections are transverse, with no zero-excess
restriction.

## Burn-down

```text
result:                  PROVED all-excess residual-fiber factorization
DAG delta:               +1 PROVED leaf
critical status delta:   none
compute:                 integer degree/tamper checks only
new assumptions:         none
```

The immediate consequence for the extremal resultant is that `r_bad` is no
longer residual: all of it is a mandatory common-fiber factor. The next
node should sharpen the Cycle-148 bound from `4+r_bad` to exactly four.
