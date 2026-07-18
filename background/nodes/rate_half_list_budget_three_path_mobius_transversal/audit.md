# Audit

## Scope checks

- The labels are the canonical path labels from the six-type table:
  singleton `3` and edges `02,12`.
- The result uses only the tight quotients; no constancy is assumed for the
  slack quotient `q_23`.
- "Exactly three" means fully `D`-split projective members of the fixed
  pencil. It is not a count of all split polynomials or all pencils.
- The first threshold is `d>=3`; the order-eight example has `d=2` and is
  deliberately outside it.
- The second threshold is `d>=6`, because one Mobius vote plus three
  exceptional votes gives the sharp elementary cap four.

## Sharp small-scale witness

After canonical relabeling, the exact `RS[F_17,mu_8,4]` witness has

```text
P_0=(X-1)(X-2),   P_1=(X-9)(X-4),
P_2=(X-13)(X-8),  P_3=(X-16)(X-15).
```

All four are `X^2+aX+2`, so at `d=2` the complementary point `w` can collide
with the single Mobius-transversal point and create a fourth split member.
The audit verifier checks this sharp exception and a root mutation.

The large-scale path type remains a genuine primitive split-pencil existence
problem.

The separate order-sixteen certificate supplies an exact `d=4` path witness
with only three first-pencil members. It does not contradict the theorem; it
confirms that the exact-three conclusion cannot itself be used as a path
exclusion.
