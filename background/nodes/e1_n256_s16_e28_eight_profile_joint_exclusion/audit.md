# Audit

The production engine uses folded signed chord classes. The independent audit
forms all 49 ordered products in the negacyclic ring and checks
anti-reciprocity before reading the profile. Both enumerate all 154 light
templates, `binom(124,3)` heavy supports, and 64 relative sign vectors, and
agree on every output row after removing runtime metadata.

The deterministic verifier replays every one of the 12,638 exceptional sparse
vectors, recomputes its profile, conductor, and third moment, and checks the
exact aggregate ledger. It verifies that the 4,372 norm inputs are exactly the
full-conductor subsequence.

FLINT and PARI use separate resultant implementations and agree in order on
all 4,372 outputs.

Modal applications:

```text
reduction probe:   ap-BEcZIXOVjDX7VcTVMin3Bd
production census: ap-PQuIHM0okhzDOzZI6rgd4Y
direct audit:      ap-ZWrJEBdrWedbKw7pdza9ho
exact norms:       ap-0LbmLFyAQLcHe8swtJKntb
```

The aborted application `ap-O0c99UzKohFBiFyJrHkEkS` failed during module
import and executed no mathematical task.
