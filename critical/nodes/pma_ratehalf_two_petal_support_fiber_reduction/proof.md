# Proof - PMA rate-half two-petal support-fiber reduction

## 1. Invertibility

The core and petals are disjoint, so `gcd(L_S,L_2)=1`. Thus `L_S` is a unit
modulo `L_2`.

On the roots of `L_3`, the source numerator `P_3=L_1L_2R_3` equals the
nonzero planted value `L_C`. The factors `L_1,L_2,L_C` are nonzero there, so
`R_3` has no common root with `L_3`. Since `gcd(L_2,L_3)=1`, the product
`L_2R_3` is a unit modulo `L_3`. Hence (SF2) is well-defined.

## 2. Every contributor enters the guarded fiber

For a normalized contributor, the zero label on the first petal gives
`L_1|P`. Write

```text
P=L_1Z.
```

The source numerator and the full petal product are also divisible by `L_1`,
so the core-list equation becomes

```text
Z=F_lambda+L_2L_3H.                                 (1)
```

If its exact core agreement set is `S`, then

```text
Z=L_SV
```

for a polynomial `V` with no root in `C\S`. The degree calculation is

```text
deg Z<=N-ell=3ell+b-2,
deg V<=3ell+b-2-m=ell-a,                            (2)
```

and exactness is precisely (SF5).

Reducing (1) modulo `L_2` gives

```text
L_SV==L_3R_2 mod L_2.
```

Because `deg V<=ell-a<ell=deg L_2`, the unique degree-`<ell` solution is
exactly `V=V_S`. Reduction modulo `L_3` then gives

```text
L_SV_S==lambda L_2R_3 mod L_3,
```

which is equivalent to (SF4). Thus every contributor enters the guarded
fiber, and its exact root set makes the map injective.

## 3. Every guarded support gives a contributor

Conversely take `S` satisfying (SF3)--(SF5), and put `Z=L_SV_S`. Definition of
`V_S` gives

```text
Z==L_3R_2 mod L_2,
```

while (SF4) gives

```text
Z==lambda L_2R_3 mod L_3.
```

Therefore `Z-F_lambda` is divisible by the coprime product `L_2L_3`, and
`H_S` in (SF6) is a polynomial. Moreover,

```text
deg H_S
 <=(m+ell-a)-2ell
 =ell+b-2
 =K_0-1.                                            (3)
```

Equation (1) now holds. Multiplying by `L_1` shows that `P_S` has normalized
label zero on the first petal, label one on the second, and label `lambda` on
the third. On the core, `P_S=L_1L_SV_S`; the petal factor has no core root,
and (SF5) says that `V_S` has no root in `C\S`. Hence its exact core root set
is `S`.

The two constructions are inverse, proving (SF7). Any additional first-match
condition is external to this fixed-cell algebra and can only delete
candidates.
