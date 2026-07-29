# KoalaBear degree-five decomposition exclusion

- **status:** PROVED
- **scope:** inner-degree-five row of the residual KoalaBear `Q=6,s=6,u=2` branch
- **dependency:** `rate_half_kb_degree60_decomposition_divisor_adapter`
- **consumer:** `rate_half_band_closure`

Let

```text
p=2130706433,       K=F_(p^6).
```

The inner-degree-five profile would have two simple outer poles. Their
preimages are two `K`-rational source points, each totally ramified with
index five. These consume the complete Riemann-Hurwitz budget, so a normalized
inner map is `x -> x^5`.

But

```text
p=3 mod 5,       p^6=4 mod 5,       gcd(5,|K|-1)=1.
```

The fifth-power map is therefore injective on `P^1(K)`. The divisor adapter
simultaneously requires every outer zero to pull back to five distinct
`K`-rational active roots. This is impossible. Hence inner degree five does
not occur.

The remaining necessary decomposition-degree set is

```text
{2,3,4,6,10,12,30}
```

of the necessary eight-row ladder. This deletes one structural row only; it
does not close the other seven rows, `u=2`, cap `68`, the owner ledger, the
adjacent certificate, or the KoalaBear row.

## Falsifier

A degree-five separable map with two distinct totally ramified `K`-points
and a fiber containing two distinct `K`-points, or a nontrivial fifth root
of unity in `K`.
