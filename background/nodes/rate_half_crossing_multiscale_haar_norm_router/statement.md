# Multiscale Haar norm-product router for crossing windows

- **status:** PROVED
- **consumer:** `rate_half_list_adjacent_crossing`
- **scope:** split prime rows, `p = 1 mod n`

Let `n=2^m`, let `S` be an `r`-subset of `Z/n`, and put

```text
F(X)=sum_(i in S) X^i.
```

For `0<=j<m`, set `N_j=n/2^j` and fold the indicator of `S` modulo
`N_j`:

```text
A_(j,u)=#{i in S:i=u mod N_j},
eps_(j,u)=A_(j,u)-A_(j,u+N_j/2),
E_j=sum_(u<N_j/2) eps_(j,u)^2,
beta_j=F(zeta_(N_j)).                                  (MH1)
```

These energies have the exact shared budget

```text
sum_(j=0)^(m-1) E_j/2^(j+1)=r-r^2/n.                  (MH2)
```

Now suppose `p=1 mod n`, `2<=w<=n/2`, and the first `w-1` moments of
`S` vanish after reduction at a primitive `n`-th root in `F_p`.  Put

```text
J={j:0<=j<=floor(log_2(w-1)), beta_j!=0},
Z={0,...,floor(log_2(w-1))}\J,
c_j=#{odd t:1<=2^j t<=w-1},
a_j=N_j/4,
C_J=sum_(j in J)c_j,
A_J=sum_(j in J)a_j,
T_J=sum_(j in J)sum_(z in Z) min(N_j,N_z)/2.          (MH3)
```

If `J` is nonempty, then

```text
2^T_J p^C_J
  divides product_(j in J)|Norm(beta_j)|,

product_(j in J)|Norm(beta_j)|
  <= product_(j in J) E_j^a_j
  <= ( n(r-r^2/n)/(2A_J) )^A_J.                      (MH4)
```

If `J` is empty, the first `floor(log_2(w-1))+1` Haar differences vanish
over the integers.  In particular, for `w=2^v`, `J` empty is exactly the
structural condition that `S` is invariant under addition by `n/2^v`.

For `w=2^v`, the all-active pattern `J={0,...,v-1}` has

```text
C_J=w-1,
A_J=n(w-1)/(2w),
B=(r-r^2/n)/(1-1/w),

p^C_J > B^A_J   iff   p>B^(n/(2w)).                  (MH5)
```

At the prize length `n=2^41`, `r=n/2-w`, and `w=2^37`, the right side of
`(MH5)` is strictly greater than `2^256`.  Therefore `(MH4)` cannot exclude
the all-active pattern at `w=2^37` for any official characteristic
`p<2^256`.  At `w=2^38` the formal `p=2^256` comparison reverses, but that
checkpoint is already covered by the proved single-scale ideal/Galois
multiplicity exclusion.

Thus multiplying all Haar-level norms is a valid sharpening and can delete
some zero-scale patterns, but it does not move the live power-of-two crossing
frontier below `2^38`.  No existence of an all-active solution is claimed.
