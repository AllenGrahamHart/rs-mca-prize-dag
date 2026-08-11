# `A=1` first-degree constant heavy-incidence pin

- **status:** PROVED
- **closure:** cancelled-row recurrence charge and exact incidence balance
- **consumer:** `rate_half_band_crossing_location`

Retain one of the two parameter-constant first-degree profiles (`j=0`).
Write

```text
A_0=B A_0^res,       deg A_0^res=a,
h=deg B=d-3-a.                                         (CHI1)
```

Let `I_H` be the total number of distinct supported incidences on the `h`
heavy residual-domain rows. Then every such incidence lies in the excess
factor of the specialized recurrence, and hence

```text
I_H<=sum_gamma c_gamma<=Delta.                         (CHI2)
```

The remaining `N-s-h=3rho+3+a` rows are saturated. Exact incidence balance
gives

```text
s=0: I_H+O=(6-a)e-3,       Delta=2e-1;
s=1: I_H+O=(3-a)e-6,       Delta=e-2.                 (CHI3)
```

Consequently the bounded residual degrees sharpen to

```text
s=0,j=0: a in {2,3,4,5};
s=1,j=0: a in {1,2}.                                  (CHI4)
```

At the smallest degrees the complete gap allocations satisfy

```text
s=0,a=2:
 (Delta-I_H)+(Delta-O)=1;

s=1,a=1:
 (Delta-I_H)+(Delta-O)=2.                             (CHI5)
```

## Scope

The theorem does not exclude the six residual degrees in `(CHI4)` or
classify the gap allocations in `(CHI5)` individually.
