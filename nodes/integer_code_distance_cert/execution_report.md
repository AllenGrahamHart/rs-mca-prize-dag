# integer_code_distance_cert execution report

- **status:** red left in place
- **closure attempted:** execute and record the previously banked certifier
- **verifier:** `python3 tools/verify_integer_code_distance_cert_report.py`
- **artifact:** `nodes/integer_code_distance_cert/execution_report.json`

## Verdict

This node should not be flipped on the current base.

The only located "requirements-met" artifact is the C-4 toy totality anchor
from the old `rs-mca-c4-certifier-pipeline` worktree.  I replayed it.  It
certifies the toy row

```text
N_prime = 16
p = 12289
weight <= 6
```

by two independent finite enumerators: split MITM and branch-and-bound.  Both
enumerators produce the same relation set.  The set has 288 relations, all of
which are the expected antipodal cyclotomic relations, and there are zero
non-cyclotomic relations.

That is a valid toy totality anchor and format exemplar, but it is not the
official-row certificate required by `integer_code_distance_cert`.

## What Was Executed

From `rs-mca-c4-certifier-pipeline`:

```bash
python3 experimental/scripts/verify_c4_certifier_pipeline_toy.py --json | python3 -m json.tool >/tmp/c4_certifier_pipeline_toy_checked.json
python3 experimental/scripts/verify_c4_certifier_pipeline_toy.py
```

Observed summary:

```text
C-4 certifier pipeline toy
status: TOY_TOTALITY_ANCHOR / DIRECT_MOD_P_MITM
N'=16, p=12289, w<=6, relations=288, noncyclotomic=0
```

The corrected direct-MITM cost table for the real `N_prime = 128` scale was
also recorded:

| w | log2 states |
|---:|---:|
| 12 | 38.336607 |
| 14 | 43.459989 |
| 16 | 48.378852 |

## Why This Does Not Close The Node

The node statement asks for a certificate that the fixed row-specific integer
matrix has no ternary kernel vector of support at most the full `2l_prime`
bound beyond cyclotomic relations.

On the current minimal base, `nodes/integer_code_distance_cert/` contained
only `statement.md`.  The adjacent dependency `multi_multiplier_reduction` is
marked `REFUTED`, so the old multi-multiplier matrix route cannot be silently
used.  I did not find a row-specific explicit matrix, row descriptor, allowed
cyclotomic-relation basis, or machine-checkable full-row certificate.

The node therefore remains red.  The next concrete closure packet needs the
official row object plus one of:

1. a deterministic exhaustive verifier over the required weight range;
2. a proof-logged finite certificate;
3. a row-specific lattice/cone certificate with a checker.

