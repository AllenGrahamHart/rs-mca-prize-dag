# Sparse completion circuits and rank-nine shadows pay K'=13

- **status:** PROVED
- **closed residual row:** `K'=13`
- **units:** `(record, eleven-subset)` component incidences

At `K'=13`, put

```text
n'=1048589,       m'=67485,       dim V'=10<=dim P_13=13.
```

Rank-deficient component incidences have absolute capacity

```text
K_cap=
  3 C(n',9)*16295594 + C(n',8)*253241283
=206481189843433295842936213010503229833431068859362597823.
```

For full-rank eleven-sets, circuits of size at least six create at least 45
rank-nine shadows.  The common-core offset theorem over `j=9,10,11,12`
gives uniform chart cap

```text
C_*=9278059895199813,
```

and high-circuit capacity

```text
H_cap=870791924265139618716231673259817164224620222733319378834968170.
```

The codimension-three completion theorem gives low-circuit cap

```text
L_*=99254447944649683780146155758753837527116020
```

per record.  At the proved record floor, complete capacity is

```text
898085191110430398284744062896212914931984716650701254999384513,
```

while dense-locator incidence requires

```text
901702217989192688449626641411280218028664942551160634607759137.
```

The positive gap is

```text
3617026878762290164882578515067303096680225900459379608374624.
```

Thus the complete positive-dimensional component target is empty at
`K'=13`, and the remaining rank-nine interval is `14<=K'<=15528`.

## Falsifier

A rank-deficient incidence above `K_cap`; a rank-nine chart above `C_*`; a
high circuit with fewer than 45 rank-nine shadows; a selected support above
the completion cap `L_*`; a nonpositive record coefficient; or failure of
the exact demand-capacity comparison.
