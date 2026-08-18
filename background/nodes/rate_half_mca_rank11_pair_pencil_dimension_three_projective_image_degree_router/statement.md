# Dimension-three projective-image degree router

- **status:** PROVED
- **scope:** the scalar-dimension-three `q=3170` endpoint

Let `W_0` be the residual three-dimensional scalar polynomial space and let
`G=gcd(W_0)`. At an official-domain root of `G`, the residual owner
multiplicity is zero. The endpoint incidence deficit therefore gives

```text
z:=|D' intersection Z(G)|
 <=floor((14709668-2952K')/218)<=310.               (PI0)
```

Put `W=G^(-1)W_0` and

```text
d=max{deg T:T in W}.
```

Homogenization defines a basepoint-free map

```text
phi:P^1 -> P(W^*)=P^2.
```

If `C` is its image, `c=deg C`, and `e=deg(phi:P^1->C)`, then

```text
d=ec,                    c>=2.                      (PI1)
```

At most `e` full owner coordinates have one projective evaluation normal.
Consequently exactly one of the following holds.

1. **Conic composition:** `c=2`. After a base-field projective change of
   basis there are coprime degree-`e` homogeneous forms `A,B` such that

   ```text
   W_hom=span{A^2,AB,B^2},
   1021<=e<=2490.                                  (PI2)
   ```

   After the common `G` roots are removed, every represented direction is a
   binary quadratic in `A,B` having at least 2,041 official-domain roots.
   Before removal, `G` times that quadratic has the original 2,351-root
   floor. The 23 endpoint rows have at least 398 through 422 distinct full
   evaluation normals, respectively.

2. **Image degree at least three:** `c>=3`. Then

   ```text
   e<=floor((K'-1)/3),
   number of distinct full evaluation normals
      >=ceil(F_218/floor((K'-1)/3))>=597.           (PI3)
   ```

   The exact row-wise lower bound rises from 597 to 633.

This classifies the image-degree-two branch; it does not classify the
rational function `A/B`, exclude either branch, or pay the endpoint.
