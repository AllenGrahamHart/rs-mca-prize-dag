# DSP8 primitive cubic shift-pair adapter

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_dsp8_correlation_bound`
- **dependency:** `f3_h3_disjoint_distance_six_split_pencil_router`

Fix an official H3 row with `|H|=n=2^s`. For a retained target `t`, order
the endpoints of one disjoint generic edge as

```text
E={x,y},       F={u,v},       r=xy,       s=uv.
```

With `Q_(t,r)(X)=X^2-(1+r-t)X+r`, put

```text
A_(E,F)(X)=(X-r)Q_(t,s)(X),
B_(E,F)(X)=(X-s)Q_(t,r)(X).                         (SPA1)
```

These are monic split cubics over `H`, decorated by the roots `r` of `A`
and `s` of `B`, and

```text
A_(E,F)-B_(E,F)=t(s-r)X,
A_(E,F)(0)=B_(E,F)(0)=-rs.                         (SPA2)
```

The six roots occupy distinct signed half-basis coordinates. Thus `(A,B)`
is a reduced degree-three, depth-one shift pair with an equal-constant
constraint. It is coefficient-primitive in the shift-pair sense: every
common quotient scale divides both `n` and the locator degree `3`, while

```text
gcd(n,3)=1.                                         (SPA3)
```

Conversely, suppose monic `H`-split cubics `A,B`, decorated roots
`r in Z(A),s in Z(B)`, and a nonzero `lambda` satisfy

```text
A-B=lambda X,       A(0)=B(0)=-rs,       r!=s,      (SPA4)
```

the six roots are distinct modulo antipodes, and the four roots left after
removing `r,s` are nonidentity. Then, with

```text
t=lambda/(s-r),                                     (SPA5)
```

the two residual quadratics are exactly `Q_(t,s)` and `Q_(t,r)`. Subject
to the original target, richness, class, and quotient-line predicates, this
reconstructs one ordered DSP8 edge and one ordered quotient record.

Let `K_25^0,K_25^A` count these decorated ordered primitive shift-pair /
quotient records on the antipodal-free and antipodal target classes. Forgetting
the two internal root orders at each endpoint, but retaining endpoint order,
gives the exact orientation ledger

```text
K_25^c=2D_6,25^c,
J_25^c=4K_25^c=8D_6,25^c.                           (SPA6)
```

Therefore the formerly selected uniform DSP8 sufficient estimate is
equivalently

```text
10K_25^0+17K_25^A<=223n^2.                          (SPA7)
```

The later antipodal quotient-mass payment weakens the live target while using
the same normalization `(SPA6)`. This identifies the whole DSP8 residue as a
coefficient-primitive SP subclass. It supplies no estimate for the
quotient-weighted primitive shift-pair count.
