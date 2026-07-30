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
source-subfield branches. QED.
