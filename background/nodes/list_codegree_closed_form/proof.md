# Proof

The proved codegree Theorem C, applied at agreement `a_j`, gives after taking
the supremum over received rows

```text
L_m(j) <= L_(m-1)(j) + B_j L_(m-1)(j+1).       (1)
```

The base case is `L_1(j)=B_j`. If `j>d`, then `a_j>n`, so both quantities are
zero.

We prove the shifted form

```text
L_m(j) <= sum_(r=0)^min(m-1,d-j)
             binom(m-1,r) product_(ell=0)^r B_(j+ell).   (2)
```

For `m=1`, the sum has only `r=0` and equals `B_j`. Assume (2) for `m-1`.
Substitute its instances at `j` and `j+1` into (1). The first summand gives
coefficient `binom(m-2,r)` on

```text
B_j B_(j+1) ... B_(j+r),
```

while the second gives coefficient `binom(m-2,r-1)` on the same product.
Pascal's identity makes their sum `binom(m-1,r)`. The upper limits truncate
correctly because the `j+1` branch is zero beyond `d`. This proves (2), and
`j=0` is (CF).

The formula is only an upper compiler. Closing the consumer still requires
proved numerical envelopes for every `B_j` that occurs and an adjacent unsafe
witness; neither is inferred here.
