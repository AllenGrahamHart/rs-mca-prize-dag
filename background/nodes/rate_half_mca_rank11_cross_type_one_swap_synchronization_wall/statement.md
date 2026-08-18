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

The existing split-pencil one-swap synchronization compares packets sharing
31 records. Under either deployed anchor-density hypothesis, every connected
component of that 31-overlap packet graph has one fixed anchor pair type. It
therefore cannot synchronize cyclic or dihedral pencils across the 520
distinct types forced by the population router.

The separate atom-collision theorem does apply to two certificates sharing
only two slopes in its primitive root-free branch. Quotient atoms are a named
nonprimitive exception, however. For two distinct atoms sharing the sharp
28-record cross-type deck, its general collision inequality forces, after a
common-core shortening of size `c`,

```text
|G|>=1079711-c,
|G\H|>=1012239-c.
```

The latter remains `36336` below the distinct-pair agreement ceiling
`K'-1=1048575-c`, so current pair uniqueness does not eliminate this escape.

This is a method wall, not a counterexample to cross-type compatibility. A
closing theorem needs to pay the large-core collision output, prove stronger
quotient-specific rigidity, use a larger packet theorem, or install a direct
factor/chronology payment.

## Falsifier

Two distinct 18-anchored types in one 32-packet; cross-type overlap above 28;
a 31-overlap edge changing the unique anchor; or interpreting the wall as
evidence that compatible quotient types actually exist.
