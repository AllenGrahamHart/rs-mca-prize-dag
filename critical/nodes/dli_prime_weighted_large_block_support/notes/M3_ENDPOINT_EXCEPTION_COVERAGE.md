# M3: endpoint-exception coverage contract

- **status:** truth-apt route obligation posed; unproved
- **scope:** every official code row, not a density-one or deployer-selected set
- **nonclaim:** A1-PROD does not discharge this obligation

## Audit finding

The earlier route language suggested that the endpoint could consume “the
deployed `q` is not exceptional,” possibly in an engineering-hardness sense.
That is not a valid input to the prize theorem. The code, including its field,
is given; a proof cannot choose a typical prime or discard a sparse set of
admissible fields.

`A1_PROD_NORM_SIEVE.md` proves an unconditional count and density bound on
exceptional primes in a dyadic band. It does not identify each exceptional
prime and does not prove that the official row is outside the exceptional
set. The source also explicitly states that absence of low-weight vanishers
cannot be certified by exhaustive search at production scale. A list of
exhibited generators therefore proves neither completeness nor a residual
upper bound.

## Certificate soundness

For an official row `R`, an endpoint-exception certificate `pi_R` must contain:

1. the exact row key, field presentation, generated-field normalization, and
   primality/order certificates;
2. for every production level, a complete low-weight orbit ledger with a
   checkable completeness proof, not only exhibited representatives;
3. exact multiplier-shadow and lift de-duplication bounds;
4. an independently checkable residual near-peak upper certificate for every
   unlisted weight/frequency class;
5. the C2'' coset/bulk/accident ownership ledger, with the aggregate reserve
   charged once;
6. an exact rational final check against the binding endpoint `2^121`.

The soundness statement is

```text
VERIFY_ENDPOINT_EXC(R,pi_R)=ACCEPT  ==>  q^{-t+H} W_cen(R) <= 2^121.
```

An implementation may have several certificate types, but each type must
prove completeness of the mass it prices. “No explicit construction is
known,” “the row is likely nonexceptional,” and PPT/engineering hardness are
rejected certificate types.

Item 5 is not consistency-only: the ownership ledger's joint bridge must
resolve to the manifest's named C2''-instance, so assumption-only item-5
content is a REJECT (catch #163), and any reserve credit must be covered
exactly by the mass of buckets owned coset/accident (catch #165).

## Coverage obligation

The truth-apt route statement is

```text
for every official row R, there exists pi_R such that
VERIFY_ENDPOINT_EXC(R,pi_R)=ACCEPT.                         (ENDPOINT-EXC-COVERAGE)
```

Soundness without coverage is only a conditional checker. Density control
without individual coverage is only an average-over-fields theorem. Both are
insufficient for the full prize result.

## Current status

No repository asset proves `ENDPOINT-EXC-COVERAGE`. The strongest available
per-row artifacts certify exhibited generators and selected low-weight
windows, while their own source notes deny a complete production-scale absence
certificate. M3 is therefore posed but open.

This blocks M4 from being presented as an unconditional DLI assembly. M4 may
still prove the exact arithmetic implication from accepted C1', C2'', and
endpoint certificates, but it must expose coverage as an input and must fail
closed when that input is absent.
