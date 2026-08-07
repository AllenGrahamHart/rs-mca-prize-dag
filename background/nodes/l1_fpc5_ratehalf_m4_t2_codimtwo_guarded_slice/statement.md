# Rate-half FPC5 codimension-two guarded slice

- **status:** PROVED
- **consumer:** `l1_fpc5_ratehalf_m4_t2_payment`

Consider the official rate-half row `k=2^40`, a maximal sunflower source with
`M=4`, and an `M=4,t=2` full-petal cell. Write

```text
d=ell+s,       c_petal=ell-s-1.
```

If the unguarded two-petal locator slice has `c_petal=2`, then necessarily

```text
5ell=k+4,
b=r=s=ell-3,
d=2ell-3.                                             (GS1)
```

Let `L_0` be the degree-`ell-3` locator of the whole unused background, let
`L_1,L_2` be the degree-`ell` touched-petal locators, and let their planted
labels `c_1,c_2` be distinct and nonzero. Every contributor lies in

```text
L_0 | W,
L_i | W-c_iF       for i=1,2,
deg F,deg W<=2ell-3.                                  (GS2)
```

Put `A_i=(W-c_iF)/L_i`. Then `deg A_i<=ell-3`, and (GS2) is equivalent to

```text
c_2 L_1 A_1 == c_1 L_2 A_2       (mod L_0),           (GS3)

G=(c_2L_1A_1-c_1L_2A_2)/((c_2-c_1)L_0),
W=L_0G,
F=(W-L_1A_1)/c_1.                                    (GS4)
```

The congruence map in (GS3) is surjective onto `K[X]/(L_0)`. Consequently
the guarded `(F,W)` slice and its projection to the locator `F` both have
dimension

```text
2(ell-2)-(ell-3)=ell-1.                               (GS5)
```

Since the degree-`<=d` locator space has dimension `2ell-2`, the true guarded
locator codimension is also

```text
(2ell-2)-(ell-1)=ell-1.                               (GS6)
```

Thus the apparent petal-equation codimension-two endpoint is not a
codimension-two full PMA cell. Its forced full-background agreement supplies
`ell-3` additional independent equations.

## Scope

This theorem gives the exact linear envelope after imposing the two touched
petals and all forced background roots. A contributor must additionally have
`F` monic and split on the source core, satisfy the primitive and exact
nonagreement guards, and retain first ownership. The theorem does not count
that remaining locus.
