# Proof - L1 partial-pullback Johnson router

## 1. Quotient agreement after partial loss

For each codeword in `(PJ6)`, equation `(PJ3)` gives the exact identity

```text
|Agr(f,U)|=s|E_f|+z(f).                                (1)
```

Since the left side is at least `a_*` and `z(f)<=Z`, one has

```text
|E_f|>=ceil((a_*-Z)/s),                               (2)
```

with the zero truncation in `(PJ4)` harmless.

By `l1_general_pullback_interleaving_descent`, the codeword maps to an
`s`-component quotient tuple agreeing with the quotient receiver on every
label in `E_f`. The evaluation map from polynomial component tuples to their
values on `B` has exact fiber size `q^kappa`.

## 2. Direct interleaved Johnson count

Two distinct quotient evaluation tuples differ in at least one component
codeword. That component is represented by a degree-below-`K_0` polynomial,
so the tuples agree simultaneously on at most `d=K_0-1` labels.

For a list of `L` distinct quotient tuples agreeing on at least `h_Z` labels,
retain exactly `h_Z` labels per tuple. The same incidence calculation as in
`l1_full_pullback_divisibility_johnson_closure` gives

```text
L(h_Z^2-bd)<=b(h_Z-d).                                (3)
```

Under `(PJ5)`, division proves the first list factor in `(PJ6)`. Its
denominator is a positive integer and `h_Z<=b` for a nonempty class, so the
factor is at most `b^2`. Multiplication by the exact evaluation-kernel size
proves `(PJ6)`.

## 3. Tame fixed-source aggregation

The tame fixed-petal census gives at most `n` map classes across the fixed
source. If `kappa<=K` and `q<=n^gamma`, union bounding `(PJ6)` over those maps
gives

```text
n q^K b^2<=n*n^(gamma K)*n^2,
```

which is `(PJ7)`. Duplicate codewords across maps only improve the bound.

## 4. Boundary witness

For the exact `F_17^*` obstruction, the quadratic has seven complete
two-point fibers and two residual domain points. The zero codeword fully
agrees on four complete fibers. It has three further agreements in partially
agreed complete fibers and two on residual points, so

```text
z=5,       b=7,       K_0=4,       d=3,       kappa=0,
h_Z=ceil((13-5)/2)=4,       h_Z^2=16<21=bd.
```

Thus the known aperiodic witness remains outside `(PJ5)`, as claimed.
