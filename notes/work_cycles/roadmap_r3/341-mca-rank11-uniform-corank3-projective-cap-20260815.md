# Cycle 341: MCA rank-11 uniform corank-three projective cap (2026-08-15)

This cycle closes the second target minted by the cycle-339 scope repair.  It
also decomposes the argument at its natural mathematical boundary: a reusable
rank-four matroid theorem, an RS specialization, and the existing exact
capacity cut are now separate DAG nodes with separate contracts and audits.

## Rank-four bounded-point/line theorem

Let `M` be a loopless rank-four matroid on `m=a+r` elements, where `a>=1` and
`r>=3`.  Suppose every parallel class has size at most `a` and every rank-two
flat has size at most `a+1`.  Put

```text
h_a(r)=min(floor((a+1)/2),floor((a+r)/4)),
C_a(r)=(a+r-1)(r-1)(r-2),
L_a(r)=3(a+r-h_a(r)-1)(r-2),
Q_a(3)=6,
Q_a(r)=min(C_a(r),Q_a(r-1)+L_a(r)).
```

The new universal leaf proves

```text
6 b(M) >= Q_a(r).                                      (BPL)
```

The proof uses deletion-contraction at an element in a smallest parallel
class `P`, of size `c`.

- If the chosen element is a coloop, the rank-three theorem in the deletion
  gives `6b(M)>=C_a(r)`.
- Otherwise the deletion retains rank four and contributes `Q_a(r-1)`.
  Simplification has at least four points, and every rank-two flat through
  `P` and another class contains at least `2c`; hence
  `c<=h_a(r)`.  The contraction is rank three on `a+r-c` nonloops with
  parallel-class ceiling `a+1-c`, so the rank-three theorem contributes at
  least `L_a(r)`.

The recurrence has an exact short evaluator.  If the last coloop reset is at
`j`, successive reset candidates differ by

```text
(j-1)(3*h_a(j+1)-a-2).
```

Because `h_a` is nondecreasing, this sign changes at most once.  The minimum
is therefore the no-reset path or the reset immediately before the first
nonnegative difference; the required sums of `h_a(x)(x-2)` are elementary
floor sums split by residue modulo four.

## Reed-Solomon specialization

After rank-seven canonical-basis cancellation and deletion of all global zero
normals, write

```text
t=K'-10-z,       0<=t<=K'-10<=1048566,
a=t+1,           r=67474.
```

The corank-three chart is

```text
(n,K,m,s)=(1048579+t,3+t,67475+t,3).
```

Support-local transversality gives parallel-class ceiling `a` and rank-two
flat ceiling `a+1`.  Applying `(BPL)`, every record owns at least
`4Q_(t+1)(67474)` ordered independent quadruples.  Consequently its count is
at most

```text
floor((1048576+t)(1048577+t)(1048578+t)(1048579+t)
      /(4Q_(t+1)(67474))).
```

Exact evaluation on the complete official interval gives

```text
maximum cap: 983902549 at t=0
t=1 cap:     983891721
t=2 cap:     983888183
far cap:     951742008
first excess: none
```

At `t=0`, `Q=307177966285344`; the next-integer numerator gap is
`172104506923776`.  Thus `983902549` is a uniform integer cap, with the
complete chart as the exact maximizer.

## Bounded computation and audits

One 512 MB, 60-second-limited Modal container exhaustively checked all
`1048567` integer rows and independently sampled the recurrence and residue
formulae:

```text
run: https://modal.com/apps/allengrahamhart/main/ap-Sv2HRoqdjrF188Uzqm7EJe
rows:              1048567
recurrence checks: 9440
residue checks:    2240
branches:          7 no-reset, 1048560 reset
```

The proof does not depend on the scan.  Focused proof verifiers, all under the
256 MB local guard, report

```text
MATROID_RANK4_BOUNDED_POINT_LINE_BASIS_FLOOR_PASS
  checks=199280 grid=80x118 controls=6/6
MATROID_RANK4_BOUNDED_POINT_LINE_BASIS_FLOOR_AUDIT_PASS
  recurrence_checks=4400 sign_checks=3240
RATE_HALF_MCA_RANK11_KERNEL_CORANK3_UNIFORM_PROJECTIVE_BASIS_CAP_PASS
  rows=1048567 cap=983902549 recurrence_checks=2340 controls=6/6
RATE_HALF_MCA_RANK11_KERNEL_CORANK3_UNIFORM_PROJECTIVE_BASIS_CAP_AUDIT_PASS
  sample_checks=30 rows=1048567 branches=7/1048560
```

The existing exact 228,261-row hierarchy replay and independent audit then
promote the corank-three capacity cut from conditional to proved:

```text
unconditional kernel cutoff: 796598
first method wall:            796599
```

```text
DAG delta:             +1 universal PROVED matroid node
                       corank-three uniform cap TARGET -> PROVED
                       corank-three capacity CONDITIONAL -> PROVED
critical orbit census: unchanged
unconditional kernel: K'=10..796598 excluded
remaining kernel:      K'=796599..1048576
delta-star movement:   none
compute:               one 512-MB/60-second Modal container, a few seconds
next route action:     select a capacity mechanism for the remaining kernel;
                       do not extend corank by rote without a scaling audit
```
