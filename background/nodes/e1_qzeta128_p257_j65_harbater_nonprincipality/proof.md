# Proof

Let

```text
L=Q(zeta_128),       xi=zeta_128^2=zeta_64,
M=Q(xi),             E=Q(i(xi+xi^(-1))).
```

The field `E` is the degree-16 CM subfield used by Dembele. Section 5.2 of
the cited paper identifies it as the unique CM extension of
`Q(zeta_32)^+` inside `Q(zeta_64)` having class number 17.

## 1. The descended prime has nontrivial Artin symbol

Dembele proves that the Hilbert class field of `E`, after normal closure over
`Q`, is the Harbater field and records in Remark 6.2 that this field is the
splitting field of Elkies's polynomial

```text
H(X)=X^17-2X^16+8X^13+16X^12-16X^11+64X^9-32X^8-80X^7
     +32X^6+40X^5+80X^4+16X^3-128X^2-2X+68.       (1)
```

Here `E/Q` is Galois: it is a subfield of the abelian extension
`Q(zeta_64)/Q`. Its Hilbert class field is therefore also Galois over `Q`,
because every rational automorphism carries the maximal unramified abelian
extension of `E` to itself. Thus the published normal closure is the Hilbert
class field itself. Its Galois group over `E` is cyclic of order 17.

The verifier proves by the exact finite-field irreducibility criterion that
`H mod 257` is irreducible. In particular it is separable, and Frobenius at
257 acts as a 17-cycle on its roots. Since

```text
257 = 1 (mod 64),
```

257 splits completely in `E`; hence this Frobenius lies in the normal
translation subgroup

```text
Gal(H_E/E) = C_17
```

of the affine group `C_17 : C_16`. A 17-cycle is nonidentity. Frobenius
elements of the primes of `E` above 257 are conjugate and therefore all
nonidentity. By the Artin isomorphism

```text
Cl(E) -> Gal(H_E/E),
```

every prime `p` of `E` above 257 is nonprincipal.                 (2)

## 2. Norm descent proves the stated ideal nonprincipal

The residues `9` and `248=-9 mod 257` have the same square `81`. Therefore
`q_1` and `q_65` contract to the same prime

```text
r=(257,xi-81)
```

of `M`, and hence to one prime `p` of `E`. All residue degrees are one. It
follows that

```text
N_(L/E)(J_65)=p^2.                                      (3)
```

If `J_65` were principal, `(3)` would make `p^2` principal. But
`|Cl(E)|=17`, so squaring is an automorphism of `Cl(E)` and `p` would be
principal, contradicting `(2)`. Therefore `J_65` is nonprincipal.
