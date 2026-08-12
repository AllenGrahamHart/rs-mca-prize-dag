# Codeword-direction gauge rank router

- **status:** PROVED
- **closure:** field-general equivalence and exact deployed rank walls
- **scope:** any support-wise MCA-bad selected explanation family

## Gauge equivalence

For any codeword `b in C`, replace

```text
(r_0,r_1,c_gamma) by (r_0,r_1-b,c_gamma-gamma b).     (G1)
```

This preserves every slope, exact agreement support, and same-support pair
noncontainment.  If `r_c` and `r_b` are the affine dimensions of the original
and transformed selected explanations, then

```text
|r_c-r_b|<=1.                                         (G2)
```

In a shortened row `(R+K,K,d+K)`, a transformed rank-`r` family is bounded
by

```text
A_(K,r)=floor(max(
  (R+K)^(falling r+1)/((d+K)d^(rising r)),
  (R+r)^(falling r+1)/d^(rising r+1))).              (G3)
```

The exact official ambient-dimension walls are pinned in the contract.  In
particular:

```text
KoalaBear:   r<=11 paid for every K<=1048576;
             r=12 through K=745260;
             r=13 through K=289603;
             r>=14 not paid uniformly by (G3).
Mersenne-31: r<=4 paid for every K<=1048576;
             r=5 through K=482472;
             r>=6 not paid uniformly by (G3).
```

Thus choosing a minimum-lift codeword `b` in the direction-distance route
also creates a rank-one gauge test.  A surviving family must lie beyond the
appropriate transformed-rank wall.

## Nonclaims

This does not force a rank drop, pay a family beyond `(G3)`, control the
remaining direction defect, or close a deployed or prize row.

## Falsifier

A changed witness support or containment status under `(G1)`, a rank change
larger than one, a violation of `(G3)`, or an incorrect adjacent rank wall.
