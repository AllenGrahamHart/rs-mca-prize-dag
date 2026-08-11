# Proof

Write

```text
A(X)=Q_m(X),             B(X)=-Q_(m-1)(X)/m.           (1)
```

The division is legal because `char F` does not divide `m`.  The leading
two coefficients of `(Gamma-x)^m-c_i` are `1` and `-mx`.  Hence `(QBL4)`
implies, on each of the three complete copies,

```text
A(tau_i x)=lambda_(i,x),
B(tau_i x)=x lambda_(i,x)=x A(tau_i x).               (2)
```

In particular `A` is nonzero.

Put `a_i=tau_i^n`.  The coset `tau_i H` is exactly the root set of
`X^n-a_i`.  For each of the three copy indices define

```text
C_i(X)=tau_i B(X)-X A(X).                             (3)
```

Its degree is at most `n`, because `deg A,deg B<=rho=n-1`.  Equation `(2)`
shows that it vanishes on all `n` points of `tau_i H`.  Therefore

```text
C_i(X)=d_i (X^n-a_i)                                  (4)
```

for some scalar `d_i`.

Subtract `(4)` for two distinct complete copies `i,j`:

```text
(tau_i-tau_j)B(X)
  =(d_i-d_j)X^n-d_i a_i+d_j a_j.                     (5)
```

The left side has degree at most `n-1`, so `d_i=d_j`.  All three scalars
are consequently one scalar `d`, and `(5)` also says that `B` is a constant,
say `b`.  Returning to `(4)` gives

```text
X A(X)=tau_i b-dX^n+d a_i.                            (6)
```

The left side has zero constant term.  Thus, for every one of the three
indices,

```text
tau_i b+d a_i=0,              A(X)=-dX^(n-1).         (7)
```

If `d=0`, then `(7)` gives `b=0` and `A=0`, contrary to `(2)`.  If `d` is
nonzero, `(7)` instead gives

```text
b/d=-a_i/tau_i=-tau_i^(n-1)                          (8)
```

for all three distinct coset representatives.  But

```text
gcd(n-1,N)=gcd(4m-1,16m)=1,                           (9)
```

so exponentiation by `n-1` is injective on the cyclic group `D=mu_N`.
Equation `(8)` would force the three `tau_i` to be equal, contradicting
that they represent distinct cosets.  Both cases are impossible, proving
the theorem.

For the pinned witness, `257^4` is congruent to `1` modulo `1024`, so the
required smooth domain exists in `F_(257^4)`.  The quartic cosets
`A_i subset F_257^*` have order `m=64`, and their row-root polynomial is
exactly `(Gamma-x)^64-c_i`.  Only the point `(0,1)` loses one supported
root; copies `1,2,3` remain complete and the preceding argument applies.
QED.
