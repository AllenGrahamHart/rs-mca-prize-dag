# XR deficient window: packed four-fiber plane payment

- **status:** PROVED
- **consumer:** `xr_band_forced_commonroot_syzygy_count` (evidence)

Work at the tuple-incidence boundary

```text
ell=floor((h-4)/7),       r=2ell+1,       d=h-r,
sigma=d-ell-1-2r.
```

Let `Tau_pack` be a `D`-local target stratum in which both selected blocks of
every target have exact `phi=[P:Q]` profile

```text
(ell,ell,1).                                           (P4F1)
```

Put

```text
t=e-4ell,       e=|D|.
```

Then

```text
2<=t<=sigma+2.                                         (P4F2)
```

There are exactly four fixed `phi` fibers of size `ell` contained in `D`.
Every selected block is the union of two of those fibers and one point from
the `t`-point tail. There are `6t` possible individual block geometries, each
target contributes two, and a fixed block owns at most three targets on an
affine plane. Consequently,

```text
|Tau_pack intersect plane|<=9t.                       (P4F3)
```

If the affine hull of `Tau_pack` has dimension `s>=2`, put

```text
N=n-e,       w=d+ell,
B_(s-2)=product_(j=3)^s(w+j)/(s-2)!.
```

The independent core-cut incidence gives

```text
|Tau_pack| B_(s-2)
 <=9t binom(N,s-2).                                   (P4F4)
```

At the next unpaid dimensions, exact official arithmetic compares `(P4F4)`
to the complete local allowance as follows.

| rates | `s` | paid exact-packed tails |
|---|---:|---|
| `1/4,1/8` | `11` | every `t=2,...,7` |
| `1/16` | `10` | every `t=2,3` |

This bounds one exact profile stratum. It is not permission to add its full
allowance to a separate cap for another profile, and it does not close a
mixed-profile family or a higher affine dimension.

## Falsifier

An exact-packed target not using four fixed full fibers and two tail points;
more than `9t` such targets on one affine plane; a violation of
`(P4F4)`; or a mismatch in the printed official pass/fail boundary.
