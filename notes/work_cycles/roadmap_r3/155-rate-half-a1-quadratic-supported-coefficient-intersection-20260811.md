# Cycle 155: rate-half `A=1` supported coefficient intersection (2026-08-11)

The primitive coefficient plane `W_q` is totally isotropic for both endpoint
Hankel forms and hence for every local derivative. Cycle 154 makes that
derivative nondegenerate on `ker M_gamma/<Q_gamma>` away from the correction
divisor. Therefore

```text
dim((W_q intersect ker M_gamma)/<Q_gamma>)
 <=floor(c_gamma/2).
```

On the exact contracted source set this becomes a coefficient-evaluation
rank theorem:

```text
e-floor(c_gamma/2)<=rank E_gamma<=e.
```

Every ordinary rank-one loss slope has exact rank `e`; its primitive
locator is the only coefficient-plane vector vanishing on the whole actual
support. A rank-two loss slope has rank `e-1` or `e`.

This is the first prize-specific structural consequence after the abstract
marked-jet fence. It does not yet exclude either root arm, but it turns the
local first jet into a macroscopic coefficient-rank condition at all but the
constant-size correction locus.

```text
result:                  PROVED coefficient-plane kernel intersection cap
DAG delta:               +1 PROVED leaf
critical status delta:   none
compute:                 integer rank-bound/tamper checks only
new assumptions:         none
```
