# Rank-eleven factor-flag clone/line dichotomy

- **status:** PROVED
- **scope:** the base-free `2 x 5` residual-flag family

Let the deep residual classes have total first-owned slope mass at least

```text
E=30210771209598495
```

and choose `b=37736` common-zero coordinates from every class. Put

```text
U=1116048,
R_4=63397365764,
R_8=4088807947303996.
```

The total weighted incidence on coordinate triples of residual evaluation
rank at most two is at least

```text
I_low=E C(b,3)-R_4 C(U,3)
     =255859400991343449179217479656.                 (CL1)
```

For any integer `3<=C<=U`, if every projective clone class of nonzero
evaluation columns on `B` has size at most `C`, define

```text
T_clone(C)=floor(U/C) C(C,3)+C(U mod C,3).
```

Then some genuine rank-two coordinate triple carries first-owned slope mass
at least

```text
ceil(max(0,I_low-R_8 T_clone(C))/C(U,3)).              (CL2)
```

In particular, at `C=10000`, every unsafe base-free `2 x 5` branch emits
one of:

1. a projective clone class of at least `10001` actual coordinates; or
2. three coordinates whose evaluation columns on `B` have rank exactly two
   and whose common residual classes carry at least
   `777301822903` first-owned slopes.

## Nonclaim

Neither horn is paid here. A projective clone of the residual five-space is
not automatically an owner-pencil coordinate clone, and a rank-two triple
is not automatically a split pencil or a line-global core.
