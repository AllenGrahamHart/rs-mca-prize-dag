# Kernel ambient/record hybrid capacity cut

- **status:** PROVED
- **scope:** the dominant rank-deficient lane for `10<=K'<=11772`
- **units:** `(record, eleven-subset)` incidences

Let `R_actual` be the number of post-near non-dense residual records, so
`R_actual>=N_min=274980728111260126`. For corank `d`, write

```text
A_d(K') = floor(
  C(n',10-d) M_d C(K'-10,d+1)/(d+2)),

P_d(K') = floor(
  C(m',10-d) C(K'-10,d+1)/(d+2)).
```

The ambient multi-basis theorem gives `I_d<=A_d`; the record-support theorem
gives `I_d<=R_actual P_d`. Hence

```text
I_kernel/R_actual
  <= sum_d min(A_d/R_actual,P_d)
  <= sum_d min(A_d/N_min,P_d).                       (H)
```

Exact integer replay proves that the right side of (H) is below the
dominant kernel-lane demand for every `10<=K'<=11772`. At the endpoint,
the demand exceeds the hybrid capacity by

```text
76504076505592948633027913576880724493595282142849410185084.
```

At `K'=11773`, the hybrid capacity exceeds demand by

```text
139343682529231472322825521514042608524569163680782450618944,
```

so the method stops there. At both boundary rows, the ambient cap is chosen
for `d=1,2` and the record-support cap for `d=3,...,9`.

## Falsifier

A row in the closed interval where the hybrid capacity reaches demand;
failure of monotonicity in `R_actual` after normalization; a boundary
stratum choosing the opposite branch; or a claim beyond `K'=11772`.
