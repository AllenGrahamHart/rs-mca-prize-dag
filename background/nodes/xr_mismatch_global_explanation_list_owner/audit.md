# Audit

## Verdict

The ownership bound is a union bound over distinct global codeword pairs, not
over local nodes or locator histories. Deduplication is legitimate because
the true-tangent injection depends only on the final pair and its discrepancy
support. A slope is assigned to its first terminal event, so it is never paid
twice.

## Boundary checks

- The root subtraction is necessary: the already-paid root tangent column can
  contain up to `n-A` slopes and is outside the mismatch residual.
- The factor is `n-A`, not a local `N_j-A_j`; every lifted pair is compared
  on the original domain and has at least `A` common agreements.
- The interleaving comparison concerns common-support agreement. Separate
  supports in the two components would not define `E_A(u,v)`.
- The equality `E<=L_A` requires `L_A^2<q`. Without it, only `(GEO4)` is
  available.

## Limitations

The theorem does not show that the relevant ordinary list has size `O(n^2)`.
It also gives no control over slopes whose first terminal event is a generic
full-zero chart. Therefore it removes a recursion multiplier but does not
promote the critical bridge.
