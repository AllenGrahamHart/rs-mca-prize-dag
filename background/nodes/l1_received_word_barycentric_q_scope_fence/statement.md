# L1 received-word barycentric Q scope fence

- **status:** PROVED
- **role:** type the global exact-shell prefix map against upstream row-sharp Q
- **consumer:** `l1_mixed_petal_amplification`

## Barycentric normal form

Let `A` be an `a`-subset of distinct field points, let

```text
L_A(Z)=prod_(x in A)(Z-x),
I_A(U)=the degree-below-a interpolant of U on A,
w=a-k>0.
```

For `0<=j<w`, put

```text
B_j(U,A)=sum_(x in A) U(x)x^j/L_A'(x).                 (BQ1)
```

Then

```text
deg I_A(U)<k  iff  B_0(U,A)=...=B_(w-1)(U,A)=0.       (BQ2)
```

The change from the top `w` coefficients of `I_A(U)` to `(B_j)` is
unitriangular. Thus `(BQ1)` is the exact dual Reed-Solomon form of the
received-word interpolation-prefix map in
`l1_exact_shell_prefix_hankel_bridge`.

## Scope mismatch with locator Q

The denominator `L_A'(x)` depends on the complete moving support `A`.
Consequently `(BQ1)` is not, without another theorem, the fixed-column linear
map on a Boolean slice required by upstream `def:primitive-q` and
`def:q-row-atom`. The latter uses the first locator coefficients, which are
Newton-equivalent to the fixed power-sum columns

```text
x |-> (x,x^2,...,x^w).
```

The mismatch is real even at depth one. Over `F_7`, take

```text
H={0,1,2,3,5,6},  a=3,  k=2,  U(x)=x^4.
```

For a triple `A`, the unique depth-one interpolation prefix is

```text
f(A)=[Z^2]I_A(U)=e_1(A)^2-e_2(A).                     (BQ3)
```

The triples `{0,1,2}` and `{1,3,6}` have the same first locator prefix because
both root sums are `3 mod 7`, but their received-word prefixes are respectively
`0` and `3`. Moreover, on the four exchanges around the base `{0}`,

```text
f(012)+f(035)-f(013)-f(025)=4 mod 7 != 0.             (BQ4)
```

Every affine fixed-column statistic `c+sum_(x in A)g(x)` satisfies the same
exchange with value zero. Hence the literal received-word coordinate has no
such representation on this slice. Also `{0,1,2}` is the complete agreement
set of its degree-below-two interpolant, so the phenomenon is visible at an
exact shell rather than only in raw support multiplicity.

## Consequence

The global L1 route remains valid only as a **new received-word barycentric
prefix-flatness theorem**, or after an explicit map-and-owner transport that
normalizes `(BQ1)` on every primitive residual chart. The currently stated
upstream locator-prefix row-sharp Q theorem cannot be cited directly.

This is a type and route fence, not a counterexample to either theorem. A
nonlinear enlargement, quotient identity, or chart-specific normalization
could still provide the missing transport.
