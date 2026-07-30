# Proof

## 1. The partition-preserving case is impossible

The parent diagonal fiber compiler supplies a fixed-point-free permutation
of the twelve source labels, induced by the endpoint deck involution `tau`,
and the whole-fiber transport identity

```text
[R_tau(y)]=[tau^* R_y].                             (1)
```

For every `k in K`, all four roots of `R_k` lie in `J`. Suppose for a
contradiction that `tau(I)=I`. Then `tau(J)=J`. The restriction of `tau` to
the six-set `I` is a fixed-point-free matching. Since `K` has odd size five,
the remaining label `xi in I minus K` must be paired with some `k in K`.

Transporting `R_k` by `(1)` shows that all four roots of `R_xi` lie in `J`.
There are two possibilities.

- If `xi in L`, then `K subset I intersect L` and both `I,L` have size six,
  so `L=I` and `xi=eta`. The exact `eta` facet supports `R_xi` entirely on
  `I`, disjoint from `J`.
- If `xi notin L`, then `xi in L^c`. The two quadratic factors of `R_xi`
  lie in the two one-exchange facets above `xi`. Each such facet contains
  only one `J` label. The outgoing facet is a reduced six-label divisor, so
  a quadratic component factor can use that label at most once. The quartic
  therefore has at most two `J` roots, counted with multiplicity.

Both alternatives contradict the four transported `J` roots. This proves
`(KBDM-1)`.

## 2. Orbit census

Let `c` be the number of labels of `I` paired by `tau` with labels of `J`.
The same number of labels crosses in the other direction, proving the first
equality in `(KBDM-2)`. The remaining `6-c` labels of `I` are paired among
themselves, so `6-c` is even. Section 1 excludes `c=0`; hence
`c in {2,4,6}` and `|I intersect tau(I)|=6-c`.

Let `a` count matching edges contained in `K`, and let `b` record the
possible edge from `xi` to `K`. The noncrossing labels of `I` are exactly
the endpoints of those `a+b` edges. Therefore

```text
6-c=2a+2b,       c=6-2a-2b.                       (2)
```

Here `0<=a<=2`, `b in {0,1}`, and `2a+b<=5`. Removing `c=0` from the
solutions of `(2)` leaves exactly the five rows in `(KBDM-3)`.

## 3. Transported root supports

Every root of `R_k` lies in `J`. Because `tau` is an involution, a root
`u in J` has `tau(u) in J` exactly when `u in J_0`, and has
`tau(u) in I` exactly when `u in J_1`.

If `tau(k) in K`, all four roots of `R_tau(k)` lie in `J`. Identity `(1)`
therefore forces all roots of `R_k` into `J_0`. If `tau(k)=eta`, all four
roots of the transported quartic lie in `I`, forcing all roots of `R_k`
into `J_1`.

Finally suppose `tau(k) in L^c`. The transported quartic is the product of
the two component stars in the paired one-exchange facets. Each facet has
only one `J` label and is reduced, so each quadratic star contains at most
one `J` root. Thus at most two of the quartic's four roots lie in `J`.
Pulling back by `tau` says that at most two roots of `R_k` lie in `J_0`,
and hence at least two lie in `J_1`. This proves `(KBDM-4)`.

## 4. The maximally mixed row

Assume `c=6`, so `tau(I)=J` and `tau(J)=I`. If `L=I`, then `eta=xi`.
The quartic `R_eta` is supported on `I`, so its transport is supported on
`J`. But `tau(eta) in J=L^c`, where a whole-fiber quartic has at most two
`J` roots. This contradiction proves `L!=I`. Hence

```text
L=K disjoint_union {eta},       eta in J,
L^c={xi} disjoint_union (J minus {eta}).            (3)
```

Now `tau(eta) in I`. It cannot equal `xi`: transporting the four `I` roots
of `R_eta` would give four `J` roots over the one-exchange label `xi`.
Therefore `tau(eta) in K`. Since `tau` is fixed-point-free, `xi` is paired
with a label

```text
ell=tau(xi) in J minus {eta} subset L^c.            (4)
```

Let `z` be the number of `J` roots of `R_xi`. The one-exchange capacity
gives `z<=2`. Since `tau` swaps `I` and `J`, the number of `J` roots of
`R_ell` is `4-z`; its one-exchange capacity gives `4-z<=2`. Thus `z=2`,
and both quartics have exactly two `J` roots. Their two reduced quadratic
stars each contain at most one `J` root, so all four stars are `I-J`.

The remaining four labels of `K` are paired with the remaining four labels
of `J minus {eta,ell}`. Their `J`-supported quartics transport to quartics
supported entirely on `I`, so every remaining `L^c` star is `I-I`. The
universal component-color theorem identifies the four `I-J` incidences with
the four simple colored roots. Consequently

```text
C_H=psi^*({xi}+{ell})                              (5)
```

as a reduced divisor. This proves `(KBDM-5)--(KBDM-6)`. The pair
`{xi,ell}` is one `tau` orbit, so its binary locator `chi` is projectively
`tau`-invariant. With the standard reciprocal lift, the two linear factors
are exchanged and their product has positive eigenvalue.

Finally write `D_K=psi^*K_5` and `D_R=psi^*R_7`. Substitution of `(5)` in
the universal colored partial-resultant identities gives

```text
Res_T(P_J,H) ~ psi^*(K_5^2 chi),
psi^*chi Res_T(P_I,H) ~ psi^*(R_7^2).              (6)
```

The right sides are deck invariant, so the left sides descend uniquely to
binary forms `Q_J,Q_I` on the `W`-line. Faithfulness of pullback by the
surjective quadratic map gives exactly `(KBDM-7)`. This uses no lift of the
diagonal automorphism to the source `X`-line, and hence applies to both
source-subfield branches.

## 5. The minimally mixed rows

Assume `c=2`, so `|J_0|=4` and `|J_1|=2`. The universal component-color
cut gives

```text
2<=d_j<=4 for every j in J,       sum_(j in J)d_j=20. (7)
```

First let `(a,b)=(2,0)`. The four labels of
`K_0=K intersect tau(K)` lie in two internal `K` orbits. By `(KBDM-4)`,
their four quartics contribute sixteen roots in `J_0`. The four labels of
`J_0` have total `K`-incidence capacity sixteen, so each has degree four
and no root of the remaining quartic `R_(k_*)` lies in `J_0`. All four of
its roots lie in the two-label set `J_1`. Each of its two quadratic stars
is reduced, hence is exactly `P_(J_1)` projectively. This proves the square
identity in `(KBDM-8)`. Equation `(7)` then forces degree two on both
labels of `J_1`. Multiplying the four `K_0` quartics gives degree sixteen
with every `J_0` root of multiplicity four, proving the product identity.

Now let `(a,b)=(1,1)`. One internal `K` orbit contributes eight roots in
`J_0`. The label `tau(xi) in K` supplies the remaining internal-I edge.

If `L=I`, then `xi=eta`, so `R_(tau(eta))` has all four roots in `J_1`.
The other two noninternal labels of `K` transport to `L^c` and contribute
at least two `J_1` roots each. Thus the two labels of `J_1` receive at least
eight `K` incidences. Their total capacity is eight, so all inequalities are
equalities: both degrees are four, the eta-paired quartic is
`P_(J_1)^2`, and each `L^c`-transported quartic has exactly two `J_1`
roots.

Suppose instead `L!=I`. Then `xi in L^c`. If `tau(eta) in K`, its quartic
contributes four `J_1` roots, while the `K` labels transported to `xi` and
to the remaining crossing label in `L^c` contribute at least two each.
The same capacity-eight argument proves `(KBDM-9)`.

Finally suppose `tau(eta) notin K`. Since `xi` is internally paired with a
label of `K`, the two labels of `I` crossing to `J` are the other two labels
of `K`. Hence a `J` label is crossing exactly when it is paired to one of
those labels. The hypothesis therefore puts both `eta` and `tau(eta)` in
`J_0`. The three non-`K` destinations of common-`K` labels are all in
`L^c`, and `(KBDM-4)` contributes at least two `J_1` roots from each. This
gives the lower bound six in `(KBDM-10)`; the upper bound eight is the two
row capacities from `(7)`. QED.
