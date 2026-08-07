# WCL `(1,5)` independent hard-tail certificate - preregistration

- **date:** 2026-08-06
- **consumer:** `dli_wcl_slot_1_5_emptiness`
- **primary packet SHA-256:**
  `026fbd0d5665bc855bfcdd56f54b33bbea2b2a563aa98c79daf6e4f042ac0f4b`
- **scope:** 194-row hard-tail manifest and 193 completed factorizations
- **expected residual:** tail index 191 only

## Decision

Package the exact primary factor-only JSON by content hash into one Modal
container.  Independently reconstruct the manifest digest from every norm,
class index, key, and timeout reason.  For each completed tail, require exact
manifest custody, sorted positive factors and exponents, complete product,
and FLINT primality for every factor.  Recompute all per-row and aggregate
prime-size, `v_2(p-1)`, high-gate, distinct-prime, and vocabulary-digest data.

Any disagreement is a candidate falsifier.  A clean result certifies the 193
completed tails but cannot promote the node while tail 191 remains unfactored.

## Predictions and gates

**P1.**  The manifest has 194 distinct indexed norms and digest
`aa7fa74e79bb80f660ac6e5c6b9e03c85419630bef834076e1d1fe1380bf1ab8`.

**P2.**  Exactly 193 rows have complete prime factorizations, comprising 399
distinct primes with digest
`4180c683ce53c2df9181656ac8afb9fab287288bdab549f0a08326a31c800cbb`.

**P3.**  Every factor passes FLINT primality, no official-gate factor occurs,
maximum `v_2(p-1)` is 17, and tail 191 is the sole residual.

## Resource ceiling

One Modal container uses one CPU, 1 GiB, and a 120-second hard cap.  Expected
cost is below `$0.01`; no retry or factoring attempt is authorized.

```text
tools/ramguard modal -- modal run \
  notes/pilots_20260806/wcl15_finish/tail_independent_cert_modal.py
```

## Operational null run

App `ap-09Oi6Aze0mEezM6J52sLyS` failed before testing a factor because the
new checker expected `factor_results` to omit tail 191.  The primary schema
instead contains all 194 indexed entries and represents tail 191 explicitly
as `PARTIAL`.  No mathematical prediction was tested.  One corrected run is
authorized with stricter custody: require all 194 entries, exactly 193
`COMPLETE`, and the exact partial timeout record at index 191.

## Outcome

Corrected app `ap-beZVadXTE7z94tsQiEsGZ7` completed in 1.017 seconds.  P1-P3
all pass: 194 manifest rows, 193 certified factorizations, 400 FLINT
primality checks, 399 distinct primes, maximum `v_2(p-1)=17`, no gate factor,
and tail 191 as the sole residual.  Manifest and prime digests reproduce
exactly.  Certificate digest is
`f218fc0a26b2ec2bc1f4084bc5b0fd1eabb58c4b96e0f21aa6729350b0be0d40`;
compact-result SHA-256 is
`2292b2a5fccc61fba288dc8566904237b2ce4db05a0c7a83587720512d94c5ba`.

The 193 completed hard tails are now proof-grade.  No node promotion occurs
until tail 191 is completely factored and independently certified.
