# KoalaBear v4 tangent-source atom

- **status:** PROVED
- **closure:** exact sparsification plus finite-image counting
- **consumer:** `rate_half_band_closure` (evidence only)
- **upstream:** `przchojecki/rs-mca` PR `#1049`, exact head
  `c15927c90091602035f617226da9ecf03cfc7316`
- **architecture:** `GRANDE_FINALE_V4_KB_MCA_TANGENT_SOURCE_ADAPTER_V1`
- **partition digest:**
  `4fade91abc408264989babcff6f8f9bbd80bcec52545a5db15ac376bf17d88fc`

Fix the deployed KoalaBear MCA candidate

```text
p=2130706433,       F=F_(p^6),
n=2097152,          k=1048576,       a=1116048.
```

For every admissible received line, use the exact far/sparse reduction from
`rate_half_mca_sparse_layer_reduction`. In the column-far case declare the
source-coordinate tangent image empty. Otherwise choose the lexicographically
first common explaining codeword pair and translate once. If its discrepancy
support is `Sigma`, then

```text
|Sigma|<=n-a=981104.                                  (KB-T1)
```

For the translated pair `(e_0,e_1)`, let

```text
T={-e_0(x)/e_1(x): x in Sigma, e_1(x)!=0}.             (KB-T2)
```

The complete MCA-bad slope set is unchanged by the translation and
`|T|<=|Sigma|`. Hence the first-match cell

```text
Z_paid=Z_bad intersect T
```

satisfies the uniform exact-row cap

```text
|Z_paid|<=981104.                                      (KB-T3)
```

Apply the frozen Q and balanced-core predicates to the successive residuals,
and put every remaining bad slope in `Z_new`. The four cells

```text
Z_paid, Z_Q, Z_BC, Z_new
```

are pairwise disjoint and have union `Z_bad`. Thus, for any uniform caps on
the three unpaid cells,

```text
|Z_bad| <= 981104 + U_Q + U_BC + U_new.                (KB-T4)
```

Exact integer arithmetic gives

```text
B*=floor(|F|/2^128)=274980728111395087,
B*-981104=274980728110413983.                           (KB-T5)
```

No value is proved here for `U_Q`, `U_BC`, or `U_new`. The legacy value
`U_paid=422354730332` is not imported. This atom proves neither the KoalaBear
row, its unsafe predecessor, nor any adjacent Prize threshold.
