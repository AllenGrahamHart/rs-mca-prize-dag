# Proof

For `j>=0`, let

```text
A_(j,r)=sum_(a=r mod N/2^j)c_a.
```

Thus `A_(0,r)=c_r`, and one dyadic merge gives

```text
A_(j+1,r)=A_(j,r)+A_(j,r+n_j/2),
b_(j,r)=A_(j,r)-A_(j,r+n_j/2).
```

The parallelogram identity therefore gives

```text
sum_r A_(j,r)^2
 =E_j/2+(1/2)sum_r A_(j+1,r)^2.                    (1)
```

Iterating (1) from `j=0` to `s-1` yields

```text
sum_a c_a^2
 =sum_(j=0)^(s-1) E_j/2^(j+1)
  +(sum_a c_a)^2/N.
```

The signed supports have `sum c_a=|P|-|Q|=0` and
`sum c_a^2=|P|+|Q|=2e`, proving `(HP-1)`.

For every `j in S`, the dyadic norm router gives

```text
p^M_j<=p^(f_j o_j)<=|Norm(beta_j)|<=E_j^a_j.
```

Multiplying these inequalities proves every part of `(HP-2)` except its last
upper bound.  Put

```text
x_j=E_j/2^(j+1),       w_j=a_j/A_S.
```

By `(HP-1)`, `sum_(j in S)x_j<=2e`.  Weighted AM-GM gives

```text
product_(j in S)(x_j/w_j)^w_j <= sum_(j in S)x_j <=2e.
```

Raise to `A_S` and restore the powers `2^(j+1)`.  Since

```text
2^(j+1)a_j=N/2
```

for every `j`, each resulting factor has the same base:

```text
product_(j in S)E_j^a_j
 <=product_(j in S)(2^(j+1) 2e a_j/A_S)^a_j
 =(eN/A_S)^A_S.
```

This proves `(HP-2)` and its cross-multiplied form `(HP-3)`.  The primitive
root-scale nonvanishing and the effective depth `T=e-d-1` are respectively
the root clause of the router and the definition of an exact locator-
difference degree. QED.
