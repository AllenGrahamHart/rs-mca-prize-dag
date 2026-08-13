# Proof

The residual four-cycle theorem gives

```text
Z_4=2B,       h^0(C,O_C(2B))=1.                    (1)
```

By definition, restricting `G` to the locator curve and subtracting the
mandatory first copies leaves the nonzero section cutting out `Z_4`.
Thus its residual line bundle is `O_C(2B)`, and `(1)` says this section is
the unique canonical section up to scalar.

On `C`, the locator `Q` vanishes. Restricting the exact Pade syzygy gives

```text
-Lambda G=L_U0 P_F.                                (2)
```

The regular-factor theorem removes the fixed domain-infinity contact and
the displayed center/row factors before defining the contact section.
After that same normalization, equation `(2)` identifies the `P_F` and `G`
residual restrictions. They are not two independent sections; both span the
one line in `(1)`.

It remains to test the first jets. Choose any pure split slope `delta`, whose
existence is proved with room `e+7`. Its fiber is

```text
G(delta,X)=zeta_delta A_delta(X),                  (3)
```

where `zeta_delta` is nonzero and `A_delta` has `n` distinct roots. Hence,
at each root `x`,

```text
G_X(delta,x)=zeta_delta A_delta'(x)!=0.             (4)
```

The classified-row identity also says that `G(t,x)` has `m=e-2` distinct
parameter roots. Therefore the same incidence is a simple parameter root,
and

```text
G_t(delta,x)!=0.                                   (5)
```

Every point in `(4)--(5)` is an actual-support common point of `Q` and `G`,
so one copy belongs to `D_mand`. A section descends from `O_C(G)` to
`O_C(G)(-D_mand)` only if it vanishes at every such point with the required
multiplicity. Equations `(4)--(5)` show that neither raw derivative does.
After formal division by the mandatory section, each has poles at all `n`
points of this pure fiber. This proves `(NSF3)` and the route fence. QED.
