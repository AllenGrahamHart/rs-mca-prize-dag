# Proof

Choose a basis `c_1,...,c_q` for the direction of the affine explanation
space and encode each selected explanation by a parameter point

```text
p_gamma=(gamma,lambda_gamma,1,...,lambda_gamma,q) in F^(q+1).
```

At coordinate `x`, agreement is an affine hyperplane whose normal is

```text
v_x=(r_1(x),-c_1(x),...,-c_q(x)).
```

## Local full rank

The normals incident with every selected `p_gamma` span `F^(q+1)`.  If not,
a nonzero annihilator `(delta,mu)` gives

```text
delta r_1-sum_i mu_i c_i=0
```

on the maximal agreement support.  When `delta=0`, a nonzero degree-`<K`
codeword has at least `m>K-1` roots.  When `delta!=0`, both `r_1` and `r_0`
have degree-`<K` explanations on that same support.  The first case is
impossible and the second contradicts pair noncontainment.

## Proper-subspace occupancy

Let `W<F^(q+1)` have dimension `r`, with `1<=r<q`, and put

```text
X_W={x:v_x in W}.
```

The annihilator `W^perp` has dimension `q+1-r`.  If its slope coordinate is
identically zero, it gives `q+1-r` independent codewords vanishing on
`X_W`.  Otherwise the kernel of the slope coordinate gives `q-r`
independent codewords vanishing there.  The MDS generalized-weight formula
therefore gives, in both cases,

```text
|X_W|<=K-q+r.                                           (1)
```

After `r` independent incident normals have been selected, (1) leaves at
least

```text
m-(K-q+r)=w+q-r
```

choices outside their span.  For `r=1,...,q-1`, these factors multiply to
`(w+1)^(q-1)_rising`.

After `q` independent normals have been selected, local full rank leaves at
least one final choice.  There is also a direction-distance refinement.  If
the annihilating relation of their hyperplane has nonzero slope coordinate,
that hyperplane contains at most `N-e` coordinate normals and hence leaves
at least `e-(N-m)=e-t` incident choices.  If its slope coordinate is zero,
the codeword root bound leaves at least `w+1`.  Since Reed-Solomon
interpolation gives `e<=N-K` and hence `e-t<=w`, every case leaves at least

```text
L=max(1,e-t)                                             (2)
```

final choices.

## Double count and zero normals

Let `z` be the number of zero coordinate normals and let `g<=z` be those
whose affine hyperplane contains every parameter point.  The `q` independent
codewords have at most `K-q` common zeros, so

```text
0<=g<=z<=K-q.
```

Each selected point is incident with at least

```text
(m-g)(w+1)^(q-1)_rising L
```

ordered normal bases.  An ordered independent coordinate tuple determines
at most one parameter point, and only the `N-z` nonzero normals can occur.
Thus

```text
|Z| <= (N-z)^(q+1)_falling /
       ((m-g)(w+1)^(q-1)_rising L).                     (3)
```

For fixed `z`, the right side is largest at `g=z`.  The successive ratio of
the remaining `z`-dependent factor has sign controlled by

```text
N-(q+1)m+qz.
```

It can change only from negative to positive, so the maximum on
`0<=z<=K-q` occurs at an endpoint.  Substituting `z=0` gives `A_q/L`, while
`z=K-q` gives `B_q/L`.  Taking the larger rational value and then the floor
proves `(PSO)`.

The `GF(1009)` counterexample to the old compiler is consistent with this
proof: `q=1` and `L=1`, so the corrected bound is 471 rather than 23.
