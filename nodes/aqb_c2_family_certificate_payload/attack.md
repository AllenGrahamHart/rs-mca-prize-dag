# ATTACK - aqb_c2_family_certificate_payload

This is now an assembly node. The live AQB leaf is
`aqb_coupled_family_entropy_manifest_payload`.

Needed output at the coupled payload:

- define the canonical finite member set for the `c=2` quotient-box geometry
  at `sigma*`;
- identify the shared quotient/fiber coordinates that all members reuse;
- record the reusable box-charge datum rather than charging one full box per
  member;
- give the transfer map from each member to the list witness used by
  `aqb_average_member_transfer`;
- include the entropy ledger for the same family, so the family certificate
  and ledger cannot drift.

Use only light local checks here. A broad WSL search for the family is not
appropriate on this machine.
