# Extension-code/interleaving list identity

- **status:** PROVED
- **consumer:** `list_large_m_scope_closure`

Let `B` be a finite field, let `E/B` have degree `m`, let `D subset B`, and
put

```text
C_B = RS[B,D,k],
C_E = RS[E,D,k].
```

After choosing any `B`-basis of `E`, coordinate expansion is a Hamming
isometry

```text
Phi : E^D -> (B^m)^D
```

that maps `C_E` bijectively onto `C_B^{==m}`. Consequently, for every
agreement/radius and every received word, the corresponding list sizes are
equal, and hence

```text
Lst(C_E,delta) = Lst(C_B^{==m},delta).           (EI)
```

For the prize list problem, the right side is still compared with
`2^-128|B|`. Identity `(EI)` does not permit replacing that denominator by
`|E|`.
