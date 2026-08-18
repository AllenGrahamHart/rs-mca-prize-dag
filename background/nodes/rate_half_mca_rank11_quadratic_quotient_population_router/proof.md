# Proof

The mass router gives, unless one packet is high complexity, at least
`M=255011043` first-owned records on synchronized pencils outside the
nonzero affine-reflection class. These records are partitioned by their
first-owned pair type.

Fix a type in one of the quadratic quotient classes. Its exact supports have
the form

```text
S_gamma=H_0 disjoint_union E_gamma,
|S_gamma|=m,       |E_gamma|=2.
```

Hence `|H_0|=m-2`. Distinct records of one type have pairwise-disjoint
exception locators, so their two-element sets `E_gamma` are disjoint in the
complement of `H_0`. That complement has size

```text
n-(m-2)=2097152-1116046=981106.
```

It follows that the type owns at most

```text
floor(981106/2)=490553=C_Q.                         (1)
```

This argument applies equally to the cyclic and dihedral classes, including
the square-`kappa` fixed points because repeated-root fibers are not among the
split squarefree exception locators.

The first-owner partition makes the record currencies of different pair
types disjoint. Thus `q` quotient types contribute at most `qC_Q` records,
and subtraction from `M` proves `(QP2)`. If no other class occurs, `M<=qC_Q`,
so integer division gives `q>=520`; indeed

```text
519*490553=254597007<255011043,
520*490553=255087560>=255011043.
```

For the table, divide the positive lower bound in `(QP2)` by the maximum
`58361-q` remaining pair types and round upward. The synchronization router
already removed every type below 29 records, which explains the final
qualification. No bound on the total mass of 520 quotient types is proved.
QED.
