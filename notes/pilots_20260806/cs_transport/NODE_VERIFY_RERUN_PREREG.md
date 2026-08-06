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
