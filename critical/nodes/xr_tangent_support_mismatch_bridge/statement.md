# XR tangent/support-mismatch bridge

- **status:** TARGET
- **scope:** the six `(RowC, prize) x (1/4,1/8,1/16)` candidates

## Statement

For every received pair `(u,v)` at an official clean-rate candidate, the XR
first-match decomposition is support-wise sound. After the proved quotient
column is removed, its support-wise MCA-bad slopes admit a disjoint split
into:

1. a genuine tangent column containing at most `n-A` slopes; and
2. a retained residual.

The first item is now proved by `xr_true_tangent_coordinate_injection`:
when the explaining codeword is exactly `c_0+z c_1`, each bad slope injects
into a discrepancy coordinate. No deep hypothesis is needed for this branch.

Every support-mismatch slope must be retained unless its actual witness is
paid by that injection. This includes slopes that remain MCA-bad even
though the pair has a joint codeword-pair explanation on another support,
and slopes diverted by a graded common-core classification without a proved
support-wise payment.

Every remaining witness has a nonzero difference codeword
`q_z=p_z-(c_0+z c_1)`. The proved
`xr_tangent_mismatch_external_zero_factor_reduction` factors the witness
zeros outside the discrepancy set and places it in a punctured GRS chart of
dimension `K-d`, agreement `A-d`, and invariant excess `A-K`. The open
content no longer includes witness-subset spray:
`xr_tangent_mismatch_full_external_zero_canonicalization` uses all external
zeros of the selected difference codeword and gives one chart per selected
slope/codeword pair.

On a generic fixed chart, `xr_generic_mds_kernel_ray_bound` applies. The
proved `xr_mismatch_chart_nongeneric_joint_support_equivalence` identifies
failure of that genericity exactly with a distinct joint codeword-pair
explanation on an `A`-support extending the chart zero core. Supports for
distinct joint explanations intersect in at most `K-1` coordinates. The
proved `xr_mismatch_nongeneric_invariant_excess_descent` shows that following
such an explanation preserves `h=A-K`, reduces ambient length by at least
`h+1`, and terminates in fewer than `256/512` transitions at every clean
candidate.

The terminal breadth is now paid. At any live instance put `H=h+1`. Distinct
joint explanations have canonical `A`-supports of size `A=K+h`, pairwise
intersection at most `K-1=A-H`, and hence Hamming distance at least `2H`.
The proved `xr_nongeneric_explanation_plotkin_width` gives at most `2N`
explanations when `N<=4H` and polynomially many throughout every window

```text
N-4H<=C log_2 n.
```

Once a canonical descent enters `N<=4H`, its whole live nongeneric subtree
has at most `1+104H` instances, and all genuine-tangent charges in that
subtree cost at most `420H^2<16n^3` at every official candidate. Thus
terminal explanation-support breadth is no longer open. Generic canonical
chart slopes and pre-terminal slope-to-explanation fibers remain open.

The same conclusion holds polynomially for a whole fixed logarithmic window.
If `N-4H<=C log_2 n` and `H>=2C log_2 n`, the live nongeneric subtree has at
most `1+200n^(C+1)` instances and at most `201n^(C+2)` genuine-tangent
charges. Thus pre-terminal means outside every such fixed logarithmic window,
not merely above the equality boundary.

The remaining red therefore has two exact bounded-depth currencies:

1. distinct slopes across the union of generic canonical charts; and
2. slopes per joint explanation before the paid terminal window, aggregated
   over this low-core support family.

For a pair outside the original generic scope of
`xr_highcore_collision_count` and `xr_lowcore_spread_heart`, the retained
residual has size at most `16n^3`. For a generic pair, the bridge preserves
the high/low-core first-match partition without increasing either `8n^3`
allocation. Consequently the bridge and `xr_smallcore_spread_count` together
give, for every pair,

```text
#bad slopes <= B_quot_ub(A) + (n-A) + 16n^3.
```

This statement is an official-row theorem target. It is not supplied by the
deep tangent theorem, whose hypothesis `3(n-A)<=n-K` fails at all six
candidates.
