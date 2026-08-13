# Proof

The gauge, deficit, and owner statements are the field-general statements
proved in `rate_half_mca_sparse_direction_heavy_fiber_profile`.  We repeat
the parts needed for the new estimate.

Outside `E`, the direction is the codeword `b`.  If a transformed
explanation `a` agreed with `r_0` on at least `m` outside coordinates, an
`m`-subset there would simultaneously explain the received pair by
`(a,b)`.  Hence `h_a>=1`.  Every selected witness has size `m` and can use
at most `e` coordinates of `E`, so `h_a<=e`.

At `x in E`, agreement at slope `gamma` is equivalent to

```text
(a(x)-r_0(x))/q(x)=gamma.
```

The ratio fibers are disjoint.  A slope owned by a deficit-`h` explanation
needs at least `h` inside agreements, so that explanation owns at most
`floor(e/h)` slopes.

It remains to count distinct transformed explanations.  Puncture `E` and
fix `h`.  Every explanation with deficit at most `h` has an agreement set
of size at least

```text
A=m-h
```

with the punctured word of length `n'=N-e`.  Two distinct degree-`<K`
polynomials agree on at most `K-1` evaluation coordinates.  If `L` is the
number of explanations and `s_x` is the number of their agreement sets
containing coordinate `x`, then

```text
sum_x s_x >= L*A,
sum_x C(s_x,2) <= (K-1)C(L,2).
```

Cauchy--Schwarz gives

```text
sum_x C(s_x,2)
 >= ((L*A)^2/n' - L*A)/2.
```

When `A^2>n'(K-1)`, comparison and division by `L` yield

```text
L <= floor(n'(A-K+1)/(A^2-n'(K-1)))=J_h.          (1)
```

Condition `(PJ0)` is exactly `(1)` at `h=e`.  Since `A=m-h` decreases with
`h`, it implies positivity for every `h<=e`.  The real-valued right side of
`(1)` is nondecreasing as `h` increases: its derivative with respect to
`A` has numerator

```text
-n'((A-(K-1))^2+(K-1)(n'-(K-1)))<0.
```

Thus `J_0<=J_1<=...<=J_e`.

Let `n_h` be the number of distinct explanations of exact deficit `h` and
`N_h=sum_(i<=h)n_i`.  Equation `(1)` gives `N_h<=J_h`.  The owner weights
`floor(e/h)` are nonincreasing, so summation by parts, or saturation of the
cumulative caps, gives

```text
|Z| <= sum_h n_h floor(e/h)
    <= sum_h (J_h-J_(h-1))*floor(e/h),
```

which proves `(PJ2)`.

Put `u=floor(e/2)`.  For `h<=u`, bound the weight by `e`; for `h>u`, the
weight equals one.  The two telescoping blocks give

```text
|Z| <= e*J_u+(J_e-J_u)=(e-1)J_u+J_e,
```

proving `(PJ3)`.

The verifier scans the finite positive-denominator prefix using exact
integer arithmetic.  It proves that `(PJ3)` is maximized at the printed
endpoint in each official row, checks the endpoint and adjacent denominator
signs, and compares the endpoint bound with the official budget.
