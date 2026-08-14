# Rank-eleven absorbing clone-to-affine collapse

- **status:** PROVED
- **scope:** a positive-dimensional polynomial clone component emitted by
  the relative correction ten-flat router
- **input:** the correction space `W` contains every high core coefficient
  `H_j`, `j>=2`

Let `s=dim W`, let `T` be an `s+1` coordinate nonproper tuple whose
evaluation rank on `W` is `s`, and choose an evaluation basis `B subset T`.
The basis equations define the unique polynomial correction curve

```text
P_B(Z)=sum_(j=0)^31 P_(B,j) Z^j in W tensor F[Z].
```

Then

```text
P_(B,j)=-H_j for every j>=2.
```

Consequently `H(X,Z)+P_B(X,Z)` has slope degree at most one and is one
global affine codeword owner line. The clone component contains at most

```text
n'-m'+1=R-d+1=981105
```

rich slopes.

Thus no genuinely nonlinear high-core-absorbing polynomial clone component
survives. The relative component frontier consists of evaluation rank-flats
plus the aggregation/chronology problem for the resulting affine owner
lines. This theorem does not sum many different affine owners.

## Falsifier

A high coefficient outside `W`; noninjective evaluation on the declared
basis; a coefficient `P_(B,j)+H_j` nonzero despite vanishing on the basis; a
clone curve retaining slope degree at least two; or more than `981105`
slopes on one affine owner line.
