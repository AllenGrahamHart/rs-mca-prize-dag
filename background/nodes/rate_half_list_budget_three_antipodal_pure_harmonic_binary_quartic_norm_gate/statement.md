# Budget-three antipodal pure harmonic binary-quartic norm gate

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:**
  `rate_half_list_budget_three_antipodal_pure_harmonic_fermat_router`

Let `K` have characteristic different from `2,3`, and let

```text
D(Y)=product_(i=0)^3 (Y-b_i)
```

be split and squarefree, with every `b_i` a nonzero square. Choose
`a_i^2=b_i`. For a monic quartic

```text
F(X)=X^4-s_1X^3+s_2X^2-s_3X+s_4
```

define its cubic binary-quartic invariant

```text
J(F)=72s_2s_4+9s_1s_2s_3-27s_3^2-27s_1^2s_4-2s_2^3.       (BQN1)
```

For the eight sign classes `epsilon in {+1,-1}^4/{+1,-1}`, put

```text
F_epsilon(X)=product_i(X-epsilon_i a_i),
R_H(D)=product_epsilon J(F_epsilon).                         (BQN2)
```

Then `R_H(D)` is independent of the ordering of the `b_i` and of every
choice of square root. It belongs to `K`, is a symmetric homogeneous
polynomial of degree `24` in the `b_i`, and therefore is a polynomial in the
four coefficients of `D`.

Moreover,

```text
R_H(D)=0
```

if and only if some choice of the four lifts has harmonic cross-ratio, that
is, cross-ratio in `{-1,2,1/2}`. Thus `(BQN2)` is an exact, relabel-free
support gate for the harmonic side of the pure harmonic-Fermat router.

The gate has a compact certificate. In

```text
A=K[a_0,a_1,a_2,a_3]/(a_i^2-b_i),
```

let `sigma_i` negate `a_i` and set `N_i(P)=P sigma_i(P)`. Reducing after each
step gives

```text
R_H(D)=N_3(N_2(N_1(J(F_+)))).                              (BQN3)
```

The right side is fixed by all four sign involutions. Formula `(BQN3)`, not
an expanded degree-24 polynomial, is the canonical evaluation and
certificate interface.

There is also a radical-free base-field formula. For a partition
`{x,y}|{z,t}` of the four roots `b_i`, define

```text
q=xy,       B=x+y,       delta=z-t,
C_0=4q+B delta-4zt,
D_0=B(t^2+q)-4tq,
D_1=2(t^2+q-Bt),
K_0=C_0^2+4delta^2q-16zD_0,
K_1=4C_0delta-16zD_1,
P_(xy|zt)=K_0^2-qK_1^2.                                (BQN4)
```

Although the display chooses orders within the two pairs, its value does
not. For the three pair partitions of `{b_0,b_1,b_2,b_3}` one has

```text
R_H(D)=P_(b_0b_1|b_2b_3)
       P_(b_0b_2|b_1b_3)
       P_(b_0b_3|b_1b_2).                              (BQN5)
```

Thus the exact gate can be evaluated using only base-field arithmetic on the
four deleted roots; no square-root extraction or symbolic expansion is
needed.
