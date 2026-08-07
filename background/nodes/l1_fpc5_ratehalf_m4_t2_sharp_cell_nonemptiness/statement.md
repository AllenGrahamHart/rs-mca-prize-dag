# Sharp rate-half `M=4,t=2` cell nonemptiness

- **status:** PROVED
- **consumer:** `l1_fpc5_ratehalf_m4_t2_payment`

Let `H_32` be the order-32 subgroup of `F_97^*`. At the exact sharp
rate-half analogue

```text
(n,k,ell,M,b,s,d)=(32,16,4,4,1,1,5),
5ell=k+4,
```

the background-guarded `M=4,t=2` cell is nonempty. More strongly, on the 50
deterministic maximal layouts printed by the certificate, solving the touched
label ratio exactly gives

```text
41 nonempty layouts,
71 primitive exact contributors,
maximum 5 contributors in one layout.                    (NE1)
```

For seed `3`, one explicit witness has touched pair `(1,3)`, labels

```text
(2,1,3,72),
```

missed core

```text
(75,28,30,50,19),
```

and coefficient vectors in increasing degree order

```text
F=(67,32,8,88,89,1),
W=(40,90,43,55,78,76).                                (NE2)
```

It has exactly `k+ell-1=19` agreements: ten retained core points, the one
background point, and the two full touched petals.

## Consequence

The sharp guarded equations cannot be closed by a universal algebraic
emptiness identity. A successful proof must count these split locators or
assign them to legitimate tangent/quotient/profile owners.

## Scope

Here the root excess is `2s+1=3`. The certificate does not construct an
unbounded-excess family, disprove polynomial image-fiber growth, or settle an
official row.
