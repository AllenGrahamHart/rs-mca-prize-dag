# E1 prize N=256 square-mass-18 variance/cofactor windows

- **status:** PROVED
- **closure:** proof plus exact rational arithmetic
- **scope:** prize-envelope `N=256`, profile `(a,b,c)=(4,2,0)`
- **dependencies:** `collision_norm_criterion`,
  `e1_prize_field_floor_even_norm_exclusion`,
  `e1_n256_local_norm_cofactor_collapse`

Let `zeta` be a primitive `256`-th root and let

```text
alpha=F(zeta)=sum_(i=0)^127 c_i zeta^i
```

have folded profile `(4,2,0)`. Thus four nonzero coefficients have absolute
value two, two have absolute value one, and

```text
sum_i c_i^2=18,        sum_i |c_i|=10.
```

For odd `u`, put `y_u=|F(zeta^u)|^2` and define

```text
V=(1/128) sum_(u odd) (y_u-18)^2.
```

Suppose `alpha` collides on a pair-feasible prize-envelope row, with row prime
`p`, norm `R=|Norm(alpha)|`, and cofactor `m=R/p`. Then

```text
V = 2 mod 8.
```

The exact pointwise majorant

```text
log x <= log 18+(x-18)/18-(x-18)^2/2367,    0<x<=100
```

and the exact prize field floor give the following cofactor-specific windows.
The onset column means that the listed variance and every larger admissible
variance are impossible.

| `m` | `v_2(m)` | exclusion onset | residual after the exact `V=2` exclusion |
|---:|---:|---:|---:|
| 2 | 1 | `V>=258` | `10<=V<=250`, `V=2 mod 8` |
| 514 | 1 | `V>=58` | `10<=V<=50`, `V=2 mod 8` |
| 1538 | 1 | `V>=10` | empty |
| 4 | 2 | `V>=234` | `10<=V<=226`, `V=2 mod 8` |
| 1028 | 2 | `V>=26` | `V in {10,18}` |
| 16 | 4 | `V>=186` | `10<=V<=178`, `V=2 mod 8` |
| 256 | 8 | `V>=82` | `10<=V<=74`, `V=2 mod 8` |

In particular, the prize-row leading profile has only six live cofactor
classes, and its `1028` class has only two live variance chambers. This is a
necessary collision classification, not a count of vectors in the residual
windows and not a proof of the aggregate E1 pair budget.
