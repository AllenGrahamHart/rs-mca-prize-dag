# Proof

Assume `S>=18167` and `h<=S-2`. Write

```text
q=b-S+1=38386-T-S+1.
```

Since `T>=1`,

```text
h+1 <= S-1,
q <= 38385-(S-1).
```

For the dimension-two residuals, the denominator of the intermediate
ordered-basis term is at most

```text
max_(x>=18166) x(38385-x)^2
=18166*20219^2
=7426405419526.
```

The maximum is at the left endpoint because `x(38385-x)^2` is decreasing
for `x>38385/3`. Therefore the intermediate dimension-two count is at least
`187184`.

For dimension-three residuals, the denominator is at most

```text
max_x x(38385-x)=floor(38385^2/4)=368352056,
```

so its count is at least `3381`. With the exact fixed-class charges

```text
R_4=63397365764,  R_6=16100859197492,
```

the two intermediate terms cost `66303977459889028`. This is already above
the full allowance `B*-E_transverse=65167969673715470` by
`1136007786173558`.

The only remaining choice is `h=S-1`, for which no intermediate class exists.
Then absence of an `S`-rich proper flat is precisely `(S-1)`-transversality.
The exact all-cutoff scan in the parent router proves that the largest payable
threshold is `h=18165`, hence the largest output is `S=h+1=18166`.
