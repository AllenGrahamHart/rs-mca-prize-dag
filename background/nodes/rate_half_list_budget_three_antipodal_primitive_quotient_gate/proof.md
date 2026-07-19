# Proof

Any common divisor of `R` and `S` divides every `R+a_iS`, hence every `G_i`.
The `G_i` are pairwise coprime, so `gcd(R,S)=1`. Each `R+a_iS` has degree
`r`; therefore `max(deg R,deg S)=r`. The reduced rational map `f=-R/S` has
degree `r`, proving `(APQ1)`.

The degree of a composition of nonconstant rational maps is the product of
their degrees. Thus a cyclic pullback `g(Y^m)` has degree divisible by `m`,
and a dihedral pullback `g(Y^m+Y^(-m))` has degree divisible by `2m`.
Fractional-linear target changes have degree one and do not alter this
conclusion. Since `s` is a power of two, `r=s-1` is odd. Every nontrivial
divisor `m` of the dyadic number `d` is even. Neither degree divisibility can
hold, which proves `(APQ2)`.

It remains to exclude the direct coset partition. Suppose the roots of each
`H_i` form one coset of the unique order-`s` subgroup of `mu_d`. Because
`b_i` belongs to that coset,

```text
H_i(Y)=Y^s-b_i^s.
```

Deleting `b_i` gives

```text
G_i(Y)=(Y^s-b_i^s)/(Y-b_i)
      =Y^(s-1)+b_iY^(s-2)+b_i^2Y^(s-3)+...+b_i^(s-1).  (1)
```

The four cosets are disjoint, so the four `b_i` are distinct. Since `s>=4`,
the first four coefficient columns of the four polynomials in `(1)` form

```text
[1, b_i, b_i^2, b_i^3]_(i=0)^3.
```

Its determinant is the nonzero Vandermonde product
`product_(i<j)(b_j-b_i)`. Therefore the four `G_i` are linearly independent.
This contradicts the proved two-dimensional pencil containing them. The
coset partition is impossible. QED.
