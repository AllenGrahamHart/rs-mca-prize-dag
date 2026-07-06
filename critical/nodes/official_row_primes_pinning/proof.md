# Proof: official row primes pinning

Status recommendation: PROVED, by citation/reframe.

## Claim

There is no finite list of literal "official row primes" to pin from the ABF
grand-challenge statement.  The challenge quantifies over admissible
Reed-Solomon codes over fields `F`, with a sufficiently-large-field proviso.
Thus certification obligations are either:

- family-uniform over the admissible field/rate/domain class; or
- exhibit-specific, naming the exact field used by the certificate.

## Citation

The page-5 grand-challenge boxes in `abf26.pdf` state the MCA and list tasks for
Reed-Solomon codes over a smooth domain `L` in a field `F`.  The relevant
fragments are pinned in `official_row_primes_reframe.json` against PDF sha256

```text
426a979c13cc61db0f2cdb909067ef4c9f24438859fe0a7a337d2b19b07fcaa5
```

The decisive fragments are:

- `assuming |F| is sufficiently large`;
- `for every choice of F, L, and k`;
- `k <= 2^40`;
- `|F| < 2^256`.

These are admissibility and quantifier conditions, not a list of prescribed
prime constants.

## Consequence

The old red-node wording asked for "authoritative literal row primes" before
certifying official rows.  That request is misframed.  A certificate that uses a
stand-in prime remains an exhibit/calibration certificate unless it is paired
with a transfer theorem.  But the prize statement itself does not require
recovering hidden official primes.

Therefore the node closes by replacing the missing-prime ask with this rule:

```text
Every certificate must declare whether it is uniform over the admissible
family or tied to a named exhibit field.
```

No additional prime list is a prerequisite of official-row certification.
