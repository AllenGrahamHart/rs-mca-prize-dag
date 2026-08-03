# Proof

As in the mixed core/block payment, the generalized-weight affine compiler
gives every target parameter at least

```text
B_(s-2)=product_(j=3)^s(d_j-(N-K-w)+b)/(s-2)!
       >=product_(j=3)^s(w+j)/(s-2)!                 (1)
```

independent `(s-2)`-subsets of its punctured-core agreement hyperplanes.
Each subset cuts the affine hull to a plane.

## Three points on the residual plane

Fix one plane and affine coordinates `c=(c_1,c_2)`.  At `x in D`, the error
vector has the form

```text
V_x(c)=E_x+lambda_x(c)W_x,
W_x=(-Q(x),P(x)),                                   (2)
```

where `lambda_x` is affine linear and its homogeneous part is

```text
L_x(c)=delta_1(x)c_1+delta_2(x)c_2.                 (3)
```

The invariant active residual makes `V_x(c)` nonzero for every parameter.
For points with distinct `phi` values, the vectors `W_x` are projectively
distinct.

Fix a total order on `D` and write each unordered triple as `x<y<z`.  Take a
triple whose `phi` values and whose defined `psi_C` values are both pairwise
distinct.  Membership in one selected block forces

```text
F_xy(c)=det(V_x(c),V_y(c))=0,
F_xz(c)=det(V_x(c),V_z(c))=0.                       (4)
```

Both are genuine conics.  Their top homogeneous parts are nonzero multiples
of `L_xL_y` and `L_xL_z`.

They have no common component.  A common quadratic component would make the
conics proportional, and comparison of their top parts would force
`L_y` proportional to `L_z`.  A common affine line must have top direction
`L_x`, the only common factor of the two top parts.  Along that line,
`lambda_x` is constant while `lambda_y` and `lambda_z` are nonconstant.
Identity of both determinants along the line therefore forces both `W_y`
and `W_z` to be collinear with the same nonzero fixed vector `V_x`, contrary
to the distinct `phi` values.

Bezout now gives four projective intersections counted with multiplicity.
The two top forms share the point `L_x=0` at infinity, so at most three
intersections are affine.  A fixed core plane and fixed nondegenerate triple
therefore own at most three target parameters.

## Incidence count

Every `r`-point block has at least

```text
r(r-ell)(r-2ell)/6                                  (5)
```

unordered triples with pairwise distinct `phi` values: choose the points in
order, avoiding at most one, then two, fibers of size `ell`, and divide by
six.  Every target has at least two disjoint selected blocks.  Combining
`(1)` and `(5)`, the total number of triple flags is at least the left side
of `(APT1)`.

Restriction-degenerate flags contribute `I_deg`.  For the others, there are
at most `binom(N,s-2)` core subsets and `binom(e,3)` point triples, and the
conic argument gives at most three target parameters.  This proves `(APT1)`.
Putting `I_deg=0`, using

```text
binom(N,s-2)<=N^(s-2)/(s-2)!,
binom(e,3)=e(e-1)(e-2)/6,
```

and cancelling `(s-2)!` gives `(APT2)`.

## Official `ell=1` slice

Put `x=d+1`.  Then

```text
e<=x-3,       r=h-x+1,
```

so `(APT2)` is at most

```text
G_s(x)=3 n^(s-2)(x-3)(x-4)(x-5)
       /[2(h-x+1)(h-x)(h-x-1)product_(j=3)^s(x+j)]. (6)
```

For the official range `x>=ceil((2h+2)/3)+1`, the ratio
`G_s(x+1)/G_s(x)` is at least one.  After cross multiplication, the required
difference is

```text
(s-2)x^2+(5-s)hx-(3s+6)x+(5s-1)h-10s-16.           (7)
```

It is positive at the left endpoint and increasing there for `s=10,11`.
The verifier checks this and the exact first failures against

```text
B_0=floor((17n^2-25(n-4))/25),
```

which is no larger than the actual local budget.  The last paid values are
exactly those in `(APT3)`.  QED.
