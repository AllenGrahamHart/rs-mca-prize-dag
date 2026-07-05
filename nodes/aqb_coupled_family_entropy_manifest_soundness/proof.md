# proof: aqb_coupled_family_entropy_manifest_soundness

Let `M` be a coupled manifest satisfying the stated predicates.

First, its family section contains a finite nonempty member set, the `c=2`
quotient-box geometry at `sigma*`, shared quotient/fiber data, reusable
box-charge data, and member-to-witness transfer maps. By
`aqb_family_certificate_semantics`, these fields are exactly the certificate
data needed for `aqb_c2_family_certificate_payload`.

Second, the manifest's ledger section is keyed to the same family members and
shared quotient/fiber data. It supplies lower bounds for the positive
shared-family entropy terms and upper bounds for the charged box, overlap,
multiplicity, and quotient/fiber normalization costs. By
`aqb_entropy_ledger_certificate_soundness`, if the certified lower-minus-upper
sum is at least

```text
429,645,547
```

bits, then the true net shared entropy gain for that same family is at least
the required threshold. These are exactly the ledger entries required by
`aqb_shared_entropy_gain_payload`.

Thus a single verified coupled manifest proves both payload nodes. The
construction of the actual manifest remains separate.
