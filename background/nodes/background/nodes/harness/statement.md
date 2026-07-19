# harness

- **status:** PROVED
- **closure:** artifact certificate

The verifier harness discovers every local `verify*.py` under the critical and
background node trees plus every `tools/verify_*.py`, classifies Modal launchers
separately, and fails closed unless the discovered set and SHA-256 hashes agree
with `tools/verifier_manifest.json`.

The pinned Modal replay executes every local verifier under its manifest hash.
All entries pass. The harness self-test rejects six independent negative
controls: an omitted verifier, a stale verifier entry, a changed verifier, a
changed proof asset, a nonzero verifier exit, and a verifier timeout.
