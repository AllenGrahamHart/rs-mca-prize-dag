# Proof

The exact-slice corridor theorem gives

```text
T=t_XR<=N/128-2.
```

Thus `d=e-T-1>0` and `e=T+d+1`.  Also

```text
4e^2=N^2/16<=N(N/4-T-1)=N(e+d),
```

so the chosen cell lies in the residual wedge.

There are at most forty supplied norm levels: `n_j=N/2^j>=4` implies
`0<=j<=39`.  At level `j`, the number of available odd frequencies obeys

```text
M_j=ceil(floor(T/2^j)/2)<=T/2^(j+1)+1/2.
```

Every Frobenius orbit at order `n_j` has length `f_j`, and
`F_p(mu_n_j)` is a subfield of `F_q`.  Therefore

```text
f_j log2(p)<=log2(q)<256.
```

Since `o_j<=M_j`,

```text
R_S log2(p)
 <256 sum_(j in S)M_j
 <=256(T+20)
 <2N+5120.                                           (1)
```

For the structural-zero exponent, every cross pair of distinct levels has
one larger index `a`, and contributes at most

```text
min(n_j,n_a)/2=N/2^(a+1).
```

There are at most `a` partners with smaller index.  Hence

```text
T_2(S,Z)
 <=sum_(a=1)^infinity aN/2^(a+1)=N.                 (2)
```

Together with `|S|<=40`, equations (1)--(2) prove `(RC-1)`.

It remains to lower-bound the ceiling.  Since scale zero is active,

```text
N/4<=A_S=sum_(j in S)N/2^(j+2)<N/2.
```

For `e=N/8`, the function

```text
g(A)=A log2(eN/A)
```

is increasing throughout this interval: its derivative is positive because
`eN/A>=N/4=2^39`.  Therefore

```text
g(A_S)>=g(N/4)=(N/4)log2(N/2)=10N,
```

which is `(RC-2)`.  Since `N=2^41`, `3N+5160<10N`; the printed norm-size
criterion cannot reject any active/zero pattern. QED.
