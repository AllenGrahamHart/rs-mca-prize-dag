# Proof

For each normalized guard `g(u)`, compute

```text
gcd(g(u), u^p-u)
```

in `F_p[u]`. Factor this squarefree field part into linear factors and record
their roots. All 54 computations complete. The verifier reconstructs each
monic field part as the product of the listed linear factors, checks that it
divides the exact source guard, and rebuilds the global incidence map. The
field parts have total degree 78 and their root union has size 67. QED.
