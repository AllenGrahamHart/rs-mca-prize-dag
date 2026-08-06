# Audit

1. `N(v)` counts all subsets of the chosen half-system; it is not restricted
   to one Hamming slice.
2. The factor `2^-S` in `(L2-1)` comes from freely adding the common
   intersection.  Omitting it changes the target by an exponential factor.
3. The map uses odd moments and the column weight `y`.  It is a restricted
   weighted-prefix instance, not automatically the standard unweighted
   coefficient-prefix map in upstream `(Q)`.
4. A max-fiber bound implies an L2 bound, but the converse need not hold.
   The F2 terminal only asks for the printed L2 collision estimate.
5. The zero Fourier mode is exactly `2^S/p^R`; non-generating rows fail when
   this entropy-average term is already exponential.  Generating rows leave
   the nonzero Fourier mass as the honest obstruction.
6. The list-recovery translation has agreement one and coordinate-list size
   two, but the code rate is `1-R/S` and the evaluation set is the explicit
   dyadic half-system.  Results for random or generic evaluation points, or
   with a fixed gap from list-recovery capacity, do not automatically apply.

Modal app `ap-Lik7i7u6TSwxHdBhbDIxzK` independently enumerated both sides on
four finite half-systems.  All 4,688 ordered collisions and 404 kernel words
matched the exact normalization, and the verifier returned PASS.

The addendum rerun in Modal app `ap-aKhhNL94Wn8oytoS1Fu1dB` also checked
all 753 nonempty finite fibers against their induced two-symbol list-recovery
instances.  Every list size matched and the full verifier returned PASS.
