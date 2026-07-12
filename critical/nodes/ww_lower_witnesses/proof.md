# Proof

Fix a clean rate `rho in {1/4,1/8,1/16}` and an official row. Write

```text
T=floor(|F|/2^128).
```

When the challenger column is spent, let `N` be the least admissible dyadic
quotient order for which

```text
C(N-1,rho*N)>T.
```

The spend-map audit proves that this `N` exists and that its maximum over the
official field range is respectively `256,256,512`. Put `M=n/N` and
`sigma=M-1`. Then `M|k`, `k/M=rho*N<=N-1`, and `1<=sigma<M`.

Choose one order-`M` coset `C0` and a `sigma`-subset `T0` of it. Let

```text
L_T0(X)=product_(t in T0)(X-t),
Y(X)=X^k L_T0(X).
```

For each union `U_A` of `k/M` other order-`M` cosets, its locator has the
form

```text
L_A(X)=X^k+c1 X^(k-M)+c2 X^(k-2M)+... .
```

Hence

```text
P_A(X)=L_T0(X)(X^k-L_A(X))
```

has degree at most `sigma+k-M=k-1`, so it is a codeword. It agrees with `Y`
on the disjoint set `T0 union U_A`, of size `sigma+k`. Distinct choices of
`A` give distinct codewords, producing exactly the required lower count
`C(N-1,k/M)>T`.

Since this count is an integer,

```text
count>T=floor(|F|/2^128)  iff  count>|F|/2^128.
```

Agreement `a=k+sigma` means Hamming distance at most `n-a`, so these words
belong to the closed ball at radius `1-a/n` exactly. There is no endpoint
shift. The lower-bound quantifier is `sup_U`, so using the construction's own
received word is sufficient; identifying it with the historical E15 family
is not a mathematical requirement.

At the largest field edge the three counts are already above `2^128`, with
the smallest margin at rate `1/8`. For smaller fields, the least admissible
`N` can only decrease. The rate-`1/2` maximum count is below `2^128` and is
correctly excluded from W2.

---

## IMPORT REPAIRS (2026-07-12 master banking; cluster audit)

R6 (domain hypothesis, stated): the construction lives on a 2-POWER
MULTIPLICATIVE evaluation domain D (order-n subgroup/coset of F^*) with T0
a coset of the order-M subgroup, M = N*-scale; the coset structure is
load-bearing (mutation control: a generic non-coset locator fails —
verify_construction.py). R5: verify.py's algebraic checks are augmented by
verify_construction.py (independent brute polynomial arithmetic, 5 cells
incl. sigma=3, 2 genuine mutation controls; catch #77 — three of
verify.py's advertised checks are tautologies and its real content is the
binomial/floor arithmetic).
