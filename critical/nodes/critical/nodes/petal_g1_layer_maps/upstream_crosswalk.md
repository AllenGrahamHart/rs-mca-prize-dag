# Upstream atlas crosswalk: analogy, not a consumer bridge

Date: 2026-07-12.

## Verdict

Upstream hard input `(A2)`, including the `(CAT)/(UNIF)` terminology in PR
#706, is not an instance of local G1 as currently posed. The two programs use
the same ledger pattern, but their counted objects and payments differ.

## Shared logic

Both statements require:

1. exhaustive coverage by a finite ordered family;
2. first-match assignment to prevent duplicate charging;
3. a paid aggregate rather than constructibility alone;
4. uniformity over the received object.

This makes upstream atlas work useful methodology and terminology.

## Object mismatch

Upstream `(A2)` starts with a received line and cells in the bad-slope witness
incidence `W_a(r)`. Its first-match parts are formed after projection to the
slope coordinate `gamma`, and its payment is a bound on distinct slopes
`|Z_i^o|` at an image or direct scale.

Local G1 starts with one received word `U`. Its charts are fixed
`(D0,R0)` sunflower auxiliary layers containing listed codewords. K4 bounds
the complete full-petal codeword image in chart `chi` by `m_chi+1`, and G1's
payment is the weighted chart sum

```text
sum_chi (m_chi+1) <= (121/128)n^6.
```

There is no slope projection in this statement. Conversely, an upstream
distinct-slope payment does not count local sunflower layers or listed
codewords.

## Quantifier and scale mismatch

- upstream: asymptotic `e^{o(n)}` profiles and slope envelope, uniformly over
  received lines;
- local G1: exact finite coefficient `121/128`, uniformly over received words
  on official rows and every consumed quotient descendant;
- upstream fixed-chart A6 payments: one line and one active chart;
- local G1: all top-band full-petal contributors and quotient closure.

## Import gate

No upstream CAT, UNIF, or per-chart slope theorem may be wired to G1 without a
new proof that supplies all three maps:

1. local full-petal contributors to the upstream witness incidence;
2. upstream cells to fixed retained-zero sunflower layers with the local
   layer/scale dictionary;
3. upstream distinct-slope budgets to the local weighted codeword-layer sum.

No such map is currently known or claimed. PR #706 is therefore an audit
analogy, not evidence toward G1's numerical payment.

## Correct local attack handles

The capf sunflower interface itself identifies the live work:

- **layer catalogue:** every top-band full-petal contributor must enter a
  concrete sunflower layer for some printed `Y,P_star,D0,R0,T_i,c_i`;
- **weighted payment:** after first-match ordering, the sum of `m_chi+1` must
  fit `(121/128)n^6`;
- **quotient closure:** the same construction and coefficient must hold on
  every consumed rate-preserving descendant of length at least `256`.

These are handles inside the single G1 leaf, not new conditional DAG nodes.
