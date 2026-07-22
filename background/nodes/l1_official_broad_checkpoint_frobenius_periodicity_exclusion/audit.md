# Audit - broad-checkpoint Frobenius periodicity exclusion

1. The signed coefficients are literally `0,+1,-1` in the characteristic
   prime field; this is what permits Frobenius propagation.
2. The zero at exponent zero uses equal support sizes and is not inferred
   from Newton identities.
3. Orbit closure is modulo `n` and runs for the exact multiplicative order.
4. The complement `M` is a frequency set, not the unused domain complement
   from the split-value census.
5. Fourier inversion occurs in the ambient field containing `zeta`; `n` is
   invertible because it is dyadic and `p` is odd.
6. Support divisibility is sign-by-sign because coefficients, not merely
   supports, are periodic.
7. The verifier recomputes every table row from the 59-row source atlas.
8. Its largest bitset has 524,288 bytes; no large local or Modal run is used.
9. The theorem closes the seven broad rows only. It does not extrapolate the
   gcd pattern to the nine small-remainder rows.
