# L1 general polynomial-pullback interleaving descent

- **status:** PROVED
- **role:** replace raw fiber-role enumeration by a quotient-list interface
  for arbitrary monic polynomial pullbacks
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Polynomial decomposition

Let `K` be a finite field of order `q`, let `P in K[X]` be monic of degree
`s>=1`, and let `k>=1`. Every polynomial `f` of degree below `k` has a unique
decomposition

```text
f(X)=sum_(j=0)^(s-1) X^j g_j(P(X)),                    (GP1)
```

where

```text
deg g_j<k_j,       k_j=max(0,ceil((k-j)/s)).           (GP2)
```

## Complete-fiber quotient receiver

Let `D subset K` be an evaluation domain. Let `B` be any set of labels for
which

```text
T_a={x in D:P(x)=a}
```

has exactly `s` distinct points. For each `a in B`, invert the Vandermonde
matrix on `T_a` and define the unique vector

```text
u(a)=(u_0(a),...,u_(s-1)(a))
```

whose degree-below-`s` polynomial interpolates the received word `U` on
`T_a`. Then

```text
f=U on T_a  iff  g_j(a)=u_j(a) for every 0<=j<s.       (GP3)
```

Put `b=|B|`, `K_0=ceil(k/s)`, and

```text
kappa=sum_(j=0)^(s-1) max(0,k_j-b).                   (GP4)
```

Let `L_s(B,K_0,h)` be the worst common-support `s`-interleaved list size at
agreement `h` for the evaluation code of degree-below-`K_0` polynomials on
`B`. The number of degree-below-`k` polynomials agreeing with `U` on at least
`h` complete fibers from `B` is at most

```text
q^kappa L_s(B,K_0,h).                                  (GP5)
```

If `L(B,K_0,h)` is the corresponding worst ordinary list size and `1<=L<q`,
the proved interleaving collapse gives

```text
q^kappa L_s
 <=q^kappa floor(L(q-1)/(q-L)),                        (GP6)
```

and this is `q^kappa L` when `L^2<q`.

## Full-partition corollary

If `D` is partitioned into complete degree-`s` fibers and `k<|D|`, then
`b=|D|/s`, every `k_j<=b`, and `kappa=0`. Thus arbitrary monic pullbacks in
this scope incur no map-internal role multiplier: their fully fiberwise
contributors inject into one quotient common-support interleaved list, which
collapses to the ordinary quotient list in the sub-square-root regime.

## Scope

The theorem does not assert a row-sharp ordinary list bound on the generally
non-smooth label domain `B`. It does not pay partial agreements in fibers,
points outside the complete fibers, or the factor `q^kappa` when complete-
fiber coverage is too sparse. It supplies the general-pullback owner interface
missing from the periodic-owner route; those remaining bounds must be proved
by the consumer.
