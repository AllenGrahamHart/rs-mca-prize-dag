# L1 m=4, h=3, nu=2 prime-field Belyi normal form

- **status:** PROVED
- **dependency:** `l1_m4_h3_tangent_radical_exclusion`
- **consumer:** `l1_mixed_petal_amplification`

Assume the surviving positive stratum

```text
(nu,eta)=(2,1),       eta=deg H.                       (PBN1)
```

Let `r_1,r_2,r_3` be the three distinct tangent roots and let their
multiplicities in `T=2aR+3b=2a(R-y_0)` be `e_1,e_2,e_3`. Then

```text
1<=e_i<p,       e_1+e_2+e_3=p,                        (PBN2)
```

and the three multiplicities are pairwise distinct. After ordering them, put

```text
d_1=e_2-e_3,  d_2=e_3-e_1,  d_3=e_1-e_2 in F_p,
t_i=d_i^(-1).                                          (PBN3)
```

There is a nonzero scalar `lambda` such that

```text
r_i=lambda t_i.                                        (PBN4)
```

Define the prime-field polynomial

```text
S_e(Z)=product_(i=1)^3 (Z-t_i)^(e_i) in F_p[Z].        (PBN5)
```

Then the depressed inner polynomial has the exact scalar-conjugate form

```text
R(X)=lambda^p (S_e(X/lambda)-S_e(0)).                  (PBN6)
```

It has only two finite critical values: `0`, with one double preimage at
`X=0` and all other preimages simple, and

```text
y_0=-lambda^p S_e(0),                                  (PBN7)
```

whose three preimages have multiplicities `e_1,e_2,e_3`. Equivalently,

```text
S_e'(Z)=c_e Z product_(i=1)^3 (Z-t_i)^(e_i-1)          (PBN8)
```

for a nonzero `c_e in F_p`.

Thus this stratum is indexed by unordered pairwise-distinct positive integer
triples summing to `p`, plus one scalar conjugacy, rather than by an arbitrary
degree-`p` polynomial. This does not prove that any such normal form has or
lacks the three official split fibers, exclude the stratum, treat `(1,2)` or
`nu=0`, classify nonembedded `h=2`, or close L1.
