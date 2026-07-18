# Rate-half ordinary-list adjacent crossing

- **status:** TARGET
- **consumer:** `list_adjacency_closing`
- **object:** ordinary Reed-Solomon worst-list size (`m=1`)

For every admissible official rate-`1/2` row `C=RS[F,D,k]`, put

```text
q=|F|,
B*=floor(q/2^128),
L_1(a)=max_u #{c in C: agr(c,u)>=a}.
```

There is an agreement index `a_L(C)` such that

```text
L_1(a_L(C)) <= B* < L_1(a_L(C)-1).                 (RHL-ADJ)
```

This is the ordinary-list rate-half input needed by
`list_adjacency_closing`. The proved `list_large_m_scope_closure` theorem then
transports the same pair to every constant common-support interleaving arity.

At the prize-max razor row

```text
n=2^41,    k=2^40,    q<2^256,
```

the proved cyclically rotated prefix floor gives

```text
L_1(k+17,179,869,183)>B*,
```

so any valid crossing satisfies

```text
a_L(C)>=k+17,179,869,184 = k+2^34.                  (RHL-LB)
```

The proved exact-integer Johnson anchor gives the first nontrivial safe
bracket. For `ell=B*+1`, define `a_IJ(C)` as the least `a` for which, on
writing `ell*a=nd+r`,

```text
n binom(d,2)+r*d > binom(ell,2)(k-1).
```

Then

```text
L_1(a_IJ(C))<=B*,       a_L(C)<=a_IJ(C).             (RHL-UB)
```

At the prize-max row, `a_IJ=3n/4` for `B*=1,2,3`, and

```text
a_IJ=floor(sqrt(n(k-1)))+1=1554944255988
```

once `B*>=332114441762`.

The first two low-budget branches are now exact. For every official
rate-half multiplicative-coset row with

```text
B* in {1,2},
```

the explicit low-budget theorem proves

```text
a_L(C)=3n/4,       L_1(3n/4)<=B*<L_1(3n/4-1).       (RHL-B12)
```

The predecessor witnesses contain respectively two and three explicit
degree-`<k` codewords. No inference is made for `B*=3` merely because its
Johnson safe anchor has the same value.

The binding open content is now the exact adjacent location for every branch
`B*>=3`: improve the safe anchor and/or construct an unsafe witness at the
predecessor of a proved safe point until the two meet. The node makes no
MCA/CA claim.

---

## BUDGET-THREE BOUNDED EDGE GEOMETRY (wave-11 audited, 2026-07-18; pin statement body appended per #104 — master text above preserved)


- **status:** TARGET
- **consumer:** `list_adjacency_closing`
- **object:** ordinary Reed-Solomon worst-list size (`m=1`)

For every admissible official rate-`1/2` row `C=RS[F,D,k]`, put

```text
q=|F|,
B*=floor(q/2^128),
L_1(a)=max_u #{c in C: agr(c,u)>=a}.
```

There is an agreement index `a_L(C)` such that

```text
L_1(a_L(C)) <= B* < L_1(a_L(C)-1).                 (RHL-ADJ)
```

This is the ordinary-list rate-half input needed by
`list_adjacency_closing`. The proved `list_large_m_scope_closure` theorem then
transports the same pair to every constant common-support interleaving arity.

At the prize-max razor row

```text
n=2^41,    k=2^40,    q<2^256,
```

the proved cyclically rotated prefix floor gives

```text
L_1(k+17,179,869,183)>B*,
```

so any valid crossing satisfies

```text
a_L(C)>=k+17,179,869,184 = k+2^34.                  (RHL-LB)
```

The proved exact-integer Johnson anchor gives the first nontrivial safe
bracket. For `ell=B*+1`, define `a_IJ(C)` as the least `a` for which, on
writing `ell*a=nd+r`,

```text
n binom(d,2)+r*d > binom(ell,2)(k-1).
```

Then

```text
L_1(a_IJ(C))<=B*,       a_L(C)<=a_IJ(C).             (RHL-UB)
```

At the prize-max row, `a_IJ=3n/4` for `B*=1,2,3`, and

```text
a_IJ=floor(sqrt(n(k-1)))+1=1554944255988
```

once `B*>=332114441762`.

The first two low-budget branches are now exact. For every official
rate-half multiplicative-coset row with

```text
B* in {1,2},
```

the explicit low-budget theorem proves

```text
a_L(C)=3n/4,       L_1(3n/4)<=B*<L_1(3n/4-1).       (RHL-B12)
```

The predecessor witnesses contain respectively two and three explicit
degree-`<k` codewords. No inference is made for `B*=3` merely because its
Johnson safe anchor has the same value.

For `B*=3`, any four-codeword witness at the Johnson predecessor
`3n/4-1` is now reduced to six incidence types and an explicit 4-wise RS
intersection matrix. Full column rank for those six types on the official
multiplicative-coset evaluation vector would improve the safe point by one.
An exact order-eight subgroup witness makes one such matrix singular, so a
proof must use official-scale subgroup algebra rather than pairwise MDS
distance alone. This reduction does not locate the adjacent crossing.

The six types now have a constant-degree split-pencil normal form. Factoring
the four omitted-triple locators `A_i` from every pair difference gives the
four triangle identities

```text
A_k b_ij+A_i b_jk=A_j b_ik,
```

where every edge factor `b_ij` has degree at most two and only three printed
slots across all six types can be quadratic. The `A_i`, singleton, full, and
edge factors partition the multiplicative-coset vanishing polynomial. Thus
the selected B*=3 safe-side task is to exclude these six low-degree
base-field-normalized split pencils, or construct one and consume its actual
list. No such exclusion is imported here.

The edge factors must first pass a bounded Plucker gate

```text
b_01b_23-b_02b_13+b_03b_12=0.
```

This identity has degree at most four and contains no large block locator.
Once it holds, all four `A_i` lie in a rank-two rational pencil generated by
`A_0,A_1`, and their product with an exceptional factor of degree at most
eight equals the subgroup vanishing polynomial. The remaining B*=3 task can
therefore classify bounded edge patterns before invoking large-subgroup
algebra.

The edge degrees have now been classified into only thirteen necessary
chambers. In particular, the pendant type has at least one genuinely
quadratic edge. Five of the six incidence types expose explicit
three-member constant split pencils; there are thirteen such pencils across
the atlas. Each degree-`d` pencil already uses three of at most four fully
subgroup-split members, and the same is true for degree `d-1` when `d>=6`.
The residual-member question is now closed. Rational-transversal analysis
shows that every one of the thirteen printed pencils has exactly its three
displayed fully domain-split members at official scale. For the `K_4-e` and
`K_4` types, the base `A_0,A_1` pencil has two complete fibers and two
injective Mobius graph fibers, and exactly two fully split degree-`d-2`
members. The pendant and triangle-plus-singleton types have respectively
degree-two and Mobius transversals around their exact-three pencils. Thus the
remaining non-cycle problem is simultaneous coupling, not a hidden fourth
member. These necessary normal forms still do not exclude a branch.

The path-plus-singleton branch is sharper still. Its two coupled pencils have
injective Mobius-transversal complements. For `d>=3` its degree-`d` pencil
has exactly three fully domain-split members, and for `d>=6` the same is true
of its degree-`d-1` pencil. The order-eight singular witness is the sharp
`d=2` four-member exception. Hence the large path branch is a primitive
three-fiber rational-map problem, not a missing fourth quotient member.

The path type is not merely an order-eight artifact. An exact
`RS[F_17,F_17^*,8]` witness has four codewords at agreement `11=3n/4-1`,
realizes the path-plus-singleton chamber at `d=4`, and has only the three
first-pencil members allowed by the Mobius theorem. It is a power-of-two
multiplicative-domain route fence, not an official-row counterexample and not
a transport to `d=2^39`.

The 4-cycle is now equally explicit. The ratio `A_1/A_0` has two complete
constant fibers on `T_0,T_1` and injective Mobius graph fibers on `T_2,T_3`; the Plucker gate
prints the exact difference of those graphs. Every other member of the
`A_0,A_1` pencil has at most six domain roots, so at official `d>=8` that
pencil has exactly two fully split degree-`d-1` members. The remaining cycle
problem is this primitive two-fiber/two-graph map, not a hidden constant
pencil.

At the official value `d=2^39`, all six incidence types are consequently
normalized as primitive two- or three-complete-fiber rational maps with
Mobius or degree-two graph fibers. Every fourth-member route has been closed.
The B*=3 task is to prove that the required maps cannot be coupled
simultaneously with the two-generator factorization of the official subgroup,
or to construct such a coupling and consume its actual list.

One chamber has a further base-field compression. In the all-linear `K_4`
type, the edge bivector is a projective line on `Gr(2,4)`. The four
degree-`d-2` block locators therefore satisfy a nondegenerate constant
four-term relation

```text
lambda_0A_0+lambda_1A_1+lambda_2A_2+lambda_3A_3=0,
lambda_0lambda_1lambda_2lambda_3!=0,
```

with no proper vanishing subsum, while their product differs from the domain
polynomial by exactly eight roots. Thus the `K_4` coupling residue is a
base-field split-unit equation, not six independent linear edge factors.
The split-unit equation remains open.

The same Grassmann-line argument covers nine of the thirteen edge-degree
chambers in total: all four cycle chambers, the linear `K_4-e` chamber, the
`K_4` chamber, both path chambers, and the triangle-plus-singleton chamber.
They are split-unit equations with exact exceptional degrees in
`{3,4,5,6,8}`. The bounded edge frontier is now exactly four quadratic
Plucker-conic chambers: the three pendant chambers and the quadratic
`K_4-e` chamber.

Those four conics are now normalized as balanced Grassmann scrolls. After a
degree-at-most-one polynomial row operation, their moving planes have an
affine-linear basis `U_0+XU_1,V_0+XV_1`. In fact their coefficient matrix is
always invertible. Writing `L_ij=[X]b_ij`, its determinant is

```text
b_01^2(L_12L_03-L_02L_13)!=0.
```

For the pendant chambers this is nonzero because `L_02=0` while
`L_12L_03!=0`; for quadratic `K_4-e` it is the negative leading coefficient
of the exact quadratic edge, multiplied by `b_01^3`. Hence the
rank-deficient quadratic split-unit branch is empty, and one constant
base-field change always gives

```text
C^(-1)A=(alpha,X alpha,beta,X beta)^T.
```

Thus the bounded edge geometry is complete: nine Grassmann lines and four
full-rank balanced scrolls. The remaining work is official-subgroup arithmetic
for the nine split-unit and four full-rank scroll chambers.

The binding open content is now the exact adjacent location for every branch
`B*>=3`: improve the safe anchor and/or construct an unsafe witness at the
predecessor of a proved safe point until the two meet. The node makes no
MCA/CA claim.

---

## WAVE-12 PIN BODY (2026-07-18; appended per #104 — the wave-12 statement of record with the primitive-module / maximal-field / single-fiber pins)


- **status:** TARGET
- **consumer:** `list_adjacency_closing`
- **object:** ordinary Reed-Solomon worst-list size (`m=1`)

For every admissible official rate-`1/2` row `C=RS[F,D,k]`, put

```text
q=|F|,
B*=floor(q/2^128),
L_1(a)=max_u #{c in C: agr(c,u)>=a}.
```

There is an agreement index `a_L(C)` such that

```text
L_1(a_L(C)) <= B* < L_1(a_L(C)-1).                 (RHL-ADJ)
```

This is the ordinary-list rate-half input needed by
`list_adjacency_closing`. The proved `list_large_m_scope_closure` theorem then
transports the same pair to every constant common-support interleaving arity.

At the prize-max razor row

```text
n=2^41,    k=2^40,    q<2^256,
```

the proved cyclically rotated prefix floor gives

```text
L_1(k+17,179,869,183)>B*,
```

so any valid crossing satisfies

```text
a_L(C)>=k+17,179,869,184 = k+2^34.                  (RHL-LB)
```

The proved exact-integer Johnson anchor gives the first nontrivial safe
bracket. For `ell=B*+1`, define `a_IJ(C)` as the least `a` for which, on
writing `ell*a=nd+r`,

```text
n binom(d,2)+r*d > binom(ell,2)(k-1).
```

Then

```text
L_1(a_IJ(C))<=B*,       a_L(C)<=a_IJ(C).             (RHL-UB)
```

At the prize-max row, `a_IJ=3n/4` for `B*=1,2,3`, and

```text
a_IJ=floor(sqrt(n(k-1)))+1=1554944255988
```

once `B*>=332114441762`.

The first two low-budget branches are now exact. For every official
rate-half multiplicative-coset row with

```text
B* in {1,2},
```

the explicit low-budget theorem proves

```text
a_L(C)=3n/4,       L_1(3n/4)<=B*<L_1(3n/4-1).       (RHL-B12)
```

The predecessor witnesses contain respectively two and three explicit
degree-`<k` codewords. No inference is made for `B*=3` merely because its
Johnson safe anchor has the same value.

For `B*=3`, any four-codeword witness at the Johnson predecessor
`3n/4-1` is now reduced to six incidence types and an explicit 4-wise RS
intersection matrix. Full column rank for those six types on the official
multiplicative-coset evaluation vector would improve the safe point by one.
An exact order-eight subgroup witness makes one such matrix singular, so a
proof must use official-scale subgroup algebra rather than pairwise MDS
distance alone. This reduction does not locate the adjacent crossing.

The six types now have a constant-degree split-pencil normal form. Factoring
the four omitted-triple locators `A_i` from every pair difference gives the
four triangle identities

```text
A_k b_ij+A_i b_jk=A_j b_ik,
```

where every edge factor `b_ij` has degree at most two and only three printed
slots across all six types can be quadratic. The `A_i`, singleton, full, and
edge factors partition the multiplicative-coset vanishing polynomial. Thus
the selected B*=3 safe-side task is to exclude these six low-degree
base-field-normalized split pencils, or construct one and consume its actual
list. No such exclusion is imported here.

The edge factors must first pass a bounded Plucker gate

```text
b_01b_23-b_02b_13+b_03b_12=0.
```

This identity has degree at most four and contains no large block locator.
Once it holds, all four `A_i` lie in a rank-two rational pencil generated by
`A_0,A_1`, and their product with an exceptional factor of degree at most
eight equals the subgroup vanishing polynomial. The remaining B*=3 task can
therefore classify bounded edge patterns before invoking large-subgroup
algebra.

The edge degrees have now been classified into only thirteen necessary
chambers. In particular, the pendant type has at least one genuinely
quadratic edge. Five of the six incidence types expose explicit
three-member constant split pencils; there are thirteen such pencils across
the atlas. Each degree-`d` pencil already uses three of at most four fully
subgroup-split members, and the same is true for degree `d-1` when `d>=6`.
The residual-member question is now closed. Rational-transversal analysis
shows that every one of the thirteen printed pencils has exactly its three
displayed fully domain-split members at official scale. For the `K_4-e` and
`K_4` types, the base `A_0,A_1` pencil has two complete fibers and two
injective Mobius graph fibers, and exactly two fully split degree-`d-2`
members. The pendant and triangle-plus-singleton types have respectively
degree-two and Mobius transversals around their exact-three pencils. Thus the
remaining non-cycle problem is simultaneous coupling, not a hidden fourth
member. These necessary normal forms still do not exclude a branch.

The path-plus-singleton branch is sharper still. Its two coupled pencils have
injective Mobius-transversal complements. For `d>=3` its degree-`d` pencil
has exactly three fully domain-split members, and for `d>=6` the same is true
of its degree-`d-1` pencil. The order-eight singular witness is the sharp
`d=2` four-member exception. Hence the large path branch is a primitive
three-fiber rational-map problem, not a missing fourth quotient member.

The path type is not merely an order-eight artifact. An exact
`RS[F_17,F_17^*,8]` witness has four codewords at agreement `11=3n/4-1`,
realizes the path-plus-singleton chamber at `d=4`, and has only the three
first-pencil members allowed by the Mobius theorem. It is a power-of-two
multiplicative-domain route fence, not an official-row counterexample and not
a transport to `d=2^39`.

The 4-cycle is now equally explicit. The ratio `A_1/A_0` has two complete
constant fibers on `T_0,T_1` and injective Mobius graph fibers on `T_2,T_3`; the Plucker gate
prints the exact difference of those graphs. Every other member of the
`A_0,A_1` pencil has at most six domain roots, so at official `d>=8` that
pencil has exactly two fully split degree-`d-1` members. The remaining cycle
problem is this primitive two-fiber/two-graph map, not a hidden constant
pencil.

At the official value `d=2^39`, all six incidence types are consequently
normalized as primitive two- or three-complete-fiber rational maps with
Mobius or degree-two graph fibers. Every fourth-member route has been closed.
The B*=3 task is to prove that the required maps cannot be coupled
simultaneously with the two-generator factorization of the official subgroup,
or to construct such a coupling and consume its actual list.

One chamber has a further base-field compression. In the all-linear `K_4`
type, the edge bivector is a projective line on `Gr(2,4)`. The four
degree-`d-2` block locators therefore satisfy a nondegenerate constant
four-term relation

```text
lambda_0A_0+lambda_1A_1+lambda_2A_2+lambda_3A_3=0,
lambda_0lambda_1lambda_2lambda_3!=0,
```

with no proper vanishing subsum, while their product differs from the domain
polynomial by exactly eight roots. Thus the `K_4` coupling residue is a
base-field split-unit equation, not six independent linear edge factors.
The split-unit equation remains open.

The same Grassmann-line argument covers nine of the thirteen edge-degree
chambers in total: all four cycle chambers, the linear `K_4-e` chamber, the
`K_4` chamber, both path chambers, and the triangle-plus-singleton chamber.
They are split-unit equations with exact exceptional degrees in
`{3,4,5,6,8}`. The bounded edge frontier is now exactly four quadratic
Plucker-conic chambers: the three pendant chambers and the quadratic
`K_4-e` chamber.

The direct quotient-periodic construction of those nine split-unit equations
is impossible. If every related locator were one degree-`d` quotient fiber
with only its exceptional points removed, partial fractions would express the
locators through disjoint subsets of at most eight geometric Vandermonde
vectors. Those vectors are independent for `d>=8`, contradicting every
nonzero constant relation. Surviving split-unit chambers must therefore be
primitive or use a genuinely multi-fiber quotient pattern.

Those four conics are now normalized as balanced Grassmann scrolls. After a
degree-at-most-one polynomial row operation, their moving planes have an
affine-linear basis `U_0+XU_1,V_0+XV_1`. In fact their coefficient matrix is
always invertible. Writing `L_ij=[X]b_ij`, its determinant is

```text
b_01^2(L_12L_03-L_02L_13)!=0.
```

For the pendant chambers this is nonzero because `L_02=0` while
`L_12L_03!=0`; for quadratic `K_4-e` it is the negative leading coefficient
of the exact quadratic edge, multiplied by `b_01^3`. Hence the
rank-deficient quadratic split-unit branch is empty, and one constant
base-field change always gives

```text
C^(-1)A=(alpha,X alpha,beta,X beta)^T.
```

The two generators are automatically coprime. In pendant chambers their
degrees are exactly `(d-2,d-1)`; in quadratic `K_4-e` they are
`(d-2,d-2)`. At official `d>=4`,

```text
<alpha,Xalpha> intersect <beta,Xbeta>={0}.
```

Thus the quadratic locator span is genuinely four-dimensional and cannot
collapse to a hidden constant split-unit relation. Its exact remaining form
is a product of four independent affine-linear combinations of this coprime
generator pair, with four or six exceptional subgroup roots.

At the maximal `n=2^41` row, the B*=3 field arithmetic also collapses. If
`q=p^e`, the exact budget interval and `2^41|q-1` force

```text
e=1 with p=1 mod 2^41,       or       e=2 with p=+/-1 mod 2^40.
```

There is no cubic or higher extension branch: the sole cubic interval
candidate is `p=5*2^41+1`, which is divisible by seven. This gate is scoped
to the maximal domain and does not replace the chamber exclusions.

Thus the bounded edge geometry is complete: nine Grassmann lines and four
full-rank balanced scrolls. The remaining work is official-subgroup arithmetic
for the nine split-unit and four full-rank scroll chambers.

The binding open content is now the exact adjacent location for every branch
`B*>=3`: improve the safe anchor and/or construct an unsafe witness at the
predecessor of a proved safe point until the two meet. The node makes no
MCA/CA claim.
