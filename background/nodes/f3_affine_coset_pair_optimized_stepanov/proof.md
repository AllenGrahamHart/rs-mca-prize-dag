# Proof

The two forms have distinct zeros because they are nonconstant and
nonproportional. An affine change of variable and nonzero rescaling of each
form turn the membership conditions into

```text
x^n=alpha,       (x-1)^n=beta                       (1)
```

for fixed `alpha,beta in F_p^*`. The in-house Stepanov proof applies to fixed
values on the right independently; their equality in the shifted-subgroup
presentation was not used in its linear-system, nonvanishing, or degree
arguments.

For completeness, use its auxiliary polynomial

```text
Psi(X)=Phi(X,X^n,(X-1)^n),
Phi=sum lambda_(a,b,c) X^aY^bZ^c,
0<=a<A,       0<=b,c<B.                            (2)
```

At the solutions of `(1)`, requiring multiplicity at least `D` imposes at
most `D(A+D)` homogeneous linear conditions on the `AB^2` coefficients.
The sparse-polynomial nonvanishing lemma in the dependency proves
`Psi!=0` whenever

```text
D(A+D)<AB^2,       AB<=n,       A+nB<p.             (3)
```

Since `deg Psi<A+2nB`, equations `(2)--(3)` then give

```text
#{solutions of (1)}<(A+2nB)/D.                      (4)
```

At every official order choose

```text
A=D=floor((27n^2/64)^(1/3)),
B=floor((125n/64)^(1/3))+1.                         (5)
```

Exact integer cubing at the 29 orders verifies

```text
D(A+D)<AB^2,
AB<=n,
A+nB<n^2+1<=p,
(A+2nB)^3<64D^3n^2.                                (6)
```

The final inequality in `(6)` and `(4)` prove `(ACS1)`. QED.
