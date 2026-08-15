# Cross-support completion-defect carrier

- **status:** PROVED
- **correction dimension:** `10`
- **source support:** `c`
- **target support:** `d`

Use the dimension-ten sparse-circuit setup with `K>=11` and `q=K-10`.
Let `2<=c,d<=9` and `0<=s<=q`.  Suppose one independent
`(c-1)`-deletion has exactly `q-s` circuit
completions.  If

```text
c+(s+1)d-s-1<=10,                                  (XC1)
```

then every support-`d` circuit lies in one carrier of size at most

```text
q+c-1+s(d-1).                                      (XC2)
```

Consequently its selected eleven-set incidence is at most

```text
C(q+c-1+s(d-1),d) C(m-d,11-d).                    (XC3)
```

For source support `c=5` and defects `s=0,1,2,3,4`, the controlled target
supports are respectively

```text
{2,3,4,5,6}, {2,3}, {2}, {2}, {2}.
```

## Falsifier

Completion labels with rank below `q-s`; more than `s` target labels needed
modulo their span; a target circuit outside the carrier while `(XC1)` holds;
or an incidence above `(XC3)`.
