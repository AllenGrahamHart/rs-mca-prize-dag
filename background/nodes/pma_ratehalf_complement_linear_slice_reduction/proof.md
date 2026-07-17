# Proof - PMA rate-half complement linear-slice reduction

## 1. Source factor and unit

The normalized first label is zero, so the CRT polynomial `E_c` vanishes
modulo `L_1`. The three petal locators are pairwise coprime and
`deg E_c<3ell`, hence there is a unique polynomial `Etilde` of degree less
than `2ell` with `E_c=L_1 Etilde`.

The other two CRT residues are one and `lambda`. Reducing this identity
modulo `L_2` and `L_3` gives (LS2). Core/petal disjointness makes `L_1` a
unit in both quotient rings, and `lambda` is nonzero. Therefore `Etilde` is
a unit modulo each of the coprime factors `L_2,L_3`, hence modulo `M`.

The normalized source division is

```text
L_C E_c=L_1F_lambda+L_1MY.
```

Cancelling `L_1` proves (LS1).

## 2. From a guarded support to a complement divisor

For a predecessor support `S`, its exact contributor satisfies

```text
L_S V_S=F_lambda+M H.                               (1)
```

Write `L_C=L_SD_S`. Subtracting (1) from (LS1) gives

```text
L_S(D_S Etilde-V_S)=M(Y-H).                         (2)
```

The support and petals are disjoint, so `gcd(L_S,M)=1`. Equation (2) implies

```text
D_S Etilde==V_S mod M.                              (3)
```

The predecessor guard has `deg V_S<=ell-a<2ell`; hence `V_S` is the
canonical remainder in (LS3). Its no-extra-core-root condition is

```text
gcd(V_S,L_C/L_S)=gcd(V_D,D_S)=1.
```

This proves that every exact contributor enters (LS6).

## 3. From a complement divisor to a contributor

Conversely, let `D|L_C` satisfy (LS6), put `L_S=L_C/D`, and set
`V=rem_M(D Etilde)`. Multiplying the defining congruence by `L_S` and using
(LS1) gives

```text
L_SV==L_C Etilde==F_lambda mod M.
```

Thus `H_D` in (LS5) is a polynomial. Its degree obeys

```text
deg H_D
 <=m+(ell-a)-2ell
 =ell+b-2
 =K_0-1.                                            (4)
```

The corresponding normalized codeword is `L_1L_SV`. It vanishes on `S`,
and `gcd(V,D)=1` says that it vanishes at no core point outside `S`.
Equation (LS5) supplies the required second and third petal residues, so this
is an exact predecessor contributor. The two constructions are inverse.

## 4. Linear-slice dimension

Reduction identifies `K[X]_<2ell` with `K[X]/(M)`. Multiplication by the unit
`Etilde` is an automorphism of this `2ell`-dimensional vector space. The
polynomials of degree at most `ell-a` form a subspace of dimension
`ell-a+1`. Its inverse image under that automorphism is exactly (LS7), proving
the dimension and codimension claims.

Because `d=2ell-a<2ell`, every candidate missed-core locator already has its
canonical representative in this quotient. No reduction ambiguity or extra
choice of a missed-core polynomial remains.

## 5. Reconciliation with the three-petal mu-basis

Set `s=ell-a`, so `d=ell+s`. If `D` lies in the degree-truncated slice, put
`V=rem_M(D Etilde)` and `W=L_1V`. The residue formulas (LS2) give

```text
L_1|W,       L_2|(W-D),       L_3|(W-lambda D).
```

Also `deg D,deg W<=d`. Hence `(D,W)` belongs to the predecessor's space
`V_s` for labels `(0,1,lambda)`.

Conversely, if `(F,W)` belongs to that `V_s`, the first divisibility condition
and `deg W<=ell+s` give `W=L_1V` with `deg V<=s`. The other two divisibility
conditions, together with (LS2), say

```text
F Etilde==V mod L_2,       F Etilde==V mod L_3.
```

Thus `V=rem_M(F Etilde)`, and `F` lies in the truncated slice. These maps are
linear inverses, proving (LS8).

The mu-basis Hilbert function with `s=ell-a` is

```text
[s-mu+1]_+ + [s-(ell-mu)+1]_+
 =[ell-a-mu+1]_+ + [mu-a+1]_+,
```

which proves (LS9). A guarded divisor has `deg D=d` and

```text
gcd(D,W)=gcd(D,L_1V)=1,
```

because core and petals are disjoint and `gcd(D,V)=1`. It is therefore a
saturated pair in the mu-basis theorem. If `s<ell/2`, equivalently
`a>ell/2`, that theorem gives dimension one. If `s>=ell/2`, it gives
`mu>=ell-s=a`; since `mu<=ell/2<=s`, both terms in (LS9) are active and sum
to `ell-2a+2`. This proves (LS10). Monic normalization cuts the nonzero
leading-coefficient locus by one affine coordinate.
