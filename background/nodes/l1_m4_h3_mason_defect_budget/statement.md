# L1 m=4, h=3 Mason defect budget

- **status:** PROVED
- **dependencies:** `l1_m4_h3_colored_cyclic_equivalence`,
  `l1_official_max_split_value_complement_census`
- **consumer:** `l1_mixed_petal_amplification`

Fix an official Mersenne row

```text
n=4(p+1),       h=3,       u=n-3p=p+4.                 (MDB1)
```

If a three-fiber split pencil exists, depress its outer cubic and write the
exact domain factorization as

```text
(R^3+aR+b)D=X^n-alpha,                                 (MDB2)
```

where `R` is monic of degree `p`, `D` is the monic squarefree complement of
degree `u`, and `D(0)!=0`. Put `nu=ord_0(R)` and `U=R/X^nu`.

Then the linear coefficient of the depressed cubic is nonzero:

```text
a!=0.                                                   (MDB3)
```

Moreover

```text
0<=nu<=4.                                               (MDB4)
```

There is an explicit nonzero low-degree Wronskian eliminant. Put

```text
L=n-3nu,
H=3X U'D+X U D'-LUD.
```

Then

```text
H!=0,       deg H<=4-nu.                               (MDB5)
```

Define the two nonnegative defect integers

```text
delta_A=deg(U)+deg(D)-deg(rad(UD)),
B_0=((aR+b)D+alpha)/X^(3nu),
delta_B=deg(B_0)-deg(rad(B_0)).                         (MDB6)
```

Here radicals are taken over the algebraic closure. Then

```text
K=(UD/rad(UD))(B_0/rad(B_0)) divides H,
delta_A+delta_B<=deg H<=4-nu.                           (MDB7)
```

Thus every repeated root of `U`, every overlap between `U` and `D`, and
every repeated root of `B_0` is localized at a root of the same quartic-or-
smaller `H`, with multiplicity charged by `K`.

Thus a hypothetical record lies in one of five valuation cases. At `nu=4`,
`H` is a nonzero constant, `U` is squarefree and coprime to `D`, and `B_0`
is squarefree. At `nu=3`
there is at most one unit of repeated-root or overlap defect, and similarly
through `nu=0` with total budget four.

This is a finite low-defect classification target. It does not prove that
the five cases are empty, count their components, classify nonembedded
two-fiber records, treat `m=8,16`, or close L1.
