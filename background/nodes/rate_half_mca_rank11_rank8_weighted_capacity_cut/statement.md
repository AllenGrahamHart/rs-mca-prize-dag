# Rank-eleven rank-eight weighted capacity cut

- **status:** PROVED
- **closed interval:** `37996<=K'<=1048576`
- **first method crossing:** `K'=37996`

For the weighted fixed nine-subset supplied by the component concentrator,
the rank-eight affine-owner alternative is impossible whenever

```text
37996<=K'<=1048576.
```

At the last open row for this method,

```text
K'=37995:
demand =579135903691691071,
cap    =579154077989218305.
```

At the first closed row,

```text
K'=37996:
demand =579191514708840299,
cap    =579155144020629315,
gap    =36370688210984.
```

The unrounded demand/cap ratio is strictly increasing, so the contradiction
persists through the deployed endpoint.

## Nonclaim

Rank eight remains open for `10<=K'<=37995`. The kernel lane remains open
from `K'=4599` onward, and rank eleven is not paid.
