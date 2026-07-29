# Frontier

For one fixed prize row `(p,r)`, choose any retained profile-`(3,6,S=18)`
collision and write its normalized prime generator as `g`.  Every other
retained vector has the form

```text
alpha=pi^mu u g,       mu in {1,2,3,4},       u in R^x,
```

subject to the exact coefficient alphabet and profile constraints.  At
`mu=4`, only the primitive multiplicity-four support branch remains.

Inside one fixed `mu`, write `u` and `u^(-1)` in the power basis. Their
coefficients lie in the uniform boxes with radii `1006,503,251,125`. The
exact row radius `floor(18^64/(2^mu p))` is preferable when `p` is pinned.
The inverse equation

```text
U(X)V(X)=1 mod X^128+1
```

must be retained together with the two sparse product constraints
`U alpha=beta` and `V beta=alpha`; the raw box alone is far too large.

The next theorem must count these bounded unit associates, or derive a
height/packing inequality that charges their full profile weight in the
weighted-kernel ledger.  Counting rational norm values independently is now
strictly weaker because every survivor already has the same normalized
principal ideal.

Do not replace unit association by root-of-unity association: the unit group
has positive rank.  Do not compare vectors from different quotient roots:
they lie over different reduction primes unless an explicit Galois transport
is retained.
