# KoalaBear positive 433-1a cell-5 signed-pair primitive residue ledger

- **status:** PROVED
- **scope:** deployed characteristic, generic `t`, cell 5, signs
  `(-1,-1)`, chart 2, guard-localized squared `DE+/DE-` pair
- **consumer:** source-guard and colored-edge norm ledger

Let `A_g` and `ell=x1+2*x0+3*b` be as in the generic-reducedness theorem.
The exact degree-24 primitive polynomial `chi(s)` factors over
`K=F_2130706433(t)` as

```text
chi = phi_1*phi_2*phi_3*phi_4*phi_5,
(deg phi_1,...,deg phi_5) = (4,4,4,8,4),
```

where every `phi_j` is monic and irreducible and every multiplicity is one.
Consequently

```text
A_g ~= product_j K[s]/(phi_j).                  (KBRL-1)
```

Thus the generic squared signed-pair algebra has exactly five residue-field
components: four of degree four and one of degree eight.  Since `chi` is
separable, it has 24 distinct geometric points after algebraic closure.

This does not lift the squared variables to source roots or count source
configurations, classify exceptional `t` fibers, impose source nonzero or
distinctness guards, append the colored `BE` edge, cover charts 3--5 or the
`DF` family, delete cell 5 or `433-1a -> O0b`, close K3, or prove either
Prize result.

## Falsifier

Failure of the exact Krylov relation, exact factor product, monicity,
irreducibility, multiplicity-one ledger, or Chinese-remainder conclusion.
