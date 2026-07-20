# DSP8 single-quotient candidate compressor

- **status:** PROVED
- **closure:** proof
- **consumers:** `f3_h3_dsp8_correlation_bound`,
  `f3_h3_official_order_template_survivor`
- **dependencies:** `f3_h3_dsp8_single_quotient_endpoint_compiler`,
  `f3_h3_double_accident_coupling_matrix_odd_saturation`,
  `f3_h3_quotient_algebra_fitting_support_compiler`

Let `E_0,...,E_d`, with `d>=1`, be the vertices of a selected product star,
put `beta_i=beta_(E_i)`, and let `Q=(u,v)` be one ordered nonidentity
quotient lift. In `O=Z[zeta_n]`, write

```text
pi=1-zeta_n,       C=1-zeta_n^u,       D=1-zeta_n^v,
J_k=((beta_i-beta_k)/pi^2:i!=k),
lambda_k=(beta_k C-D)/pi,
I_k=(J_k,lambda_k).                                (SQC1)
```

Then all displayed elements are integral and

```text
J_k=J_0,       I_k=I_0       for every k.          (SQC2)
```

The equality is exact over `O`, not merely after inverting two. Moreover
`I_k` is nonzero even if `lambda_k=0`, because the distinct star vertices
give a nonzero product-difference generator. At an official survivor prime
ideal `mathfrak p`, one has

```text
I_k subset mathfrak p,       p divides Norm(I_k).  (SQC3)
```

Thus the `(36,1)` packet may use the star's canonical center and its sole
quotient lift. No search for a nonzero coupling center and no zero-locus test
is required for completeness. The zero-locus classifier remains useful for
deduplication and diagnostics.

There is also an exact quotient-index-free candidate support. In the notation
of the quotient-algebra Fitting compiler, let `s_(n,c)^X` be the positive odd
generator of

```text
(Qhat_n,Pcal_n^[0],...,Pcal_n^[c]) intersect Z[1/2]. (SQC4)
```

On every official H3 order and every prime `p=1 mod n`,

```text
p divides s_(n,35)^X
  iff some t!=1 has P(t)>=36 and R(t)>=1
  iff Dbar_17^0+Dbar_17^A>0.                       (SQC5)
```

The cutoff hierarchy satisfies

```text
s_(n,35)^X divides s_(n,18)^X.                    (SQC6)
```

Consequently a complete implementation may compute the single scalar
annihilator `s_(n,35)^X`, factor only its official-range support, and evaluate
the exact class-sensitive `Dbar_17` moment on those rows. This theorem does
not bound or efficiently compute the annihilator, factor it, prove the moment
inequality, promote DSP8, or close C36'.
