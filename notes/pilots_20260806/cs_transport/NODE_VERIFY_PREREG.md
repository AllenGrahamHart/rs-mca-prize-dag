# Ideal/Galois multiplicity node verification - preregistration

- **date:** 2026-08-06
- **node:** `rate_half_crossing_ideal_galois_multiplicity_exclusion`
- **input audit:** Modal app `ap-JNBoN1s1INvr1ovkHvbf8h`, PASS

Run the candidate node's primary verifier and independent contract verifier
inside one fresh Modal container after compiling the manifest-owned DAG.
The primary verifier must independently replay the registered audit and
match its persisted JSON byte-for-semantics; the contract verifier must
recheck the exact one-cell benchmark boundary, tower coefficients, preserved
failed run, scope disclaimers, and evidence-edge contract.

One CPU, 1 GiB RAM, 120-second function cap, 90-second subprocess cap, no
retry.  `2/2` successful subprocesses authorize the PROVED node commit.
Any failure blocks promotion and preserves the candidate packet for repair.

## First-launch result

Modal app `ap-AUcIbMTIlcrZT1pkX43Hla` failed before either verifier ran.  On
remote import, the launcher was mounted at `/root/cs_node_verify_modal.py`,
so its local-only `Path(__file__).parents[3]` lookup raised `IndexError`.
Modal automatically retried the import; the client was stopped once the
repeated identical failure was visible.  This is a launcher-path failure,
not a verifier result, and authorizes no promotion.
