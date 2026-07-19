# Quadratic MCA staircase and four certified prize rows

- **status:** PROVED
- **object:** support-wise affine MCA with full-field challenge
- **target:** `epsilon*=2^-128`
- **upstream source:** `przchojecki/rs-mca@9262f63c`,
  `experimental/rs_mca_thresholds.tex`

Let `C=RS[F,D,k]`, where `|D|=n`, and let `B_C(a)` be the maximum
number of support-wise MCA-bad finite slopes at agreement at least `a`.
Put `R=n-k`. For every integer `0<=r<=R-1`, if

```text
(n-r)^2 >= n(k+r),
```

then

```text
B_C(n-r)=r+1.                                      (QMS)
```

The upper bound in `(QMS)` holds for every linear MDS code. The matching
lower bound is the universal coordinate-tangent construction.

There are four explicit prime-field multiplicative-subgroup rows with
`k=2^40`:

| rate | `n` | prime `p` | `B=floor(p/2^128)` |
|---:|---:|---:|---:|
| `1/2` | `2^41` | `132540169958804033333249306710494641010898987122689` | `389500552609` |
| `1/4` | `2^42` | `411940680852499481698306614369841346700408394874881` | `1210584858040` |
| `1/8` | `2^43` | `979947269755402568812854322316630667196565607677953` | `2879806199253` |
| `1/16` | `2^44` | `2121285573237585848299875619011192262679065433997313` | `6233898019554` |

In every row, `n | p-1`, the unique order-`n` subgroup
`D<=F_p^*` is a smooth evaluation domain, and exact arithmetic gives

```text
B_C(n-B+1)=B,             B_C(n-B)>=B+1.           (ADJ)
```

Consequently the complete safe real-radius set is

```text
{delta:e_mca(C,delta)<=2^-128}=[0,B/n).
```

The largest safe grid radius is `(B-1)/n`; `B/n` is the real supremum and
is unsafe. These are exact MCA determinations for four particular eligible
rows. They do not determine the canonical near-capacity corridor rows, any
ordinary or interleaved list threshold, or a universal threshold for every
smooth-domain code of the same rate.
