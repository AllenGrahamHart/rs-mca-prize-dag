# C2 official-shape `t=2` CRT falsifier: preregistration

## Decision target

Test the unproved candidate

```text
J_prim <= sqrt(2n)
```

at the first exact analogue having the official aspect ratio `n/t=256`:

```text
(n,t,q)=(512,2,7681).
```

Here `q` is prime and `512 | q-1`. A firing is the exact integer inequality

```text
[(Z_0-C_1)2^n]^2 > 2n (Z_1B_0)^2.
```

PASS means only that this one row survives. It supplies no depth transport
and cannot promote C2'' or the square-root candidate.

## Exact method

Use additive Fourier inversion over `F_q`. For `Z_0`, quotient the `q^2`
dual characters by the exact action

```text
(a,b) -> (a*zeta,b*zeta^2),
```

where `zeta` has order `n`. This leaves about `q^2/n` products, each of
length `n`. Compute `Z_0,C_1,Z_1,B_0` modulo ten distinct deterministic
60-bit primes `R=1 mod q`. Their product has 600 bits, exceeding the strict
`2^512` count bound, so ordinary CRT reconstructs each count uniquely.

Every modulus is checked by deterministic 64-bit Miller--Rabin. No floating
value participates in the verdict. Two single-modulus controls reproduce the
already frozen `(32,2,97)` and `(32,2,5857)` censuses.

## Frozen moduli

```text
1152921504607075139  1152921504607136587
1152921504607459189  1152921504607597447
1152921504608457719  1152921504609241181
1152921504609333353  1152921504609486973
1152921504609978557  1152921504610301159
```

Control moduli are `1152921504606848701` for `q=97` and
`1152921504607016701` for `q=5857`.

## Resource fence

- Modal only for the census.
- Twelve one-CPU, 1 GiB tasks; ten target CRT shards and two controls.
- Per-task timeout 240 seconds; partial results are rewritten after every
  returned shard.
- No retry with larger resources and no second target row in this pilot.
- Expected cost is comfortably below `$1`; stop if the first returned target
  shard exceeds 120 seconds.

## Interpretation

- **FIRE:** record an exact counterexample and retire `(SQRT)` immediately.
- **SURVIVE:** retain `(SQRT)` as evidence only. The next action remains a
  proof or refutation of support-overlap-times-tail control.
- **INCOMPLETE:** bank returned residues; make no mathematical inference.

