# Proof - L1 exact-shell complement Toeplitz normal form

## 1. Complement cancellation

For `x in A`, differentiate `Omega=LM` at `x`. Since `L(x)=0`,

```text
Omega'(x)=L'(x)M(x).
```

Also `Omega'(x)=n x^(n-1)=n beta/x`, because `x^n=beta`. Hence

```text
1/L'(x)=xM(x)/(n beta).                               (1)
```

The complement locator vanishes on `H\A`, so the barycentric moment from
`l1_received_word_barycentric_q_scope_fence` becomes

```text
sum_(x in A) U(x)x^j/L'(x)
 =1/(n beta) sum_(x in H) U(x)M(x)x^(j+1).            (2)
```

Write `UM=sum_t c_t Z^t`. On the root coset of `Z^n-beta`,

```text
1/n sum_(x in H)x^m = 0          if n does not divide m,
                         beta^q  if m=qn.
```

Here `deg U<n`, `deg M=r=n-a`, and `0<=j<w=a-k`. Every exponent
`t+j+1` in `(2)` is positive and at most

```text
(n-1)+(n-a)+(a-k-1)+1=2n-k-1<2n.
```

Thus the only possible multiple of `n` is `n`, arising from
`t=n-j-1`. Its coset average is `beta`; the factor `1/beta` in `(2)`
cancels it. This proves `(CT1)`.

The barycentric criterion says that `deg I_A(U)<k` exactly when these `w`
moments vanish. Their coefficient indices are `n-1,...,n-w`, proving
`(CT2)`.

## 2. Linearity and codeword-shift invariance

For fixed `U`, multiplication by `U` followed by projection to a coefficient
window is linear in `M`. Restricting to monic degree-`r` polynomials fixes one
coordinate and makes the map affine.

If `deg R<k`, then

```text
deg(RM)<k+r=k+n-a=n-w.
```

Therefore `RM` has no coefficient in degrees `n-w,...,n-1`, proving `(CT4)`.

## 3. Exact-shell ownership

Every monic degree-`r` divisor `M` of `Omega` is the locator of a unique
`r`-subset of `H`; its complement has locator `L=Omega/M` and size `a`.
By `(CT2)`, the gap condition is equivalent to `P=U mod L` having degree
below `k`. Write `U-P=LQ`. Since `deg U<n` and `deg L=a`, one has
`deg Q<r`.

At a complement root `y` of `M`, the locator `L(y)` is nonzero. Hence

```text
U(y)=P(y)  iff  Q(y)=0.
```

Because `M` is squarefree, no complement root is an extra agreement exactly
when `gcd(Q,M)=1`. Thus the agreement set of `P` is exactly `A` precisely
under the guard in `(CT5)`. Complementation is unique in both directions, so
the correspondence is a bijection.
