# Deployed pole-line typed witness certificate

- **status:** PROVED
- **closure:** pinned upstream certificate plus independent reconstruction
- **row:** deployed KoalaBear MCA at agreement `1116048`

## Statement

The upstream `#1159` record `KB_SPARSE_BOUNDARY_ACTUAL_RECORD_V1` is a typed,
machine-checked actual MCA witness, not a profile label.

Over the deployed order-`2^21` subgroup, let `E` be the first `67473`
subgroup powers and `S` the following `1116048` powers.  In
`F_p[alpha]/(alpha^6+alpha+6)`, define

```text
v(x)=-1/(x-alpha),
u(x)=1_E(x)+alpha/(x-alpha),
gamma=alpha.
```

Then `u+gamma v=1_E`, so the zero polynomial explains the slope word on the
exact support `S`.  No polynomial of degree below `k`, or even below `k+1`,
explains `v` on `S`; hence the pair is not simultaneously explained there.
The support-complement locator with numerator zero passes the degree-guarded
lattice adapter and reconstructs this identical support and explanation.

The received-word lattice minimum is exactly `67473` under both shifts.  It
is a boundary numerical profile under `K=k` and a first-interior numerical
profile under `K=k+1`.

## Owner field

```text
frozen Q owner:    UNASSIGNED
frozen BC owner:   UNASSIGNED
frozen U_new:      UNASSIGNED
```

The typed witness proves actual badness and profile sensitivity.  Neither
the pinned sources nor this import infer a frozen owner from either numerical
profile.

## Falsifier

A failed field or subgroup check, overlapping exponent intervals, a failed
line cancellation, a degree-below-`k` explanation of the direction word on
`S`, a lower shifted-degree vector, or any upstream replay failure at the
pinned `#1159` head.
