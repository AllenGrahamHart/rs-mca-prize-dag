# Claim contract

## Proved

- Primitive swap unions descend bijectively to half-order supports whose
  locators satisfy `(L_Y+c_Y)/Z=T_Y^2`.
- Trivial union stabilizer modulo antipodal exchange is equivalent to trivial
  scaling stabilizer of `Y`.
- Swap scaling orbits and half-order support orbits have equal counts.
- The half-order generator is deterministic and removes all sign choices.
- Equivalently, the locators are the divisors `ZT^2-c` of `Z^(n/2)-1` with
  the stated degree, scalar, and stabilizer conditions.

## Consumer

`f3_hge4_norm_gate_count`, through its primitive near-square union route.

## Falsifier

A primitive swap union whose squared support fails `(HOS1)`, or a primitive
half-order support satisfying `(HOS1)` whose reconstructed factors do not form
a primitive swap pair, falsifies the theorem.

## Nonclaims

- No upper bound on the number of half-order square supports is proved.
- No statement about free-stabilizer near-square unions is made.
- No efficient enumeration of every coefficient tuple `(T,c)` is claimed.
- The HGE4 aggregate remains open.
