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

For a projective clone class `D`, let `mu_D` be the complete first-owned
slope mass of residual classes contained in the common kernel `B_D`; call
`D` active when `mu_D>0`. At `C=10000`, put

```text
L=M=388650911452.
```

Then every unsafe base-free `2 x 5` branch emits one of:

1. an active projective clone class `D` of at least `10001` actual
   coordinates with `mu_D>=388650911452`; or
2. three coordinates whose evaluation columns on `B` have rank exactly two
   and whose common residual classes carry at least
   `388650911452` first-owned slopes.                         (CL3)

The one-sided consequence of `(CL2)` remains available: if every clone
class, active or not, has size at most `10000`, the rank-two output improves
to `777301822903` slopes.

## Nonclaim

Neither horn is paid here. A projective clone of the residual five-space is
not automatically an owner-pencil coordinate clone, and a rank-two triple
is not automatically a split pencil or a line-global core.
