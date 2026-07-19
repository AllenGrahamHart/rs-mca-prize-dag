# Proof

The parity dependency gives `E(z)=(1-w)(1-tw)` after normalization. Hence
`Q`, the canonical fourth-root truncation `B`, and the normalized secondary
polynomial `Cbar` are all even. Write them as in `(DEF1)`.

The canonical-span dependency expands a surviving candidate as

```text
Q=B^4+alpha z^(2h)B^2Cbar^2
     +beta z^(3h)BCbar^3+gamma z^(4h)Cbar^4.          (1)
```

Here `h=2M+1` is odd. Every term in `(1)` except the `beta` term is even in
`z`, while `z^(3h)BCbar^3` is odd and nonzero. Comparing odd parts proves
`beta=0`.

The split outer quartic is now

```text
W^4+alpha W^2+gamma.                                  (2)
```

It has four distinct base-field roots. Evenness pairs each root with its
negative. Distinctness rules out zero and repeated squared roots, so there
are distinct nonzero `lambda,mu` in the base field such that

```text
W^4+alpha W^2+gamma=(W^2+lambda)(W^2+mu).             (3)
```

In particular `lambda+mu=alpha` and `lambda mu=gamma`. Substituting
`z^(2h)=w^h` into `(1)` and using `(3)` gives `(DEF3)`.

The generic floor has `deg_z Cbar=h-3=2M-2`, so
`deg_w C_0=M-1`. Also `B` is even and has degree at most `r=4M-1`, hence
`deg_w B_0<=2M-1`. Since `lambda,mu` are nonzero, the `w^hC_0^2` term has
exact degree

```text
h+2(M-1)=4M-1,                                       (4)
```

one larger than the possible degree of `B_0^2`. Both factors in `(DEF3)`
therefore have exact degree `4M-1`; their constant terms are `B_0(0)^2=1`.

Finally, `t^(8M)=1` and `t!=1`, so the denominator in `(DEF1)` removes the
two distinct roots `1,t^(-1)` from `1-w^(8M)`. The characteristic is greater
than `d=16M`, making that binomial squarefree. Thus `Q_0` is squarefree with
the root set in `(DEF4)`. Any two factors whose product is `Q_0` are coprime,
and their roots partition that set.

It remains to record the prefix consequence. Since both factors in `(DEF3)`
have constant term one, write them uniquely as

```text
H_lambda(w)=product_(a in A_lambda)(1-w/a),
H_mu(w)=product_(a in A_mu)(1-w/a).                   (5)
```

Their difference is

```text
H_lambda-H_mu=(lambda-mu)w^hC_0^2.                   (6)
```

Thus their coefficients agree through degree `h-1=2M`, and the coefficient
difference at degree `h` is `lambda-mu`. Newton's identities for a
constant-normalized root polynomial say

```text
p_j+q_1p_(j-1)+...+q_(j-1)p_1+jq_j=0,                (7)
```

where `q_j=[w^j]H` and `p_j` is the sum of the `j`th powers of the inverse
roots. Comparing `(7)` for the two cells proves equality for `1<=j<h` and
gives the difference `-h(lambda-mu)` at `j=h`, proving `(DEF6)`.

For `j<N=8M`, the sum of the `j`th powers over all `N`th roots is zero. The
inverse roots omitted from `(DEF4)` are `1,t`, so the total over both cells is
`-(1+t^j)`. Dividing this total equally proves `(DEF5)`. This completes the
proof.
