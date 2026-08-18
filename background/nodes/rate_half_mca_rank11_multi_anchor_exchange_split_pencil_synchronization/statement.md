# Multi-anchor exchange synchronization

- **status:** PROVED
- **scope:** every triple-owner heavy-ruling pair type with at least 29
  first-owned records

Let `p` be any triple-owner pair type owning `r>=29` slopes. Re-base the
parent's core-recovery packet at `p`. There are `t` secondary pair types,
where `1<=t<=4`, and three fixed records are chosen from each. Hence the
anchor contributes

```text
s=32-3t in {29,26,23,20}.
```

Fix core-saturated exact supports once for all `r` anchor records and the
fixed secondary records. A base `s`-subset and the one-swap packet for every
remaining anchor slope give the unconditional alternative:

1. some admissible packet emits `chi>=2299571`; or
2. every packet is rational and one fixed coprime polynomial pencil of
   degree `1..11` contains all `r` anchor exception locators.

The conclusion is per pair type. Different pair types may have different
pencils.

## Falsifier

A triple-owner type with `r>=29` that cannot be used as the packet anchor,
more than four secondary component-difference generators, a packet with
fewer than 20 anchor records, packet-dependent core cancellation after fixed
support choice, or rational one-swap pencils that share two independent
locators but remain distinct.
