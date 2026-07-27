# DSP8 smooth quotient-cap compiler

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_dsp8_correlation_bound` (evidence)
- **dependencies:** `f3_affine_coset_pair_mattarei_bound`,
  `f3_h3_dsp8_smooth_residual_router`,
  `f3_h3_dsp8_unit_product_trace_normal_form`

For `c in {0,A}`, let `U_sm^c` count the raw normalized smooth base tuples

```text
(r,u,s,x)                                           (SQC1)
```

that satisfy every DSP8 product, trace, split, richness, class, and
signed-disjointness predicate, but before choosing the ordered quotient pair
`(z,w)`. The target attached to a base tuple is

```text
t=1+rs(r+s-sigma),       t notin {0,1}.             (SQC2)
```

The exact quotient ledger and Mattarei's pointwise affine-pair bound give

```text
G_sm^c=sum_(base tuples in class c) R(t)
      <C_M n^(2/3) U_sm^c,       C_M=3*2^(-2/3).   (SQC3)
```

Consequently the uniform smooth target follows from the class-sensitive
unweighted estimate

```text
189(10U_sm^0+17U_sm^A)<=144344 n^(4/3).            (SQC4)
```

The class-blind estimate

```text
3213(U_sm^0+U_sm^A)<=144344 n^(4/3)                (SQC5)
```

is also sufficient. Its effective unweighted threshold is

```text
U_sm^0+U_sm^A <=(144344/3213)n^(4/3)
               <44.926 n^(4/3).                   (SQC6)
```

This compiler removes the quotient weight only at the price of a strong
`n^(4/3)` unweighted smooth-SP estimate. It proves no such estimate and does
not replace the retained richness, smoothness, or signed-disjointness
predicates by a marginal curve-point or full shifted-energy count.
