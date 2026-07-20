# Budget-three fiber-two c=2 outer torsion-trace gate

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:**
  `rate_half_list_budget_three_fiber_two_cycle_mismatch_trace_resolvent_elimination`

Retain a generic canonical survivor in the `c=2` denominator-mismatch
stratum. Put

```text
N=2^40,
O(W)=W^4+alpha W^2+beta W+gamma,
I=alpha^2+12gamma,
J=72alpha gamma-27beta^2-2alpha^3,
K_O(Z)=4I^3 Z(Z-36)^2-J^2(Z+12)^3.                  (CTT1)
```

The outer quartic is separable, so `K_O` has exact degree three.

Define the trace polynomials by

```text
C_0(X)=2,       C_1(X)=X,
C_(m+1)(X)=X C_m(X)-C_(m-1)(X).                     (CTT2)
```

Equivalently, `C_m(t+t^(-1))=t^m+t^(-m)` and

```text
C_(2m)(X)=C_m(X)^2-2.                                (CTT3)
```

There is a constant-size official-order gate. In the quotient algebra
`F[Z]/(K_O)`, put

```text
Q_0=Z-2,
Q_(j+1)=Q_j^2-2 mod K_O,       0<=j<40.             (CTT4)
```

Every `Q_j` has degree at most two. A valid `c=2` mismatch survivor
necessarily satisfies

```text
gcd(K_O,Q_40-2)!=1,                                  (CTT5)
```

or equivalently

```text
Res_Z(K_O,Q_40-2)=0.                                 (CTT6)
```

Indeed, a passing completion pair `{A,B}` supplies

```text
t=A/B in mu_N,       z=(A+B)^2/(AB)=t+t^(-1)+2.     (CTT7)
```

Then `K_O(z)=0` and `Q_40(z)=C_N(z-2)=2`.

The test requires exactly forty squarings and reductions of degree-at-most-two
polynomials modulo one cubic. It never constructs a degree-`N` Chebyshev or
cyclotomic polynomial. It is an outer-only necessary gate: a common root
need not come from a pair of actual roots of `D_*`, satisfy canonical span,
or reconstruct a cycle. The theorem does not exclude the `c=2` stratum,
address `c=1`, enumerate denominator quartics, or authorize a large run.

