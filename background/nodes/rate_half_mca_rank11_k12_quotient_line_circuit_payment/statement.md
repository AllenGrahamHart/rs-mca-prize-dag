# Quotient-line circuits and rank-nine shadows pay K'=12

- **status:** PROVED
- **closed residual row:** `K'=12`
- **units:** `(record, eleven-subset)` component incidences

At `K'=12`, put

```text
n'=1048588,       m'=67484,       dim V'=10<=dim P_12=12.
```

Rank-deficient component eleven-sets have absolute capacity

```text
K_cap=C(n',9)*16295594
     =68823412552626461731638254358120971630939282959681665560.
```

For full-rank eleven-sets, split the unique quotient-line circuit by support
size.  Circuits of size at least six create at least 45 rank-nine
nine-shadows.  The common-core offset theorem gives the uniform rank-nine
chart cap

```text
C_*=9276963034268184,
```

so all high-circuit incidences have capacity

```text
H_cap=floor(C(n',9)C_*/45)
     =870681505337379475658181372289433062059140012353857046633355381.
```

The codimension-two quotient-line theorem gives per-record low-circuit cap

```text
L_*=11868577829520852215896202871552159662636920.
```

For `R_actual` residual records, every component incidence therefore obeys

```text
I_component <=K_cap+H_cap+R_actual L_*.             (K12C)
```

At the proved record floor `R_actual=N_min=274980728111260126`, the right
side is

```text
873945204333998831582903951502910514268526233054054867526472861,
```

while dense-locator incidence requires

```text
901555241262544083284435178226046105523688795046262319915891531.
```

The demand exceeds capacity by

```text
27610036928545251701531226723135591255162561992207452389418670.
```

The gap increases with `R_actual`.  Hence the complete positive-dimensional
component target is empty at `K'=12`, and the remaining rank-nine interval
is `13<=K'<=15528`.

## Falsifier

A rank-deficient incidence above `K_cap`; a rank-nine chart above `C_*`; a
circuit of size at least six with fewer than 45 rank-nine shadows; a
recordwise support-at-most-five count above `L_*`; failure of the exact
comparison; or a nonpositive record coefficient.
