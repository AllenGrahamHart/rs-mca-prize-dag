# Proof

For `k>=1` and even `s`, let `U_k(s)` be the following recursive upper bound
for the number of ordered zero-sum triples in a symmetric `s`-element subset
of `Z/2^k Z` containing neither zero nor the involution:

```text
U_1(0)=0,
U_k(s)=max_b [ U_(k-1)(s-b)
               +3 min((s-b)b,b^2-b) ],             (1)
```

where `b` runs over feasible even sizes of the odd part.

To prove `(1)`, split a symmetric support into its even and odd parts, of
sizes `a=s-b` and `b`. The all-even relations descend after division by two
to `Z/2^(k-1) Z`. Every other relation has one even and two odd entries. For
one fixed ordering, choosing an even and an odd gives at most `ab` relations;
choosing the two odds gives at most `b^2-b`, because their `b` opposite
ordered pairs force the absent zero entry. There are three positions for the
even entry. This proves the recursion.

Now let the eleven positive all-unit lags define the full symmetric support
in `Z/128 Z`. Exact local multiplicity two forces the number `o` of odd
positive lags to be odd. Thus the odd oriented part has size `b=2o`. Exact
evaluation of `(1)` gives

```text
o:                       1    3    5    7    9   11
U_6(22-2o):             348  210  114   42    6    0
top-level bound:        354  300  384  378  222    0.
```

The signed relation index is bounded in absolute value by this unsigned
count, so

```text
M_3<=384.                                           (2)
```

For one representative from each positive conjugate pair, put

```text
y_u=F(zeta_256^u)F(zeta_256^-u)>0.
```

The conductor-256 moment dictionary and `(2)` give

```text
mean_u y_u=18,
mean_u y_u^2=18^2+22,
mean_u y_u^3<=18^3+3*18*22+384.                    (3)
```

Let `p` be the cubic interpolant matching `log y` and its derivative at
`17` and `37`. Its Hermite remainder is nonpositive on all `y>0`, and its
leading coefficient is

```text
gamma=(540-629 log(37/17))/2516000>0.               (4)
```

Substitution in `(3)` gives

```text
mean_u log y_u
 <= (3761/4000) log 17
    +(239/4000) log 37
    -1353/125800
 < (1/64) log(514*p_min).                          (5)
```

The verifier proves `(4)--(5)` with 96-term rational atanh intervals. The
positive margin in `(5)` has numerator and denominator bit lengths `27836`
and `27849`. Therefore `Norm(F)<514*p_min`, contradicting a cofactor-`514`
prize-row collision. QED.
