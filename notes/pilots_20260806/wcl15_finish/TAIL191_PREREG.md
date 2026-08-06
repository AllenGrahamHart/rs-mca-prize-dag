# WCL `(1,5)` tail 191 targeted factor probe - preregistration

- **date:** 2026-08-06
- **consumer:** `dli_wcl_slot_1_5_emptiness`
- **parent campaign:** hard-tail app `ap-9R3y73LE4xoHSDpoqUXGoN`
- **scope:** the sole unresolved 269-bit norm

```text
648504938724625892617537595827566622528651020454874372151735040370465231483079169
```

## Decision

Run ten independent, deterministic, bounded factor probes: eight GMP-ECM
workers at staggered `B1` depths and sigma seeds, one fresh PARI worker, and
one FLINT worker.  Every decimal token returned by a worker is treated only
as a candidate and accepted only if exact division succeeds.  A discovered
divisor and cofactor are then given a short bounded PARI completion attempt.

This is not a retry of the 193 completed tails.  It reads no volume and writes
no remote checkpoint.  The compact local packet retains stdout/stderr tails,
timeouts, exact divisors, products, and source hash.

## Predictions and outcomes

**P1.**  At least one independent worker finds a nontrivial divisor.

**P2.**  Any complete factorization has no prime below `2^256` with
`v_2(p-1)>=41`.

If P1 fails, the exact norm becomes a named external ECM/NFS request and no
further Modal factoring is automatic.  If a divisor is found but the cofactor
is not certified prime/factored, only the factor split is banked.  Only an
exact product with every factor passing PARI `isprime` pays this tail.

## Resource ceiling

At most ten one-CPU, 2-GiB containers; 330-second function cap and 300-second
main subprocess cap per worker.  The ECM workers use fixed seeds and run until
factor, completion, or timeout.  Conservative cost ceiling is `$0.50`.  No
retry or larger `B1` is authorized, and the app stops when the client exits.

```text
tools/ramguard modal -- modal run \
  notes/pilots_20260806/wcl15_finish/tail191_ecm_modal.py
```

App `ap-qUcK72KF9ec7cN4chlxoA9` completed and stopped normally.  All ten
workers reached their 300-second subprocess cap without a divisor; no client
error occurred.  PARI printed `PRIME:0`, independently confirming that the
integer is composite.  Result SHA-256 is
`11cbae528206806d411efe4e0deb9da59956335358d9afae6dd729780e1eae6f`.
The preregistered retry budget is exhausted.  The norm is now the explicit
external request in `EXTERNAL_REQUEST.md`.
