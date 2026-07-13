# DLI primitive-ledger zone coverage

- **status:** see `dag.json`

At every official production row, after generated-field normalization and
first-owner de-duplication of multiplier shadows and level lifts, every one of
the 34 levels `L=1..34` satisfies

```text
W_cl(R,L) <= 1/32,                                 (WCL-ZONE)
```

where `W_cl` is exactly the C1' primitive signed-shift ledger

```text
sum_(primitive O, L+1<=w(O)<=L+5) 2N_L*2^-w(O),
N_L=256L.
```

Equivalently, every official row admits a complete per-level certificate for
that inequality. A certificate must pin the row and generated field, prove
the primitive ledger complete in the stated weight window, and prove
multiplier/lift ownership. A density bound over primes or a list of merely
exhibited relations is not coverage.

No C1' inequality, C2'' joint reserve, residual near-peak bound, or final
endpoint check is part of this statement. In particular, the old
reserve-credit mechanism is absent.

