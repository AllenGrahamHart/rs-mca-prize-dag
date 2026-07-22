# L1 raw support-ledger exponential route fence

- **status:** PROVED
- **role:** rule out raw summation of the two fixed-support ledgers
- **consumer:** `l1_mixed_petal_amplification`

## Formal profile

For `j=2^s` with `s>=4`, put

```text
n=2^j,       k=n/2,       N=k-1,
ell=n/j,     M=j/2,       b=1.                         (RF1)
```

Consider the balanced formal support profile

```text
t=M,       r=0,       a_i=ell/2 for every petal,
h=sum_i a_i=n/4,       d=h-ell=n/4-ell.                (RF2)
```

It satisfies every elementary source and list constraint used by the raw
fixed-support ledgers:

```text
N+b+Mell=n,       b<ell,       r+h=ell+d,
0<a_i<=d,         h>d.                                 (RF3)
```

This is only a formal profile; algebraic realizability is not asserted.

## Route fence

For the root-pinning ledger define

```text
u=tell-h=n/4,
e=max(0,2d+1-h)=n/4-2ell+1.                           (RF4)
```

Its raw right-hand side at `(d,t,h)` is

```text
R_PRP=binom(M,t) binom(tell,h) binom(N,e).             (RF5)
```

Already

```text
R_PRP>=binom(n/2,n/4)>=2^(n/4).                        (RF6)
```

For any one exact support pattern in the same profile, the maximal
background-anchor ledger assigns the local allowance

```text
q^gamma,
gamma=d-max(r,a_i)+1=n/4-3ell/2+1>=n/8.               (RF7)
```

Thus for every `q>=2` this allowance is at least `2^(n/8)`. Consequently,
neither of the following operations can prove a uniform polynomial L1 bound:

1. summing the root-pinning right-hand side over all formally admissible
   support profiles;
2. assigning the background-anchor allowance independently to every exact
   support pattern and then taking a raw union bound.

Any successful fixed-source proof must add an algebraic feasibility/sparsity
theorem, a collective injection across support patterns, or a globally paid
quotient/Forney owner classification.

## Scope

The theorem proves that two numerical upper-bound expressions are
exponentially loose on a legal parameter profile. It does not construct one
listed codeword in that profile, refute either local ledger, or refute L1.
