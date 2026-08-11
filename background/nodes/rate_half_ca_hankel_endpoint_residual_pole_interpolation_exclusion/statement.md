# Strict-endpoint residual-pole interpolation exclusion

- **status:** PROVED
- **closure:** pole-ideal interpolation and surface cohomology
- **consumer:** `rate_half_band_crossing_location`

Retain any strict `A=3`, `e=m` endpoint on an even row `m>=6`:

```text
rho=4m-1,       N=16m,       T=4m+1,
0<=O=sum_(gamma in Z)(rho-u_gamma)<=m-1.              (RPI1)
```

Let `C:Q=0` be the reduced endpoint curve, and put

```text
G(X)=X^N-1,       H(z)=product_(gamma in Z)(z-gamma),
ell=m/2-1.                                             (RPI2)
```

The rational section `G/H` of `O_C(N,-T)` has a pole-cancellation ideal
`J=(H:G)` whose quotient has length

```text
d=length(O_C/J)<=O<=m-1.                              (RPI3)
```

Since

```text
h^0(P^1 x P^1,O(1,ell))=2(ell+1)=m>d,                (RPI4)
```

there is a nonzero biform `F` of bidegree `(1,ell)` whose restriction lies
in `J`. Hence

```text
s_G=F G/H in H^0(C,O_C(N+1,ell-T))                   (RPI5)
```

is regular and nonzero on every irreducible component.

Let `s_F` be the universal Forney contact section in
`O_C(-rho-3,m+1)`. The product `s_F^4 s_G` is nonzero and lies in

```text
O_C(4(-rho-3)+N+1,4(m+1)+ell-T)
 =O_C(-7,ell+3).                                      (RPI6)
```

However

```text
H^0(C,O_C(-7,ell+3))=0.                              (RPI7)
```

Therefore no strict `A=3`, `e=m` endpoint profile exists on the official
row `m=2^37`, for any omission defect `0<=O<=m-1`.

## Scope

This closes the first strict `A=3` endpoint. It does not close the remaining
`e>m` strict profiles, residual `A=1` profiles, the complete MCA crossing,
or the adjacent unsafe witness.
