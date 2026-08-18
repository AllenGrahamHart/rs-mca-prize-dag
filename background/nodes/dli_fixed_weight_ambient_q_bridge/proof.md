# Proof

## Fourier-positive marginals

Let `G` be a finite additive group and let `Y,Y'` be iid `G`-valued random
variables. For every character `chi` of `G`,

```text
E chi(Y-Y') = E chi(Y) conjugate(E chi(Y)) = |E chi(Y)|^2 >= 0.   (1)
```

If independent difference variables are added after arbitrary homomorphisms
into another finite additive group `H`, the Fourier transform of the sum is
a product of terms of the form `(1)`, hence is nonnegative at every
character of `H`. Fourier inversion therefore gives

```text
P(sum=0) = |H|^(-1) sum_(chi in H^) Fourier(sum)(chi) >= |H|^(-1),   (2)
```

because the trivial character contributes one.

At junction `j`, the variables

```text
D_(j,i)=M_(j,i)-M_(j,i+h_j/2)
```

are independent differences of iid `Binomial(2^j,1/2)` variables. The
odd-band syndrome is a sum of their images in `B^(|U_j|)`. Applying `(2)`
with `|H|=q^(|U_j|)` proves `P(O_j)>=q^(-|U_j|)`.

At the terminal level, pair `i` with `i+h_m/2`. Since `zeta_m` has exact
even order `h_m=n/t`,

```text
zeta_m^(i+h_m/2)=-zeta_m^i.
```

The terminal syndrome is therefore a sum of independent differences of iid
`Binomial(t,1/2)` variables, after multiplication by `zeta_m^i`. Applying
`(2)` in the additive group of `B` proves `P(T_m)>=q^(-1)`.

There are

```text
|U_j| = t/2^(j+1)
```

odd frequencies at level `j`. Hence

```text
1 + sum_(j=0)^(m-1) |U_j| = 1+(t/2+t/4+...+1)=t,
```

and multiplication of the marginal bounds proves `(AQ2)`.

## Fixed-weight dictionary

The Haar identity identifies the joint event with `Phi^(-1)(0)`, and its
first-owner deletion with `Prim intersect Phi^(-1)(0)`. Partitioning the
uniform binary cube by Hamming weight gives

```text
P(Prim intersect Phi^(-1)(0))
 = 2^(-n) sum_w f_w
 = q^(-t) sum_w [M_w/2^n] [q^t f_w/M_w].                 (3)
```

For every `w`, multiplication and cancellation in `(AQ1)` gives

```text
Delta_img(w) kappa_img(w)
 = (q^t/L_w)(f_w L_w/M_w)=q^t f_w/M_w.                  (4)
```

Divide `(3)` by the product of Haar marginal probabilities and use `(AQ2)`.
Equations `(3)` and `(4)` give every equality and the inequality in `(AQ3)`.

## Extreme layers

Any `s<=t` distinct columns

```text
(zeta^i,zeta^(2i),...,zeta^(ti))
```

are linearly independent: after scaling column `i` by `zeta^(-i)`, their
first `s` rows form a Vandermonde matrix on distinct `zeta^i`. Thus a
nonempty binary support of size at most `t` cannot lie in `Phi^(-1)(0)`.

For `1<=r<=t<n`, the complete-domain power sum is zero. Therefore
`Phi(1-x)=-Phi(x)`, so complements preserve the zero fiber. This excludes
all nonfull zero-fiber supports of size at least `n-t`. The empty and full
words are antipodally invariant and are removed by `Prim`. This proves
`(AQ4)`.

Finally `(AQ5)` and `(AQ3)` imply `J_prim<=2^21`, which is `HAAR-21` and
hence suffices for C2''. If `t/n` is bounded below by a positive constant,
`(AQ4)` places all surviving weights in fixed-density slices. Uniform
`kappa_img(w)=exp(o(n))` and `Delta_img(w)=exp(o(n))` then make their weighted
average `exp(o(n))`. No finite 21-bit estimate follows from that asymptotic
notation.

