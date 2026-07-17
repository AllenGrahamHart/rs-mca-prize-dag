# Exact MCA far-CA/sparse-layer reduction

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`

Let `C` be a linear code in `F^D`, let `|D|=n`, and fix an integer agreement
`1<=a<=n`. Put `r=n-a` and let:

- `B_mca(a)` be the maximum number of slopes carrying a failed support-wise
  MCA witness of size at least `a`;
- `B_ca^far(a)` be the maximum number of slopes whose line word agrees with a
  codeword on at least `a` coordinates, where the received pair has no common
  code-pair explanation on `a` coordinates;
- `S_sparse(a)` be the maximum number of MCA-bad slopes over pairs
  `(epsilon_1,epsilon_2)` satisfying
  `|supp(epsilon_1) union supp(epsilon_2)|<=r`.

Then

```text
B_mca(a)=max(B_ca^far(a),S_sparse(a)).                    (MS1)
```

Consequently, for every integer budget `B*`,

```text
B_mca(a)<=B*
  iff B_ca^far(a)<=B* and S_sparse(a)<=B*.               (MS2)
```

For the finite-slope Reed-Solomon challenge, division by `q=|F|` turns these
numerators into the corresponding probabilities. Thus `(MS2)` is an exact,
lossless reduction of the rate-half safe edge, not an asymptotic estimate.
