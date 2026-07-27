# L1 Mersenne HNF order-one involution-component exclusion

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_order_one_frobenius_gate`
- **consumer:** `l1_mixed_petal_amplification`

For odd `h`, put

```text
Phi_h(rho,c)=[t^h](1-t)^(c rho)(1-ct)^(-rho).
```

The integral polynomial `h!*Phi_h` is divisible by

```text
rho*c*(c-1)*(c+1).                                  (IOC1)
```

The order-one chamber already saturates by `rho*c*(c-1)`. The additional
component `c=-1` is empty on all five official next-to-maximal rows

```text
(n,p,m,h) in {
  (65536,       8191,       8, 7),
  (1048576,     131071,     8, 7),
  (4194304,     524287,     8, 7),
  (17179869184, 2147483647, 8, 7),
  (131072,      8191,       16,15)
}.
```

Consequently every survivor lies on the residual factor `Psi_h=0`. Exact
coefficient construction gives

```text
h=7:  deg_rho Psi_7=2, deg_c Psi_7=4,  10 terms;
h=15: deg_rho Psi_15=6, deg_c Psi_15=12, 64 terms.   (IOC2)
```

This deletes one complete order-one component and lowers the live curve
degrees. It does not prove either residual empty, impose the reciprocal or
pointwise Frobenius equations, or close L1.
