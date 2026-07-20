# Proof

An antipodal target has the form

```text
t=1-a^2,       a in H\{1,-1}.                       (1)
```

Because the official subgroup order is even, `-1` belongs to `H`. In odd
characteristic the map `a -> a^2` has fibers exactly `{a,-a}` on `H`.
Consequently `(1)` produces exactly `(n-2)/2` distinct nonzero nonidentity
antipodal targets before the richness filter is imposed.

For every retained target, the proved affine coset-pair theorem gives

```text
R(t)<(51/16)n^(2/3).                                (2)
```

Summing `(2)` over at most `(n-2)/2` selected antipodal targets proves
`(AQM1)`.

Put

```text
T_0=sum_(t antipodal-free, P(t)>=25)R(t).
```

The exact quotient-mass identity gives `T_0+S_A<=Q_n`. The support-overlap
theorem gives at most six overlapping edges on an antipodal-free target and
at most eight on an antipodal target. Therefore

```text
O_6,25^0+(17/10)O_6,25^A
 <=6T_0+(68/5)S_A
 <=6Q_n+(38/5)S_A,                                  (3)
```

which is `(AQM2)`.

Let `D_0,D_A` denote the corresponding disjoint moments and put

```text
B_(n,6)=300n^2-102Q_n.
```

The proved `E=6` compiler says that C36' follows when

```text
(D_0+O_6,25^0)+(17/10)(D_A+O_6,25^A)<=B_(n,6)/8.   (4)
```

By `(3)`, it is enough that

```text
D_0+(17/10)D_A+6Q_n+(38/5)S_A<=B_(n,6)/8.          (5)
```

The primitive shift-pair adapter proves `K_25^c=2D_c`. Multiplying `(5)` by
`20`, substituting this identity, and collecting the two quotient-mass terms
gives exactly

```text
10K_25^0+17K_25^A+152S_A<=750n^2-375Q_n,
```

which proves `(AQM3)`.

Finally, `(AQM1)` gives

```text
750n^2-375Q_n-152S_A
 >750n^2-375Q_n-(969/4)(n-2)n^(2/3).               (6)
```

Every official order has `n>=8192>8000`, hence `n^(1/3)>20`. Also
`Q_n<n^2` and `(n-2)n^(2/3)<n^(5/3)`. The right side of `(6)` is therefore
strictly greater than

```text
(375-969/80)n^2=(29031/80)n^2.                     (7)
```

Thus `(AQM4)` implies `(AQM3)`, completing the proof. QED.
