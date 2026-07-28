# E1 prize N=256 profile-(3,6) cofactor windows

- **status:** PROVED
- **closure:** proof plus exact finite enumeration
- **scope:** prize-envelope `N=256`, profile `(a,b)=(3,6)`

Let

```text
alpha=F(zeta)=sum_(i=0)^127 c_i zeta^i
```

have three coefficients of absolute value two and six coefficients of
absolute value one. Thus its square mass is `S=18` and its coefficient
`L1` norm is 12. Put

```text
R=|Norm(alpha)|,          mu=v_2(R),
V=(1/128) sum_(u odd) (|F(zeta^u)|^2-18)^2.
```

If `alpha` collides on a pair-feasible prize-envelope row, write `R=pm` for
the row prime `p`. Then

```text
mu in {1,2,3,4,5,6,8,9,10}
```

and the exact possible cofactors are

```text
{2,4,8,16,32,64,256,512,514,1024,1028,1538}.       (1)
```

The variance is a positive even integer and cannot equal two. The remaining
cofactor-specific windows are:

| `m` | exclusion onset | residual even `V` |
|---:|---:|---:|
| 2 | `V>=352` | `4<=V<=350` |
| 4 | `V>=316` | `4<=V<=314` |
| 8 | `V>=280` | `4<=V<=278` |
| 16 | `V>=246` | `4<=V<=244` |
| 32 | `V>=210` | `4<=V<=208` |
| 64 | `V>=176` | `4<=V<=174` |
| 256 | `V>=106` | `4<=V<=104` |
| 512 | `V>=70` | `4<=V<=68` |
| 514 | `V>=70` | `4<=V<=68` |
| 1024 | `V>=36` | `4<=V<=34` |
| 1028 | `V>=36` | `4<=V<=34` |
| 1538 | `V>=14` | `4<=V<=12` |

This is a necessary collision classification. It does not assert that any
listed chamber is populated and does not count the profile's weighted edges.
