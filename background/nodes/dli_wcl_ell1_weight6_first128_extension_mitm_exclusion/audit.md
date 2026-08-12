# Audit

## Scope

The panel targets the smallest characteristics omitted by the prior
degree-one search.  Exact valuations 39 and 40 produce generated extension
degrees four and two.  The search is exhaustive within every listed row but
the row panel is finite, so only an evidence edge is permitted.

## Arithmetic

The verifier supplies full-factorization Pocklington proofs rather than
treating probable-prime output as a certificate.  It independently checks
the exact multiplicative order modulo `2^41`, the field power, the `2^256`
cap, and exact order of every displayed 512th root.  All C++ products use
unsigned 128-bit intermediates while every characteristic is below `2^52`.

## Completeness

Rotation, pair/triple coverage, and equality/antipodality checks are the same
mathematical normalization as the proved degree-one packet.  The new source
is separate so that its weaker and necessary `512|p-1` precondition cannot
alter the hash-pinned degree-one artifact.

## Independence

The primary implementation uses an unordered multimap.  The audit uses a
sorted vector and binary search and replays four class endpoints.  Mutation
controls alter field metadata, root data, exhaustion counts, and result
headers; both verifiers reject every registered mutation.

## Operations

Phase zero run `ap-TyGVKBQkJKs4YI7zsRSEr5` exhausted the smallest row.  Full
run `ap-OBpurxpqKbSaEWcdfigWRb` returned all 128 rows in 102.84 aggregate CPU
seconds with no relation.  Independent run `ap-sl5Tvw3eProIKsCqV5Sy37`
returned four exhausted rows.  Modal printed an asynchronous-generator close
warning after both completed maps; both local entry points exited zero and
wrote `status=COMPLETE` artifacts with no worker errors.
