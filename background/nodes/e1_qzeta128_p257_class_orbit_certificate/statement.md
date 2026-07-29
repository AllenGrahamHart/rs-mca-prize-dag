# Q(zeta_128) prime-257 class-orbit certificate

- **status:** TARGET
- **scope:** `K=Q(zeta_128)`, all degree-one primes above 257

Produce an unconditional exact certificate that the 64 prime ideals of
`Z[zeta_128]` above 257 have pairwise distinct ideal classes.

An acceptable stronger certificate may prove the published class-index
description

```text
Cl(K) = Z/359057,
[q_1] = 1,
sigma_-1(e) = -e,
sigma_3(e) = 29301 e.
```

Here `q_1` is one prime above 257, `sigma_a(zeta_128)=zeta_128^a`, and the
index is chosen so that `q_1` has class one. The source evidence for these
exact integers is pinned in `source_evidence.md`, but source evidence is not
the independent replay required to prove this node.

## Falsifier

Two distinct primes above 257 with the same certified ideal class, or a
failure of any asserted class-group relation under exact ideal arithmetic.
