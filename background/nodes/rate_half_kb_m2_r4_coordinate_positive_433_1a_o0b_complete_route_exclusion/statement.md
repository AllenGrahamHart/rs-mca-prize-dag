# KoalaBear positive 433-1a to O0b complete route exclusion

- **status:** PROVED
- **scope:** the complete positive residual route `433-1a -> O0b` over the
  deployed KoalaBear field `F_2130706433`
- **dependencies:** the exact signed-edge atlas, the exact common root-sign
  quotient, and the nine PROVED orbit-exclusion nodes listed in
  `dependency_subdag.md`
- **consumer:** `rate_half_band_closure`

Every packet on this route lies in one of the two signed target lanes of the
signed-edge atlas and has one of the 60 common matching/root-sign rows.  The
exact source-projectivity quotient partitions those 60 rows into ten
algebraically distinct representatives:

```text
[0] | [1,2]_(epsilon_1 epsilon_2=+1)
    | [1,2]_(epsilon_1 epsilon_2=-1)
    | [3,6] | [4,7] | [5,8] | [9,10]
    | [11] | [12,13] | [14].                     (KBPCR-1)
```

The nine orbit-exclusion theorems cover these representatives and raw rows
as follows:

```text
[0]      4 rows      [1,2]    8 rows
[3,6]    8 rows      [4,7]    8 rows
[5,8]    8 rows      [9,10]   8 rows
[11]     4 rows      [12,13]  8 rows
[14]     4 rows                              total 60. (KBPCR-2)
```

Each exclusion is uniform in the signed cycle lane and outside assignment,
or excludes a necessary common/signed-pair subsystem that every such packet
must satisfy.  Therefore no row in either signed lane lifts to a complete
packet.  The positive residual route `433-1a -> O0b` is empty.

This closes one coordinate route only.  It does not close the other
rate-half routes, K3, `rate_half_band_closure`, LIST, MCA, or either Prize
problem.

## Falsifier

An admissible packet outside the two signed lanes or 60 common rows, an
incorrect source-symmetry orbit in `(KBPCR-1)`, a row not covered by
`(KBPCR-2)`, or a guard-valid survivor of any cited orbit theorem.
