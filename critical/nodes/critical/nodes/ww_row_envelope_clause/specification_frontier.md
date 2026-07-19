# W3 specification frontier

Status: OPEN SPECIFICATION INPUTS. This note records a bounded source audit;
it is not a mathematical close or evidence that the envelope is true.

## What can be reconstructed

The repository fixes the threshold shape

```text
B* = floor(q_line / 2^128)
```

and proves the aggregate consumer law once a disjoint paid/residual ledger is
available. It also supplies exact formulas for individual planted and dyadic
quotient-staircase constructions. Those ingredients determine how a completed
row certificate must be checked.

## What is not present

1. **Official row registry.** W3 quantifies over every official row, while
   `w2_spend_map_20260710.py` prints selected RowC, prize, and maximum rows.
   No machine-readable asset states that this finite list is the complete W3
   scope, and `list_adjacency_closing` instead says every admissible row.
2. **Exact field line per row.** The W2 script uses `T=2^128` as the
   conservative `log2(q)=256` edge and explicitly notes that the specification
   has `|F|<2^256`. It therefore does not print the exact `q_line` required by
   W3 for each row.
3. **Paid-column table.** `dyadic_profile_evaluation/proof.md` says its values
   match `qa22_staircase_budget.json`, but no file with that name or an
   equivalent complete QA.22 paid-column ledger is present in this worktree.
   The available proof packets print selected logarithmic margins, not every
   exact integer subtraction defining `P_paid(U)`.
4. **Ownership theorem.** `worst_word_planted/statement.md` asserts that the
   E15 mixed-petal challenger is the quotient-coset staircase, but the only
   detailed E22 proof classifies challengers by petal-touch patterns. No
   full-scope proof maps every such official challenger into the paid
   staircase column. W3 therefore cannot erase the residual class using that
   assertion.

Consequently, the current repository cannot instantiate even the left side of
the requested row-certificate format without adding assumptions. MCA-side
QA.22 candidate margins must not be substituted for the list-side per-word
ledger.

## Minimal materialization packet

A close attempt must first emit one machine-readable registry containing:

- the complete row key `(characteristic, extension degree, n, k, sigma)` and
  exact generated field for every W3 row;
- exact `q_line`, `B*`, and the selected minimum-#493 branch;
- an ordered list of paid column descriptors, exact counts or sound
  allocations, and provenance for each count;
- a coverage/disjointness certificate for the paid first-match assignment;
- the residual cell grammar and a proof that it covers every layout, scalar
  choice, and received word;
- exact residual allocations whose aggregate is at most `B_chal(U)`.

The registry verifier must reject omitted rows, omitted paid columns, negative
residuals, overlapping ownership, and non-integral or logarithmic substitutes
for exact counts.

## Disposition

W3 remains `TARGET`. Further numerical challenger censuses are not the next
step: they cannot close the missing row and ownership quantifiers. Resume this
lane when the official registry and QA.22 integer ledger are available, or
when a uniform structural theorem bounds the residual class without rowwise
enumeration.
