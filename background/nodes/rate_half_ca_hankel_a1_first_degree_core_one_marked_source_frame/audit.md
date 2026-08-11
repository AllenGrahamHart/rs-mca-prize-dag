# Audit

- The common isotropy follows from symmetry and the complete minimal-vector
  coefficient chain; maximality is not claimed at this matrix size.
- Core contraction rescales source weights. It does not justify replacing
  them by the original received-word values or declaring them nonzero.
- The marked source is represented by a duplicate Vandermonde column. Any
  term selecting both copies vanishes, which is why `J` excludes `x_*`.
- The unmarked Cauchy--Binet terms sum to `det M=0`; they are not discarded
  termwise.
- Vandermonde squares are nonzero in the field, but no order or positivity
  exists and source-weight cancellation remains possible.
- `(MSF9)` is a necessary identity and does not promote the critical target.
