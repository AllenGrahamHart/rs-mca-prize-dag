# Proof

For each `d=1,...,9`, the canonical-basis globalizer bounds the number of
decorated rank-`d` incidences above a fixed rank-`(10-d)` basis by

```text
M_d C(K'-10,d+1).
```

There are `C(n',10-d)` possible bases. The multi-basis decoration theorem
says that every undecorated rank-`d` incidence occurs under at least `d+2`
bases. Hence its aggregate capacity is the corresponding summand in (1).
The nine corank strata are disjoint, so their integer floors may be summed.

The dominant kernel-lane demand from the rank-eleven component-incidence
dichotomy is

```text
D(K')=ceil(495405467*N_min*C(m',11)/10^9).           (3)
```

The primary verifier evaluates (1) and (3) with exact integers at all
11,632 rows from `K'=10` through `K'=11641`. Every row has `D>A_multi`.
The independent verifier reconstructs all binomial coefficients by
factorial quotients, reconstructs each `M_d` from the two support-local
endpoints, and repeats the interval comparison without importing the
primary implementation.

At the endpoint,

```text
D(11641)=
2591384066635142502908383042256351622731341380873039963561978373,

A_multi(11641)=
2591366297181592043758997588431403606654604298535516256668116289.
```

Their difference is the stated positive gap. At the next row,

```text
D(11642)=
2591744422433696117405077127353817203908414876886966153966883140,

A_multi(11642)=
2591931453757282857595955896472738264566777184331157486904335756,
```

so the comparison reverses by the stated amount. This proves exactly the
printed interval and no more.
