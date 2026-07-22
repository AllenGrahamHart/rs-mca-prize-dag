# Proof - L1 boundary shifted-lattice affine Q cell

## 1. Boundary coordinates

The balanced shifted-lattice theorem gives

```text
deg A<=omega-d_1,       deg B<=omega-d_2.
```

Substituting `(BQ1)` gives `(BQ2)`, with `B` a scalar.  Uniqueness follows
from the fact that `g_1,g_2` are an `F[Z]`-basis.

Monic normalization identifies scalar multiples of a pair `(W,N)`, so the
coefficient pairs split projectively into `B=0` and `B!=0`.  These cases are
disjoint.  In the second case division by `B` gives the unique affine form
`(BQ3)`; subsequent scaling makes `W` monic without changing its roots,
codeword `N/W`, or gcd guard.

## 2. The point at infinity

Suppose `B=0` gives a census element.  Then

```text
(W,N)=A(W_1,N_1),       W|Omega,       W|N.
```

Since `W` is squarefree, `W_1` and `A` are split squarefree up to units and
`W_1|N_1`.  Thus every such support is explained by the same codeword

```text
P_0=N_1/W_1,       deg P_0<k.
```

The complete agreement set of a fixed codeword is unique.  Therefore the
exact-shell guard can retain at most one of the supports on this ray, and it
retains one exactly when that complete agreement set has size `m`.  This
proves the first class.

## 3. The affine cell and injectivity

Every `B!=0` member has form `(BQ3)` after projective normalization.  Suppose
two parameters produce the same valid support.  Since `m>=k`, that support
has a unique explaining degree-below-`k` codeword, so the corresponding
normalized pairs `(W,N)` are equal.  Basis-coordinate uniqueness then gives
the same `A`.  Thus valid supports inject into the affine parameter space.

The split, degree, monic, and gcd requirements are precisely those inherited
from the balanced exact-shell theorem, proving the second class.

If `W_1=1`, adding a polynomial of degree at most `omega-w-1` cannot change
the coefficients of degrees `omega,omega-1,...,omega-w`.  Conversely every
monic degree-`omega` polynomial with those `w+1` coefficients differs from
`W_2` by such an `A`.  This proves `(BQ4)` and the locator-Q specialization.
