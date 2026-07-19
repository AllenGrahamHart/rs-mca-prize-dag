# Budget-three quadratic scrolls are full rank

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`

Use the balanced row basis `U=U_0+XU_1`, `V=V_0+XV_1` from the quadratic
scroll atlas, and put

```text
C=(U_0,U_1,V_0,V_1).
```

For an edge polynomial `b_ij`, write `L_ij=[X]b_ij`. Then

```text
det C=b_01^2 (L_12 L_03-L_02 L_13).                 (QFR1)
```

This determinant is nonzero in all four quadratic chambers.

1. In every pendant chamber, `b_02` is constant while `b_12,b_03` are exact
   linear factors. Thus `L_02=0` and

   ```text
   det C=b_01^2 L_12L_03!=0.                         (QFR2)
   ```

2. In the quadratic `K_4-e` chamber, all four factors
   `b_02,b_03,b_12,b_13` are linear and `b_23` is exactly quadratic. The
   leading coefficient of the Plucker identity gives

   ```text
   [X^2]b_23=(L_02L_13-L_03L_12)/b_01,
   det C=-b_01^3 [X^2]b_23!=0.                       (QFR3)
   ```

Therefore the rank-deficient branch of the quadratic scroll atlas is empty.
Every quadratic B*=3 chamber has the full-rank base-field normal form

```text
C^(-1)A=(alpha,X alpha,beta,X beta)^T.              (QFR4)
```

This theorem removes the quadratic split-unit subbranch. It does not exclude
the full-rank scroll module on the official subgroup.
