# L1 full-locator Pade section for all cofactor degrees

- **status:** PROVED
- **role:** remove the `e=k` representation gap in the exact-shell route
- **consumer:** `l1_mixed_petal_amplification`

## Uniform section

Let the normalized received word have degree `h`, fix `k<a<=h`, and put

```text
w=a-k,       e=h-a,       d=h-k=e+w.
```

There is no restriction on `e`.  For a monic degree-`a` locator, reverse all
of its coefficients and the required high coefficients of `U`:

```text
Lhat(T)=1+l_1 T+...+l_a T^a,
Uhat(T)=sum_(t=0)^d [Z^(h-t)]U T^t.
```

Define the full-locator Pade section `V_(U,a)` by the `w` equations

```text
[T^(e+1)] Uhat/Lhat = ... = [T^(e+w)] Uhat/Lhat = 0. (FA1)
```

Division is well-defined because `Lhat(0)=1`.  For `Lhat` in the section,
put

```text
Qhat=Uhat/Lhat mod T^(e+1).                          (FA2)
```

## Exact shell

Let `D_a` be the monic degree-`a` divisors of the domain locator `Omega`, and
let `Q_L` be the ordinary polynomial obtained by reversing `(FA2)`.  Then

```text
E_a(U)
 <-> {L in D_a intersect V_(U,a) : gcd(Q_L,Omega/L)=1}. (FA3)
```

The codeword is `P=U-LQ_L`.  Thus every cofactor degree is represented by one
received-word-dependent `w`-equation section of full locator coefficient
space; no union over `q^e` cofactors is needed to state the exact object.

## The `e=k` transition

If `e<k`, then `d<a`.  Equations `(FA1)` depend only on the first `d`
locator coefficients.  The prefix Pade graph theorem shows that the first
`e` are free and the next `w` are determined; the remaining `a-d=k-e`
locator coefficients are free.  Hence

```text
V_(U,a) = G_(U,a) x F^(k-e),       |V_(U,a)|=q^k.    (FA4)
```

If `e>=k`, then `d>=a`: the reciprocal series continues beyond the last
locator coefficient.  The same `w` equations `(FA1)` remain exact, but
`(FA4)` is not asserted.  This is a change of chart geometry, not a new
exact-shell species.

## Scale and scope

Formally, `w` transverse equations have density `q^(-w)`, giving the desired
split-divisor scale `binom(n,a)/q^w`.  This node does not prove independence,
codimension `w`, or a row-sharp intersection bound when `e>=k`; those are the
open content.  It also does not pay quotient/periodic members.  It proves only
the all-cofactor section and exactness interface. The follow-on
`l1_pade_remainder_jacobian_tangent_dichotomy` proves that the section has
full local codimension `w` whenever `gcd(L,Q)=1`; global split-point
transversality remains open.
