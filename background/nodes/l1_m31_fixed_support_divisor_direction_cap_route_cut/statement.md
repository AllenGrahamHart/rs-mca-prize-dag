# M31 fixed-support divisor-direction cap route cut

- **status:** PROVED
- **closure:** explicit algebraic construction
- **requires:** `l1_m31_rank7_dense_top_decorated_shift_pair_router`
- **consumer:** the proposed `15413` successor to the dense top stratum

Let `F` contain at least `72428` distinct elements, let `S subset F` have
size

```text
m=72428,
```

and let `L_S` be its monic locator. Choose a `(t-1)`-subset `R0 subset S`
with `t=4980`, and write `R` for its monic locator. Then the six-dimensional
space

```text
V=span_F {R X, R, 1, X, X^2, X^3}                         (RC1)
```

has no common zero, but contains

```text
m-t+1=67449                                               (RC2)
```

distinct projective classes represented by monic degree-`t` divisors of
`L_S`, namely

```text
J_a=R(X-a),       a in S minus R0.                        (RC3)
```

Therefore a universal cap `15413` based only on a fixed support locator, a
six-dimensional direction space, no common zero, and maximum root count is
false by a factor greater than four.

## Scope

The construction does not supply a received table, exact-weight list class,
source normalization, or decorated cofactor identities. It does not refute a
source-bound `15413` cap that retains `A C_i-B C_j=c`, nor the neighbor cap
`215792`. It proves that those target/Pade constraints are load-bearing.
