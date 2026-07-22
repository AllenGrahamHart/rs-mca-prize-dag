# Proof

The circuit matrix in the dependency has rows

```text
[1,gamma,...,gamma^t,
 q_gamma(U),gamma q_gamma(U),...,gamma^tq_gamma(U)]. (1)
```

Its determinant is identically zero exactly when there is a nonzero kernel
pair `(A,B)` of degree at most `t` satisfying `(QPRC1)` on the circuit.
Since the circuit has more than `t` points, `B` cannot be zero. Divide out
`gcd(A,B)` to obtain a primitive relation. This proves existence; the same
kernel implication proves the converse.

Suppose primitive relations `[A:B]` and `[A':B']` agree on a common set.
Eliminating `q_gamma(U)` shows that every common point is a root of

```text
AB'-A'B.                                            (2)
```

This polynomial has degree at most `2t`. If it is zero, the two primitive
pairs represent the same element of `P^1(K(Z))`; otherwise it has at most
`2t` roots. This proves `(QPRC2)` and uniqueness for a circuit of size
`2t+2`.

For one relation class, multiply `(QPRC1)` by `I(gamma)` and put

```text
Q_U=U^2M_0-2UM_1+M_2,
F_R=IA+Q_UB.                                        (3)
```

The polynomial `F_R in K[Z]` has degree at most `e+t`. It is nonzero:
`gcd(I,Q_U)=1` because `Q_U(xi_i)=mu_iN_i(U)` is a nonzero quadratic in
`K`; an
identity `IA=-Q_UB` would force `I|B`, impossible for `deg B<=t<e`, and
then force `A=0`. Every class point is a root of `F_R`, proving `(QPRC3)`
and the fixed-factor formulation `(QPRC6)`.

Every zero circuit belongs to exactly one class, so summing its `s`-subsets
gives the first identity in `(QPRC4)`. Distinct classes intersect in at most
`2t=s-2`; hence an `(s-1)`-subset belongs to at most one class. This gives
the shadow inequality.

Let `h_max=max_R h_R`. Then

```text
D_t
 =sum_R binom(h_R,s-1)(h_R-s+1)/s
 <=[(h_max-s+1)/s]binom(3e,s-1).                    (4)
```

Therefore

```text
h_max>=s-1+ceil[sD_t/binom(3e,s-1)].                (5)
```

Use the exact integer lower bound for `D_t` from `(QPCIR5)`, with
`e=2^38-1`, `(t,N)=(6,3e-8)` and `(8,3e-11)`. Equation `(5)` gives `172410`
and `2128`, respectively. QED.
