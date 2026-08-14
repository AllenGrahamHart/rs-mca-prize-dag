# Kernel nine-shadow containment coupling

- **status:** PROVED
- **scope:** one residual record and the complete kernel incidence union
- **units:** flags `(eleven-subset, contained nine-subset)`

For one exact residual support `S`, let `I_d(S)` count rank-`(10-d)`
eleven-subsets, and put

```text
I(S)=sum_(d=1)^9 I_d(S),
B_9=C(m',9),
E_0=C(m'-9,2),
E_1=C(K'-10,2).
```

Then

```text
[52+3E_0/E_1] I_1(S) + 55 sum_(d=2)^9 I_d(S)
  <= E_0 B_9.                                        (FC)
```

If `E_1=0`, the corank-one incidence count is zero and (FC) is read after
deleting its first term.

To prove (FC), partition the record's nine-subsets into rank nine and lower
rank. A rank-nine nine-subset extends to a kernel eleven-set in at most
`E_1` ways, while every lower-rank nine-subset extends in at most `E_0`
ways. Every corank-one eleven-set has at least three spanning rank-nine
nine-subsets. Counting all 55 contained nine-subsets, rather than only the
spanning shadows, gives (FC).

## Falsifier

A rank-nine nine-subset extending outside its rank-nine closure; more than
`E_0` support-pair extensions of one lower-rank nine-subset; a corank-one
eleven-set with fewer than three spanning nine-subsets; or a record
violating (FC).
