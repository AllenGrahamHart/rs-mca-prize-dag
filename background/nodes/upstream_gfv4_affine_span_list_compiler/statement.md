# Affine-span Reed-Solomon list compilers

- **status:** PROVED
- **closure:** proof
- **source:** `experimental/grande_finale.tex` at upstream pin `b13de811`
- **upstream labels:** `thm:affine-span-list`, `thm:rank-flat-list`

Let `C=RS[F,D,K]` have length `n`, let `u in F^D`, and put

```text
m=K+w<=n.
```

Let `A=c_0+C'` be an affine subspace of codewords whose direction space
`C'` has dimension `s`. Then

```text
|{c in A: agr(c,u)>=m}|
 <= floor((n-K+s) falling s / (w+1) rising s)
  = floor(C(n-K+s,s)/C(w+s,s)).                    (AS1)
```

For `s=0` the empty products are one. In particular, a codeword pencil
contains at most

```text
floor((n-K+1)/(w+1))                                (AS2)
```

members of the list.

There is also a generalized-weight refinement. Let `d_j` be the `j`-th
generalized Hamming weight of `C'`, put `t=n-m`, let `G` be the common-zero
set of `C'`, and let `b` count the coordinates of `G` where the common
affine value does not agree with `u`. Then

```text
|{c in A: agr(c,u)>=m}|
 <= floor(d_s falling s / product_(j=1)^s(d_j-t+b)), (AS3)

d_j>=n-K+j,       d_j-t+b>=w+j+b>0.                 (AS4)
```

The claims hold over every field and for every distinct evaluation domain.
