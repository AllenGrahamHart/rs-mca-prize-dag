# Proof - L1 Pade split-section/support-moment inversion

## 1. Split locators equal valid supports

For an `m`-subset `A`, let

```text
L_A=product_(x in A)(Z-x).
```

The remainder `P_A=Uhat mod L_A` is the unique polynomial of degree below
`m` agreeing with `U` on `A`.  Therefore `U|A` extends to a polynomial of
degree below `k` if and only if `deg P_A<k`.  This is exactly the ordinary-
coefficient form of the full-locator Pade-section equations.  The map
`A->L_A` is bijective because the domain is split and squarefree, proving
`S_m=C_m`.

## 2. Support moment

Because `m>=k`, at most one degree-below-`k` polynomial can agree with `U`
on a fixed `m`-subset: two such polynomials would have at least `k` roots
but difference degree below `k`.

Now group every valid support `A` by its unique explaining codeword `P`.  If
`P` has complete agreement set of size `a`, exactly `binom(a,m)` of its
`m`-subsets are valid and are assigned to `P`.  Summing over the `Z_a`
codewords at every `a>=m` proves `(PS1)`.

The complement gcd guard in the exact-shell theorem says that the recovered
cofactor has no root in `H\A`.  This holds exactly when `A` is the complete
agreement set of its codeword.  Hence guarded level-`m` split points are
precisely `Z_m`, while the unguarded section contains all support subsets.

## 3. Binomial inversion

Substitute `(PS1)` into the right side of `(PS2)`.  The coefficient of a
fixed `Z_b`, `b>=a`, is

```text
sum_(m=a)^b (-1)^(m-a) binom(m,a) binom(b,m)
=binom(b,a) sum_(j=0)^(b-a) (-1)^j binom(b-a,j)
=1 if b=a, and 0 otherwise.
```

Here `binom(b,m)binom(m,a)=binom(b,a)binom(b-a,m-a)` and the last sum is
`(1-1)^(b-a)`.  This proves `(PS2)`.  Inequality `(PS3)` follows directly
from `(PS1)` because all terms are nonnegative and the `a=m` coefficient is
one.
