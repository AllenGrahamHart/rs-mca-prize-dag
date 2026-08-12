# Proof

Choose a minimum lift of the direction syndrome in the form

```text
q=r_1-b,       b in RS[F,D,s],       wt(q)=R-j,
```

and put `E=supp(q)`.  Every selected witness support has size `d+s`, while
the zero set of `q` has size `s+j`.  Therefore

```text
|S_gamma intersect E| >= (d+s)-(s+j)=d-j.           (1)
```

For `x in E`, let `Z_x` be the slopes whose declared exact witness contains
`x`.  All their explanations agree with the received line at `x`.
Subtract the two received values at `x`, divide by `X-x`, and delete `x`.
The common-core cancellation argument maps `Z_x` injectively to a
support-wise MCA-bad family in

```text
(R+s-1,s-1,d+s-1),
```

preserving `R`, `d`, slopes, and same-support noncontainment.

Let `j_x` be the child direction defect.  Any child direction codeword
lifts to an original degree-`<s` codeword constrained to agree with `r_1`
at `x`.  Its residual has the same weight after deleting `x`.  Since `q`
was a globally minimum direction lift, every such residual has weight at
least `R-j`.  Hence the child minimum lift weight is at least `R-j`, so

```text
j_x<=j.                                               (2)
```

By the child hypothesis, `|Z_x|<=M_(s-1)(j)`.  Double-counting the pairs
`(gamma,x)` with `x in S_gamma intersect E`, using `(1)` and `|E|=R-j`,
gives

```text
|Z|(d-j) <= sum_(x in E)|Z_x|
           <= (R-j)M_(s-1)(j),
```

which proves `(RS1)`.

For the deployed envelopes, initialize at `s=13` on KoalaBear and `s=5`
on Mersenne-31 with the exact all-defect affine-span bounds.  At each next
dimension take the minimum of `(RS1)` and the direct direction-distance
bound when its denominator is positive.  Both ingredients are
nondecreasing in `j`, so the resulting bound is uniform for all child
defects at most `j`.  Exact integer iteration yields the pinned checkpoints.
