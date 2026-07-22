# Proof

Assume global antiweight:

```text
H(a_k)+H(b_k)=0       for every k.                   (1)
```

For the actual internal-slice quartic `P_l`, the support crossing then
reduces to

```text
r_l(a_k)=r_l(b_k)       (k!=l),                     (2)
```

where `r_l=P_l/D_l^2`.

Let `L` be the indices for which `P_l=c_lD_l^2`. We first prove
`|L|<=2`. The internal-slice value formula at a root `a` of `D_k`, with
`k!=l`, is

```text
P_l(a)=lambda_k^3 r_k^(0)(a)^3 D_l(a)^2/
       [C(a)(xi_l-xi_k)^2],                          (3)
```

where `r_k^(0)=BA_k/[xi_k I'(xi_k)]` is the nonzero polynomial from the
lambda-cube dependency. If `l in L`, cancellation gives

```text
c_l(xi_l-xi_k)^2=t_k,                               (4)
```

for one nonzero `t_k` independent of `l`. If `|L|>=3`, choose distinct
`k,m` so that at least three indices `l in L` differ from both. This is
always possible on the official row: use two indices outside `L` when
`|L|<=e-2`, and otherwise use one or two indices of `L`. Dividing `(4)`
for `k` and `m` makes

```text
((xi_l-xi_k)/(xi_l-xi_m))^2=t_k/t_m.                (5)
```

The equation in `(5)` has degree at most two in `xi_l`, so it cannot hold
at three distinct internal slopes. Hence `|L|<=2`.

For every `l notin L`, the function `r_l` is nonconstant, has degree at
most four, and identifies all exceptional pairs except possibly pair `l`.
Put

```text
K=F_p(r_l:l notin L),       d=[F_p(X):K].            (6)
```

Suppose `d=1`. Successive generator selection needs at most three of the
degree-at-most-four functions: after the first selection the extension
index is at most four, and every strict enlargement divides it by at least
two. All pairs outside those selected indices give common off-diagonal
collisions of the selected functions by `(2)`. Their coincidence divisors
have bidegree at most `(3,3)` after removing the diagonal. Since the
selected functions generate `F_p(X)`, they have no common off-diagonal
component; a base-field generic combination and Bezout bound the common
ordered collisions by

```text
3*3+3*3=18.                                          (7)
```

The official packet supplies at least `2(e-3)>18`, a contradiction.
Therefore `K=F_p(psi)` by Luroth, with

```text
2<=d=deg psi<=4.                                     (8)
```

If `d=2`, at most two `r_l=g_l(psi)` are needed to generate `K`, and their
outer degrees are at most two. A generating tuple of degree-at-most-two
functions on the `psi`-line identifies at most two ordered distinct points:
its off-diagonal `(1,1)` coincidence graphs have no common component and
intersect in at most two points. Each has at most `d^2=4` ordered lifts.
After excluding the at most two selected pair indices and at most four
normalization pairs, at least

```text
e-6                                                   (9)
```

exceptional pairs are fibers of `psi`. The published Mobius-graph bound and
special-graph classification used in the degree-two/three dependency force
`psi`'s deck involution to be antipodal or constant-product. This is
stronger than the required `e-40` conclusion.

If `d` is three or four, one selected `r_l` already generates `K`: its
degree is a positive multiple of `d` and at most four. Its outer function is
Mobius, so `psi` identifies all `e-1` pairs outside that one index. Degree
three is excluded by the degree-two/three dependency. Degree four gives the
second asserted branch, with a stronger `e-1` count.

Combining this absorption of `(1)` with the alternatives already proved in
the degree-two/three dependency leaves exactly bounded-tail dihedral or
degree four. QED.
