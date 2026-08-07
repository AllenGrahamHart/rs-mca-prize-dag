# Proof

The parity of `sum_i x_i` equals the parity of the number of odd exponents.
In the even sector, both the odd and even exponent classes have even size, so
each class can be paired internally. In the odd sector, both classes have odd
size. Pairing internally leaves exactly one exponent of each parity, whose
final pair is the unique mixed pair.

For any pair `(a,b)`,

```text
r_a r_b=zeta_512^(x_a+x_b)
```

lies in `K_0` exactly when `x_a+x_b` is even. This proves the asserted field
degrees for the parity-adapted pairings. The pair-Heron theorem then places
all eight factors in `K_0` in the even sector. In the odd sector, changing the
sign of the unique mixed pair product is exactly the nontrivial conjugation
of `K/K_0`; the remaining pair products are fixed.

It remains to calculate that quadratic norm. With `U=s+2t`, the Heron
polynomial can be written

```text
H(U,V,W)=U^2-2U(V+W)+(V-W)^2.
```

Using `t^2=d` gives

```text
H(s+2t,V,W)=C+Dt,
```

with `C,D` from `(PAD1)`. Replacing `t` by `-t` and multiplying gives
`C^2-dD^2`, proving `(PAD2)`. There are four sign choices for the two
same-parity pair products, so these four norms partition the eight Heron
factors and hence all 32 signed lifts.

Sorting the two parity lists and pairing consecutive entries gives the
printed deterministic rule. In the odd case remove one fixed endpoint from
each list, pair the remaining consecutive entries, and pair the endpoints.
This changes no algebra because the pair-Heron identity holds for every
pairing. QED.
