# Proof

Fix `14<=K'<=21`, and put `n=1048576+K'`, `m=67472+K'`, and
`q=K'-10`.

## 1. Rank-deficient capacity

For evaluation corank `d`, the canonical-basis globalizer gives extension
factor `C(q,d+1)`.  Retain every `1<=d<=min(9,q-1)`.  Its fixed-basis record
cap is

```text
M_d=floor(max{
  (1048576+s)_fall_(d+1)/((67472+s)(67473)_rise_(d-1)),
  (1048576+d)_fall_(d+1)/(67473)_rise_d
}),

s=K'-(10-d),                                             (1)
```

for `d<=8`; use the proved `M_9=61871313426630599` at `d=9`.  Hence the
absolute kernel capacity is

```text
K_cap=sum_d C(n,10-d) M_d C(q,d+1).                       (2)
```

No rank-deficient incidence enters the full-rank shadow ledger.

## 2. One joint full-rank ledger

For every core size `9<=j<K'`, specialize the weighted split-pencil theorem
at

```text
P=m-j,       S=n-j,       r=j-9.
```

Let `C_*` be the maximum of these exact chart caps and put

```text
G=C(n,9) C_*.
```

The verifier scans every honest `j`; on all eight rows the maximum is at
`j=K'-1`.

For one record, the completion theorem gives two support-cap vectors:

```text
L_c^S=C(q+4,c)C(m-c,11-c),

L_c^U=floor(C(m,c-1)(q-1)C(m-c+2-q,11-c)/c).       (3)
```

Here `q-1` is the exact completion-count maximizer throughout the declared
range.  A support-`c` circuit creates

```text
q_c=55-C(11-c,2)
```

rank-nine shadows.  Applying the joint ledger to (3) gives

```text
P_*=max_(a in {S,U}) sum_(c=2)^5 (45-q_c)L_c^a,

F_cap=floor((G+R_actual P_*)/45).                   (4)
```

The unstructured premium is larger on every row, but both branches are
computed before taking the maximum.

## 3. Exact row comparison

The dense-locator component theorem requires

```text
D(R_actual)=ceil((990810934/10^9)R_actual C(m,11)). (5)
```

For every row the record coefficient

```text
45*990810934*C(m,11)-10^9*P_*                     (6)
```

is positive.  At `R_min=274980728111260126`, the stronger unfloored cross

```text
R_min*(6)-10^9*(45*K_cap+G)
```

is positive.  Therefore (5) exceeds `(2)+(4)` at the floor and for every
larger record population.  Exact evaluation gives the eight printed gaps.

At `K'=22`, evaluating the identical formulas gives total capacity

```text
905885518366475292751564400874300832826807604203127204847344067
```

against demand

```text
903025989085629081334365478664955214394150391409598064684975031.
```

That next-row comparison is deliberately retained as a method wall, not
promoted to a claim.  QED.
