# ATTACK - aqb_shared_entropy_gain

This is now an assembly node.

After `aqb_c2_family_certificate_payload` fixes the family through
`aqb_c2_average_family`, the live entropy task is
`aqb_shared_entropy_gain_payload`: write an exact or interval-certified
accounting for:

- shared family entropy;
- charged box entropy;
- overlap and multiplicity normalization;
- quotient/fiber normalizations.

The result should be interval-certified or exact integer arithmetic, and must
show net gain at least `429,645,547` bits.
