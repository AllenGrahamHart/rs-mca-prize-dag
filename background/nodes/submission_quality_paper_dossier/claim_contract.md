# Claim contract

- **claim id:** `submission_quality_paper_dossier`
- **mathematical statement:** none beyond the two grand dependencies; this is
  the final artifact predicate in `statement.md` and `acceptance.md`
- **scope:** both official prize problems in their complete row, rate, object,
  field, endpoint, and arity scope
- **consumer:** `packaging`
- **status:** `TARGET`
- **dependencies:** `mca_grand`, `list_grand`
- **new open content:** materialize, hash, and clean-replay the final paper,
  compiler certificates, verifier, provenance ledger, and upstream handoffs
- **falsifier:** one missing official row/rate/object/arity, one open required
  premise, one required-scope nonclaim, one hash mismatch, or one certificate
  not independently replayable
- **nonclaims:** the partial dossier does not close this target; current
  compiler refusal behavior does not prove total official coverage; green
  mathematical roots alone do not materialize a submission artifact
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/submission_quality_paper_dossier/verify.py`
- **upstream mapping:** final Paper-D submission spine and all five hard-input
  packets
