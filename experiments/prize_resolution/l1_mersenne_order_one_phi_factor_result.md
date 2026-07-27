# L1 order-one hypergeometric factor result

One exact 1-CPU Modal worker constructed and factored `h!*Phi_h(rho,c)`
over the integers for both official next-to-maximal widths. After the three
factors already excluded by the order-one chamber, the result is

```text
h=7:   7!*Phi_7  = 6*rho*c*(c-1)*(c+1)*Psi_7,
       deg_(rho,c)(Psi_7)=(2,4), 10 terms;

h=15: 15!*Phi_15 = 14*rho*c*(c-1)*(c+1)*Psi_15,
       deg_(rho,c)(Psi_15)=(6,12), 64 terms.
```

The new component `c=-1` is theorem-empty on every official row by the
torsion equation `(c-1)^n=1`. The residual `Psi_h=0` remains open.

```text
app: ap-HLlQUd2eURywjmrrMr2EeV
worker: 0.688987 s, 88 MB
spend: exact bill not queried; conservative bound < $0.01
```
