# DLI primitive Haar-event correlation identity

Let `n` and `t=2^m` be powers of two with `t<n`, and let `zeta` have exact
order `n` in an odd-characteristic field. Draw

```text
M_(0,i) in {0,1},       i in Z/n,
```

uniformly and independently. At dyadic junction `j`, put

```text
h_j = n/2^j,
M_(j+1,i) = M_(j,i) + M_(j,i+h_j/2),
D_(j,i)   = M_(j,i) - M_(j,i+h_j/2),
zeta_j    = zeta^(2^j).
```

Let `O_j` be the odd-band null event

```text
sum_(i in Z/(h_j/2)) D_(j,i) zeta_j^(u i)=0
for every odd u with u*2^j<=t,                              (H1)
```

and let `T_m` be the terminal event

```text
sum_(i in Z/h_m) M_(m,i) zeta_m^i=0.                       (H2)
```

Then

```text
{M_0 is null in moments 1,...,t}
    = T_m intersect O_0 intersect ... intersect O_(m-1).   (H3)
```

For the exact weighted tower censuses,

```text
P(O_j)=B_j/2^n,             P(T_m)=Z_m/2^n.                (H4)
```

Let `Prim` be the complement of invariance under the antipodal shift
`i->i+n/2`. With `C_1=Z_0(q,n/2,t/2)`, first-owner deletion gives

```text
P(Prim intersect T_m intersect all O_j)=(Z_0-C_1)/2^n.     (H5)
```

Consequently

```text
J_prim
 = P(Prim intersect T_m intersect all O_j)
   / (P(T_m) product_(j<m) P(O_j))
 = 2^(nm)(Z_0-C_1)/(Z_m product_(j<m) B_j).                (H6)
```

The proposed square-root route is therefore exactly

```text
P(Prim intersect T_m intersect all O_j)
 <= sqrt(2n) P(T_m) product_(j<m) P(O_j).                  (H7)
```

No correlation bound is asserted here.

