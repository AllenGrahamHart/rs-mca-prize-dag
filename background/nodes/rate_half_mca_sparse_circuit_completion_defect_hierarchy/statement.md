# Sparse-circuit completion-defect hierarchy

- **status:** PROVED
- **support depths:** `d_2=7`, `d_3=2`, `d_4=1`, `d_5=0`

Use the dimension-ten completion-ladder setup and put `q=K-10`.  Fix a
support size `c` and an integer `s>=1` satisfying

```text
(s+2)c-s-1<=10.                                    (DH)
```

If one independent `(c-1)`-deletion has `q-s` completions, then every
support-`c` circuit lies in one carrier of size at most

```text
q+(s+1)(c-1).                                      (DC)
```

Consequently, with

```text
d_c=floor((11-2c)/(c-1)),
```

the support-`c` incidence cap is the maximum of the carrier counts `(DC)`
for `1<=s<=d_c` and the deletion count with at most `q-d_c-1`
completions.  Thus

```text
d_2=7,       d_3=2,       d_4=1,       d_5=0.
```

At `K'=23`, the active completion maxima for supports `2,3,4,5` are
respectively

```text
5, 10, 11, 12.
```

## Falsifier

`q-s` completion labels of dimension below `q-s`; failure to span the
support-`c` label space with at most `s` further labels; a representation
outside the carrier while `(DH)` holds; or an exact incidence above the
declared hierarchy maximum.
