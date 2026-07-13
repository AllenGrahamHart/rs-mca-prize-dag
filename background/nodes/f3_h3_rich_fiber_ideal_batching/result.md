# Result

The ideal sandwich `(IB)` is proved uniformly for every dyadic order and every
same-fiber collision family. An exact boundary certificate shows that its
lower bound is attained immediately on both complete rich fibers at

```text
(n,p,g)=(8192,67657729,41542468).
```

The rich locus consists of exactly two targets. Each target has ten distinct
unordered shifted-product representations. Taking the first pair as reference,
the gcd of the principal norms for the next two collisions is already

```text
4p=270630916.
```

The gcd remains `4p` after all nine collision norms are included. Therefore,
for each of the two measured fibers, the first two obstruction differences
generate `(1-zeta)^2 P` exactly.

| target | unordered pairs | gcd of first two norms | gcd of all nine |
|---|---:|---:|---:|
| `40697698` | 10 | `4p` | `4p` |
| `16650852` | 10 | `4p` | `4p` |

The exact norms and pair lists are stored in
`experiments/prize_resolution/h3_rich_norm_gcd_result.json`. They were
computed by eighteen independent 60-second FLINT shards on Modal; run
`ap-WgM34tE25CAe0FYz8owGUJ` completed every shard.

## Route fence

The ordinary two-polynomial resultant is the wrong compressed object on this
row. After dividing the first two obstruction polynomials by their exact
rational polynomial gcd, the reduced resultants still have:

| target | rational gcd degree | resultant bits | non-`p` cofactor bits |
|---|---:|---:|---:|
| `40697698` | 752 | 2906 | 2880 |
| `16650852` | 217 | 3481 | 3455 |

Both rational gcds have two nonzero terms, and both reduced resultants contain
`p` to valuation one. Their large cofactors refute any claim that this raw
resultant operation isolates the row prime up to a small universal factor.
The saturated cyclotomic ideal, not the ordinary resultant, is the useful
same-fiber object.

## Nonclaim

Two boundary fibers do not give a uniform ideal-index upper bound and do not
control how many saturated ideals or quotient-weighted rich fibers can occur.
C36' remains TARGET. The next arithmetic step is a theorem bounding the index
or multiplicity of the same-fiber ideal from several short generators across
the entire middle-field range.

## Verification

- exact certificate audit: 20 pairs, 18 norms, and 7/7 mutation controls PASS;
- full Modal verifier replay `ap-qRrj1Gz8O2TVvDuVfKZ7Kl`: 133/133 PASS;
- five integration gates `ap-91ugW72Kq5IAxs1qjQonZt`: PASS; and
- critical orbit: 202 PROVED, 33 CONDITIONAL, 11 UNPROVED.
