# Rank-two large-clone Pade router

- **status:** PROVED
- **input:** `MOVING_DENOMINATOR_RANK_TWO` from the large-clone Mobius
  router

Write its pulled-back owner data as

```text
Qhat(gamma)=q_0+gamma q_1,
Nhat(gamma)=p_0+gamma p_1+gamma^2 p_2,
```

where `q_0,q_1` are linearly independent nonzero polynomials of degree at
most `d=m-k`, and `deg p_i<=m`. Define the exact division obstruction

```text
Omega=q_1^2 p_0-q_0 q_1 p_1+q_0^2 p_2.               (RP1)
```

For every coordinate `x` in the clone class `C`, the owner-incidence
identity implies `Omega(x)=0`. Hence

```text
deg Omega<=m+2d.                                      (RP2)
```

The following alternatives are exhaustive.

1. If `c=|C|>=m+2d+1`, then `Omega=0` identically. With
   `L=lcm(q_0,q_1)`, put

   ```text
   A_*=p_0 L/q_0,       B_*=p_2 L/q_1.
   ```

   Then

   ```text
   L Nhat=(q_0+gamma q_1)(A_*+gamma B_*).             (RP3)
   ```

   Thus every rational point of the split pencil has one fixed
   affine-in-slope rational owner. After cancelling common `X` factors, its
   denominator has degree at most `2d`; with two root-free source owner
   points its reduced denominator is root-free on the evaluation domain.
2. If `c=m+2d`, then either the same fixed-owner conclusion holds or

   ```text
   Omega=mu Lambda_C,       mu!=0.                    (RP4)
   ```
3. Otherwise the genuinely moving branch is confined to

   ```text
   m<=c<=m+2d.
   ```

At the deployed rows the exact upper walls are

```text
KoalaBear:    m+2d=1250992,
Mersenne-31:  m+2d=1250920.
```

This is a structural router. A fixed denominator of degree up to `2d` is an
extension-depth owner, not the degree-`d` owner required by the current
large-owner payment.
