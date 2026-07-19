# Budget-three deleted-pair trace gcd router

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:**
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_chebyshev_gegenbauer_sign_router`

Retain the correctly posed system `(CGR1)--(CGR5)` in the official split
branch. Thus the characteristic is odd, all relevant polynomial
denominators and leading coefficients are invertible, and

```text
L=2M,       x=2y^2-1,       epsilon in {1,-1},
C=C_L^(1/4)(x),       P=P_(2L-1)(x),       s^2=-epsilon.   (TGR1)
```

The deleted-pair distinctness condition `t!=1` implies `x^2!=1`. Define

```text
G_-(x)=T_(2L)(x),       G_+(x)=U_(2L-1)(x),          (TGR2)
```

where the subscript on `G` is the value of `epsilon`. Then

```text
T_(8L)(y)=epsilon       iff       G_epsilon(x)=0.    (TGR3)
```

Let `R` be the remainder of `P_(2L-1)` on division by `C`. For each of the
two choices of `s`, put

```text
E_(0,s)=(R+s)^2-2s^2(x+1),
E_(1,s)=2(R+s)^2-(x+1)(R-s)^2,
E_(2,s)=(x+1)(R-s)^2-8s^2.                          (TGR4)
```

For `j=0,1,2`, there exists a trace `y` satisfying `x=2y^2-1`, the source
torsion equation, and the corresponding signed equation `(CGR5)` if and
only if

```text
C(x)=G_epsilon(x)=E_(j,s)(x)=0.                    (TGR5)
```

The trace is reconstructed without a search by

```text
j=0: y=(R+s)/(2s),
j=1: y=(R+s)/(R-s),
j=2: y=-2s/(R-s).                                  (TGR6)
```

The denominators in the last two lines cannot vanish on `(TGR5)`.

Equivalently, reduce `G_epsilon` and every `E_(j,s)` modulo `C`. Each signed
branch is empty over the algebraic closure exactly when

```text
gcd(C, G_epsilon mod C, E_(j,s) mod C)=1.           (TGR7)
```

Thus the live first-rejection problem is six characteristic-explicit gcd or
subresultant tests among polynomials of degree less than or equal to `L` in
one variable. A nontrivial gcd is only a scalar-gate survivor and must still
pass the retained nonzero-next-coefficient, official-characteristic,
distinctness, split-lift, gcd-degree, and fourth-power filters. This theorem
does not prove any of the six gcds to be one.
