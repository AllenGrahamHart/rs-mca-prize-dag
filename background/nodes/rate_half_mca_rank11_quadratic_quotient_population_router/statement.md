# Quadratic quotient population router

- **status:** PROVED
- **scope:** the 255,011,043-record synchronized residual after nonzero
  affine-reflection charging

Assume no admissible packet emits `chi>=2299571`. Let `q` be the number of
first-owned pair types whose synchronized pencil is one of the quadratic
cyclic/dihedral quotient classes. Then each such type owns at most

```text
C_Q=floor((n-(m-2))/2)=490553                       (QP1)
```

records. If `R_other` is the residual mass on every other synchronized
pencil class, then

```text
R_other >= max(0,255011043-490553q).                (QP2)
```

Consequently, either a synchronized nonquotient pencil survives or at least

```text
ceil(255011043/490553)=520                          (QP3)
```

distinct first-owned pair types carry quotient-factored rational slope maps.
The latter is an aggregate quotient-population target, not one exceptional
pencil.

Selected exact tradeoffs are:

```text
q cap       nonquotient mass floor    one-type averaging floor
0                 255011043                    4370
100               205955743                    3536
200               156900443                    2698
300               107845143                    1858
400                58789843                    1015
500                 9734543                     169
517                 1395142                      25
518                  904589                      16
519                  414036                       8
```

Every nonempty synchronized type already has at least 29 records, so the last
three averaging floors are informational only.

## Falsifier

A quotient type with more than 490,553 pairwise-disjoint degree-two
exceptions outside its common core; overlap of first-owned type currencies;
incorrect residual subtraction; or treating 520 types as a payment.
