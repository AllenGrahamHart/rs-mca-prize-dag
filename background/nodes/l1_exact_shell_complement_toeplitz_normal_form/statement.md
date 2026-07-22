# L1 exact-shell complement Toeplitz normal form

- **status:** PROVED
- **role:** convert moving barycentric exact shells to fixed split-divisor sections
- **consumer:** `l1_mixed_petal_amplification`

## Statement

Let `H` be the `n` distinct roots of

```text
Omega(Z)=Z^n-beta
```

over a field whose characteristic does not divide `n`. Represent a received
word by its unique interpolant `U` of degree below `n`. Fix `k<a<=n`, put

```text
w=a-k,       r=n-a,
```

and, for an `a`-support `A`, let

```text
L=L_A,       M=L_(H\A)=Omega/L.
```

Then for every `0<=j<w`,

```text
sum_(x in A) U(x)x^j/L'(x)=[Z^(n-j-1)] U(Z)M(Z).      (CT1)
```

Consequently,

```text
deg I_A(U)<k
iff [Z^(n-w)]UM=...=[Z^(n-1)]UM=0.                   (CT2)
```

Define the fixed Toeplitz coefficient map

```text
C_(U,a)(M)=([Z^(n-w)]UM,...,[Z^(n-1)]UM).            (CT3)
```

It is linear on the coefficient space of degree-at-most-`r` polynomials and
affine on the monic degree-`r` slice. It is also invariant under codeword
shifts:

```text
C_(U+R,a)=C_(U,a)        for every deg R<k.           (CT4)
```

## Exact-shell divisor bijection

For a monic degree-`r` divisor `M` of `Omega`, put `L=Omega/M`, let
`P=U mod L`, and put `Q=(U-P)/L`. The exact shell `E_a(U)` is in bijection
with

```text
{M monic: M|Omega, deg M=r, C_(U,a)(M)=0,
          gcd(Q,M)=1}.                                (CT5)
```

The bijection is `A |-> L_(H\A)`. The gcd is the exactness guard: it excludes
an extra agreement at every complement root.

## Consequence

The global L1 route no longer requires moving barycentric weights. Its exact
object is a primitive split-divisor census in a fixed codimension-at-most-`w`
Toeplitz linear section. This is closer to upstream boundary Q, which also
counts split divisors in affine coefficient sections, but it is not yet the
same theorem: upstream `def:q-row-atom` prescribes a locator prefix, whereas
`(CT3)` prescribes a received-word-dependent convolution window.

The missing global theorem can therefore be stated precisely as one of:

1. row-sharp primitive flatness for every realized Toeplitz section `(CT3)`;
2. a first-match decomposition of such sections into a paid number of
   upstream prefix-affine divisor atoms; or
3. a split-divisor-preserving change of variables transporting `(CT3)` to
   those atoms.

This node proves the normal form and exact ownership only. It supplies no
flatness bound.
