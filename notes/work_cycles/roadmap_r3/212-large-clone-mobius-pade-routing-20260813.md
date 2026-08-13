# Cycle 212: large-clone Mobius and Pade routing (2026-08-13)

## Selection

The live upstream `(E)` exception terminal and PR `#1156` leave one unique
coordinate-clone class of size at least `m`. Subcritical classes already have
a simultaneous `2n` payment. This cycle attacked that exact residual rather
than adding another support-only packing bound.

## Result

Two proved routers were added.

First, an irreducible common `(1,1)` owner-pencil component has the exact
Mobius pullback

```text
Qhat=(c+d gamma)Q_0-(a+b gamma)Q_1,
Nhat=(c+d gamma)(A_0+gamma B_0)
     -(a+b gamma)(A_1+gamma B_1),
```

with slope degrees one and two and `Nhat=Qhat(r_0+gamma r_1)` on every
clone coordinate. If the denominator coefficients span one polynomial
direction, every clone of size at least `m+1` cancels to one fixed coherent
rational owner. At size exactly `m`, the sole obstruction is
`mu Lambda_C` at the denominator-zero parameter.

Second, in denominator rank two, writing

```text
Qhat=q_0+gamma q_1,
Nhat=p_0+gamma p_1+gamma^2 p_2
```

produces the exact Padé remainder

```text
Omega=q_1^2p_0-q_0q_1p_1+q_0^2p_2.
```

It vanishes on the clone and has degree at most `m+2d`. Above that root
wall it vanishes identically and the moving pencil becomes one fixed owner
of reduced denominator degree at most `2d`. At equality it is zero or a
scalar clone locator. The moving support bands therefore end at
`1250992` (KoalaBear) and `1250920` (Mersenne-31).

## Audit

The clone coordinates remain owner incidences, not selected-support roots.
The degree-`2d` owner is not fed to the current degree-`d` large-owner
theorem. The equality locator residues and the finite moving support bands
remain open. Two independent checkers replay the Mobius identities, factor
boundary, Padé remainder, division identity, official walls, and hostile
metadata controls with constant memory.

```text
start:                   fc74e16cd
result:                  NARROWED; +2 PROVED large-clone routers
DAG delta:               +2 PROVED background nodes, +6 edges
critical status delta:   none; the MCA exception route is sharpened
upstream terminal delta: PR #1156 unique large clone split into exact leaves
delta-star movement:     none
compute:                 bounded local exact arithmetic; no Modal spend
next route action:       attack the c=m locator remainder first, then the
                         finite moving band or degree-2d owner reduction
```
