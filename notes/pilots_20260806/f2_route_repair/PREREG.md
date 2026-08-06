# F2 Round-17 critical-route repair - replay registration

- **date:** 2026-08-06
- **stale route:** `f2_growing_order_myerson -> f2_conditional_close`
- **proved replacement supplier:** the admissible-row direct-sum/GRS
  reduction in `notes/pilots_20260806/f2_adm/PROOFS.md`
- **route alarm:** `(O1)` is false on explicit admissible rows with
  `ord_n(p)<[F_q:F_p]`

## Registered replay

Run the canonical self-contained `f2_adm/verify.py` in one fresh Modal
worker, mounting exactly its 26 quoted source locations.  Require all ten
stages, `373 PASS`, `0 FAIL`, and digest `F2_ADM_ALL_PASS`.

The replay is a provenance gate, not the proof.  The written proof must still
be audited when the supplier node is minted.  In particular the DAG surgery
may use only these exact consequences:

1. every admissible row has at most two moving rungs;
2. each deployed kernel decomposes into at most four prime-field GRS/MDS
   class kernels, with exact dimension and multiplicative ternary mass;
3. the trace collapse uses `ord_n(p)`, not the ambient extension degree;
4. the old `(O1)` all-row premise fails whenever `ord_n(p)<e`; and
5. growing-order Myerson no longer suffices as the sole requirement of an
   all-admissible-row conditional close.

## Resource ceiling

One Modal container, one CPU, 1 GiB RAM, 180-second function cap,
150-second subprocess cap, no retry, and no new parameter sweep.  Expected
cost is below `$0.02`.

## Decision

- `373/373 PASS`: mint the proved reduction supplier and repair the stale
  critical wiring without promoting the F2 conclusion.
- Any failure: preserve the result and do not alter the critical route until
  the source/provenance discrepancy is understood.
