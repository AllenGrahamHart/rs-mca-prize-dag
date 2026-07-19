# M1 result audit

- **status:** experiment certificate verified; evidence only
- **result:** C2'' survived its first preregistered adversarial round
- **nonclaim:** this does not prove C2'', B-WEAK, or the DLI target

`verify_m1_result.py` independently reads the emitted
`m1_dli_m1_results.json`; it does not import the experiment driver. It checks
the complete 45-row preregistered grid, both depths, all empty sub-orbit anomaly
flags, and the exact F-a octave rule. It then reconstructs the 32 F-c rare
windows, the Poisson-binomial exceedance test, and the Poisson orbit-quanta
test.

The replay obtains:

```text
F-a fired depths: 0 (kill requires at least 2)
F-c primary:      X=0, p=0.02581
F-c secondary:    T=2, lambda=4.350, p=0.3823
```

Both p-values exceed the preregistered `10^-3` kill line. No fractional orbit
quanta are present, so the secondary read is scored legitimately. C2'' is now
eligible to become a route predicate under the pre-existing F-round rule, but
that route surgery remains separate from this evidence audit.
