# Consumer-backward audit - pma_exact_periodic_owner

Verdict: `NO ISSUE` after two statement repairs recorded below.

## Construction checks

1. **Quantifiers.** The received word is fixed before codewords are counted.
   An owner is a subset on which both candidate codewords equal that same
   word, so root uniqueness applies.
2. **Scale.** The exact stabilizer order determines the unique subgroup of a
   cyclic domain. Using merely a contained periodic scale would duplicate the
   full-support codeword across every divisor; the verifier keeps this as a
   mutation guard.
3. **Tail supports.** Agreement size may exceed `k+sigma`. Selecting the first
   `ceil((k+sigma)/M)` contained fibers still gives at least `k` points, so the
   owner remains injective without fixing the exact support size.
4. **Boundary `h_M=N`.** A proper exact-`M` support cannot contain every
   quotient fiber. Thus the class is empty for `M<n`; at `M=n` there is at
   most one full-support codeword.
5. **Profile identity.** For `h_M<N`, the conversion from `binom(N,h_M)` to
   `binom(N-1,h_M)` is the exact Pascal ratio `n/(n-A_M)`. No ambient field or
   chart cardinality enters.
6. **Large dyadic scales.** On the official grid, `(n-k)/2` lies in
   `[n/4,n/2)`, so the only omitted divisors are `n/2,n`. Their total is at
   most `2+1`; the rate-half `n/2` class is empty.
7. **Arithmetic.** QA.22 supplies the `M<=M_cut` dominance and `Q_2>=1`; the
   remaining absorption is a coefficient inequality. The Modal verifier also
   checks exact `n=2^13` binomials.

## Consumer checks

- The predicate uses the original source codeword's full agreement set, not
  the auxiliary PMA agreement set. It is therefore stable under defect-chart
  changes and repeated chart presentations.
- The owner must run before the full-petal/mixed-petal split. `imgfib` was
  repaired accordingly so the old full-petal periodic line is not added to
  the new global line.
- The theorem does not call exact stabilizer one primitive. Its downstream
  scope theorem separates the folded-receiver class, which is periodic, from
  algebraically folded/nonfolded-receiver and low-defect objects, which remain
  in the red PMA obligation.
- The general owner formula and the official `sigma=1` absorption are distinct
  statements. The audit repaired wording that could have exported the `719`
  line to general reserve.

No status promotion of `pma_wide_residual` follows from this supplier.
