# KoalaBear positive 433-1a cell-5 signed-pair primitive coordinate map

- **status:** PROVED
- **scope:** deployed characteristic, generic `t`, cell 5, signs
  `(-1,-1)`, chart 2, guard-localized squared `DE+/DE-` pair
- **consumer:** source-guard and colored-edge norm ledger

Let `K=F_2130706433(t)`, let `A_g` be the generic guard-localized squared
signed-pair algebra, and put `s=ell=x1+2*x0+3*b`.  In the primitive
presentation

```text
A_g ~= K[s]/(chi(s)),
```

there are explicit, certificate-backed polynomials

```text
p_x1(s), p_x0(s), p_b(s) in K[s],  degree_s < 24,
```

such that

```text
x1 = p_x1(s),   x0 = p_x0(s),   b = p_b(s).             (KBCM-1)
```

Their 72 rational-function coefficients are recorded exactly.  They obey

```text
p_x1(s) + 2*p_x0(s) + 3*p_b(s) = s                    (KBCM-2)
```

coefficientwise over `K`.  Hence every polynomial or rational invariant in
`b,x0,x1` can now be restricted explicitly to each of the five residue
fields in the primitive residue ledger.

This does not prove that any source square, nonzero, collision, or chart
guard is a unit; compute a guard norm; classify exceptional `t` fibers;
lift squared points to source roots; append the colored `BE` edge; cover
other charts or the `DF` family; delete cell 5 or `433-1a -> O0b`; close
K3; or prove either Prize result.

## Falsifier

Failure of exact Krylov reconstruction, any missing map coefficient, failure
of (KBCM-2), or disagreement with the independently generated multiplication
columns at a regular fiber.
