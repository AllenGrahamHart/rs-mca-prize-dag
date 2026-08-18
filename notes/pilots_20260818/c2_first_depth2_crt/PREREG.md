# C2 first depth-two CRT falsifier: preregistration

## Decision target

Test the unproved full-tower candidate

```text
J_prim <= sqrt(2n)
```

on the first currently reachable row with a genuine nonempty tail:

```text
(n,t,q)=(64,4,193),       m=2.
```

The exact firing predicate is

```text
[2^(nm)(Z_0-C_1)]^2 > 2n [Z_m product_(j<m) B_j]^2.
```

A firing refutes the candidate. A survivor is evidence only and supplies no
transport to the official `m=33` row.

## Exact method

Use additive Fourier inversion modulo three deterministic 60-bit primes
`R=1 mod 193`. For the four-dimensional `Z_0` sum, quotient dual tuples by

```text
(a_1,a_2,a_3,a_4) ->
(a_1*zeta,a_2*zeta^2,a_3*zeta^3,a_4*zeta^4).
```

Gauge the first nonzero coefficient into one multiplicative-coset
representative. If that coefficient is in position `r`, retain all later
coefficients and weight the normalized slice by `n/gcd(n,r)`. This counts
every full orbit exactly, including residual stabilizers. The resulting
workload is `21,791,257` normalized tuples including zero and
`1,394,640,384` nonzero-tuple local factors, rather than a `2^32` subset
MITM.

Two CRT moduli give more than 120 bits against the strict `2^64` count bound;
the third is an independent residue check. The same executable must reproduce
the frozen `(32,2,97)` control before the target is accepted.

## Frozen moduli

```text
1152921504606850301
1152921504606873847
1152921504606875777
```

The control modulus is `1152921504606848701`.

## Resource fence

- Modal only for the census.
- Three target shards at eight CPUs and 2 GiB, plus one small control.
- Per-task timeout 240 seconds; partial output after every returned shard.
- No larger retry and no second depth-two row in this pilot.
- Stop with `INCOMPLETE` if any target shard times out. Expected total cost is
  below `$1`.

## Interpretation

- **FIRE:** retire `(SQRT)` and retain only `(C2-INT)` as the live target.
- **SURVIVE:** bank the first exact depth-two datum; do not infer depth
  monotonicity.
- **INCOMPLETE:** preserve residues and make no mathematical inference.
