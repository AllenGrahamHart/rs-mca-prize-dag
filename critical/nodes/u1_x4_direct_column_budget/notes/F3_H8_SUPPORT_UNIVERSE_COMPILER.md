# F3 h=8 support-universe compiler

Status: PROVED COMBINATORIAL COMPILER / RESIDUAL-SIZE AUDIT, NOT A FULL h=8
CERTIFICATE.

This packet records the exact size of the h=8 n=64 support universe that remains
after the x83 support-to-trade reduction.  It is deliberately a bookkeeping
compiler: it does not enumerate the universe and it does not promote the h=8
n=64 partial rows.

## Pre-registration

Question:

```text
How large is the anchored non-antipodal 16-support universe, and how much of it
is represented by the already banked paid-branch local x83 shell workloads?
```

Success criterion:

- compute the anchored 16-support universe with exponent 0 included;
- compute the antipodal anchored subfamily;
- compute the non-antipodal residual universe;
- compute the blind left/right h=8 join sizes;
- compute the multiplicity workload of radius-r exchange shells around the
  seven paid h=8 square-lift supports;
- verify that the banked radius-three certificates process exactly the
  radius-three workload.

Failure criterion:

- treat a local shell as a global certificate;
- count antipodal supports in the residual non-antipodal target;
- hide the `binom(63,7)` blind left table cost;
- claim h=8 closure without a support-level x83 certificate.

## Exact support counts

Anchored h=8 n=64 support certificates can be posed as 16-subsets of the
64-root domain with exponent 0 included.  Hence the complete anchored support
universe has size

```text
binom(63,15) = 122,131,734,269,895.
```

The antipodal supports are exactly those that contain whole antipodal pairs.
Since the pair containing exponent 0 is forced, their count is

```text
binom(31,7) = 2,629,575.
```

Thus the non-antipodal residual target is

```text
122,131,731,640,320
```

anchored supports.

## Blind join cost

The blind h=8 n=64 left table has

```text
binom(63,7) = 553,270,671
```

anchored records, about `16.49 GiB` at 32 bytes per record before metadata and
before scanning the right side

```text
binom(63,8) = 3,872,894,697.
```

This confirms that the remaining h=8 branch should be attacked by x83 support
keys or a sharded/external signature join, not by a laptop left-table build.

## Paid-branch local shell scale

At the two banked x83 shell primes `p=4289` and `p=262337`, the paid h=8
square-lift branch has seven supports.  The multiplicity workload at exchange
radius `r` around those seven supports is

```text
7 * binom(16,r) * binom(48,r).
```

The exact workloads are:

```text
r=0: 7
r=1: 5,376
r=2: 947,520
r=3: 67,800,320
r=4: 2,478,949,200
```

The banked radius-three certificates process exactly `67,800,320` candidates at
each of `p=4289` and `p=262337`, with `full_zero = 0`.  The full radius
`<= 3` paid-branch workload is only

```text
68,753,223
```

which is about `0.562943` parts per million of the anchored non-antipodal
support universe.  This is useful adversarial evidence near the paid branch,
but it is not a global h=8 certificate.

## Residual target

The h=8 n=64 residual is now quantitatively pinned:

```text
certify every one of the 122,131,731,640,320 anchored non-antipodal
16-supports by x83 obstruction keys, orbit compression, or an external/sharded
signature join; local shells around the seven paid square-lift supports are not
large enough to stand in for the global target.
```

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_support_universe_compiler.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_residual_frontier_audit.py
```

Expected digests:

```text
H8_SUPPORT_UNIVERSE_COMPILER_PASS
H8_RESIDUAL_FRONTIER_AUDIT_PASS
```
