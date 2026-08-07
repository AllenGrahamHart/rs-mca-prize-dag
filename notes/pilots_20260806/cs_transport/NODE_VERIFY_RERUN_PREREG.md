# Ideal/Galois multiplicity node verification - launcher remediation

- **date:** 2026-08-06
- **failed app:** `ap-AUcIbMTIlcrZT1pkX43Hla`
- **failure class:** remote-import path resolution before verifier execution

The sole launcher correction chooses the checked-out local repository root
when the source path has enough parents, and `/repo` when Modal imports the
launcher from `/root`.  The mounted node packet, pilot packet, DAG, verifier
commands, resource cap, and `2/2` promotion rule are unchanged.

One clean rerun is authorized.  Any verifier failure blocks promotion; a
second launcher failure ends this wrapper route rather than triggering
another repair cycle.

## Result

Modal app `ap-kaveXQab3dd0pe4ot3QnS1` reached both verifiers.  The primary
verifier passed all 816 norm checks, 1,104 divisibility checks, exact
boundary checks, and both evidence edges.  The contract verifier then failed
only because it searched for the literal token `not uniform` while the
contract states the equivalent and stronger token `no uniform percentage`.
Result JSON SHA-256:
`a5c6c14768b82439ac3fcf58fd729b4c8b5be85ce0d1c81d851b46560d5feeac`.
Promotion remains blocked pending a separately registered static-check
repair and a final `2/2` result.
