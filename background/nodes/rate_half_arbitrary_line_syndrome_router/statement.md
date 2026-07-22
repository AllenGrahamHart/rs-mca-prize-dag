# Arbitrary received-line syndrome router

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **role:** exact finite attack model for the non-polynomial received-line flank

Let `C` be a linear code with parity-check matrix `H`, and write `V_E` for
the span of the columns of `H` indexed by `E`. Fix agreement `a=n-r` and a
received pair with syndromes `(s_0,s_1)`. A finite slope `gamma` is
support-wise MCA-bad at agreement at least `a` if and only if there is a set
`E` with `|E|<=r` such that

```text
s_0+gamma s_1 in V_E,
not (s_0 in V_E and s_1 in V_E).                     (SL1)
```

Consequently exhaustive search over all syndrome pairs is exhaustive over
all received lines modulo `C^2`; no polynomial received-word ansatz is
needed. Code translation and changing representatives of either syndrome do
not change the bad-slope set.

For the rate-half MDS toy row `(q,n,k,a)=(7,6,3,4)`, take a Vandermonde
parity-check matrix with columns `(1,x,x^2)` for `x in F_7^*`. The pair

```text
s_0=(0,1,0),       s_1=(0,0,1)                       (SL2)
```

satisfies `(SL1)` at every finite slope. Thus it has seven bad slopes while
the universal tangent baseline is only `r+1=3`. This saturation has an
explicit moving-secant presentation. For each `gamma`, choose distinct
nonzero `x_gamma,y_gamma` with `x_gamma+y_gamma=gamma`; then

```text
(0,1,gamma)
  =(x_gamma-y_gamma)^(-1)
    ((1,x_gamma,x_gamma^2)-(1,y_gamma,y_gamma^2)).    (SL3)
```

Hence the slope syndrome lies in the two-column span indexed by
`{x_gamma,y_gamma}`. The two individual syndromes cannot both lie in that
span.

This toy witness is a falsification lead, not an official-row witness. No
lifting theorem from `(SL2)` to the order-`2^41` prize domain is claimed.
The existing `rh_band_witness_census_modal.py` searches special zero-sum and
polynomial locator fibers, so it cannot adjudicate this arbitrary-line
flank.
