# Proof

## Saturate the exact supports

Retain the pair types `p_0,...,p_t`, `1<=t<=4`, and the same 32 distinct
owned slopes selected by the degree-24 seed. For `p=(a,b)`, its pair core
`H_p` lies in the agreement set of every owned explanation
`h_gamma=a+gamma b`.

The support re-selection is performed after pair ownership is fixed.

Support-wise pair noncontainment gives `|H_p|<m`: otherwise any `m` points
of `H_p` would simultaneously support the codeword pair `(a,b)`. Since each
owned explanation has at least `m` agreement coordinates, choose an exact
size-`m` support containing all of `H_p`. This downstream support choice
does not alter the already fixed pair owner, slope, or explanation.

If `gamma` and `eta` are distinct slopes owned by `p`, a coordinate in both
agreement sets satisfies

```text
r_0+gamma r_1=a+gamma b,
r_0+eta   r_1=a+eta   b.
```

Subtraction gives `r_1=b`, then `r_0=a`. Thus the two saturated exact
supports intersect exactly in `H_p`: inclusion of `H_p` was imposed, and
the reverse inclusion follows from these equations.

The seed takes at least two records from every `p_i`. Therefore the complete
intersection of its 32 saturated supports is

```text
C=intersection_(i=0)^t H_(p_i)=J.                    (1)
```

The parent core-recovery theorem proves `|J|<K-2`. Exact cancellation is
therefore available with residual dimension `K'=K-c>=3`. It preserves the
same degree-`24..31` nonaffine packet and the exact partial-relative
trichotomy.

## Two pair cores exceed the locator degree

For each selected pair, cancel `C` from its two components and write its
residual core as `H_p'`. Equation (1) gives `C subset H_p`, so

```text
|H_p'|=|H_p|-c>=m-c-11=m'-11.                        (2)
```

The packet contains at least two distinct pair types, `p_0` and `p_1`.
Their residual pairs remain distinct: equality after division would
multiply back to equality before cancellation. At least one component of
their difference is therefore a nonzero polynomial of degree below `K'`.
Every point in `H_(p_0)' intersection H_(p_1)'` is a root of that
polynomial, so

```text
|H_(p_0)' intersection H_(p_1)'|<=K'-1.              (3)
```

Combining (2)--(3),

```text
|H_(p_0)' union H_(p_1)'|
 >=2(m'-11)-(K'-1)
 =m'+(m'-K')-21
 =m'+67451
 >m'.                                                (4)
```

## Exclude a pure locator

Suppose the router emits a pure-locator certificate

```text
(c_0+c_1 gamma_i)Lambda_i'=A'+gamma_i B',            (5)
```

where `deg A',deg B'<=m'` and the solution is nonzero. Take the two
selected slopes from one represented pair `p`. Their saturated residual
supports both contain `H_p'`, so both locators vanish there. Evaluating (5)
at a point of `H_p'` and subtracting the two distinct-slope equations gives

```text
A'=B'=0 on H_p'.                                     (6)
```

Apply (6) to `p_0` and `p_1`. By (4), each of `A'` and `B'` has more than
`m'` distinct roots while having degree at most `m'`. Hence both are the
zero polynomial. Equation (5) then gives

```text
(c_0+c_1 gamma_i)Lambda_i'=0
```

for all 32 distinct slopes. Since every locator is nonzero, the affine
scalar vanishes at more than one slope, forcing `c_0=c_1=0`. This makes the
homogeneous solution trivial, a contradiction.

The pure-locator output is excluded. The exact router leaves only the
nontrivial rational-profile or official high-complexity output. QED.
