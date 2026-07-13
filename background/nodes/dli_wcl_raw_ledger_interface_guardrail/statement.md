# DLI WCL raw-ledger interface guardrail

- **status:** PROVED
- **closure:** deduction

## Statement

The `W_cl` quantity consumed by C1' is the raw weighted sum over every reduced
primitive signed-vanisher orbit in the window:

```text
W_raw = sum_(primitive O, L+1<=w(O)<=L+5) 2N*2^-w(O).
```

Multiplier shadows, additive clusters, and level lifts may classify orbit
families, but they do not remove primitive lattice points from the per-level
Fourier excess. Consequently the WCL-ZONE premise used in the 100-bit baseline
must be `W_raw<=1/32`. A first-owner sum that deletes later multiplier or lift
orbits is not a valid substitute unless a separate theorem charges every
deleted orbit's full weight to its owner.

At the actual low production dimensions `ell in {1,2,4,8}`, `W_raw<=1/32`
is equivalent to an empty primitive window. Thus the terminal exclusions and
the canonical `ell=2` emptiness falsification program are unchanged by this
interface repair. Starting at `ell=16`, the exact raw weighted count matters.

## Nonclaim

This does not prove WCL-ZONE or assert that a multiplier/lift family violates
it on an official row. It proves which ledger the existing C1' implication
requires.

## Falsifier

A derivation of C1' in which multiplier/lift-related primitive orbits are
deleted without their weighted mass appearing elsewhere, or a downstream
baseline proof that does not consume the same ledger as C1'.
