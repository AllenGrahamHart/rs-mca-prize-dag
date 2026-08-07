# Coefficient-scale quotient sieve for shift pairs

- **status:** PROVED
- **closure:** proof
- **upstream source:** `rs-mca` commit `93fba1be`,
  `experimental/grande_finale_work/sp_next_section.tex`, introduced by
  `9af5ba8e5`.

Let `D=alpha H` be a multiplicative coset of a cyclic group of order `n` in
a field of characteristic coprime to `n`.  For `S subset D`, `|S|=e`, write

```text
L_S(X)=X^e+sum_(j=1)^e lambda_j X^(e-j)
```

and define

```text
s(S)=gcd(n,e,{j:lambda_j!=0}).
```

For every divisor `c|n`, the following are equivalent:

1. `S` is a union of complete orbits of the order-`c` subgroup of `H`;
2. `L_S(X)=L_bar(X^c)` for a unique monic locator `L_bar` split over
   `D_c={x^c:x in D}`;
3. `c|e` and `lambda_j=0` whenever `c` does not divide `j`.

Consequently `s(S)` is the maximal periodicity scale of `S`.

Now let `(A,B)=(L_P,L_Q)` be a disjoint depth-`t` shift pair of degree `e`,
and put

```text
c=gcd(s(P),s(Q)),  d=deg(A-B).
```

If `c>1`, then the pair is quotient-borne.  It has unique forms

```text
A(X)=A_c(X^c),  B(X)=B_c(X^c),
e_c=e/c,        t_c=ceil((t+1)/c)-1,
d=c deg(A_c-B_c),
```

and `(A_c,B_c)` is a depth-`t_c` shift pair on `D_c`.  Extraction at the
maximal `c` leaves a coefficient-primitive quotient pair.  Conversely, a
coefficient-primitive quotient pair at this depth pulls back to a pair whose
maximal common scale is exactly `c`.

In particular, every primitive pair has `c=1`, while every quotient-borne
pair satisfies

```text
c | gcd(n,e,d).                                      (QS-1)
```

At the local official dyadic length `N=2^41`, an imprimitive nonconstant pair
must therefore have both `e` and `d` even.
