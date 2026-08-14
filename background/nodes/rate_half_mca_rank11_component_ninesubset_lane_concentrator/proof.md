# Proof

Let

```text
N=274980728111260126,
lambda=495405467/10^9.
```

The component-incidence theorem says that the two declared lanes together
carry at least twice `lambda` of all pairs `(gamma,T)`, where `gamma` is a
record and `T` is an eleven-subset of its support. Choose a lane with at
least

```text
I >= lambda*N*C(m',11)                              (1)
```

incidences.

For every incidence `(gamma,T)` in that lane, mark all
`C(11,9)=55` pairs `(gamma,B)` with `B subset T` and `|B|=9`. For a fixed
pair `(gamma,B)`, its eleven-subset `T` is obtained by adjoining two
coordinates from `S_gamma minus B`. Hence it is marked at most

```text
C(m'-9,2)                                           (2)
```

times. The number `P` of distinct marked `(gamma,B)` pairs therefore obeys

```text
P >= 55*I/C(m'-9,2)
  >= lambda*N*C(m',9),                              (3)
```

where the last equality uses

```text
55*C(m',11)=C(m',9)*C(m'-9,2).
```

Averaging (3) over all `C(n',9)` domain nine-subsets gives one fixed `B`
carrying at least

```text
ceil(lambda*N*C(m',9)/C(n',9))                     (4)
```

distinct records in the chosen lane.

The binomial ratio in (4) is the product of the nine factors

```text
(67472+K'-i)/(1048576+K'-i),  0<=i<=8.
```

Every factor increases with `K'`, because `1048576>67472`. Thus the minimum
is at `K'=10`. Exact integer evaluation there gives

```text
ceil((495405467/10^9)*274980728111260126
     *C(67482,9)/C(1048586,9))
 =2578110.
```

The lane was fixed before marking, so every retained record has an
extension in that same lane. This proves the statement.
