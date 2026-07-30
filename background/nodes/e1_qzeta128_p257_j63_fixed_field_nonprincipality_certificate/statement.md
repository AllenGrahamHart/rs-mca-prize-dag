# Q(zeta_128) J_63 fixed-field nonprincipality certificate

- **status:** PROVED
- **closure:** Jacobi-sum Stickelberger relation plus an explicit
  auxiliary-prime power-residue obstruction
- **scope:** one degree-one prime in a degree-32 CM field

Put `zeta=zeta_128`, `beta=zeta-zeta^(-1)`, and

```text
E_63=Q(beta),
p_66=(257,beta-66).
```

An exact defining polynomial for `E_63` is

```text
f_63(Y)=Y^32+32Y^30+464Y^28+4032Y^26+23400Y^24+95680Y^22
       +283360Y^20+615296Y^18+980628Y^16+1136960Y^14
       +940576Y^12+537472Y^10+201552Y^8+45696Y^6
       +5440Y^4+256Y^2+2.
```

Indeed,
`Res_Z(Z^64+1,Z^2-YZ-1)=f_63(Y)^2`, and `beta` has degree 32.

Then `p_66` is nonprincipal in `O_(E_63)`.

Indeed, `E_63` is the fixed field of
`sigma_63(zeta)=-zeta^(-1)`, both `q_1` and `q_63` lie above `p_66`, and the
ambiguous-class-number calculation proves that `E_63` has odd class number.
Extension through the quadratic field `Q(zeta_128)/E_63` is therefore
injective on ideal classes.

## Falsifier

An exact generator of `p_66`, equivalently an exact generator of
`J_63=q_1q_63`.
