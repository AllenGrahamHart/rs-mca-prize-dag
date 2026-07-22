# Proof

## Moment route

Normalize the pruned fiber masses by the full support slice and write them as
`mu(z)`, so `sum_z mu(z)=tau`. There are at most `|B|^w` formal prefix
values. Convexity gives the upstream moment lower bound

```text
Gamma_r >= tau^r.
```

The ordinary finite moment criterion requires

```text
log2(Gamma_r)+w log2|B| <= r Delta_Q.
```

Substitution and rearrangement give `(RC1)`. Setting `tau=1` and using the
audited real-average margins gives `(RC2)`. The verifier uses the twelve-
decimal source pins and checks each ceiling with 50-digit Decimal arithmetic.
The Mersenne-31 MCA floor is convention-sensitive: using the ceiling-average
margin gives `641594`, while the source theorem's real-average convention
gives `641593`.

## Packing route

The imported Q packing estimate has normalized logarithmic overhead

```text
w log2|B|
 - log2 binom(a_+,floor(w/2))
 - log2 binom(n-a_+,floor(w/2)).
```

Grande Finale evaluates it at the four active rows and obtains the table
pinned in `route_cuts.json`. Every value exceeds its row margin by more than
1.66 million bits. Therefore that upper theorem cannot supply the required
finite row inequality.

## BC route

The boundary-Q unknown is `Q_z+A` with
`deg A<=omega-w-1`, where `omega=n-a_+`. Hence its coefficient parameter
space has dimension `omega-w`. Exact substitution gives `(RC3)`. A theorem
for one projective line inside this affine space supplies no aggregate bound
without coverage and a line count. This is precisely the missing bridge, so
the one-pencil moving-root theorem cannot be used directly as boundary-Q
payment. QED.
