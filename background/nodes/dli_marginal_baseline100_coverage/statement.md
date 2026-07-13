# DLI marginal 100-bit baseline assembly

- **status:** see `dag.json`

For an official prize row `R`, write

```text
E_L(R) = E_U[rho_L],
A(R)   = product_(L=1)^34 E_L(R).
```

Assume the two wired predicates at every production level:

```text
C1':       E_L - 1 <= 4 r_L (1 + W_cl(R,L)),
WCL-ZONE:  W_cl(R,L) <= 1/32.
```

The official schedule has `N_L=256L`, and the field pin `q<2^256` gives
`r_L=q^L/2^N_L<1`. Consequently

```text
E_L <= 1 + 4(1 + 1/32) = 41/8,
A(R) <= (41/8)^34 < 2^100.
```

The final comparison is the exact integer inequality `41^34<2^202`.
`conditional.md` gives the complete proof, and `verify.py` checks the pins and
eleven fail-closed mutations.

This assembly contains no cross-level joint-correlation claim. The separate
`dli_c2pp_joint_reserve` predicate supplies the 21-bit C2'' reserve. It also
contains no endpoint certificate, reserve credit, residual certificate, or
typical-prime assumption.
