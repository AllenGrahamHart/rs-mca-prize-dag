# Proof

All interval endpoints in `verify.py` are finite decimals and hence rational
numbers.  Addition, subtraction, multiplication, division, and square roots
are performed in separate `ROUND_FLOOR` and `ROUND_CEILING` contexts.

Machin's identity

```text
pi=16 atan(1/5)-4 atan(1/239)                         (1)
```

and 100 terms of the alternating arctangent series give an interval for
`pi`; the next term bounds the remainder.  On `[0,pi/2]`, 50 terms of the
alternating sine and cosine series give endpoint enclosures, again with the
next term as an absolute remainder bound.  For logarithms, first scale the
sine interval into `[1,2)` and use

```text
log y=2 sum_(m>=0) z^(2m+1)/(2m+1),
z=(y-1)/(y+1),                                      (2)
```

with `0<=z<1/3`; 110 terms and the geometric tail bound enclose the result.
The same formula at `z=1/3` encloses `log 2`.  Thus every

```text
f_t=2log|sin(pi*5^t/256)|                           (3)
```

is enclosed without a library transcendental function.

The 64 roots `exp(2 pi i k/64)` are built from the same sine/cosine intervals
and exact quadrant symmetries.  Directed complex interval summation of

```text
kappa_j=sum_t f_t exp(-2 pi ijt/64)                 (4)
```

then gives 63 rectangles disjoint from zero.  Rounding each magnitude
interval outward after multiplication by `10^30` gives the digest in the
statement.  Conjugate frequencies and the real frequency `j=32` are checked
independently.  Summing reciprocal lower bounds proves `(CEP1)`.

Because `p>2^255` and `mu>=1`, monotonicity gives

```text
D=log(18^64/(2^mu p))<log(18^64/2^256).             (5)
```

The same certified logarithm routine and directed square root give `(CEP2)`.
Substitution in `(CER8)--(CER9)` gives real upper bounds strictly below `102`
and `8`.  Since the left sides are integers, `(CEP3)` follows.

For `(CEP4)`, use dynamic programming over the 64 coordinates.  After `r`
coordinates, the state `(s,q)` stores the exact number of prefixes with sum
`s` and square mass `q`.  Extend by each integer in `[-7,7]`, discard
`q>101`, and after 64 coordinates sum states with `s=0`.  This is an exact
integer recurrence and returns the printed count.

Finally, if `xi` has `k` entries `+1` and `k` entries `-1`, Parseval gives

```text
sum_j |widehat(xi)_j|^2=64 sum_t xi_t^2=128k.       (6)
```

Bounding every spectral weight by `max_j|kappa_j|^2` shows that the weighted
left side of `(CER10)` is at most

```text
128k max_j|kappa_j|^2.                              (7)
```

The certified bounds make `(7)<=64R_max^2` for every `k<=5`, where `R_max`
is the universal enclosing radius from `(CEP2)`.  Choosing disjoint positive
and negative supports gives exactly the binomial sum `(CEP5)`.  Thus neither
the coarse bounds nor the weighted ellipsoid can be enumerated as the first
filter.  The exact sparse-product constraints remain mandatory. QED.
