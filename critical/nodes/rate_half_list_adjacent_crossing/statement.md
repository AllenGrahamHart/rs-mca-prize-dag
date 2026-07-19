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

---

## WAVE-13 PIN BODY (2026-07-19; appended per #104 — the statement of record with the 27 deleted-pair/weld/core-one pins)


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

That exact support pattern is now arithmetically isolated. A full cyclotomic
minor has norm `2^170 17^4`, so its rank defect is impossible in every odd
characteristic other than `17`; characteristic `17` cannot carry an
order-`2^41` domain below the official field cap. This removes the printed
witness as an unchanged-exponent transport, but does not exclude another path
assignment.

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

The quotient-periodic exclusion now extends beyond one completed fiber in the
six cycle/path chambers. If every size-`d=sm` completed block is a union of
`s` fibers of one map `X^m` and one root `r_i` is deleted, the top `m`
coefficients of its locator form the geometric vector on `r_i`. Distinct
deleted roots give a Vandermonde-independent family. Thus all cycle
constructions of this form are impossible for `m>=4`, and all path
constructions are impossible for `m>=3`. At `d=2^39`, direct power-of-two
multifiber constructions in these six chambers survive only at fiber sizes
`1,2`; mixed maps, incomplete fibers, and primitive locators remain open.

Multiple exceptional roots are now covered as well. If the related locators
delete disjoint root sets of sizes `ell_i`, their reversed top coefficients
are the rational series

```text
z^(ell_i-ell_min)/product_(r in R_i)(1-rz).
```

They are independent once `m>sum ell_i-ell_min`. The linear `K_4-e`, `K_4`,
and triangle-plus-singleton profiles have thresholds `6,7,5`; therefore every
power-of-two fiber size `m>=8` is excluded in all nine linear chambers. Their
remaining direct equal-fiber sizes are `1,2,4`, while cycle/path retain only
`1,2`. This does not touch mixed maps, partial fibers, primitive locators, or
the four quadratic scrolls.

The fiber-four residue gate removes two of the three additional linear
profiles. Multiplication by the deleted-root product gives a `4 x 4` residue
matrix over `F(X^4)`. Rank four forbids a relation, while rank three forces
the degree-`2^37` completed blocks to share a factor and contradicts disjoint
block locators. Linear `K_4-e` and triangle-plus-singleton always have rank at
least three. The only direct `m=4` residual is therefore the linear `K_4`
rank-two reciprocal locus; antipodal deleted pairs show that this algebraic
locus is nonempty, but do not construct an official witness.

On the antipodal component `P_i=X^2-a_i`, the residual descends one exact
quotient level. Writing `Y=X^4`, each completed block is
`H_i=(Y-a_i^2)G_i`, each locator is `(X^2+a_i)G_i(X^4)`, and the four
degree-`2^37-1` polynomials `G_i` are pairwise coprime members of one
two-dimensional base-field pencil satisfying

```text
product_i G_i(Y)=(Y^(2^39)-1)/product_i(Y-a_i^2).
```

Thus this component is an exact quotient split-pencil census, not an
official-degree locator search.

The two descended relations also weld the pencil parameters to the deleted
pairs. After one base-field change of pencil basis, the antipodal residual is
the single quartic norm equation

```text
product_(i=0)^3(R+a_iS)
 =kappa (Y^(2^39)-1)/product_(i=0)^3(Y-a_i^2),
deg R,deg S<=2^37-1.
```

Equivalently, before the basis change the four pencil parameters are one
Möbius image of the four `a_i`.

This welded map is now known to be primitive. Its reduced rational degree is
exactly `2^37-1`, which is odd, so it cannot factor through any nontrivial
cyclic or dihedral quotient of the dyadic order-`2^39` domain. The direct
index-four coset partition is impossible too: deleting one root in each
coset gives four geometric-series factors whose first four coefficients form
a nonzero Vandermonde matrix and hence span dimension four, not two. The
remaining quartic norm problem is a primitive, nonperiodic pencil census.

It is also degree-balanced. If `V` is the unique degree-drop direction in the
monic quotient pencil, reverse-polynomial contact at infinity proves

```text
deg V>=2^36-2.
```

The proof centers the four pencil parameters, so the first correction to the
leading fourth power has reverse order `2(r-deg V)`. The maximal-row field
collapse ensures that the characteristic exceeds `d=2^39`, making the
derivative argument valid. Constant and low-degree translation pencils are
therefore absent; the surviving primitive census has two high-degree
directions.

If the centered coefficient `e_2` vanishes, the first reverse correction has
order at least `3(r-deg V)`, strengthening the official floor to

```text
deg V>=(2^38-4)/3.
```

These floors now carry exact original-coordinate residuals. If
`q=min{j in {2,3,4}:e_j!=0}`, `h=r-deg V`, and

```text
T=dDU-Y(D'U+4DU'),
```

then `T` is nonzero of exact degree `r+4-qh`. Every repeated root of `U`,
and every root of `U` lying in `Z(D) union {0}`, is a root of `T`. On the
lowest official generic boundary `T` is linear, so there is at most one such
exceptional root. On the lowest intermediate boundary it is quadratic, so
there are at most two. Above either floor its degree grows by `q` for each
added degree of `V`.

The two low-residual boundaries have a canonical fourth-root form. Set

```text
E(z)=z^4D(z^-1),       E(z)^(-1/4)=sum_(m>=0)a_mz^m.
```

Whenever `deg T<=3`, the monic direction is unique and

```text
z^rU(z^-1)=sum_(m=0)^r a_mz^m.
```

The norm contact is exactly the index of the first nonzero omitted
coefficient. Thus the official generic boundary requires
`a_(r+1)=a_(r+2)=0` and `a_(r+3)!=0`; the intermediate boundary requires
`a_(r+1)=0` and `a_(r+2)!=0`. The coefficients satisfy an explicit
four-term recurrence. This replaces an unknown official-degree `U` by a
coefficient-gap problem determined only by the degree-four deleted divisor.

On the generic floor, the same normalization also eliminates the lower
direction up to scale. With `C=z^vV(z^-1)`, `h=2^36+1`, and

```text
R=E^(-1)(1-z^d)-B^4,
J=z^(-2h)R/B^2,
P=(J/J(0))^(1/2),       P(0)=1,
```

the norm identity gives `P=C/C(0) mod z^h`. Since `deg C=h-3`, existence
forces the secondary gap

```text
[z^(2^36-1)]P=[z^(2^36)]P=0.
```

Thus the lowest generic stratum has no remaining official-degree polynomial
variables: `U` and normalized `V` are nested fourth-root and square-root
truncations determined by the four deleted roots. Their simultaneous primary
and secondary coefficient gaps remain to be excluded.

The nested square root has a direct two-window form. Since
`r=2h-3`, the primary gap is

```text
a_(2h-2)=a_(2h-1)=0,       a_(2h)!=0.
```

If `L=sum_(m<h)a_mz^m` and
`T=sum_(m<h)a_(2h+m)z^m`, then

```text
P^2=L T/a_(2h) mod z^h.
```

Thus the secondary gap is exactly the assertion that this normalized product
is the square of a polynomial of degree at most `h-3`. The full shifted tail
also satisfies a first-order differential equation with forcing of degree at
most one. This removes the nested-series implementation but does not exclude
the square congruence.

There is an exact one-variable reduction on the sublocus where the four
deleted roots are two antipodal pairs. Write `d=16M`, so `h=2M+1`, and set
`w=z^2`. Then `E` and `E^(-1/4)` are even. The primary coefficient at
`4M+1` and the secondary coefficient at `2M-1` vanish automatically. After
normalizing the two squared deleted roots to `{1,t}`, the remaining gate is

```text
F_(2M)(t)=0,       F_(2M+1)(t)!=0,       G_M(t)=0,
t^(8M)=1,          t!=1,
```

where `F_j(t)=[x^j]((1-x)(1-tx))^(-1/4)` and `G_M` is the final coefficient
of the reduced two-window square root modulo `x^(M+1)`. Thus this deleted-pair
stratum has one torsion variable and two nonautomatic scalar equations; their
simultaneous nonvanishing remains open.

If such a deleted-pair candidate reaches the complete canonical span, parity
also forces its odd outer coefficient `beta` to vanish. The split outer
quartic is even, and the full cyclotomic quotient factors exactly as

```text
(1-w^(8M))/((1-w)(1-tw))
 =(B_0^2+lambda w^(2M+1)C_0^2)
  (B_0^2+mu     w^(2M+1)C_0^2),
```

where `lambda,mu` are distinct and nonzero. Both factors have degree `4M-1`,
are coprime, and partition the remaining `8M`-torsion roots. Classifying this
primitive square-pencil partition is sufficient for the complete deleted-pair
sublocus. The two inverse-root cells have identical power sums through
frequency `2M`, each equal to `-(1+t^j)/2`; their first difference at
`h=2M+1` is exactly `-h(lambda-mu)`.

In the original coordinate this complete sublocus has a second exact
compression. Writing `x=Y^2` gives

```text
D=D_0(x),       U=YU_0(x),       V=V_0(x),
D_0(x)(xU_0^2+lambda V_0^2)(xU_0^2+mu V_0^2)=x^(8M)-1.
```

The lowest official generic boundary has a linear residual, and parity makes
that residual odd. It is therefore `kappa Y`, where `kappa!=0`, and the monic
direction obeys the constant-forcing ODE

```text
(16M-4)D_0U_0-2xD_0'U_0-8xD_0U_0'=kappa.
```

For fixed `D_0`, its coefficient recurrence determines at most one monic
`U_0` and leaves one terminal equation. It also proves that the forced simple
root of `U` at zero is its only exceptional root: all other roots are simple
and avoid `D`. This is still a compression, not a classification of the
square-pencil system.

The Möbius matching on this sublocus is finite as well. Choose a fourth root
`iota` of unity and normalize the four deleted-root lifts to

```text
(1,iota,r,iota r),       r^4=t.
```

If `q=mu/lambda` is the squared ratio of the two outer antipodal pairs, then
the root-cell constant terms force `q^N=1`. The matching is equivalent to one
of exactly three reciprocal equations:

```text
r^2(1+q)^2=4q(r^2-r+1)^2,
(r-1)^4(1+q)^2=4q(r+1)^4,
(r^2+1)^2(1+q)^2=4q(r^2-4r+1)^2.
```

They are the three possible pullbacks of the target antipodal pairing. Thus a
fixed `r` allows at most three unordered outer ratios `{q,q^(-1)}`, and only
their `N`-torsion values remain. The cleared equations retain `q=-1`; this is
an exact router, not an exclusion of the three resulting square-pencil
systems.

Those three systems now have an exact reconstruction test with no free `V_0`.
Put

```text
Q=(x^N-1)/D_0,       A=xU_0^2,       R=Q-A^2.
```

For `q!=-1`, divide `R=AS+T` with `deg T<deg A`. A square-pencil survivor is
equivalent to

```text
deg S=2M-2,
T=qS^2/(1+q)^2,
S/(1+q) is a nonzero polynomial square.
```

The quotient reconstructs the unique scaled `V_0^2`; the remainder is
automatically a fourth power. For `q=-1`, the complete criterion is that
`-R` be a fourth power of a degree-`M-1` polynomial. Thus only a uniform
torsion-indexed square/fourth-power rejection remains on this deleted-pair
sublocus.

The harmonic alternative is now excluded at the official field scale. At
`q=-1`, the three Möbius equations force respectively

```text
r^2-r+1=0,       r=-1,       or       r^2-4r+1=0.
```

The first has order six and the second has `r^4=1`. In the third, the trace
recurrence `c_0=4`, `c_(j+1)=c_j^2-2` must vanish by index `38`. A complete
32-shard screen of all `4,495,441` moduli `p=1 mod 2^40` in the exact official
interval finds no zero. Therefore every remaining official deleted-pair
candidate has `q!=-1` and is governed only by the Euclidean quotient-square
criterion.

That nonharmonic criterion is now outer-ratio free. For the three source
pairings define

```text
(a_0,b_0)=(r^2,(r^2-r+1)^2),
(a_1,b_1)=((r-1)^4,(r+1)^4),
(a_2,b_2)=((r^2+1)^2,(r^2-4r+1)^2).
```

If `R=AS+T`, a complete deleted-pair pencil exists only if one pairing has

```text
4b_jT=a_jS^2,       y=4b_j/a_j-2,
y notin {2,-2},       y_(m+1)=y_m^2-2,       y_38=2.
```

The final exact condition is that `S/(1+q)` be a nonzero polynomial square,
where `q` is either root of `X^2-yX+1`; the verdict is independent of the
reciprocal root choice. Conversely these tests reconstruct the Mobius match
and square pencil. Thus only three one-variable certifiers in `r` remain for
this sublocus, but their uniform rejection is not yet proved.

There is no need even to choose a root `q` for the final polynomial verdict.
Put `chi=r+r^(-1)` and

```text
h_0=1/(2(chi-1)),
h_1=(chi-2)/(2(chi+2)),
h_2=chi/(2(chi-4)).
```

The three scalar identities are exactly `T=(h_jS)^2`. On any selected
branch, the condition that `S/(1+q)` be a square is equivalent to `T=W^4`
for a nonzero degree-`M-1` polynomial `W`. Thus the exact final classifier is
three cleared scalar identities, three length-38 trace gates, and one common
fourth-power test; it contains no outer-ratio root or root-dependent square
test. Uniform failure of this classifier remains open.

Its first exact rejection is only one scalar coefficient. Reverse `A,R` at
degrees `4M-1,6M-3` and put

```text
sigma=[z^(2M-2)](R_rev/A_rev mod z^(2M-1))=S(0).
```

The three branches respectively require

```text
t sigma^2+4(chi-1)^2=0,
t(chi-2)^2sigma^2+4(chi+2)^2=0,
t chi^2sigma^2+4(chi-4)^2=0.
```

These equations can reject before a full Euclidean remainder, gcd, or
fourth-power test. A compressed official-scale formula for `sigma` and a
uniform nonvanishing argument remain open.

The ODE supplies one more exact rejection gate. With

```text
P=2N+kappa x^2U_0^3,
```

the Euclidean residual obeys

```text
2xD_0R'=P+2(ND_0-xD_0')R.
```

If `T=W^4` on any passing scalar branch, then `W|P`; consequently
`S|P^2` and `deg gcd(S,P)>=M-1`. This half-degree gcd condition can be
checked before constructing a fourth root. It is necessary only, and no
uniform upper bound contradicting it has yet been proved.

The primitive cyclotomic resultant of the corresponding balanced two-zero
signed coloring has a Parseval bound. It forces `p<4N^2` when `p=1 mod N`
and `p<2N` when `p=-1 mod N`, for `N=8M=2^38`. The official prime field is
larger than the first bound, and Frobenius doubles the zero block in the
nonsplit quadratic field, whose budget lower bound exceeds the second.
Therefore complete deleted-pair survivors are impossible in both branches;
only `q=p^2`, `p=1 mod 2^40` remains for this sublocus. In that branch the
two root-cell factors, `B_0,C_0,lambda,mu`, all four outer roots, and the
Möbius matching descend to `F_p`; only the full evaluation domain can remain
genuinely quadratic.

The generic boundary now has a complete canonical certifier. Let

```text
Q=(1-z^d)/E,
R=Q-B^4,
Rbar=z^(-2h)R,
alpha=Rbar(0),
Cbar=P mod z^h.
```

After the two terminal coefficients of `P` vanish, `Cbar` has degree `h-3`.
Define

```text
S=Rbar-alpha B^2Cbar^2,
X=z^hBCbar^3,
Y=z^(2h)Cbar^4.
```

The complete norm equation is equivalent to the exact polynomial identity

```text
S=beta X+gamma Y,
```

together with splitting of `W^4+alpha W^2+beta W+gamma` into four distinct
centered parameters that are fractionally-linearly matched to square-root
lifts of the deleted roots. The coefficients are unique:
`beta=[z^h]S` and `gamma=[z^(2h)](S-beta X)`. Thus four subgroup roots
determine both pencil directions and all outer coefficients; checking only a
prefix of the span identity is insufficient.

The lowest intermediate stratum has a parallel Hensel certifier. Here

```text
h=(2^37+1)/3,       deg V=2h-2,
Rbar=z^(-3h)((1-z^d)/E-B^4),
theta=Rbar(0),      H=Rbar/(theta B),
C_*=H^(1/3).
```

Set

```text
Delta=[z^(h-1)]C_*^2/B,
kappa=[z^(2h-1)]C_*.
```

For each outer ratio `u` there is a unique normalized formal solution

```text
H=C_u^3(1+u z^h C_u/B),
C_u=C_*-(u/3)z^hC_*^2/B mod z^(2h).
```

The degree bound gives `3kappa-uDelta=0`. Therefore `Delta!=0` fixes the
unique candidate `u=3kappa/Delta`; `Delta=0,kappa!=0` rejects immediately;
only `Delta=kappa=0` retains one scalar. Surviving candidates must be exact
polynomials of degree at most `2h-2`, satisfy the multiplied identity, and
pass the distinct split/Möbius check for `W^4+theta W+theta u`.

The centered pure-quartic parameter stratum is sharper. Writing `e_j` for the
elementary symmetric functions of the centered pencil parameters,

```text
e_2=e_3=0       ==>       deg V=r-1=2^37-2.
```

A second-derivative Wronskian retains two orders from each fourth-power root
and the `d-2` binomial contact at zero. Its lower and upper degree bounds force
the displayed equality. In fact it factors exactly as

```text
A'B''-A''B'=Y^(d-2)U^2V^2L,       deg L=1.
```

Thus this special outer-parameter locus has only the codimension-one degree
gap and one linear differential residual. Both `U,V` are squarefree, and at
most one root of `UV` lies in `Z(D) union {0}`; its existence remains open.

The Möbius weld further forces the pure deleted-root lifts to be harmonic.
After relabeling and common scaling, write the four lifts as `1,x,y,w` in the
order-`2d` subgroup. Then

```text
w=(2x-y(1+x))/(1+x-2y),
```

the denominator is nonzero, and all four squares must remain distinct. The
polynomial content is exactly the coprime Fermat decomposition

```text
Q=(1-z^d)/E=B^4+Z^4,
B(0)=1,       ord_0Z=1,       deg B,deg Z<=r.
```

Conversely, a harmonic lift quadruple and this decomposition reconstruct the
pure pencil and locator relations. Harmonicity alone is not empty over finite
two-power subgroups; official work must exclude the matched Fermat
decomposition while retaining the squarefree and linear-Wronskian constraints.

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
