# Proof

The core-free endpoint has no nonconstant parameter-independent factor of
`Q`, and minimal-basis primitivity excludes a parameter-only factor.  Gauss's
lemma therefore gives `(CPR2)` with primitive irreducible factors satisfying

```text
r_i>=1,       e_i>=1,
sum_i r_i=rho,       sum_i e_i=m.                     (1)
```

No specialization `Q_i(U,V;x)` at `x in D` is the zero parameter form;
otherwise `X-x` would divide `Q_i`.  Likewise no specialization at a
supported parameter is identically zero in `X`; otherwise its parameter
linear form would divide `Q_i`.  Both alternatives contradict the positive
bidegrees and irreducibility just recorded.

For each component, let

```text
I_i=|{(x,gamma) in D x Z:Q_i(gamma;x)=0}|.             (2)
```

Counting in a fixed parameter fiber and in a fixed domain column gives

```text
I_i<=T*r_i,       I_i<=N*e_i.                         (3)
```

The union of the component incidence sets is the zero set of `Q` on
`D x Z`.  Thus

```text
sum_i I_i=I+E                                          (4)
```

for a nonnegative overlap count `E`.  Define the row shortfall

```text
D_i=T*r_i-I_i>=0.
```

Equations `(CPR1)`, `(1)`, and `(4)` give the exact aggregate ledger

```text
sum_i D_i
 =T*rho-(I+E)
 =O-E
 <=O
 <=m-1.                                               (5)
```

The column bound in `(3)` now implies

```text
D_i>=T*r_i-N*e_i.                                     (6)
```

If `r_i>=4e_i+1`, then

```text
T*r_i-N*e_i
 >=T(4e_i+1)-N e_i
 =4e_i+T
 >m-1,
```

contradicting `(5)`.  Hence

```text
r_i<=4e_i                                              (7)
```

for every component.  The nonnegative integer defects

```text
a_i=4e_i-r_i
```

sum, by `(1)`, to

```text
sum_i a_i=4m-rho=1.                                   (8)
```

Exactly one component has `a_i=1` and all others have `a_i=0`.  This proves
`(CPR3)` and `(CPR4)`.

Every balanced component satisfies, again by `(6)`,

```text
D_i>=T*(4e_i)-N e_i=4e_i.
```

Summing this inequality away from the unique defect-one component and using
`(5)` yields

```text
4 sum_(i!=i_*)e_i<=m-1.                               (9)
```

This is `(CPR5)`.  Since `m>1`, its lower bound on `e_(i_*)` is at least two,
which excludes complete splitting into parameter-linear factors.

For `m=2^37`, equation `(9)` gives residual parameter degree at most
`2^35-1`; subtracting from `m` gives `e_(i_*)>=3*2^35+1`, and `(CPR3)` gives
`r_(i_*)>=3*2^37+3`.  This proves `(CPR6)`.  QED.
