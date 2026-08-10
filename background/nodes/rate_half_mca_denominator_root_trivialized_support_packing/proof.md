# Proof

Fix one reduced support `S_i'`. If two degree-`<k` pairs both simultaneously
explain `r0,r1` there, the two first components agree on `|S_i'|=M>=k`
distinct points and are equal as polynomials; the same holds for the second
components. The explaining pair is unique.

Now take distinct slopes `i,j`. If the reduced supports intersected in at
least `k` points, the two unique first components would both interpolate
`r0` on those points and hence be equal. The second components would also be
equal. This contradicts the pair-injectivity theorem in the cancellation
dichotomy. Therefore their intersection has size at most `k-1`.

No `k`-subset of the reduced domain can consequently lie in two supports.
Each size-`M` support contains `binom(M,k)` such subsets and the size-`N`
domain contains `binom(N,k)`, proving the packing inequality.

For the numerical fence,

```text
binom(N,k)/binom(M,k)
  = product_{j=0}^{k-1} (N-j)/(M-j)
  >= (N/M)^k.
```

Since `N=n-t`, `M=m-t`, and `n>m`, the ratio `N/M` is increasing in `t`.
At both rows `n/m>3/2`, while `k=1048576>100` and
`3^100>2^158`. Hence `(3/2)^k>(3/2)^100>2^58`. The literal KoalaBear and
Mersenne-31 budgets are respectively below `2^58` and `2^24`. The support
packing bound therefore cannot certify either budget. QED.
