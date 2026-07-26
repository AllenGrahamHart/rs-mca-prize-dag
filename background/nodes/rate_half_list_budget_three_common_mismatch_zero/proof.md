# Proof

The budget-three intersection reduction proves that every viable selected
incidence pattern has `n_0=0`. Equivalently,

```text
D=S_0 union S_1 union S_2 union S_3.                 (1)
```

Take `x in G`. By the definition of the direction code, all four codewords
have the same value at `x`:

```text
c_0(x)=c_1(x)=c_2(x)=c_3(x).                         (2)
```

By `(1)`, there is an index `i` with `x in S_i`. Since `S_i` was chosen
inside the agreement set of `c_i`,

```text
c_i(x)=u(x).                                         (3)
```

Equations `(2)` and `(3)` show that the common value at every point of `G`
agrees with `u`. Thus `g=|G|=z`, and hence `b=z-g=0`. QED.
