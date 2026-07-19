# Audit

The parity hypothesis concerns the four deleted roots themselves. It is
strictly narrower than the surrounding fiber-four component, whose name is
already "antipodal" for a different descent reason. The ordinary size-128
primary-gap orbits in the order-128 pilot are outside this theorem.

The official divisibility `d=16M` is load-bearing. It makes `h=2M+1` odd, so
the second primary index and the first secondary terminal index are odd. A
generic even `d` would not give the same pair of automatic equations.

The exact order-128 packets `{0,20,64,84}` over `F_257` and
`{0,6,64,70}` over `F_641` replay `(DPP3)--(DPP6)`. Their remaining secondary
coefficients are respectively `31` and `381`, so both are rejected. They are
audits only; the proof is the formal parity and scaling argument.

A tiny characteristic-zero diagnostic computed the two elimination
resultants for `M=1,...,5`: primary against `t^(8M)-1`, and primary against
the cleared secondary numerator. Their gcd prime supports were respectively

```text
{}, {5,7}, {3,5,11}, {3,5,11,13}, {3,13,17,19}.
```

Every prime is at most `4M-1`, so the standing `char(F)>16M` would exclude
all five toy simultaneous loci. This is a route clue only. No uniform
resultant-support theorem in `M` is claimed.

Replay this bounded diagnostic with

```text
tools/ramguard tiny -- python3 experiments/prize_resolution/rate_half_list_deleted_pair_resultant_support.py
```
