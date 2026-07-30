# Proof

## V4 stabilizer law

Work over the algebraic closure of the deployed odd-characteristic field.
The separable quadratic map `h` is the quotient of `P1` by its unique deck
involution `tau`. Therefore

```text
q=h x h : P1 x P1 -> P1 x P1
```

is a generically free Galois quotient with group
`V4=<a,c>`, where `a=tau x 1` and `c=1 x tau`.

Let `C=q(Gamma)`. In a Galois cover, the group acts transitively on the
irreducible components above the generic point of an irreducible image.
If `S=Stab_V4(Gamma)`, then the generically free restriction identifies the
normalization of `C` with `Gamma/S`. Hence

```text
deg(Gamma -> C)=|S|.                                (KBM2-1)
```

The transverse compiler gives `delta*r=8`. The subgroup orders of V4 are
one, two, and four, so `(KBM2-1)` gives exactly

```text
r=2, delta=4, S=V4;
r=4, delta=2, S=<a>, <c>, or <ac>;
r=8, delta=1, S=1.                                 (KBM2-2)
```

## No primitive outer case

The outer map has degree 30, and `C` is a non-diagonal component of its
self-fiber product of bidegree `(r,r)`. If the outer map were
indecomposable, its geometric monodromy would be primitive and `r` would be
a point-stabilizer subdegree.

The complete pinned GAP `PrimGrp` degree-30 entry has four groups:

```text
PSL(2,29), PGL(2,29), A30, S30,
```

and every complete subdegree row is `1,29`. None supports `r=2,4,8`, so the
outer map has a proper right factor of degree

```text
d in {2,3,5,6,10,15}.                              (KBM2-3)
```

Composing that factor with `h` gives an endpoint inner map of degree
`2d`, respectively

```text
4,6,10,12,20,30.                                   (KBM2-4)
```

Inner degrees 4 and 12 are empty. Inner degree 20 is absent from the
exhaustive source-pole/Riemann-Hurwitz profile. Degree 6 routes to degree
two or the deleted degree-five row; degree 10 routes to degrees 2,3,6, and
the degree-three router then returns to degree two; degree 30 routes to
degree 6 and then degree two. Thus every surviving path in `(KBM2-4)`
returns to `m=2`. This is recurrence, not a nonexistence proof.

## Coordinate-stabilized source lift

Let `H_0` be the actual irreducible bidegree-`(2,4)` source component in
coordinates `(T,X)`, let `b` be the deck involution of the quadratic source
map `psi(X)=W`, and let

```text
(T,X) -> (T,psi(X))
```

map `H_0` birationally to `Gamma`. The imported birational-quartic theorem
also says that `H_0` and `bH_0` are distinct components of the quadratic
base change.

Assume `a=tau x 1` stabilizes `Gamma`. Since `a` fixes `W`, its lift with
`X` fixed either preserves `H_0` or exchanges `H_0` and `bH_0`. In the
first case a bihomogeneous equation `H` of `H_0` satisfies

```text
H(tau(T),X)=lambda H(T,X)
```

for a constant eigenvalue. The degree-two binary forms that are
eigenvectors of a nontrivial projective involution form a projective line
together with one isolated eigendirection. The irreducible coefficient
image would therefore lie in a line (or be constant), contradicting the
already-proved residual birational-quartic branch. Hence the fixed-`X` lift
exchanges the two base-change components, and composing it with `b` gives
the preserving lift

```text
(T,X) -> (tau(T),b(X)).                             (KBM2-5)
```

## Source-star parity

The degree-two source profile consists of six unramified fibers, so `tau`
pairs the twelve source labels without fixed points. Write the partner of
`i` as `bar(i)`. Put `q_i=H(alpha_i,X)`. The complete-source theorem gives

```text
div(q_i) <= div(B/z_i),                             (KBM2-6)
```

where the pairwise disjoint coordinate quadratics `z_i` and their product
`B` are invariant under `b`. Equation `(KBM2-5)` gives

```text
div(q_i)=b^* div(q_bar(i)).                         (KBM2-7)
```

Pulling `(KBM2-6)` for `bar(i)` back by `b` and intersecting it with
`(KBM2-6)` for `i` yields

```text
div(q_i) <= div(B/(z_i z_bar(i))).                  (KBM2-8)
```

At every root `x` of `B`, complete-source saturation says that exactly two
source labels contribute, counted with the root multiplicity `m_x`.
Equations `(KBM2-5)--(KBM2-7)` send that unordered pair to its `tau`-image
at `b(x)`. Thus star weights are equivariant.

The only two-subsets of a fixed-point-free twelve-label involution that are
fixed are the six matching pairs `{i,bar(i)}`. The weight of an occupied
fixed vertex is even: nonfixed `b`-preimages occur in equal pairs, while a
`b`-fixed root of `B` is a ramification point of one quadratic `z_i` and
has multiplicity two. The complete-source defect bound

```text
sum_v binom(w_v,2) <= 3                             (KBM2-9)
```

therefore makes every occupied fixed vertex have weight exactly two.
A nonfixed weight-three vertex would bring its distinct partner and cost at
least six in `(KBM2-9)`, while a fixed weight-three vertex has odd weight.
Hence the weight-three defect type is absent. If `d` is the number of
weight-two vertices and `e` the number of fixed matching vertices, then
nonfixed doubles occur in pairs, so

```text
0<=e<=d<=3,       e=d mod 2.                        (KBM2-10)
```

This proves every claimed refinement and leaves the recurrent actual
source-coupled leaf open. QED.
