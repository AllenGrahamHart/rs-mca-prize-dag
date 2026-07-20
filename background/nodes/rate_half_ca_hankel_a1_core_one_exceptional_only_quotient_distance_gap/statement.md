# `A=1` core-one exceptional-only quotient-distance gap

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_distance_router`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_factor_pin`

Retain the official exceptional-only face and put

```text
h=delta_A(h_1),       e=2^38-1,       r=2e+1.         (QDG1)
```

Then the quotient distance has the exact gap

```text
h=3,
or
h>=2e/3+3=183251937965.                               (QDG2)
```

In particular, every putative branch

```text
4<=h<=183251937964                                    (QDG3)
```

is empty.

More generally, let `T` be a minimal quotient support of size `h>=4` and put
`S=R_A union T`. Among the `4e` ordinary supported slopes, call a fiber
internal when its clean source representation equals the representation on
`S`. If `N_int` is their number, then

```text
N_int(h-1)<=2e.                                      (QDG4)
```

Every other ordinary clean locator meets `S` in at most `h-3` points. The
exact row-deficit ledger therefore forces the necessary inequality

```text
2e^2+eh-3e
 <=4e(h-3)+floor(2e/(h-1))(2e+4-h).                 (QDG5)
```

Inequality `(QDG5)` fails throughout `(QDG3)`, proving the gap. This theorem
does not exclude the distance-three chart or the high-distance tail in
`(QDG2)`.
