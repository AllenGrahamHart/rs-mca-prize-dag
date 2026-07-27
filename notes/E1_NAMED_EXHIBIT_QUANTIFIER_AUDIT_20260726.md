# E1 named-exhibit quantifier audit

Date: 2026-07-26

## Ruling

The former critical route

```text
two named N'=128,256 no-vector certificates
  -> named-exhibit manifest
  -> e1_official_prime_exception_control
  -> e1_fullness
```

did not preserve quantifiers. The certificate soundness theorem is valid for
the exact field/root named by a complete transcript. The grand challenges are
not posed over two hidden official fields: the pinned ABF statement says "for
every choice of F, L, and k" under its admissibility conditions. A finite set
of exhibit certificates therefore cannot imply uniform control over every row
assigned to the direct E1 route.

The authoritative source packet is
`background/nodes/official_row_primes_pinning/official_row_primes_reframe.json`,
which pins `abf26.pdf` at SHA-256
`426a979c13cc61db0f2cdb909067ef4c9f24438859fe0a7a337d2b19b07fcaa5`.

## Status consequences

- `e1_official_prime_exception_control` is re-posed as a `TARGET` over every
  row assigned to the direct E1 route.
- As an unresolved logical leaf, it has no `req` parents. The proved official
  quantifier pin and three former certificate-route inputs have `ev` edges only.
- The 14 quantifier-pin/named-exhibit/certificate nodes are retained under
  `background/nodes/`; their printed mathematical statuses are unchanged.
- `e1_fullness` remains `CONDITIONAL` on the corrected route-uniform target.
  The follow-up unsafe-side audit makes this E1 chain an evidence route to the
  universal row payload rather than a complete row router.

This is a route-sufficiency correction, not a counterexample to the corrected
route-uniform statement. No claim is made here that direct-E1 control is true
or false. Non-generating ambient extension rows remain admissible globally;
their unsafe-side payload is owned by `unsafe_crossing_family_instantiation`,
not silently discharged by the safe-side `f1_case_tower` theorem.

## Correct closure standard

One of the following is required:

1. a route-uniform theorem proving the exact exceptional-incidence budget for
   every row assigned to direct E1; or
2. a complete per-input theorem/certifier whose termination, soundness, and
   coverage are proved for every assigned row.

Named exhibits, birthday scans, heuristic lattice reduction, and finitely many
complete transcripts are evidence or partial results only unless a transport
theorem supplies the missing route-wide quantifier.

## Orbit consequence

The mathematical critical orbit changes from
`260 = 190 PROVED / 45 CONDITIONAL / 25 TARGET` to
`246 = 183 PROVED / 39 CONDITIONAL / 24 TARGET`. This removes two
exhibit-specific targets and installs one correctly scoped route-wide target;
it does not close mathematical work. The submission orbit remains the math
orbit plus its fixed 15-node packaging spine.

These counts record the E1 audit in isolation. The subsequent
`unsafe_at_crossing` false-green correction changes the live orbit again; its
audit and generated census are authoritative for the current frontier.

The correction is fail-closed by
`tools/verify_e1_certificate_status_regression.py` and the ordinary DAG,
orbit, propagation, and critical/background partition verifiers.
