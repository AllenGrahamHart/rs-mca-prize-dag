# FPC5 joint-owner probe

- **status:** exact finite experiment; not a theorem or official-row payment
- **launcher:** `fpc5_joint_owner_probe_modal.py`
- **result:** `fpc5_joint_owner_probe_result.json`
- **Modal envelope:** one CPU, 1 GB RAM, 60-second hard timeout
- **completed runtime:** 30.789 seconds

The probe reuses the exact small-cell FPC5 chart enumeration and records the
joint owner consisting of common defect roots plus common background roots.
It ran 256 `T1`, 64 `T2`, and 128 `C8` configurations.

Across all three cells there were 1,095 anchor views and 4,274 ordered
anchor-neighbor incidences. The results were:

```text
anchor views with injective neighbor -> owner map: 905 / 1095
realized owner groups of multiplicity one:          3781 / 4012
duplicate incidences beyond one per owner:           262 / 4274
maximum observed fixed-owner multiplicity:                    4
fixed-owner packing violations:                               0
```

The effect is strongest in `C8` and `T1`: 414/423 and 250/261 anchor views,
respectively, had one distinct owner per neighbor. In `T2` the owner map was
injective at 241/411 anchor views, but 2255/2466 owner groups were still
singletons.

## Interpretation

This resists the simplest coalescence premise that a guarded remainder graph
realizes only a few joint owners. The proved fixed-owner packing theorem is
consistent with every observation, but most observed owner chambers contain
one candidate, so its per-owner charges do not aggregate automatically.

The experiment does not refute a chronology-valid transport theorem or a
global split-root inverse theorem. It redirects the attack from bounded
owner count toward structure relating many distinct owners in the same
remainder graph. These are small exact cells, not asymptotic or official-row
evidence.
