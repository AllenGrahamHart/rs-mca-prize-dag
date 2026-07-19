# Proof certificate

The pair-quadratic router normalizes any putative relation to a legal pair
`x=zeta^i`, `y=zeta^j` in `O=Z[zeta_1024]`. Its final two roots belong to
`mu_1024` only if the two cleared router equations

```text
F=C^1024-v^1024,
G=E_1024-2v^1024
```

vanish after evaluation at the exact-order root in `F_q`. Here `E_m` is the
division-free Dickson recurrence proved in the ideal-index node.

Evaluation at that root is a degree-one prime ideal of `O` above `q`. If it
contains `F`, multiplication by `F` is singular modulo `q`, so
`q | |Norm(F)|`; similarly `q | |Norm(G)|`. Therefore every supporting
characteristic divides

```text
g(i,j)=gcd(|Norm(F)|,|Norm(G)|).                 (NG)
```

This principal-norm obstruction is weaker than the full pair-ideal index but
is sufficient for exclusion. Absolute norms and `(NG)` are invariant under
odd Galois dilation.

The certificate enumerates the legal unordered pairs and quotients by every
odd dilation. There are exactly `1,514` orbits. For one canonical pair in each
orbit, FLINT computes both exact resultants against `X^512+1` and then their
integer gcd. A second complete Modal pass recomputes all `1,514` rows and
matches the SHA-256 digest of every pair, norm bit length, and gcd. The largest
gcd has `9,137` bits.

PARI factors the `507` distinct nontrivial gcds. Their products are checked
exactly. A recursive 282-node Pocklington graph proves primality of all `168`
factor roots; the largest root has 206 bits. Direct valuation then gives

```text
max_p v_2(p-1)=18.
```

If an official relation existed, its characteristic would divide one of the
certified gcds and hence equal one of those prime factors. Official splitting
requires `v_2(q-1)>=41`, contradicting the displayed maximum.

Production runs:

```text
exact gcd ledger:  ap-e2r2Z9nKcbst0ZOVU0mP3Q
factor ledger:     ap-BoaLKWu26WqiKT4dONcQsz
prime certificate: ap-iy4e0DQbGNA6O87XHliCx4
exact replay:      ap-NGbbYxPmeouUvAUMhNPpVu
```

The remote replay launcher is retained under `notes/`; run its app with the
generation script's `--full --verify-only` entrypoint to reproduce the pinned
replay artifact.
