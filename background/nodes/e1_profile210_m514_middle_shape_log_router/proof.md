# Proof

For `E<=13`, every nonzero integral autocorrelation has magnitude at most
three. Let `(n_1,n_2,n_3)` count those of magnitudes one, two, and three. Then

```text
E=n_1+4n_2+9n_3,
L=sum_d |A_d|=n_1+2n_2+3n_3,
|x_u|<=2L.                                           (1)
```

The exact square partitions of `E=5,...,13` give 32 profiles.

## The sparse energy-five profile

For `(E;n_1,n_2,n_3)=(5;1,1,0)`, equation `(1)` gives `|x_u|<=6`. On
`[-6,6]`,

```text
log(1+x/18)>=x/18-(13/6400)x^2.                     (2)
```

The derivative of the difference has one negative turning point, so it is
enough to check `x=-6`. The positive atanh series with parameter `1/5`
gives

```text
log(3/2)<73/180<1951/4800=1/3+36*(13/6400),         (3)
```

with margin `13/14400`. Summing `(2)` and using
`sum x_u^2=128E=640` gives

```text
log Norm>=64log(18)-13/10.                          (4)
```

The geometric exponential majorant gives

```text
exp(13/10)<(1-13/160)^(-16)=(160/147)^16
           <18^64/(514*p_max).                      (5)
```

Thus this profile lies above the official interval.

## The high-middle profiles

Put `z=69/50`. For each boundary pair

```text
(E,L)=(9,3),(10,6),(11,7),(12,10),(13,11),          (6)
```

set `C_E=z/(128E)`. Exact one-term atanh sums plus geometric tails prove

```text
log(1+2L/18)<2L/18-C_E(2L)^2.                       (7)
```

The five rational margins, in the order `(6)`, are

```text
253/100800,
11/36000,
931/95040,
607/229824,
321013/16286400.                                    (8)
```

Moreover

```text
1/(36(18+2L))<C_E<1/648.
```

Hence the derivative of
`log(1+x/18)-x/18+C_E x^2` has one turning point in `(0,2L)`; the function is
nonpositive on `(-18,2L]` by `(7)` and its value zero at the origin. The same
majorant applies to every profile at that energy with `L1<=L`. Summing gives

```text
log Norm<64log(18)-C_E*128E
        =64log(18)-69/50.                           (9)
```

Finally,

```text
exp(69/50)>1+z+z^2/2+z^3/6+z^4/24
          >18^64/(514*p_min),                       (10)
```

by exact cross-multiplication. Every profile covered by `(6)` is therefore
below the official interval.

Deleting the sparse energy-five profile and the five downward-closed `L1`
classes from the 32 square partitions leaves exactly the 17 profiles printed
in the statement. QED.
