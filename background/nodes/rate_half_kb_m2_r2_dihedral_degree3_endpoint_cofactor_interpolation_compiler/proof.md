# Proof

## 1. Exact interpolation gate

Assume first that `M=H N`. Bidegrees give

```text
bideg(N)=(9,18).
```

At `T=alpha_i`, equation `(KBM3I-1)` and the normalized Lagrange law give

```text
M(alpha_i,X)=kappa_i B(X)/z_i(X).
```

Since `H_i` divides `B/z_i`, evaluation of `M=HN` gives

```text
N(alpha_i,X)=kappa_i E_i(X).                       (1)
```

Conversely, if a form `N` of `T`-degree at most nine satisfies `(1)`, then
`M-HN` has `T`-degree at most eleven and vanishes at the twelve distinct
values `alpha_i`. It is therefore zero. Thus component realization is
equivalent to interpolation of the twelve values in `(1)` by a polynomial
of degree at most nine in `T`.

The unique interpolant of degree at most eleven is

```text
N_11(T,X)=sum_i kappa_i E_i(X)
           A(T)/((T-alpha_i)A'(alpha_i)).           (2)
```

Write `s=sum_i alpha_i`. Since `A` is monic, the coefficients of `T^11`
and `T^10` in its `i`th normalized Lagrange polynomial are respectively

```text
1/A'(alpha_i),       (alpha_i-s)/A'(alpha_i).       (3)
```

The interpolant `(2)` has degree at most nine exactly when both leading
coefficients vanish. With `w_i=kappa_i/A'(alpha_i)`, the first vanishing
condition and then the second reduce exactly to `(KBM3I-3)`. Distinctness
of the source labels and nonvanishing of the actual source weights make
every `w_i` nonzero. Conversely, any full-support solution of `(KBM3I-3)`
defines nonzero `kappa_i=w_i A'(alpha_i)` and makes `(2)` the required
bidegree-`(9,18)` cofactor. This proves necessity and sufficiency.

Taking coefficients of the two degree-18 identities gives the printed
`38 x 12` matrix criterion.

## 2. Star-edge holonomy

Let `x` be a simple root of `B`. Complete-source saturation gives exactly
two labels `a,b` for which `H_a(x)=H_b(x)=0`, and the locator partition gives
a unique label `c` for which `z_c(x)=0`. Locator avoidance says that `a,b,c`
are distinct. Consequently `E_i(x)` vanishes unless `i` is one of `a,b,c`,
while each of `E_a(x),E_b(x),E_c(x)` is nonzero.

Evaluate both identities `(KBM3I-3)` at `x` and subtract `alpha_c` times the
first from the second. The `c` term disappears and the result is exactly
`(KBM3I-4)`. Since the labels, weights, and displayed cofactor values are
all nonzero in the required differences, solving for `w_b/w_a` gives the
printed edge transport. Around a directed cycle

```text
a_0 -> a_1 -> ... -> a_r=a_0
```

the transport product telescopes as

```text
product_(j=0)^(r-1) rho_(a_j->a_(j+1))
 =product_(j=0)^(r-1) w_(a_(j+1))/w_(a_j)=1.       (4)
```

This proves the local necessary holonomy condition.

For the complete criterion, retain all three labels in
`S_x={a,b,c}`. For any ordered pair `u,v`, eliminating the third label
`r` from the two local equations gives exactly `(KBM3I-5)`. Hence a
full-support kernel supplies a vertex potential `w` whose ratio on every
gain edge is the printed gain. Products around closed walks telescope, so
the gain multigraph is flat.

Conversely, suppose the gain multigraph is flat. In each connected component
choose one label and assign it an arbitrary nonzero weight. Transporting
that weight along a path defines all other weights; closed-walk flatness
makes the definition path-independent. Every gain is nonzero, so the
resulting weights have full support. At each root `x`, the edge relations
on the triangle `S_x` put

```text
(w_i E_i(x))_(i in S_x)
```

in the one-dimensional kernel of the two rows
`(1)_(i in S_x)` and `(alpha_i)_(i in S_x)`. The two sums in
`(KBM3I-3)` therefore vanish at `x`. Each sum has degree at most 18 and
the residual generic-pole profile has 24 distinct complete-source roots, so
both sums vanish identically. This proves the exact gain-flatness
equivalence.

## 3. Pinned deleting fixture

Work over `F_47` with the geometric model from the parent node. Its two
generic cubic pole values are `7` and `18`. The twelve source labels are

```text
5,10,17,19,21,23,24,26,28,30,37,42,
```

and the 24 complete-source roots are

```text
3,6,8,11,12,13,14,15,16,18,20,21,
26,27,29,31,32,33,34,35,36,39,41,44.
```

Index the labels in the displayed order. Assign the two roots of `z_i` by

```text
0:(32,31)   1:(11,36)   2:(6,41)    3:(16,33)
4:(3,39)    5:(12,35)   6:(18,29)   7:(34,14)
8:(20,27)   9:(44,13)  10:(21,26)  11:(15,8).      (4)
```

The independent verifier reconstructs `phi`, `psi`, and `H`, rather than
trusting a star table. It checks that `(4)` partitions the complete-source
roots, avoids the four roots of every corresponding `H_i`, and has invariant
label set

```text
I={1,2,5,6,8,10}.
```

The invariant fibers induce the fixed-point-free bijection

```text
1->10, 2->8, 5->6, 6->5, 8->2, 10->1,
```

so `L=I`. The other six quadratics form the required simple two-regular
bipartite pole graph. Exactly four noninvariant pole edges satisfy the
degree-two component color test `H(alpha_j,-x)=0`.

Constructing `E_i` from `(KBM3I-2)` gives rank 11 for the first coefficient
block. Its kernel is generated by

```text
(0,13,0,0,0,19,14,0,0,0,1,0),
```

which already cannot encode nonzero actual weights. More decisively, after
stacking the `alpha_i E_i` block, rows `0,...,10,19` form a square minor
with determinant

```text
7 mod 47.
```

There is already a local obstruction. The source deck pairs split the two
star components into the parts

```text
(0,11)|(2,9)|(4,7),       (1,10)|(3,8)|(5,6).
```

Orient each of the three standard `K_(2,2)` squares in each component by
taking the first entry in the first part, the first entry in the second,
then the two second entries. Direct evaluation of the transport formula
gives

```text
11,26,17 and 2,41,31 mod 47.                       (5)
```

Every value in `(5)` differs from one, so any one of these squares rules out
a full-support kernel. Independently, the stacked matrix has rank 12 and no
kernel at all. By the exact equivalence above, this admissible abstract
packet cannot divide an endpoint form of `(KBM3I-1)`. QED.
