# proof: aqb_family_certificate_semantics

Let `Cert` be a certificate satisfying the stated predicates.

The member-set predicate gives a finite nonempty set `F`. The geometry
predicate assigns each `w in F` to the `c=2` quotient-box geometry at
`sigma* = 8,592,912,738`, so the family is an admissible AQB `c=2` family.

The shared-data predicates give quotient and fiber data common to all members
of `F`. The reusable-charge predicate records that the corresponding box
charge is attached to the shared data rather than charged once per member.
Thus the family has the nontrivial shared quotient structure required by
`aqb_c2_average_family`.

Finally, the transfer predicate gives the map from each family member to the
list witness used by the AQB averaging argument. Therefore the certificate
contains exactly the data asserted by `aqb_c2_average_family`: a finite
averaged `c=2` quotient-box family at `sigma*` with shared quotient/fiber
structure and transfer maps to list witnesses.

This proves the certificate semantics. It does not construct the certificate;
that is the separate payload node.
