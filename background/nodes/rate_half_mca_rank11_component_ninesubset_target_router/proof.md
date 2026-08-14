# Proof

Apply the nine-subset lane concentrator and fix its dominant lane, its
nine-subset `B`, and its population `G>=2578110`.

## Kernel lane

If the dominant lane is rank-deficient, every retained record has an
eleven-subset `T` containing `B` with `rank(ev_T)<=9`. Restriction to `B`
cannot increase rank, so `rank(ev_B)<=9`. Moreover

```text
ker(ev_T) subset ker(ev_B),
```

and every retained component is attached to this one fixed nonzero kernel
chart. This is route 1.

## Affine-owner lane

Suppose the dominant lane is affine-owner. Every retained record has an
eleven-subset `T` containing `B` with `rank(ev_T)=10`, and the component
supplies an actual owner pair agreeing with the received pair on `T`.
Deleting the two coordinates `T minus B` can lower rank by at most two,
while nine coordinates have rank at most nine. Hence

```text
rank(ev_B) in {8,9}.                                (1)
```

If the rank is nine, all owner pairs agreeing on `B` form one affine plane.
Every retained record has a nonempty owner line in that plane. Lift the
plane, its owner lines, and the exact supports through the reversible
line-global common-core cancellation adapter. The record population and
the nine residual coordinates are unchanged, while the deleted coordinates
enter every lifted owner core. The nine-cell pair-core extension gives the
low-core cap 1434405, while

```text
G>=2578110>1434405.
```

The complete plane therefore shares at least 134944 received coordinate
pairs. This is route 2.

Assume instead that `rank(ev_B)=8` and put `U=ker(ev_B)`, so `dim U=2`.
Choose one retained owner pair `(A_*,B_*)`. Every other selected owner pair
has the form

```text
(A_gamma,B_gamma)=(A_*,B_*)+(alpha_gamma,beta_gamma),
(alpha_gamma,beta_gamma) in U^2.
```

Because it owns the selected explanation at slope `gamma`,

```text
h_gamma=A_*+gamma B_*+v_gamma,
v_gamma=alpha_gamma+gamma beta_gamma in U.
```

Thus the selected error is

```text
e_gamma=(r_0-A_*)+gamma(r_1-B_*)-v_gamma.
```

After anchoring one slope, all error differences lie in
`span(U,r_1-B_*)`, of dimension at most three. This proves route 3 and
exhausts (1). Exact locator multiplication in the reverse common-core lift
is injective, so it preserves this error-difference rank.
