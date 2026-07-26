# E1 certificate false-green audit

## Ruling

The E1 folded-certificate branch was green for two incompatible reasons:

1. `e1_folded_no_vector_certificate_128_payload` cited a rounded fpylll
   shortest-vector observation with no banked exact output or completion
   certificate.
2. `e1_folded_no_vector_certificate_256_payload` had been rewritten in
   `dag.json` as an almost-all-primes density estimate while its folder
   statement and `req` consumer still demanded a complete zero-vector
   certificate in one named field.

Neither leaf met its printed contract. Both are restored to `TARGET`, and the
automatic consumer chain is regressed to `CONDITIONAL` through `mca_unsafe`.

## The N'=128 gap

The only historical executable is now retained at
`background/nodes/e1_folded_no_vector_certificate_128_payload/notes/modal_e1_cert.py`.
It computes a lattice, runs BKZ, attempts `SVP.shortest_vector`, catches every
exception, and returns rounded summaries. The returned schema does not say
whether exact SVP completed. No exact primitive root, basis, shortest vector,
proof log, result JSON, source-image pin, or independent checker is banked.

A BKZ vector gives an upper bound on the shortest norm. It cannot prove that
there is no shorter box vector. The historical `31.67 > 16` observation is
therefore evidence, not a certificate.

## The N'=256 mismatch

The no-vector leaf is a premise of
`e1_folded_certificate_cell_256_payload`, whose conditional proof requires
zero nonzero vectors in `{-2,-1,0,1,2}^128` over the named field. The density
calculation in `PRO_W3_e1_density.md` instead averages bounded norm divisors
over primes. It gives at most an asymptotic almost-all-primes statement about
folded-vector survivors.

That estimate does not:

- certify the named Pocklington prime;
- prove a zero-vector statement;
- provide a finite explicit prime-counting error at the 250-bit scale;
- convert coefficient-vector survivors to the collision multiplicity consumed
  downstream; or
- prove the family-uniform quantifier required for every admissible input code.

The estimate remains useful partial evidence through
`are_exceptional_density`; it cannot inhabit a no-vector certificate node.

## Quantifier fence

The challenge has no hidden finite list of official primes. A named exhibit
certificate proves only that exhibit. An almost-all-primes theorem proves only
typicality. The complete prize route needs one of:

- a route-uniform theorem over every row assigned to the E1 supplier;
- a proved total per-input certificate procedure whose exact output is checked
  for the supplied code; or
- a formally narrowed exhibit claim that is not used to prove the grand
  family-uniform theorem.

## Status delta

Direct leaves:

```text
e1_folded_no_vector_certificate_128_payload  PROVED -> TARGET
e1_folded_no_vector_certificate_256_payload  PROVED -> TARGET
```

Regressed automatic consumers:

```text
e1_folded_certificate_cell_128_payload       PROVED -> CONDITIONAL
e1_folded_certificate_cell_256_payload       PROVED -> CONDITIONAL
e1_folded_certificate_manifest_payload       PROVED -> CONDITIONAL
e1_open_cell_control_payload                  PROVED -> CONDITIONAL
e1_official_typicality_or_certificate         PROVED -> CONDITIONAL
e1_official_prime_exception_control           PROVED -> CONDITIONAL
e1_fullness                                  PROVED -> CONDITIONAL
zone_b                                       PROVED -> CONDITIONAL
mca_unsafe                                   PROVED -> CONDITIONAL
```

Subsequent quantifier audit: this regression was necessary but not sufficient.
The named-exhibit branch cannot discharge the universal prize statement even
if both leaf certificates close. It is now background evidence, while
`e1_official_prime_exception_control` is a direct family-uniform `TARGET`; see
`E1_NAMED_EXHIBIT_QUANTIFIER_AUDIT_20260726.md`.

## Compute decision

No Modal job was launched. Repeating the old fpylll run would only reproduce
an unaudited observation. A future run is authorized only after an exact
certificate schema and independent checker exist. The `N'=256` zero-vector
claim should be falsified or re-routed before any expensive exhaustive search.

## Burn-down

- **our starting pin:** `a938a37b`
- **canonical prize pin:** `cc979e4befcbc42e1cb2725661941c037e4662ab`
- **upstream main pin:** `b13de8113a03f06b6fc22bbd2f289a8abcdf7e95`
- **result:** `FALSIFIED` as a proof packet; mathematical no-vector truth is
  unresolved
- **delta-star movement:** none
- **new assumptions:** none
- **live compute request:** none; exact-certificate design is prerequisite
- **next route-deciding action:** attack the route-uniform E1 quantifier or a
  different closure-capable critical red, rather than repeating BKZ

Follow-up: `UNSAFE_AT_CROSSING_FALSE_GREEN_AUDIT_20260726.md` established that
E1 is only a supplier route. Universal row coverage now belongs to
`unsafe_crossing_family_instantiation`.
