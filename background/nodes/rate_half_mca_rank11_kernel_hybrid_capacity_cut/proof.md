# Proof

For each corank `d`, the ambient all-bases capacity gives `I_d<=A_d`, while
summing the record-support capacity over all `R_actual` residual records
gives `I_d<=R_actual P_d`. Therefore

```text
I_kernel <= sum_d min(A_d,R_actual P_d).             (1)
```

Divide by `R_actual`. Every function

```text
min(A_d/R_actual,P_d)
```

is nonincreasing in `R_actual`. Since `R_actual>=N_min`, (1) is at most

```text
R_actual sum_d min(A_d/N_min,P_d).                   (2)
```

The dominant kernel lane would require at least

```text
(495405467/10^9) R_actual C(m',11)                  (3)
```

incidences. Thus it is enough to compare (2) and (3) at `N_min`.
Multiplying through by `N_min`, the exact hybrid capacity is

```text
H(K')=sum_d min(A_d,N_min P_d).
```

This is the per-corank minimum of the two independently proved summation
orders; no branch is mixed before its integer floor.

The primary verifier evaluates `H(K')` and the integer demand ceiling on
all 11,763 rows from `K'=10` through `K'=11772`. The independent verifier
reconstructs binomial coefficients, support-local caps, both branch
capacities, and every comparison separately.

At `K'=11772`,

```text
demand =
2638980478250968287927366543992242676555390991946419343981097642,

H =
2638903974174462694978733516078665795830897396664276494570912558.
```

At `K'=11773`,

```text
demand =
2639346846038291415008760907926714174516393961642653417898655661,

H =
2639486189720820646481083733448228217124918530806334200349274605.
```

These differences prove exactly the printed interval and first reversal.
