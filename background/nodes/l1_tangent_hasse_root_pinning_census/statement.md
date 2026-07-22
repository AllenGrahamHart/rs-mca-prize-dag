# L1 tangent Hasse root-pinning census

- **status:** PROVED
- **role:** quantify the same-locator tangent first owner
- **consumer:** `l1_mixed_petal_amplification`

## Exact tangent strata

Let the squarefree domain locator be

```text
Omega=product_(x in H)(Z-x),       |H|=n,
```

and fix one exact shell of size `a>k`.  For a shell member write

```text
U-P=LQ,       deg P<k,       L=product_(x in A)(Z-x),
w=a-k,        e=deg Q.
```

Its tangent owner is the monic polynomial

```text
T=gcd(L,Q),       r=deg T.                            (TH1)
```

Tangency means `r>=1`, and necessarily `r<=min(a,e)`.

## Fixed-root payment

Fix a monic degree-`r` divisor `D|Omega`.  Among exact shell members with
`D|L`,

```text
D|Q  <->  D^2 | U-P.                                 (TH2)
```

Because `D` is squarefree and split, `(TH2)` is equivalent to the `2r`
Hermite/Hasse conditions

```text
P(x)=U(x),       P^[1](x)=U^[1](x)       for every x|D. (TH3)
```

The linear map from `F[Z]_<k` to these `2r` values has rank
`min(k,2r)`.  Consequently a fixed `D` supports either no candidate
codeword or exactly

```text
q^(k-min(k,2r)) = q^max(k-2r,0)                      (TH4)
```

solutions of `(TH3)` before the exact-shell and exact-gcd guards.

Every exact shell codeword has one complete agreement locator, and every
tangent member has the unique owner `T=gcd(L,Q)`.  Thus, if `N_r` counts
exact shell members with `deg gcd(L,Q)=r`, then

```text
N_r <= binom(n,r) q^max(k-2r,0),
sum_(tangent members) 1
    <= sum_(r=1)^min(a,e) binom(n,r) q^max(k-2r,0).   (TH5)
```

This is a canonical census with no support-subset overcount.

## Quantitative rank loss

At a tangent point with `r=deg gcd(L,Q)`, multiplication by `Q` on
`F[Z]/(L)` has rank `a-r`.  Hence the Jacobian rank of the `w` high-remainder
Pade equations obeys

```text
rank >= max(0,w-r),       Jacobian corank <= min(w,r). (TH6)
```

Each tangent root can therefore remove at most one section rank while
forcing two Hasse conditions on the codeword.

## Scope

The raw sum `(TH5)` can be exponentially larger than the official reserve.
This node does not prove the row-sharp tangent payment, primitive split-point
concentration, or quotient absorption.  It replaces an untyped resultant
locus by exact root-set strata and identifies the remaining need: aggregate
the feasible `D` collectively or transfer them to an existing paid owner.
