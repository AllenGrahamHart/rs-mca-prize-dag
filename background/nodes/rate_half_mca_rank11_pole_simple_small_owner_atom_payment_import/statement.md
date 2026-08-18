# Pole-simple small-owner atom payment

- **status:** PROVED
- **source:** upstream `experimental/grande_finale.tex`,
  `thm:owner-localization` and `cor:small-owner`, pinned at `93fba1be3`
- **scope:** one coherent official KoalaBear pole-simple scalar-locator atom

Let `I` be a set of records certified by one atom

```text
Qh_i+(c_0+c_1 gamma_i)Lambda_i=A+gamma_iB,
```

with every displayed scalar nonzero, `deg Q<=67472`, and every domain root
of `Q` contained in at most one selected support. Let `P` be the domain-root
set of `Q`, `rho=|P|`, and on `D\P` define the rational owner line

```text
r_tilde=(A/Q,B/Q).
```

Let `G` be the coordinates where the received line equals this owner and put
`g=|G|`. Then:

```text
g<m:             |I|<=n-m+1=981105,                 (OP1)
m<=g<=2m-K:      |I|<=n=2097152.                    (OP2)
```

In particular, an atom carrying more than `n` records has

```text
g>=2m-K+1=1183521.                                  (OP3)
```

The pole-simple adaptation is exact: at most `rho` supports touch `P`; after
puncturing `P`, upstream owner localization and its small-owner payment apply,
and adding those `rho` records cancels the loss in punctured domain length.

This theorem does not prove the upstream exclusive large-owner image bound
for `g>2m-K`.

## Falsifier

More support records touching denominator roots than `rho`; failure of owner
localization after puncturing; an incorrect telescoping charge; a coherent
atom with `g<=1183520` and more than `2097152` records; or use of the result
when a zero scalar has not been separated.
