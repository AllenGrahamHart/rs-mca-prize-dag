# Global derivative-ideal exceptional-prime reduction for C36'

- **status:** PROVED
- **consumer:** `f3_h3_mobius_excess_half`
- **dependency:** `f3_h3_shifted_product_sidon`

Let `n=2^s`, `s>=2`, let `zeta=zeta_n`, and put

```text
K=Q(zeta),       O=Z[zeta],       d=[K:Q]=n/2,
A_K={1-zeta^e:1<=e<n}.
```

Define the ordered shifted-product polynomial

```text
Pcal(T)=product_(a,b in A_K)(T-ab).
```

For `1<=u,v<n`, `u!=v`, put `c_u=1-zeta^u`, `d_v=1-zeta^v` and
`gamma_uv=d_v/c_u`. Let `Pcal^[j]` denote the `j`th Hasse derivative and
define the nonzero fractional ideal

```text
I_uv=(Pcal^[0](gamma_uv),...,Pcal^[18](gamma_uv)) O[1/2].
```

Equivalently, if `D_uv,j` is the coefficient of `U^j` in the integral
polynomial

```text
G_uv(U)=product_(a,b in A_K)(d_v-c_u ab+c_u U),
```

then

```text
J_uv=(D_uv,0,...,D_uv,18) subset O
```

has the same odd localization as `I_uv`. Define

```text
E_n = odd part of Norm_O(product_(u!=v) J_uv).
```

There is a unique positive odd integer `e_n` such that

```text
E_n=e_n^d.                                             (GD1)
```

Now let `p=1 mod n` be any odd prime, let `H<=F_p^*` have order `n`, and
put `A=(1-H)\{0}`. For

```text
P(t)=#{(a,b) in A^2:ab=t},
R(t)=#{(c,d) in A^2:d/c=t},
X_18=sum_(t!=1)(P(t)-18)_+ R(t),
```

one has

```text
p^X_18 divides e_n.                                   (GD2)
```

Consequently:

1. if `p` does not divide `e_n`, then `X_18=0` and the C36' leaf is paid on
   that row;
2. either exact inequality

   ```text
   17 log(e_n)<=300 n^2 log(p),
   e_n^17<=p^(300 n^2)
   ```

   implies the critical target `17X_18<=300n^2`.

Thus each dyadic order has a finite, explicitly defined exceptional-prime
set containing every row on which the rich product/quotient correlation can
be nonzero. This theorem does not bound or factor `e_n`, so it does not by
itself close the critical leaf.
