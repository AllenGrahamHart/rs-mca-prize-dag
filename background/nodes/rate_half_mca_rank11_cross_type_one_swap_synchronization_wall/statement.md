# Cross-type one-swap synchronization wall

- **status:** PROVED
- **scope:** order-32 rational packets used to synchronize heavy-ruling pair
  types

Call a 32-record packet `a`-anchored at a pair type when it contains at least
`a` records owned by that type. For `a>=17`, the anchor type is unique. If two
packets are anchored at different pair types, their overlap is at most

```text
64-2a.                                                  (SW1)
```

Consequently:

```text
a=18: cross-type overlap <=28,
a=20: cross-type overlap <=24.                         (SW2)
```

The existing one-swap synchronization and primitive certificate-collision
tools compare packets sharing 31 records. Under either deployed anchor-density
hypothesis, every connected component of the 31-overlap packet graph has one
fixed anchor pair type. Those tools therefore cannot synchronize cyclic or
dihedral quotient pencils across the 520 distinct types forced by the
population router.

This is a method wall, not a counterexample to cross-type compatibility. A
closing theorem needs rigidity from at most 28 shared records, a larger packet
theorem, or a direct factor/chronology payment.

## Falsifier

Two distinct 18-anchored types in one 32-packet; cross-type overlap above 28;
a 31-overlap edge changing the unique anchor; or interpreting the wall as
evidence that compatible quotient types actually exist.
