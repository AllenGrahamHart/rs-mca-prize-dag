# Cycle 494: pair-pencil coprime-direction normal form

## Result: PROVED base-field rank-one reduction

In the rational rank-two branch, the determinant identities over `F[X]`
factor every pair difference through one fixed coprime direction:

```text
(a_p-a_0,b_p-b_0)=R_p(U,V).
```

Multiplication by `(U,V)` is injective, so the 520 or more distinct scalar
polynomials `R_p` lie in an `F`-linear space of dimension at most four.
Every pair-core intersection lies in the zero set of `R_p-R_q`; because each
core has size `m-2`, every listed nonzero difference has at least 134,940
distinct official-domain roots. The fixed direction has degree at most
913,635.

## Burn-down

```text
starting local pin:       28bb0329a
canonical prize pin:      0dd5b3244
upstream frontier pin:    PR #1173 at 2788d5ec3
DAG delta:                +1 PROVED normal-form node, +3 edges
critical status delta:    none
closed interface:         arbitrary rational pair pencil to rank-one support census
compute spend:            none
next action:              price common content or census the scalar family
```

## Nonclaims

- no equality between pair-core intersections and complete difference-root
  sets;
- no enumeration or payment of the scalar-polynomial family;
- no high-complexity payment, rank-eleven closure, or MCA closure.
