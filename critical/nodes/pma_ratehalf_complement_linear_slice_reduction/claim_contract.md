# Claim contract - PMA rate-half complement linear-slice reduction

## Proven

1. The normalized CRT polynomial factors as `L_1 Etilde`, with `Etilde` a
   unit modulo `L_2L_3`.
2. Complementing an exact support changes the guarded map into multiplication
   by `Etilde` followed by a low-coefficient projection.
3. Exact contributors are in bijection with the guarded split divisors (LS6).
4. The unguarded slice has exact dimension `ell-a+1` and codimension
   `ell+a-1`.
5. Its degree-`<=2ell-a` truncation is exactly the proved three-petal
   mu-basis space; on a nonempty guarded upper-branch cell its dimension is
   `ell-2a+2`.
6. The resulting object is a BC/SCK-shaped split-in-subspace atom, not an
   identified instance of the F2 Frobenius-moving-sector theorem.

## Still open

Bound or profile-own the monic split divisors of `L_C` in (LS6), uniformly in
the source cross-ratio, generated field, smooth core, and tail parameters.

## Consumer effect

Use this theorem as evidence for `petal_mixed_amplification` and
`shared_census_kernel`. It proves no census estimate and changes no critical
status. The mu-basis reconciliation recovers existing parameter freedom; it
must not be advertised as an additional dimension saving.
