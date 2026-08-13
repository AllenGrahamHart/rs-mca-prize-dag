# Cycle 213: profile-(4,4) low-energy resultant contraction

## Route choice

After two export/harvest cycles without critical bracket movement, this
cycle returned to the direct critical E1 branch of
`unsafe_crossing_family_instantiation`. The binding low-square-mass pair
budget had paid profiles `(3,6)`, `(2,10)`, `(1,14)`, and `(0,18)`. Its next
profile `(4,4,S=20)` permits at most seven complete shift/sign orbits, while
the existing local-norm fence left `1133` possible cofactors.

## Falsification first

A `55`-second, constant-memory Modal annealing probe found realizable
autocorrelation energy `E=2`, falsifying any proposed universal
coefficient-level floor above two. A complete normalized four-singleton
parity census also found `264` one-lag masks. Thus low energy cannot be
discarded by parity or abstract coefficient combinatorics alone.

The discovered energy-two witness has nonzero autocorrelations

```text
A_60=A_62=1
```

and a `277`-bit exact norm, so a coarse norm-size argument also does not
remove it.

## Exact official exclusion

For an abstract integer spectrum `(A_d)`, define

```text
H_A(X)=20X^D+sum_d A_d(X^(D+d)+X^(D-d)).
```

Then

```text
|Res(X^128+1,H_A)|=|Norm(F(zeta_256))|^2.
```

Three exact FLINT censuses exhausted all spectra through energy four:

```text
E=1:       126
E=2:      7812
E=3:    317688
E=4:   9530766
```

No energy-one, -two, or -three norm factors as `p m` with `p` in the exact
official interval and `m` in the `1133`-value legal cofactor set. At energy
four, no norm even has an integer multiple in that interval. The complete
certificate used `8`, `16`, and `128` shards; every worker had `512 MiB`,
and the largest layer allowed at most `96` concurrent workers. No local
enumeration was run.

Therefore every official collision has

```text
E>=5,                 V=2E>=10.
```

## Analytic contraction

Integer autocorrelation gives the cap `y_u<=20+V`. The quadratic logarithmic
majorant on that interval yields

```text
Norm(alpha)<=20^64 exp(-16/5)(3/2)^(32/5).
```

Exact degree-37 Taylor bounds for `e^16` place this quantity strictly
between `932364 P` and `932365 P`, where `P=B_P 2^128` is the lower official
prime endpoint. Hence every collision has `m<=932364`.

Intersecting with the exact local list leaves `657` cofactors, down from
`1133`; the pure `2^20` branch is excluded. Thirteen pure branches and `644`
non-pure branches remain. This is a strict route contraction, not a collision
or orbit count.

## Banked nodes

- `e1_profile44_official_energy_le4_exclusion` — PROVED;
- `e1_profile44_energy_floor_cofactor_contraction` — PROVED.

Both have primary and independent local verifiers, source-hash contracts,
hostile controls, explicit nonclaims, and direct edges into the critical E1
pair-budget and unsafe-crossing nodes.

## Next route

Do not continue abstract energy enumeration mechanically: energy five grows
by an order of magnitude and still does not control orbit multiplicity. The
next proof attempt should exploit the retained families collectively, either
through a common-prime associate-height collapse adapted to profile
`(4,4)`, or through a direct weighted payment that avoids requiring one
orbit per cofactor.
