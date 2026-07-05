# conditional: aqb_shared_entropy_gain

## Predicate nodes

- `aqb_entropy_ledger_certificate_soundness`
- `aqb_shared_entropy_gain_payload`

## Claim

Conditional on the concrete entropy ledger payload, the averaged `c=2`
quotient-box family has net shared entropy gain at least `429,645,547` bits.

## Proof

The remaining predicate `aqb_shared_entropy_gain_payload` supplies certified
lower bounds for the positive shared-family entropy terms and certified upper
bounds for all charged costs, with certified net lower bound at least
`429,645,547` bits.

The proved node `aqb_entropy_ledger_certificate_soundness` says that such a
monotone ledger soundly lower-bounds the true net gain. Therefore the true
net shared entropy gain is at least the required threshold.
