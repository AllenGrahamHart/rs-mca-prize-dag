# L1 cofactor-prefix Pade graph normal form

- **status:** PROVED
- **role:** replace the cofactor union by one codimension-`w` locator-prefix section
- **consumer:** `l1_mixed_petal_amplification`

## Reversed-series chart

Use a normalized received word `U` of degree `h`, an exact shell size
`k<a<=h`, and

```text
w=a-k,       e=h-a,       0<=e<k,       d=w+e<a.
```

Write the high coefficients in reversed order:

```text
Uhat(T) = sum_(t=0)^d [Z^(h-t)]U T^t,
Qhat(T) = sum_(t=0)^e q_(e-t) T^t,
Lhat(T) = 1+l_1 T+...+l_d T^d.
```

The constant terms of `Uhat` and `Qhat` are both `c=lc(U)!=0`.  The product
equations from fixed-cofactor transport are exactly

```text
Qhat(T)Lhat(T) = Uhat(T) mod T^(d+1).                (PG1)
```

## Pade graph

For every `Qhat` of degree at most `e` with constant term `c`, `(PG1)` has
the unique solution

```text
Lhat(T) = Uhat(T)/Qhat(T) mod T^(d+1).               (PG2)
```

Let `G_(U,a)` be the resulting set of depth-`d` locator prefixes.  Then:

1. `|G_(U,a)|=q^e`;
2. projection to `(l_1,...,l_e)` is a bijection from `G_(U,a)` to `F^e`;
3. the final `w` coordinates are polynomial functions of the first `e`;
4. equivalently, `G_(U,a)` is the codimension-`w` section

```text
[T^(e+1)] Uhat/Lhat = ... = [T^(e+w)] Uhat/Lhat = 0. (PG3)
```

The inverse recovers the complete cofactor by

```text
Qhat(T) = Uhat(T)/Lhat(T) mod T^(e+1).               (PG4)
```

Thus distinct cofactors induce distinct deeper-prefix targets.

## Exact shell

Let `D_a` be the monic degree-`a` divisors `L` of the domain locator
`Omega`, and let `Phi_(a,d)(L)` be the first `d` nonleading coefficients.
For a graph point, let `Q_L` be recovered by `(PG4)`.  There is an exact
bijection

```text
E_a(U)
 <-> {L in D_a : Phi_(a,d)(L) in G_(U,a),
                  gcd(Q_L,Omega/L)=1}.               (PG5)
```

The codeword is `P=U-Q_L L`.  The gcd condition is precisely the exclusion
of extra agreements outside the roots of `L`.

At `e=0`, the graph is one point and `(PG5)` is the scalar-cofactor locator-Q
fiber.  For general `e<k`, its ambient density in `F^d` is
`q^e/q^d=q^(-w)`, so the natural transverse divisor count is
`binom(n,a)/q^w` without any cofactor overhead.

## Scope

This node proves the graph and the exact bijection, not transversality of the
split-divisor prefix image against the graph.  It does not bound the graph
intersection or pay quotient/periodic members. The follow-on
`l1_full_locator_pade_section_all_cofactors` extends the exact section
representation through `e>=k` without asserting a bound there. A census over
independent cofactors and prefixes is obsolete; the open positive statement
is row-sharp split-divisor intersection with the received-word Pade section.
