# Audit

1. The theorem uses only three complete copies, so the single deleted
   incidence in copy zero cannot be hidden in a coefficient correction.
2. Arbitrary nonzero row scales are allowed and become the values of the
   leading coefficient polynomial `A`.
3. The contradiction occurs before Hankel compatibility.  This makes the
   obstruction stronger for the stated embedding but not broader than it.
4. Coset-preserving means exactly `(i,x) -> tau_i x`, allowing arbitrary
   multiplicative representatives `tau_i`; arbitrary permutations within a
   copy are outside scope.
5. The locator-degree threshold is load-bearing.  Raising it above `n-1`
   invalidates the degree comparison in `(5)`.
6. The primary verifier checks the corresponding interpolation systems at
   five independent finite scales.  The audit verifier checks the cyclic
   exponent argument and hostile scope mutations independently.
