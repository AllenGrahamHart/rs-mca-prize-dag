# WCL `(1,5)` tail-191 independent factor certificate - preregistration

- **date:** 2026-08-06
- **consumer:** `dli_wcl_slot_1_5_emptiness`
- **source:** `tail191_cado_portable_v2_result.json`
- **source SHA-256:**
  `c093d5e05aea1e2b2851042e550f89cf44f093c8b1714c80780efd27b72ec608`

## Decision

Independently certify the two factors returned by the successful bounded
CADO-NFS run.  The checker consumes the content-pinned result, checks its
norm and immutable image custody, multiplies the factors back to the exact
tail-191 norm, and asks FLINT to prove each factor prime.  It then computes
the factor bit lengths and `v_2(p-1)` values from scratch and applies the
official gate `p < 2^256` and `v_2(p-1) >= 41`.

This checker does not trust CADO's primality labels or printed factor order.
It is separate from the 193-tail certificate and produces one compact JSON
record.  A factor-product mismatch, a composite returned factor, a source
digest mismatch, or either official-gate factor is `FAIL`, not partial.

## Predictions

**P1.**  The factors multiply to the exact 269-bit norm and are both prime.

**P2.**  Their bit lengths are 112 and 158, and their `v_2(p-1)` values are 9
and 12.  Consequently neither is an official-gate prime.

**P3.**  Combining this result with the independently certified 193-tail
packet leaves no hard residual.  Node promotion still requires the finite
completeness router and easy-census replay to be assembled explicitly in the
node proof; this certificate alone does not change DAG status.

## Resource ceiling

One Modal container, one CPU, 1 GiB RAM, 120-second function timeout, and no
parallel workers.  Expected cost is below `$0.01`.  No factor search is run.

```text
tools/ramguard modal -- modal run \
  notes/pilots_20260806/wcl15_finish/tail191_factor_cert_modal.py
```

