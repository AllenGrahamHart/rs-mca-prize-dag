# Cycle 471: bounded exception split-pencil normal form

## Starting pins

```text
our SHA: c5c721ac4
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
upstream factor-synchronization tip: #1173 at 2788d5ec3
upstream split-pencil tip: #1170 at d296510e80
```

## Result: PROVED exact SPI reduction

In the pole-simple rational branch, let `H_0` be the residual anchor pair
core. Pair noncontainment and low margin give

```text
1<=e=m'-|H_0|<=11.
```

Each of at least 20 exact anchor supports is
`H_0 disjoint_union E_gamma`, where the exception sets have size `e` and
are pairwise disjoint. Writing their monic locators as
`Lambda_gamma=L_0 L_{E_gamma}`, the rational identity factors as

```text
A-Qa_0=L_0u,
B-Qb_0=L_0v,
u+gamma v=(c_0+c_1 gamma)L_(E_gamma).
```

The quotient polynomials have degree at most `e`. The affine scalar cannot
vanish on an anchor slope, since that would make every other exception
locator proportional to one fixed polynomial despite disjoint nonempty root
sets. It follows that

```text
max(deg u,deg v)=e,
gcd(u,v)=1.
```

Every exception locator is a split squarefree degree-`e` divisor of the
residual domain locator, and the locators are pairwise coprime. The
pole-simple theorem also gives `gcd(Q,L_0)=1`. Thus the rational branch is
an exact degree-`1..11` split-pencil census with at least 20 disjoint split
fibers, rather than an arbitrary degree-`67472` rational profile.

## Burn-down

```text
critical target attacked: rate_half_band_crossing_location
DAG delta: +1 background PROVED node, +2 edges
critical status delta: none
route delta: pole-simple rational certificate -> bounded degree-1..11 exception SPI
new assumptions: none
next action: classify/count the 20 disjoint split fibers using smooth-domain structure
```

## Nonclaims

- no identically-split conclusion from 20 fibers;
- no SPI census, base-field descent, rational payment, or whole-line owner;
- no adjacent-row safety or MCA closure.

## Replay

```text
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_heavy_ruling_exception_split_pencil_normal_form/verify.py
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_heavy_ruling_exception_split_pencil_normal_form/verify.py --tamper-selftest
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_heavy_ruling_exception_split_pencil_normal_form/verify_audit.py
```
