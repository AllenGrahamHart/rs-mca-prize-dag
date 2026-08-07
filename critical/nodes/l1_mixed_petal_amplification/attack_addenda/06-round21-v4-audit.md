# Round-21 v4 PMA attack correction

## Field-normalized census re-read

The banked witness-preserving scalar schedules gave raw counts

```text
43 -> 2879 -> 109391,
33 -> 2857 -> 108600.
```

The second doubling also doubles the field from 97 to 193. The banked
fixed-`(n,k)` control in `pma_d4r0_census_results.json` has a 98.0%-exact
`1/p` retention law. After field correction, the growth exponent is flat at
6.14-6.21, above the separately disproved `n^6` line. Therefore the former
reading that the super-polynomial trend "did not fire" was unsupported: a
flat exponent is evidentially neutral, while these numerics and the proved
`n^6` insufficiency point in the same direction. The decisive queued control
is the census at `(n,k,p)=(64,32,97)`.

This remains evidence, not a uniform theorem or floor-band emptiness result.
The `n=128` run remains parked as contributor request `L1-N10-128`.

## Campaign survey

The v4 PMA campaign is fully imported in Waves 8-9; canonical is ahead in
every divergent file. All 65 verifiers replay, the retraction passes all
three scope tests, and the campaign's eight self-retractions were preserved.
The companion catch concerning the struck hypothesis on the sigma-one floor
is applied in `pma_sigma_one_variable_defect_exact_hit_floor`.
