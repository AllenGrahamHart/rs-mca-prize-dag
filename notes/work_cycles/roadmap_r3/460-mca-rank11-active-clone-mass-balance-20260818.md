# Cycle 460: rank-eleven active clone mass balance

## Starting pins

```text
our SHA: c029d4d3c
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
upstream rich-flat tip: PR #1173 at 2788d5ec3
```

Canonical prize and the complete open upstream PR list were rechecked before
this cycle. PR #1173 still terminates at factor-flag synchronization, while
the local branch has already reached the residual clone/line split.

## Result: PROVED active-mass strengthening

The original clone/line theorem allowed the large projective clone to be an
inactive feature of the ambient residual code. Let `mu_D` be the complete
first-owned mass of residual classes in the common evaluation hyperplane of
clone class `D`. At cutoff 10,000, the small active classes cost at most

```text
R_8*T_clone=4088807947303996*18531303013296.
```

After also bounding every genuine rank-two triple by `L-1`, the weighted
incidence remaining on active large clones is

```text
J=90044230978447536156470456344.
```

Since all clone triples together number at most `C(1116048,3)`, exact
integer balancing at

```text
L=M=388650911452
```

forces either:

```text
an active projective clone with size >=10001 and mass >=M,
or a genuine rank-two triple with mass >=L.
```

The one-sided `777301822903` rank-two bound remains valid when every clone
class is small.

## Burn-down

```text
critical target attacked: rate_half_band_crossing_location
DAG delta: strengthened one background PROVED node; no status change
route delta: large clone -> active large clone with owner-preserving mass
new assumptions: none
next action: divide the active clone hyperplane by its squarefree locator
```

## Replay

```text
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_factor_flag_clone_line_dichotomy/verify.py
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_factor_flag_clone_line_dichotomy/verify.py --tamper-selftest
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_factor_flag_clone_line_dichotomy/verify_audit.py
```
