# Audit

## Scope audit

The experiment checks all reduced six-term relations on 64 prime-field rows.
It does not sample relations. It does sample the official characteristic
range, so no target status changes.

## Completeness audit

Normalization loses no relation because multiplication by a power of the
order-512 root is a bijection. Removing indices `0` and `256` leaves exactly
510 candidates and 255 antipodal pairs. The pair/triple split covers every
five-subset. Final cross checks enforce all missing compatibility conditions.

## Arithmetic audit

All products use unsigned 128-bit intermediates below `2^256`, while every
tested modulus is below `2^51`; modular multiplication is exact. Each stored
root satisfies the exact-order tests. The panel dependency separately owns
primality and first-64 completeness.

## Implementation audit

The primary implementation uses an unordered multimap. The independent audit
uses a sorted vector of `(sum, packed pair)` records and binary search, so it
does not inherit hash-table lookup behavior. It replays the first, middle, and
last rows exactly. The full 64-row primary regeneration remains a bounded
Modal command.

## Operational audit

Final run `ap-3shnVd7pQ1dxDBBYN2Z7Ar` returned all 64 rows and zero worker
errors. Modal emitted an asynchronous-generator warning only while closing
the already completed local client; the final artifact was written with
`status=COMPLETE`, 64 ordered rows, and `relation_count=0`.
