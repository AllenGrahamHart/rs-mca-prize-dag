# Budget-three fiber-two c=1 parity Mobius router

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_fiber_two_cycle_c1_normalized_torsion_compiler`,
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_even_factorization`

Retain the normalized generic `c=1` chamber when `D_*` has two
antipodal root pairs. Put

```text
M=2^36,       L=8M=2^39,
D_A(Y)=(Y^2-1)(Y^2-r^4),
r^(4L)=1,       r^4!=1,       iota^2=-1.             (CPM1)
```

The two complete role patterns are

```text
R: unused c=-1,       {b,d}={r^2,-r^2},
   source X_R=(1,-1,r,iota r);

P: unused c=r^2,      {b,d}={-1,-r^2},
   source X_P=(1,-1,iota,iota r).                    (CPM2)
```

Changing signs, conjugating `iota`, or replacing `r` by `-r`
accounts for all lift choices and the alternative unused root `-r^2`.

The even-factorization dependency gives

```text
O(W)=(W^2+lambda)(W^2+mu),       q=mu/lambda in mu_L,
q!=1,
tau_O=q+q^(-1)=(alpha^2-2gamma)/gamma.               (CPM3)
```

For a cross ratio `z`, define

```text
tau(z)=4((z+1)/(z-1))^2-2.                           (CPM4)
```

All denominators below are nonzero. The three perfect matchings of each
source pattern have cross ratios

```text
z_R0=(r-1)(r-iota)/((r+1)(r+iota)),
z_R1= 2(1+iota)r/((r+1)(r+iota)),
z_R2=-2(1+iota)r/((r-1)(r-iota)),                    (CPM5)

z_P0=iota(r-iota)/(r+iota),
z_P1=(1-iota)(r-1)/(r+iota),
z_P2=(1+iota)(r-1)/(r-iota).                         (CPM6)
```

The completion-root Mobius matching holds if and only if

```text
tau_O=tau(z_Xj)                                      (CPM7)
```

for at least one `X in {R,P}` and `j in {0,1,2}` compatible with its
role pattern. No outer-root factorization or permutation search remains.
Each candidate trace must also satisfy

```text
y_0=tau(z_Xj),       y_(m+1)=y_m^2-2,
y_0!=2,       y_39=2,                                (CPM8)
```

which is equivalent to its reciprocal outer-ratio pair lying in
`mu_L\{1}`.

The harmonic value `q=-1`, equivalently `tau_O=-2`, specializes the six
tests to

```text
R0: r^2+iota=0,
R1: r^2+3(1+iota)r+iota=0,
R2: r^2-3(1+iota)r+iota=0,                           (CPM9)

P0: r=-1,
P1: 5r-4+3iota=0,
P2: 5r-4-3iota=0.                                    (CPM10)
```

`P0` contradicts `r^4!=1`. On `R0`, the parity parameter is
`t=r^4=-1`, but

```text
F_(2M)(-1)=(1/4)_M/M! !=0,                           (CPM11)
```

contradicting the primary gap. Up to `r -> -r` and
`iota -> -iota`, only two harmonic residue classes remain:

```text
H_R: r^2+3(1+iota)r+iota=0,
H_P: 5r-4+3iota=0.                                   (CPM12)
```

This theorem does not exclude those two classes or any nonharmonic class.
It does not transfer the matched-cycle field router and authorizes no
characteristic campaign.

