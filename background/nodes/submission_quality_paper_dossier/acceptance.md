# Acceptance contract

The final artifact must provide one machine-readable manifest with these
fail-closed sections:

```text
schema
paper_artifact + sha256
grand_claims: mca_grand, list_grand
official_scope: rows, rates, objects, arities
claim_provenance
compiler + descriptor schema
certificate_index
independent_verifier
clean_checkout_replay
open_required_claims
required_scope_nonclaims
upstream_handoffs
```

Acceptance requires:

- both grand claim statuses are `PROVED` at the pinned DAG hash;
- `open_required_claims` and `required_scope_nonclaims` are empty;
- every proof, compiler, verifier, certificate, and paper path exists and
  matches its hash;
- the compiler and independent verifier agree on every indexed certificate;
- the scope table explicitly contains rates `1/2,1/4,1/8,1/16`, both prize
  objects, every admissible row family, and the full arity statement;
- a clean-checkout replay is complete with no failure, timeout, skipped
  required verifier, or remote-only unverifiable row;
- upstream handoffs identify the offered commit or PR, exact local claims,
  terminology bridge, and review status.

Missing sections, empty hashes, a surviving red/amber requirement, or a
"partial" scope label fail acceptance. This contract is deliberately not
satisfied by assembling the current partial dossier around future promises.
