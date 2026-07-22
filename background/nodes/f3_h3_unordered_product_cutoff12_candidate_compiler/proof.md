# Proof

The odd Galois group permutes the `c_a` and therefore permutes both the
diagonal roots `c_a^2` and the unordered products `c_a c_b`. The coefficients
of `Delta_n` and `Ucal_n` are fixed rational algebraic integers, so both
polynomials lie in `Z[T]`.

The resultant identity for `Delta_n` follows by evaluating `T-X^2` at every
root of the monic polynomial `F_n`. Write

```text
Scal_n(T)=product_(a<b)(T-c_a c_b).
```

Then, directly from ordered versus unordered multiplicities,

```text
Pcal_n=Delta_n Scal_n^2,       Ucal_n=Delta_n Scal_n.
```

This proves `Ucal_n^2=Pcal_n Delta_n`. The degree is

```text
d+d(d-1)/2=d(d+1)/2=n(n-1)/2.
```

The dyadic shifted-product Sidon theorem says two characteristic-zero
products `c_a c_b,c_u c_v` agree only when their unordered exponent pairs
agree. Thus all roots of `Ucal_n` are distinct, so `Ucal_n` is squarefree.
In particular `Ucal_n` and its first Hasse derivative have no common root
over `Qbar`. The derivative ideal is therefore the unit ideal over `Q[T]`,
and remains so after adjoining `(T-1)Y-1`. Before adjoining `Y`, its quotient
over the PID `R=Z[1/2]` is a finite torsion module: `Ucal_n` is monic, and
the quotient vanishes after tensoring with `Q`. Inverting the endomorphism
`T-1` takes a quotient of the stable image of that finite module, so the
selected quotient is finite torsion as well. Hence `J_(n,12) intersect R` is
nonzero and has the positive odd generator in `(UPC3)`.

Now let `p=1 mod n`. Since `p` does not divide `n`, all `n`th roots are
simple and lie in `F_p`. Reduction of the roots `c_a` gives exactly
`A=(1-H)\{0}`. The multiplicity of `t` in `Ucal_n mod p` is therefore the
number `U(t)` of unordered product representations.

For a polynomial over a field, a point is a common root of its zeroth
through `c`th Hasse derivatives exactly when its multiplicity is at least
`c+1`. The selector equation has a solution exactly when `t!=1`.
Consequently the reduction of `J_(n,12)` is proper exactly when some
nonidentity target has `U(t)>=13`. The selected quotient is a finite
`R`-module, so its reduction modulo `p` is nonzero exactly when `p` divides
its scalar annihilator. This is equivalent to

```text
p divides a_(n,12)^neq iff some t!=1 has U(t)>=13,
```

which proves `(UPC5)`.

Finally, swapping the two entries of an ordered representation has one fixed
point for each diagonal representation. Therefore `P(t)=2U(t)-D(t)`. The
equation `x^2=t` has at most two roots, so `D(t)<=2`. If a nonidentity target
has `P(t)>=25`, then `U(t)=(P(t)+D(t))/2>=13`, proving `(UPC6)`. If
`U(t)>=14`, then
`P(t)>=28-2=26`; at `U(t)=13`, the identity gives `P(t)=26-D(t)`, and only
`D(t)=2` falls below 25. This proves `(UPC7)`. QED.
