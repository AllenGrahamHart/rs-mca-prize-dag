# Proof

## Factor-lifting theorem

The complete proof of the RF3-double-prime integer core theorem is vendored in
`upstream_bridge.md`. It factors the interpolant over `F[X,Z][Y]`, pays global
and specialized contents separately, guards discriminants and leading
coefficients at a common regular specialization, repairs the nonlinear
coefficient recurrence, and handles factors linear in `Y` directly. It proves

```text
|S| > (1+2Ud^2)G + (r+1)d
```

implies a retained linear factor whose two endpoint polynomials explain both
received coordinates on one of the originally chosen agreement supports.
The chosen-support conclusion is part of the theorem, rather than an
untracked transport after factor lifting.

The proof was independently re-derived in `upstream_ordinary_audit.md`. That
audit confirms the factor/content ledger, both local recurrences, all boundary
cases, the final pair sum, the chosen-support incidence argument, the Paving
parameter map, and the four exact ceilings. The two vendored artifacts are
hash-pinned by `verify.py`.

## From RF3-double-prime to an MCA upper bound

Use the retained-degree interpolation box with parameters `U,V,W,m`. Its
coefficient count is

```text
sum_(j=0)^(V-1) (U-Kj)(W-j),
```

while multiplicity-`m` interpolation on all `n` coordinates imposes at most

```text
n sum_(s=0)^(m-1) (W-s)(m-s)
```

homogeneous linear conditions. The strict RF4 inequality therefore supplies
a nonzero interpolant `Q`.

For every MCA-bad slope, choose an exact `A`-point witness support and its
degree-below-`K` explaining polynomial. Multiplicity gives at least `mA`
zeros after substitution into `Q`, while the substituted polynomial has
degree below `D_X<mA`; it vanishes identically. If the bad-slope count were
larger than

```text
ceil((1+2U D_Y^2)D_Z + (r+1)D_Y),
```

the RF3-double-prime theorem would explain both received coordinates on one
chosen support. This contradicts support-wise MCA nontriviality. Hence the
ceiling is a valid numerator upper bound.

## Four exact rows

Set `p=2^31-2^24+1`. The identity `p-1=127*2^24`, together with
`3^((p-1)/2)=-1 mod p`, is a Proth certificate, so `p` is prime. Since
`2^21` divides `p-1`, the required evaluation subgroup exists in `F_p^*`.

For each row, `verify.py` checks with exact rational arithmetic:

- all RF1 and RF2 inequalities;
- the strict RF4 interpolation count;
- the RF3-double-prime ceiling;
- `q=p^6` and `B*=floor(q/2^128)`;
- the displayed agreement/radius conversion; and
- `R''<=B*` with the four exact positive margins.

Thus each displayed agreement is safe. The proof supplies no lower packet at
the preceding agreement, so the compiler must not emit an adjacent crossing
or a maximal radius from this node alone.
