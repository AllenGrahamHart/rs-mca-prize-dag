# XR rank-two dual support-extension factorization

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_highcore_collision_count`
- **dependency:** `xr_higher_rank_uniform_split_pencil_reduction`

Use a uniform rank-two trade on active union

```text
|X|=a+d+1,       1<=d<=a-1.
```

For an active row `lambda_i`, let `A_i` be its selected block of size `a+h`
and put

```text
S_i=supp(lambda_i),
Z_i=X\S_i,        z_i=|Z_i|,
T_i=A_i\S_i.                                         (SE1)
```

Write `Lambda_Y` for the monic locator of a finite set `Y`. After the fixed
dual-GRS normalization, write the same extended row as

```text
lambda_i(x)=F_i(x)/Lambda'_X(x)       on X,
lambda_i(x)=P_i(x)/Lambda'_(A_i)(x)   on A_i,
deg F_i<=d,       deg P_i<h.                         (SE2)
```

Then

```text
|T_i|=h-d-1+z_i,                                  (SE3)
F_i=R_i Lambda_(Z_i),
P_i=R_i Lambda_(T_i),
deg R_i<=d-z_i,                                     (SE4)
R_i(x)!=0                    for every x in S_i.     (SE5)
```

The cofactor `R_i` is unique. On its support the row has the extension-free
normal form

```text
lambda_i(x)=R_i(x)/Lambda'_(S_i)(x),       x in S_i. (SE6)
```

Conversely, let `S,Z,T` be finite sets with `X=S disjoint_union Z`,
`A=S disjoint_union T`, `|X|=a+d+1`, `|A|=a+h`, and let a polynomial `R`
of degree at most `d-|Z|` avoid `S`. Then

```text
F=R Lambda_Z,       P=R Lambda_T
```

define the same extended support-`S` word through the two formulas in
`(SE2)`, and that word lies in both relevant dual `GRS_a` codes. Thus
`(SE3)--(SE6)` are an exact dual-codeword support-extension certificate.

The theorem does not assert that an abstract extension `T_i` is an actual
agreement block for the received pair, count the permitted extensions,
choose a first Maxwell core, or pay the cross-core aggregate.
