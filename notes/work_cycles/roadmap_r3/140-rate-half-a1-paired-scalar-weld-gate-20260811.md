# Cycle 140: rate-half `A=1` paired scalar-weld gate (2026-08-11)

## One common-biform system

The fixed-domain and zero-excess parameter factorizations cannot be tested as
independent biforms. On every nonincidence cell they obey

```text
lambda_x P_x(delta)=zeta_delta F_delta(x).
```

Choose one nonincident anchor per fiber and eliminate `zeta_delta`. This adds
a sparse matrix `W`, with exactly two nonzero entries per row, to the existing
fixed-domain coefficient matrix. The row and fiber data are realized by one
biform if and only if

```text
[Krow; W] lambda=0
```

has a kernel vector with every coordinate nonzero. The converse is exact:
`Krow` reconstructs the biform coefficientwise, while `W` makes each selected
fiber agree with its full padded root polynomial on more points than its
degree. The parameter-direction coefficient gate then follows automatically
and is not counted as independent evidence.

The guaranteed weld-row lower bounds at zero line deficit on the official row
are

```text
extremal: 201487636602438195784362,
strict:    75557863726738957139970.
```

These row counts are not rank arguments.

## Burn-down

```text
result:                  PROVED scalar-weld augmented-kernel equivalence
DAG delta:               +1 PROVED
DAG after compile:       2292 nodes, 6736 edges
critical status delta:   none; 28 every-route TARGETs remain
node replay:             normal/-O/audit/tamper all pass
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

The next falsifier is now small in description: an allowed incidence/root
profile whose augmented matrix has a full-support kernel. Such a survivor
must then be checked against the retained Hankel/source identities; absence
of a survivor in random profiles is not a proof.
