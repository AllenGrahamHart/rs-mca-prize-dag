# KoalaBear m2 r4 diagonal c2 (1,1,2) source-line q-slice resultant gate

- **status:** PROVED
- **scope:** every saturated source-line `(1,1,2)` packet
- **dependencies:**
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_colored_quotient_compiler`
  and
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_internal_star_reconstruction`
- **consumer:** `rate_half_band_closure`

Put `q=P_(J_1)`, let `w` be the forced-square quotient label, and let
`K_mix={k_1,k_2}` be the two remaining common-`K` labels carrying the four
mixed `J_0-J_1` stars. Define

```text
G(T,W)=U(T,W)^2-W V(T,W)^2,
chi_mix(W)=(W-k_1)(W-k_2).
```

Every actual packet satisfies the degree-eight identity

```text
Res_T(q(T),G(T,W))
  ~ (W-w)^4 chi_mix(W)^2.                          (KBQS-1)
```

This includes the repaired forced-ramified case, where `w=0`. In the two
quotient branches the target quadratic is already known:

```text
aligned:       chi_mix ~ tau^*q,
near-aligned:  chi_mix ~ tau^*chi_Omega,
               Omega={xi,ell}.                    (KBQS-2)
```

Thus every one of the at most eight reconstructed source-deck pairs can be
rejected first by one quadratic-versus-quartic resultant and a projective
degree-eight coefficient comparison. Failure of `(KBQS-1)` deletes that
candidate before either degree-six partial resultant or the remaining
source rows are formed.

This gate does not assert that `(KBQS-1)` is sufficient for the colored
quotient identities. It does not delete every candidate, packet, aligned or
near-aligned branch, the `(1,1,2)` row, an owner, payment, row, or Prize
result.

## Falsifier

An actual saturated source-line `(1,1,2)` packet for which `(KBQS-1)` fails,
or for which the aligned or near-aligned target locator differs from
`(KBQS-2)`.
