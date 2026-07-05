# c1_scalable_certificate

- **status:** CONDITIONAL
- **closure:** proof
- **refs (legacy repo):** ['experimental/notes/roadmaps/a_pilot_wh_torsion_data.md']

## Statement

The (A) closure needs a scalable certificate for the absence of non-toral
mod-p solutions of the anchored system

```text
rem(X^n - 1, S^2 - S(1)^2) = 0
```

at `n = 1024`, for every `h` in the official window and for the six official
primes. Direct elimination is infeasible. The certificate is decomposed into:

- bottom-window direct certificates (`c1a_lowh_direct_certificates`);
- the proved descent-injection certificate (`c1b_descent_injection`);
- the remaining mid/large-`h` certification (`midlarge_h_certification`).

## Ledger

CONDITIONAL (Codex critical pass): this is an assembly node. It remains open
exactly because `c1a_lowh_direct_certificates` is conditional on prime pinning
and `midlarge_h_certification` is still a target.
