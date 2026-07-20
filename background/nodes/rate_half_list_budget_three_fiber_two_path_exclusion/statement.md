# Budget-three fiber-two path exclusion

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:**
  `rate_half_list_budget_three_multifiber_vandermonde_exclusion`

Let `F` be a field, let `r_0,r_1,r_2` be distinct elements of `F`, and let
`H_i(Y)` be nonzero polynomials of one common degree `s>=2` such that

```text
H_i(r_i^2)=0.                                          (F2P1)
```

Define

```text
A_i(X)=H_i(X^2)/(X-r_i).                               (F2P2)
```

If the three `A_i` are pairwise coprime, then there is no relation

```text
lambda_0 A_0+lambda_1 A_1+lambda_2 A_2=0,
lambda_0 lambda_1 lambda_2!=0.                         (F2P3)
```

Indeed, write

```text
H_i(Y)=(Y-r_i^2)K_i(Y),
A_i(X)=(X+r_i)K_i(X^2).                                (F2P4)
```

Separating the odd and even parts of `(F2P3)` forces

```text
(lambda_0K_0,lambda_1K_1,lambda_2K_2)
 =K(r_1-r_2,r_2-r_0,r_0-r_1)                          (F2P5)
```

for one nonzero `K in F[Y]`. Thus all three locators contain the common
factor `K(X^2)`. Since `deg K=s-1>=1`, this contradicts pairwise
coprimality.

In either linear path-plus-singleton chamber, the tight-triangle locators
have deficits `(1,1,1)` and are pairwise coprime. If their completed
degree-`d` blocks are equal unions of fibers of the common map `X^2`, then
`s=d/2`. At the prize maximum `d=2^39`, so `(F2P1)--(F2P3)` apply and exclude
the construction.

Together with the proved multifiber Vandermonde exclusion for `m>=3`, this
eliminates every direct equal-complete-fiber path construction with common
fiber size `m>=2`. It does not exclude the structure-free `m=1` case,
different quotient maps between blocks, partial fibers, or primitive
locators. It makes no claim about the four-cycle or other budget-three
chambers.
