# Whole-line global-core cancellation router

- **status:** PROVED
- **closure:** exact line-global corollary of common-core cancellation
- **scope:** one declared selected explanation state per residual slope on one
  received line

## Statement

Let `Z` be a finite set of at least two distinct support-wise MCA-bad slopes
on one Reed-Solomon received line. For every `gamma in Z`, fix one declared
degree-`<k` explanation `h_gamma`, its maximal agreement support
`S_hat_gamma`, and an actual size-`m` noncontained witness inside that
support. Define the line-global core

```text
C_* = intersection_(gamma in Z) S_hat_gamma,
c_* = |C_*|.
```

Exactly one of the following holds.

1. All selected explanations lie on one global codeword line
   `h_gamma=A+gamma B`.
2. `c_*<k`, and one simultaneous application of common-core cancellation
   maps the entire selected slope set to the unique shortened row

   ```text
   (n',k',m')=(n-c_*,k-c_*,m-c_*).
   ```

In the second case every slope has an actual size-`m'` same-support bad
witness in the shortened row. The slope map is the identity, its fibers have
size one, and `m-k`, `n-k`, and `n-m` are preserved. There is one global
core family, so no sum over record-local cores or core-choice add-back occurs.

For the imported KoalaBear staircase this gives one exact router:

```text
global affine                                      -> GLOBAL_AFFINE
s=k-c_* <= 2                                      -> paid fixed-core family
3 <= s <= 13 and direction separation holds       -> paid affine-span family
3 <= s <= 13 and direction separation fails       -> DIRECTION_LIST_SHORTENED_S
s >= 14                                            -> GLOBAL_CORE_SHORTENED_S_GE_14
```

The last two outcomes are residual labels, not payments.

## Consequence

This is a correct line-global alternative to assigning each critical record
its own core. It resolves exactly-once slope ownership and projection-fiber
multiplicity for the cancellation step. It may lose the favorable small
dimension of individual local cores because `C_*` is their intersection.

## Nonclaims

The theorem does not bound either residual label, prove first-match coverage,
define Q or BC, or close a deployed or prize row. It does not permit adding
payments from larger record-local cores after the global route is chosen.

## Falsifier

A selected non-global-affine line with `c_*>=k`; failure of simultaneous
cancellation or badness preservation for one selected slope; a nonidentity
slope fiber; or a claimed paid outcome outside the printed gates.
