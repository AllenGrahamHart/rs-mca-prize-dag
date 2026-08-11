# `A=1` core-one zero-incidence-gap two-point normal form

- **status:** PROVED
- **closure:** exact local multiplicity, adjugate, and contact-divisor ledger
- **consumer:** `rate_half_band_crossing_location`

Retain the core-one scalar-residual packet

```text
(u,v,I_0,c_(x_*))=(0,2,0,2),                          (ZTP1)
```

from the constant triple-tangency theorem. Put

```text
d=rho-1=3e-2,       Delta=e-2,
q_*(U,V)=Qbar(U,V;x_*).                               (ZTP2)
```

There are distinct supported slopes `alpha,beta` and a squarefree form
`P_ord` of degree `e-4` such that, up to nonzero scalars,

```text
D=P_ord L_alpha L_beta,
q_*=P_ord L_alpha^2 L_beta^2
   =D L_alpha L_beta.                                 (ZTP3)
```

Here `D` is the degree-`Delta` middle-Hankel adjugate factor. At the
`e-4` roots of `P_ord`, `x_*` is a double specialized `X`-root whose simple
copy belongs to `Q_min`. At `alpha,beta`, it is a simple extra root outside
`Q_min`, while `q_*` has parameter multiplicity two.

The specialized Forney numerator and first `X`-jet satisfy

```text
N_F(U,V;x_*)=D C_3,             deg C_3<=3, C_3!=0;
(partial_X Qbar)(U,V;x_*)=P_ord S_4,
                                   deg S_4<=4,
S_4(alpha)S_4(beta)!=0.                               (ZTP4)
```

If `P_alpha,P_beta` are the two points of `C` above
`(alpha,x_*),(beta,x_*)`, the contact section has reduced zero divisor

```text
div(s_F)=V_(x_*)-P_alpha-P_beta.                       (ZTP5)
```

Consequently

```text
O_C(-rho-1,e+1)
  =O_C(1,0)(-P_alpha-P_beta),

O_C(rho+2,-e-1)=O_C(P_alpha+P_beta).                  (ZTP6)
```

The second line is an effective degree-two Picard obstruction.

## Scope

The theorem does not prove that the degree-two line bundle in `(ZTP6)` is
impossible. It applies only to the first packet in `(CTP5)`.
