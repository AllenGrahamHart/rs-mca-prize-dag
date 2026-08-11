# Proof

The packet theorem gives two distinct heavy roots of the residual quadratic
and

```text
I_E=d_(x_1)+d_(x_2)=2e-2-I_0,
c_1+c_2=2e-I_E=2+I_0.                                 (1)
```

The two row forms have degree `e`; division by their squarefree supported
locators proves the first factorization in `(CFN2)`.

The Forney numerator vanishes at every distinguished incidence, so
`P_i|N_F(U,V;x_i)`. Its parameter degree is at most `e+1`, leaving quotient
degree at most `c_i+1`. The two quotients cannot both vanish identically. If
they did, the surface numerator would contain
`(X-x_1)(X-x_2)`. The cancelled cube identity makes the contact section
nonzero on every mixed component, while those factors would put two full
vertical fibres, of total degree `2e`, in its zero divisor. This contradicts
the contact degree `Delta=2e-1`.

The regular Kronecker determinant has degree `Delta`. At each distinguished
incidence, the corresponding row root lies in the specialized excess
recurrence factor. Fibre by fibre, the product `P_1P_2` therefore divides
`D_reg`, with multiplicity when the two slope sets overlap. Its degree is
`I_E`.

If `I_0=1`, the local cube theorem makes the unique ordinary incidence
consume at least two excess degrees, so `L_0^2` also divides `D_reg`, after
retaining any overlap multiplicity already present in `P_1P_2`. The degree
left after these forced factors is

```text
Delta-I_E-2I_0=1-I_0.                                 (2)
```

This proves `(CFN3)`.

All heavy incidences are zeros of the contact section. Their reduced
divisor has degree

```text
I_E+I_0=2e-2=Delta-1.                                 (3)
```

The section is nonzero on every component and has total zero degree
`Delta`, so the residual zero divisor is an effective `E_1` of degree one.
This proves `(CFN4)`.

Each vertical fibre has degree `e`, and removing its reduced supported
incidence divisor leaves

```text
Z_i=V_(x_i)-R_i,       deg Z_i=e-d_(x_i)=c_i.          (4)
```

Substitute `R_i=V_(x_i)-Z_i` into `(CFN4)`. The two vertical fibres have
class `O_C(2,0)`, while the contact line bundle is
`O_C(-rho-1,e+1)`. Rearrangement gives `(CFN5)`. Its degree is

```text
c_1+c_2-I_0-1=1,                                     (5)
```

equivalently

```text
(rho+3)e-(e+1)rho=3e-rho=1
```

because `rho=3e-1`. QED.
