# Budget-three Plucker edge gate

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`

In the B*=3 split-pencil normal form, orient the six nonzero edge polynomials
`b_ij` by `b_ji=-b_ij`. Then

```text
b_01 b_23-b_02 b_13+b_03 b_12=0.                    (PG1)
```

Every factor in `(PG1)` has degree at most two, so this is a polynomial
identity of degree at most four which is independent of the four large block
locators.

More explicitly, put

```text
u=(b_01,0,-b_12,-b_13),
v=(0,b_01,b_02,b_03).
```

Over `F(X)`, all six `2x2` minors of the matrix with rows `u,v` are
`b_01 b_ij`. The block-locator vector lies in this rank-two pencil:

```text
b_01(A_0,A_1,A_2,A_3)=A_0 u+A_1 v.                 (PG2)
```

Let

```text
R=W J product_(i<j)e_ij,
N_2=A_1b_02-A_0b_12,
N_3=A_1b_03-A_0b_13.
```

The exceptional factor has `deg R=n_1+n_2+n_4<=8`, and the official
multiplicative-coset vanishing polynomial obeys the two-generator identity

```text
R A_0 A_1 N_2 N_3=b_01^2 Lambda_D.                 (PG3)
```

The gate is invariant under relabeling: any nonzero `b_ij` may serve as the
base edge. It reduces the selected B*=3 task to first classifying one of six
bounded edge-factor patterns satisfying `(PG1)`, then classifying a
two-generator factorization `(PG3)`. It does not prove that either object is
absent.
