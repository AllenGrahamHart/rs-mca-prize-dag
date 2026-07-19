# Proof

The factors in `(NSR3)` simplify in the trace coordinate as

```text
r^2-r+1=r(chi-1),       (r+/-1)^2=r(chi+/-2),
r^2+1=r chi,             r^2-4r+1=r(chi-4).          (1)
```

Consequently the three scalar values

```text
c_j=a_j/(4b_j)=q_out/(1+q_out)^2                     (2)
```

are

```text
c_0=1/(4(chi-1)^2),
c_1=(chi-2)^2/(4(chi+2)^2),
c_2=chi^2/(4(chi-4)^2).                              (3)
```

These are exactly `h_j^2`. The nonharmonic scalar identity
`T=c_jS^2` is therefore equivalent to `(NFR4)`, and clearing the nonzero
denominators gives `(NFR7)`.

Likewise the initial outer traces from `(NSR5)` satisfy

```text
y_j=4b_j/a_j-2,                                      (4)
```

and substitution of `(1)` gives exactly `(NFR3)`. The scalar router already
proves that `(NFR5)` is equivalent to recovering a reciprocal pair
`q_out,q_out^(-1)` in `mu_N\{1,-1}`. This proves all trace assertions.

It remains to remove the root-dependent square test. Fix either recovered
`q_out`. Since `4N` divides `p-1`, write

```text
q_out=eta^4,       eta in F_p^*.                     (5)
```

Then

```text
h'=eta^2/(1+q_out)                                  (6)
```

is a square root of `c_j`. Hence `h'=+/-h_j`. Put
`Z=S/(1+q_out)`, as in the remainder-square router. Equations `(5)--(6)`
give

```text
h'S=eta^2 Z.                                         (7)
```

The scalar `eta^2` is itself a square, so `Z` is a nonzero polynomial square
if and only if `h_jS` is one; changing the sign is harmless because
`p=1 mod 4` makes `-1` a square.

Finally `(NFR4)` says `T=(h_jS)^2`. If `h_jS` is a square, then `T` is a
fourth power. Conversely, if `T=W^4`, unique factorization in `F_p[x]`
gives

```text
W^2=+/-h_jS.                                         (8)
```

Again `-1` is a square, so `(8)` makes `h_jS`, and hence `Z`, a square.
Degree comparison gives `deg W=M-1`. Thus `(NFR6)` is exactly the final
square condition of the scalar router once `(NFR4)` holds. Both directions
now follow from that proved exact router. QED.
