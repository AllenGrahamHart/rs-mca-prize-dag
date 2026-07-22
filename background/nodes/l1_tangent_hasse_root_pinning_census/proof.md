# Proof - L1 tangent Hasse root-pinning census

## 1. Double-root equivalence

Fix `D|L`.  Since `L` divides the squarefree polynomial `Omega`, write
`L=DL_0` with `gcd(D,L_0)=1`.  From `U-P=LQ` we have

```text
D^2 | U-P
 <-> D^2 | D L_0 Q
 <-> D | L_0 Q
 <-> D | Q.
```

This proves `(TH2)`.  The distinct linear factors of `D` are pairwise
comaximal.  The Chinese remainder theorem gives

```text
F[Z]/(D^2) = product_(x|D) F[Z]/((Z-x)^2).
```

Reduction modulo `(Z-x)^2` is specified by a polynomial's value and first
Hasse derivative at `x`.  Therefore `D^2|U-P` is exactly `(TH3)`.  This
formulation is valid in every characteristic.

## 2. Confluent evaluation rank

Let

```text
H_D : F[Z]_<k -> F^(2r),
P |-> (P(x),P^[1](x))_(x|D).
```

If `k<=2r`, an element of its kernel is divisible by `D^2` but has degree
below `k<=2r`; it is zero.  Thus the rank is `k`.  If `k>=2r`, the Chinese
remainder theorem supplies a representative of degree below `2r` for every
residue class modulo `D^2`; this representative lies in `F[Z]_<k`, so the
map is surjective and has rank `2r`.  In both cases the rank is `min(k,2r)`.

The equations `H_D(P)=H_D(U)` therefore have either zero solutions or one
affine fiber of dimension `k-min(k,2r)`, proving `(TH4)`.

## 3. Canonical exact-shell count

For a fixed codeword `P`, its complete agreement set with `U` on `H` is
unique.  If it has size `a`, it determines the locator `L` and then the
cofactor `Q=(U-P)/L` uniquely.  Restricting the affine fiber in `(TH4)` to
members whose complete agreement set has size `a` and whose exact tangent
gcd equals `D` can only decrease its size.

There are exactly `binom(n,r)` monic degree-`r` divisors of the squarefree
split polynomial `Omega`.  The exact gcd `T` assigns each tangent member to
one and only one such divisor.  Summing the fixed-`D` bound proves `(TH5)`.
Since `T` divides both the degree-`a` locator and the degree-`e` cofactor,
only `r<=min(a,e)` can occur.

## 4. Rank-loss bound

Evaluation on the `a` roots of squarefree `L` identifies `F[Z]/(L)` with
`F^a`.  Multiplication by `Q` is diagonal in these coordinates.  It has one
zero diagonal entry for every root of `gcd(L,Q)` and no others, so its rank
is exactly `a-r`.

The Pade Jacobian is this map followed by projection from all `a` remainder
coefficients to the top `w=a-k` coefficients.  The projection kernel has
dimension `k`.  For any linear map `M`,

```text
rank(projection M) >= rank(M)-k.
```

Thus its rank is at least `a-r-k=w-r`, or zero if this expression is
negative.  Comparing with the `w` available rows proves `(TH6)`.
