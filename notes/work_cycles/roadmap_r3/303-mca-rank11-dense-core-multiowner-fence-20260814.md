# Cycle 303: MCA rank-11 dense-core multi-owner fence (2026-08-14)

Cycle 302 isolated the first unpaid KoalaBear MCA stratum at error rank
eleven. Upstream PR `#1168` forces any over-budget line into a local terminal
containing a pair with deficiency at most four and at least `200632` owned
slopes. The next proposed route was to coalesce such heavy pair groups into
one owner. This cycle tests that inference at the deployed parameters.

The new proved route-fence node
`rate_half_mca_rank11_dense_pair_core_multiowner_fence` gives an explicit
received line with twelve distinct pair types. Put `d=9`, choose twelve
degree-below-nine polynomials of affine rank nine, absorb all pairwise
collision roots into a common set `J` of size `K-9`, and multiply by the
locator of `J`. Twelve disjoint petals of size `w+8` then give twelve exact
deficiency-one pair cores of size `m-1`.

The unassigned remainder has exact size

```text
n-(K-9)-12(w+8)=238825.
```

Over the deployed sextic line field, a greedy avoidance ledger chooses one
received value per remainder coordinate so that all
`12*238825=2865900` extension slopes are distinct. The worst forbidden set
has size only `34390656 < p^6`. Each pair therefore owns `238825` exact
size-`m`, support-wise MCA-bad, post-near records with margin one. The
explanation affine rank is exactly ten and the error rank is exactly eleven.

This construction strictly satisfies the local `#1168` dense-pair terminal
for every one of twelve different owners. It therefore refutes the inference
that the terminal alone forces a unique pair, a global affine owner, or
coalescence of heavy cores. It does **not** refute rank-eleven payment or
KoalaBear safety: the total is far below `B_*`. The surviving route is an
aggregate multi-owner payment or an S/A/E chronology theorem with an
additional classification premise.

The symbolic construction is backed by a complete independent GF(29) toy:

```text
D=[28,0,1,...,12], K=5, m=6, w=1,
|J|=3, four petals of size 2, |R|=3,
12 globally distinct slopes,
explanation/error ranks = 3/4.
```

Focused verification:

```text
RATE_HALF_MCA_RANK11_DENSE_PAIR_CORE_MULTIOWNER_FENCE_PASS
  pairs=12 per_pair=238825 total=2865900 toy=12 ranks=3/4 controls=8/8
RATE_HALF_MCA_RANK11_DENSE_PAIR_CORE_MULTIOWNER_FENCE_AUDIT_PASS
  pairs=12 per_pair=238825 toy_slopes=12 controls=4/4
DAG_MANIFEST_PASS nodes=2441 edges=7252 bytes=5550943 mutations=3/3
JOINT_CROSSWALK_PASS rows=103 identical=12 pins=052061e85/93fba1be
CRITICAL_HARNESS_COVERAGE_PASS proved=167 local=63 no_artifact=0
RUN_ALL_VERIFIERS total=2 failures=0
```

No Modal computation was used. All work was exact and ran under RAMguard.
The result is separated into statement, proof, contract, dependency sub-DAG,
primary verifier, and independently written audit rather than appended to a
large campaign file.

```text
start:                   93ff0bd46
DAG delta:               +1 PROVED route-fence node, +1 requirement edge,
                         +1 evidence edge
critical status delta:   none
upstream terminal delta: single-owner/coalescence inference rejected;
                         aggregate multi-owner/chronology route remains
delta-star movement:     none
compute:                 exact local arithmetic only; no Modal spend
next route action:       formulate the common-core/petal spread alternative
                         and test whether existing S/A/E routing pays it
                         before seeking a new rank-eleven theorem
```
