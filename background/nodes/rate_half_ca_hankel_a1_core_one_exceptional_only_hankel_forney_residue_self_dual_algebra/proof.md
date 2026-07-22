# Proof

Kernel-plane transversality gives `q_1(a)!=0` at every exceptional root.
The support locator `B_T` is disjoint from those roots, and the Forney theorem
gives `gcd(Phi,A)=1`. Thus all three classes in `(HFR2)` are units.

The coefficient column of `g_a(z)=Q(z;a)/z` is

```text
(q_1(a),...,q_e(a))^T
 =q_1(a)(p_0(a),...,p_(e-1)(a))^T.                  (1)
```

The split-frame theorem says the unnormalized columns have weighted Gram
zero with weights `beta_a`. The Forney interpolation identity is

```text
Phi(a)=beta_a q_1(a)A'(a)B_T(a).                    (2)
```

After the normalization `(1)`, equations `(1)--(2)` change the diagonal
weight to

```text
beta_a q_1(a)^2=C(a)/A'(a),                         (3)
```

which is `(HFR6)`. The normalized coefficient matrix retains rank `e`, so
`dim U_q=e`.

For a squarefree monic polynomial `A` of degree `2e`, Lagrange interpolation
gives `(HFR3)`. In evaluation coordinates, `(HFR4)` is diagonal with entries
`C(a)/A'(a)`, all nonzero. It is therefore nondegenerate. The normalized
Gram identity and `dim U_q=e` prove the self-duality `(HFR5)`.

Self-orthogonality says `tau_A(Cuv)=0` for every `u,v in U_q`, proving
`(HFR7)`. The kernel of a nonzero functional on the `2e`-dimensional algebra
has dimension `2e-1`, giving the dimension bound. If `U_q^2` has that full
hyperplane dimension, its annihilator is one-dimensional, so
`tau_A(C dot)` is unique up to scalar. The map

```text
R_A -> R_A^*,       D |-> tau_A(D dot)
```

is an isomorphism by the nondegeneracy of the unweighted residue pairing.
Hence `C` itself is unique up to scalar. The lower-dimensional alternative
is exactly the final branch in the statement. QED.
