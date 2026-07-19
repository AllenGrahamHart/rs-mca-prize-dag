# Proof

Write

```text
m=R-r,       n_c=r+1,
```

so `M(Z)` is `m x n_c`.  Work first over the function field `K=F(Z)`.
The rank-zero case has zero endpoint Hankel matrices and is column-close, so
assume `rho>=1`.

## 1. The same apolar generator controls both kernels

Let `Phi_Z` be the binary divided-power form of degree `R-1` whose coefficient
sequence is `y_0+Zy_1`.  The degree-`r` catalecticant of `Phi_Z` is exactly
`M(Z)`: divided powers remove all binomial coefficients, in every
characteristic.

The homogeneous apolar ideal

```text
I_Z=Ann(Phi_Z) subset K[A,B]
```

is an Artinian Gorenstein ideal in two variables.  Hence it is a complete
intersection

```text
I_Z=(Q_Z,P_Z),       deg Q_Z=a<=deg P_Z,
deg Q_Z+deg P_Z=R+1.                                (1)
```

For completeness, the codimension-two step is algebraic rather than a
characteristic-zero inverse-system assertion: the divided-power pairing makes
`K[A,B]/I_Z` Artinian Gorenstein of type one; its length-two minimal free
resolution therefore has a rank-one final module, and Hilbert--Burch leaves
exactly two coprime minimal generators. Their degree sum is socle degree plus
two, giving `(1)`.

Since `rho<min(m,n_c)`, both the degree-`r` and degree-`m-1` catalecticants
have nonzero kernels.  Thus `a<=min(r,m-1)`.  Equation `(1)` then gives

```text
deg P_Z>max(r,m-1).
```

Only multiples of `Q_Z` occur in either of those two apolar degrees.  Their
quotient Hilbert function has value `a`, so `a=rho`, and

```text
ker_K M(Z)     = Q_Z K[A,B]_{r-rho},
ker_K M(Z)^T   = Q_Z K[A,B]_{m-1-rho}.                (2)
```

This is the two-sided principal-kernel statement needed below.  It is the
standard codimension-two complete-intersection proof, carried out in the
divided-power dual, so it has no restriction on `char F`.

Clear denominators in `Q_Z` and divide the coefficient vector by its gcd in
`F[Z]`.  Let its resulting `Z`-degree be `e`.  The shifted coefficient vectors
in the first line of `(2)` form a polynomial minimal basis: they span the
rational kernel, their leading coefficient vectors are independent shifts of
the nonzero leading form of `Q_Z`, and primitivity makes their specialization
full-rank at every projective parameter.  The same holds on the left.  Hence
all

```text
nu_R=n_c-rho,       nu_L=m-rho
```

right and left minimal indices equal `e`.

Let `delta` be the size of the regular part in the Kronecker canonical form of
the pencil.  Normal rank is the sum of all singular-block indices and the
regular size, so

```text
(nu_R+nu_L)e+delta=rho.
```

Since `nu_R+nu_L=R+1-2rho=A`,

```text
delta=rho-Ae.                                          (3)
```

Only the regular part can lose rank under specialization.  Its homogeneous
determinant has degree `delta`, so there are at most `delta` finite rank-drop
slopes.

## 2. Strip fixed domain roots and repeat the degree budget

Assume `e>=1`.  Let `S subset D` be the set of evaluation points whose
homogeneous linear factors divide `Q_Z` identically in `Z`, and set

```text
H=product_{x in S} L_x,       s=|S|,
Q_Z=H Qbar_Z,                 d=rho-s.                  (4)
```

If a fixed domain factor occurs with multiplicity greater than one, no
generic-rank specialization of `Q_Z` can divide a squarefree locator.  The
regular supported set is then empty and the exceptional bound alone is
stronger than `(MI2)`.  Hence in the only nonvacuous branch the factors in
`H` are simple, as written.

There is no moving case with `d=0`: if every factor is fixed, primitivity
makes `Q_Z` fixed and `e=0`.

Apply the fixed divided-power differential operator `H` to `Phi_Z`.  Apolar
contraction gives

```text
Ann(H o Phi_Z)=Ann(Phi_Z):H.
```

The two complete-intersection generators in `(1)` are coprime.  Since `H`
divides `Q_Z`, it is coprime to `P_Z`, and therefore

```text
(Q_Z,P_Z):H=(Qbar_Z,P_Z).                              (5)
```

Thus `Qbar_Z` is the minimal apolar generator of the residual pencil
`H o Phi_Z`, of form degree `d` and the same parameter degree `e`.  This
residual form has degree `R-1-s`.  Use its degree-`(r-s)` catalecticant.  It
still has `m=R-r` rows, and its right and left nullities sum to

```text
((r-s+1)-d)+(m-d)=A+s.
```

Repeating the Kronecker rank identity and discarding the nonnegative residual
regular size yields

```text
(A+s)e<=d,                                             (6)
```

which is `(MI1)`.

## 3. Count regular supported slopes

At a slope outside the at most `delta` rank-drop values, specialization of
the minimal basis in `(2)` is the whole kernel.  If that kernel contains a
degree-`r` squarefree locator split over `D`, then `Q_gamma` divides the
locator.  Consequently `Q_gamma` itself consists of `rho` distinct domain
factors.  After `(4)`, `Qbar_gamma` has `d` distinct roots in `D\S`.

For each `x in D\S`, the specialization `Qbar_Z(x)` is a nonzero polynomial
of degree at most `e`; otherwise `x` would belong to `S`.  Counting pairs

```text
(gamma,x),       x in D\S,       Qbar_gamma(x)=0
```

in the two orders gives

```text
T_reg d <= (N-s)e.                                    (7)
```

Adding the at most `delta` exceptional slopes and using `(3)` proves

```text
T<=delta+floor((N-s)e/d)
 <=rho-Ae+floor((N-s)e/d),
```

which is `(MI2)`.  If the homogeneous generator has a boundary factor at a
generic slope, it cannot divide a locator whose roots are all finite domain
points, so such a slope contributes nothing to `(7)`.

When `e=0`, `(2)` is a fixed generic kernel.  The proved node
`rate_half_ca_hankel_fixed_kernel_branch` gives `T<=rho` for a column-far
pair.  This completes the general theorem.

## 4. Official arithmetic

Now set `N=2^41` and `R=2^40`.  In a deficient branch `rho<=r<=R/2`, so

```text
A=R+1-2rho
```

is a positive odd integer.  For `e>=1`, `(6)` and `d=rho-s` imply

```text
s<=(rho-A)/2,       d>=(rho+A)/2.                      (8)
```

If `A>=9`, then

```text
A d >= A(rho+A)/2
     = A(R+1+A)/4
     >= 9(R+10)/4
     > 2R=N.
```

Thus `(N-s)/d<A`, and `(MI2)` gives `T<=rho`.

If `A=7`, then `rho=R/2-3`.  The worst allowed `s` in `(8)` gives

```text
7d-(N-s) >= 4rho-N+21=9,
```

so again `T<=rho`.

It remains to check `A=5`, where `rho=R/2-2`.  If `e=1`, `(6)` gives

```text
s<=(rho-6)/2=R/4-4,       d>=R/4+2,
```

and the increasing ratio in `s` satisfies

```text
floor((N-s)/d)
 <=floor((7R+16)/(R+8))=6.
```

Therefore `T<=rho-5+6=rho+1`.

If `e>=2`, `(6)` instead gives

```text
d>=e(rho+5)/(e+1).
```

Since

```text
(N-rho)/(rho+5)=(3R+4)/(R+6)<3,
```

we obtain

```text
e(N-s)/d
 =e+e(N-rho)/d
 <e+3(e+1)=4e+3.
```

Its floor is at most `4e+2`, and `(MI2)` gives

```text
T<=rho-5e+4e+2=rho-e+2<=rho.
```

Hence every deficient branch with `A>=5` has `T<=rho+1<=r+1`.  If
`r<=R/2-2`, then every `rho<=r` indeed has `A>=5`; the already-proved
full-column-rank branch handles `rho=r+1`.  The split-pencil equivalence and
the previously proved sparse/adjacent reduction now give the official
corollary through `B=r+1<=R/2-1=2^39-1`.  QED.
