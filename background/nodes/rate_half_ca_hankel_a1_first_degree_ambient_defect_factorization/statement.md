# `A=1` first-degree ambient defect factorization

- **status:** PROVED
- **closure:** boundary restriction isomorphism and rowwise quotient divisor
- **consumer:** `rate_half_band_crossing_location`

Work on either live core at the first official degree

```text
e=e_0=ceil((rho-1)/3),       3e=rho+1.                (ADF1)
```

For `s in {0,1}`, put `beta=s` and write the three possible slacks as

```text
ell=e-3+beta+j,       j in {0,1,2}.                   (ADF2)
```

The pole-absorbing three-contact product extends uniquely from the residual
curve to a nonzero ambient biform

```text
A_j(X;U,V) in H^0(P^1 x P^1,O(d-3,j)),
s_F^3G/H=A_j|_C.                                     (ADF3)
```

For each residual domain row `x in D\S`, put

```text
q_x(U,V)=Qbar(U,V;x),
g_x=gcd(q_x,H),       R_x=q_x/g_x,
c_x=deg R_x=e-deg g_x=e-d_x.                         (ADF4)
```

Then

```text
R_x divides A_j(x;U,V).                               (ADF5)
```

In particular, if `c_x>j`, every parameter coefficient of `A_j` vanishes
at `x`. If

```text
B_j(X)=product_(x in D\S, c_x>j)(X-x),               (ADF6)
```

then

```text
B_j divides A_j,       deg B_j<=d-3.                 (ADF7)
```

After writing `A_j=B_j A_j^res`, every row outside the heavy set has
`c_x<=j`, and its complete missing-root factor `R_x` divides
`A_j^res(x;U,V)`.

## Scope

The theorem does not yet bound the residual domain degree of `A_j^res` or
exclude any of the six boundary profiles.
