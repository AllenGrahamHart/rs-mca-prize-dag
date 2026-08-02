# Proof

The reciprocal-projection theorem sends every guarded common point to
`P(b,t)=0`.  The rational-lift atlas contains the exact linear equation

```text
c L_2(b,t)+M_2(b,t)=0.                            (0)
```

The hash-pinned exact function-field basis packet prints
`DENOMINATOR_GCD_DEGREES 0,0`.  In its sealed program the second degree is
computed as `degree(gcd(cLeading,primitive))`, where `cLeading=L_2` and the
monic `primitive` is `P` in `K[b]`.  Thus `gcd(P,L_2)=1`.  Consequently
`L_2` is invertible in `K[b]/(P)`, and `(0)` reconstructs
`c=-M_2/L_2` at every point of the generic common locus.  Hence chart 2 is
global over `K`; the remaining atlas charts concern only specializations.

The target-free signed-family interface gives, at the `DE+` source root
`z_0`,

```text
N/D=de,       (d+e)^2=q^2/(Delta^2 D^2),
q^2=x beta^2(x-1)^2,       x=z_0^2.              (1)
```

Since `e` is nonzero, the product row reconstructs `d=N/(De)`.  Substitution
in the squared-sum row of `(1)` and clearing the guarded denominator
`Delta^2 D^2 e^2` gives exactly `(KBGCE-1)`.  Thus every actual
`DE+/DE-` signed-pair point satisfies `H(e)=0`; retaining only the `DE+`
consequence is a valid relaxation.

For the colored `BE` record, the product is `be` and the squared sum is
`(b+e)^2`.  The proved outside-edge eliminant says that every actual source
root is a common root in `w` of the product quadratic and squared-sum
quartic.  In the sparse normalization the sum equation is cleared by
`Delta^2`; exact division of the compact norm by its displayed `A^3`
factor returns the full polynomial resultant `C(e)`.  Hence every actual
colored edge also satisfies `C(e)=0`, including degree-drop cases.

The primitive-coordinate map restricts `b,x0,x1`, and then the proved
rational atlas restricts `r,c`, to each field `E_j`.  The generic guard-unit
ledger proves that all denominators used here are nonzero in every `E_j`.
The primary exact Euclidean computation returns monic gcds and Bezout
multipliers `U_j,V_j` satisfying

```text
U_j H+V_j C=e^2-1,        j=1,2,3,5,
U_4 H+V_4 C=1.                                      (2)
```

All rational-function coefficients are stored in the hash-pinned packet

```text
710b438062fc2e80f5c7b14ffb987d8f36a02d4b57953b30419bb320b88877a7.
```

An independent exact audit rebuilds every `phi_j`, reparses every
rational-function coefficient, and verifies `(2)` directly in
`K[s]/(phi_j)[e]` without invoking the primary gcd algorithm.  Its packet is

```text
e1651bf40f716eeef1daafab71b0f0b49a010d2d38395aa6ecde1d3e82b7bb81.
```

A separate standard-library replay specializes at the regular fiber `t=2`,
factors every specialized `phi_j`, and independently checks the returned
Bezout, gcd, guard, and quotient identities in every finite subfactor.

Finally, target distinctness gives `e^2-1!=0`.  If both necessary equations
vanished at an admissible point, `(2)` would force either `e^2-1=0` or
`1=0`, both impossible.  Thus the necessary `DE+/DE-/BE` triple is empty on
the entire generic common locus.  Every packet in this cell and sign row
contains that triple, so the whole generic cell-5 sign row `(-1,-1)` is
empty. QED.
