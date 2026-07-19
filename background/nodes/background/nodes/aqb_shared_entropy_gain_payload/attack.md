# ATTACK - aqb_shared_entropy_gain_payload

This is now an assembly node. The live AQB entropy/family leaf is
`aqb_coupled_family_entropy_manifest_payload`.

The monotone interval-ledger soundness rule is proved in
`aqb_entropy_ledger_certificate_soundness`. What remains is the coupled
manifest for the averaged `c=2` family and its ledger:

- lower-bound the shared-family entropy;
- upper-bound all charged box, overlap, multiplicity, and quotient/fiber
  normalization costs;
- keep all arithmetic exact or interval-certified;
- prove the resulting net lower bound is at least `429,645,547` bits.

This ledger depends on the concrete family certificate; the coupled manifest
keeps them keyed to the same member set and shared quotient/fiber data.

Do not use floating knife-edge arithmetic for the final ledger.
