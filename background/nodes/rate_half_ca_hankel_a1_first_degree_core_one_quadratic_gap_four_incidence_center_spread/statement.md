# `A=1` core-one quadratic gap-four incidence-center spread

- **status:** PROVED
- **closure:** exact locator design and column-far codeword-line cap
- **consumer:** `rate_half_band_crossing_location`

Retain the core-one scalar quadratic double-root packet at `u=4`. Put

```text
rho=3e-1,       N=4rho,       T=rho+4,       d=rho-1. (ICS1)
```

For each supported slope `gamma`, let `E_gamma subset D` be the full root
set of the specialized split degree-`rho` locator. Then

```text
|E_gamma|=rho       for every gamma.                 (ICS2)
```

There is a partition

```text
D={s_0} disjoint_union L disjoint_union {x_*}
  disjoint_union H_0                                  (ICS3)
```

with

```text
|L|=3rho+5,       |H_0|=rho-7,                       (ICS4)
deg_Z(s_0)=T,
deg_Z(x_*)=e-6,
deg_Z(x)=e       for x in L,
deg_Z(x)=0       for x in H_0.                       (ICS5)
```

Here `deg_Z(x)=|{gamma:x in E_gamma}|`. Thus the retained packet is an
exact nonuniform block design, not only an aggregate incidence count.

Let `f_gamma=f_0+gamma f_1` be the received word at a supported slope.
Because the rate-half RS code has minimum distance `2rho+1`, there is a
unique codeword `c_gamma in C` with

```text
wt(f_gamma-c_gamma)<=rho.                            (ICS6)
```

Let

```text
Z_*={gamma:x_* in E_gamma},       |Z_*|=e-6.         (ICS7)
```

The actual error weights are exact:

```text
wt(f_gamma-c_gamma)=rho-1       if gamma in Z_*,
wt(f_gamma-c_gamma)=rho         if gamma notin Z_*.  (ICS8)
```

Any affine codeword line

```text
c(t)=c_0+t c_1,       c_0,c_1 in C                  (ICS9)
```

containing `h` assigned centers, of which `r` lie in `Z_*`, satisfies

```text
h<=rho+1-r.                                          (ICS10)
```

Hence, for every two distinct supported slopes `alpha,beta`, at least

```text
3+|{alpha,beta} intersect Z_*|                       (ICS11)
```

other supported slopes `gamma` satisfy

```text
|E_alpha union E_beta union E_gamma|>=2rho+1.        (ICS12)
```

## Scope

The theorem does not prove that the exact design `(ICS2)--(ICS5)` is
impossible. It isolates the next joint combinatorial gate: any realization
must satisfy the locator degrees and the center-line/triple-union spread
simultaneously.
