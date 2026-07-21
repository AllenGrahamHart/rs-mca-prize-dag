# HGE4 near-third Kummer midpoint pencil

- **status:** PROVED
- **consumers:** `f3_hge4_kummer_midpoint_trace_power_gate`,
  `f3_hge4_norm_gate_count`
- **dependency:** `f3_hge4_near_third_belyi_necklace_bound`

Retain the near-third notation over a field `K` containing `mu_m`:

```text
m=3h+e,       0<e<h,       c=h+e,
U=S-ay^h,     V=S+ay^h,     D=UV,
DW=1-y^m,     deg W=c,
F=Z^(-1/3),  S=F mod y^c,  deg Z=e,  deg S=h.
```

There is a unique scalar `lambda in K` such that

```text
W=ZS+lambda y^c.                                  (KMP1)
```

Put `kappa=1-a^2 lambda`. Then `kappa!=0` and

```text
S | 1-kappa y^m.                                  (KMP2)
```

Thus every surviving near-third pair belongs to the three-member divisor
pencil

```text
S-ay^h,       S,       S+ay^h,                    (KMP3)
```

whose outside members divide `1-y^m` and whose midpoint divides one twisted
binomial `1-kappa y^m`.

If `K=F_q`, let `theta=kappa^(-1)`, choose `alpha^m=theta`, and put

```text
eta=alpha^(q-1) in mu_m,       d=ord(eta).
```

Every irreducible factor of `y^m-theta` over `K` has degree `d`. In
particular,

```text
d | m,       d | h,       d | gcd(m,h)=2^v_2(h). (KMP4)
```

In fact primitivity forces

```text
d=1.                                               (KMP5)
```

Indeed, if `d>1`, Frobenius stability gives `S(eta y)=S(y)`, while `d|h`
gives `eta^h=1`. Hence both `S-ay^h` and `S+ay^h` have the same nontrivial
scaling stabilizer `eta`, contrary to primitivity. Therefore the midpoint
`S` splits over the base field at every width, and all three pencil members
are base-field split.

This is a structural router, not an orbit bound or an emptiness theorem.
