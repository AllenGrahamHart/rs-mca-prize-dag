# Proof

Write `m=df`, let `s=(d+f)^2` be its source squared-sum record, put
`z=1/d`, `y=z^2`, and set `q=de`. Then

```text
f=mz,  e=qz,
M(y)=1+(2m-s)y+m^2 y^2=0.                         (1)
```

The colored pair in matching 3 is

```text
C(z)=Pair(bmz,sigma_c cmz).
```

It is quartic. Split it uniquely as `C(z)=E(y)+z O(y)`, where `E` is
quadratic and `O` is linear. Every root of `C` satisfies the sign-free
quartic

```text
K(y)=E(y)^2-y O(y)^2=C(z)C(-z)=0.                (2)
```

Divide `K` by the quadratic `M` in the exact four-basis source tower. Each
of the eight source-sign/`sigma_c` rows has linear remainder
`R(y)=r_0+r_1y`. If `M(y)=p_0+p_1y+p_2y^2`, a common root forces

```text
r_1^2 p_0-r_1 r_0 p_1+p_2 r_0^2=0.              (3)
```

The compiler norms (3) through the basis `1,t,b,bt`. Its candidate set is
the union of all roots of the norm numerator and denominator and all
inverse-guard numerators and denominators. It then lifts each candidate
through the base `t` quadratic, the `b` quadratic, linear `c` recovery, and
the compact kernel. At every guarded source point it intersects the full
quartics `M(z^2)` and `C(z)`; thus the sign-free elimination introduces no
accepted spurious lift.

Across eight rows the norm has degree 1112. The complete candidate union has
60 `r` roots. There are 56 guard terminals, 16 no-lift terminals, and 16
guarded source points. Eight common `z` lifts remain. For each lift the
first pair gives the quartic

```text
A(q)=Pair(q,-q)=0,
```

with two field roots. For each `sigma_o`, the second pair gives

```text
O_q(q)=Pair(q,sigma_o q m z^2)=0.
```

Independent intersection of `A` and `O_q` leaves zero common q roots in all
16 lane records. Hence no target representative is formed. The target-
boundary, witness, free-branch, and unresolved ledgers are empty. QED.
