# General star records do not universally inject into minimal trades

- **status:** PROVED
- **closure:** exact finite-field counterexample and complete census

Let `D=F_17^*`.  An unordered disjoint pair `(P,Q)` of `h`-subsets is a
general order-`t` star-PTE record when

```text
e_j(P)=e_j(Q)  for 1 <= j <= t.
```

Call it minimal at width `h` when these equalities hold through `j=h-1`,
the F-4/constant-shift condition used by the current `u1` tail ledger.
Then:

1. `P={1,2,3}` and `Q={4,5,14}` form a general order-1, width-3 record,
   but they contain no width-2 minimal subrecord and are not themselves
   minimal.
2. There are exactly `4576` unordered general order-1, width-3 records on
   `D`.
3. The numbers of unordered minimal records at widths `1,...,8` are

   ```text
   120, 364, 352, 126, 0, 0, 0, 1,
   ```

   for a total of `963`.  Excluding the vacuous width-1 padding leaves the
   current width-`2,...,8` total `843`.

Consequently there is no multiplicity-one injection from all general
order-1, width-3 records into the entire minimal-record ledger, even if the
target is generously enlarged to include width 1.  In particular, neither
subset peeling nor a scale-free algebraic general-to-minimal injection can
supply `x4_primitive_star_u1_coverage`.

This is a route cut, not an official-row counterexample.  Here `n=16` and
`|F|=17<n^2`, and no quotient/dihedral/moment/U2/DLI first-owner partition
has been imposed.  The critical target may still hold by an official-row,
strip-aware classification, or after broadening `u1` to count general
order-`t` records and proving a new budget.
