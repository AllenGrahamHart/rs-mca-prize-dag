# Proof: aligned common-pencil emptiness

## 1. The multiplier degree gate

An LS6 locator `D` is monic of degree `j=2ell-a` and satisfies

```text
deg rem_M(D Etilde)<=s=ell-a,       deg M=2ell.       (1)
```

The multiplier is a unit modulo `M`, hence it is nonzero. If
`e=deg Etilde<a`, then

```text
deg(D Etilde)=2ell-a+e<2ell.
```

No reduction modulo `M` occurs, so the remainder in `(1)` is `D Etilde`
itself. But

```text
deg(D Etilde)>=2ell-a>ell-a=s,
```

contradicting `(1)`. Thus nonemptiness implies `(CP1)`.

## 2. The aligned common pencil

Affine normalization of the labels in `(CP2)` sends them to

```text
(0,1,lambda),       lambda=(z_3-z_1)/(z_2-z_1).       (2)
```

Put `e_0=(z_2-z_1)^(-1)`. Modulo `L_2=P-z_2`, one has

```text
e_0 L_1=e_0(P-z_1)=1.
```

Modulo `L_3=P-z_3`, equation `(2)` gives

```text
e_0 L_1=(z_3-z_1)/(z_2-z_1)=lambda.
```

These are exactly the two CRT residues that characterize `Etilde` in the
complement-slice theorem. Both `e_0` and `Etilde` have degree below
`deg(L_2L_3)=2ell`, so uniqueness of the CRT representative gives
`Etilde=e_0`. Its degree is zero, while the tail has `a>=1`; the multiplier
gate makes the atom empty. QED.
