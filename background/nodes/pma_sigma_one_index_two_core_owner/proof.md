# Proof - PMA sigma-one index-two near-core owner

Order the two cosets `B_0,B_1`, and order the points in each coset. For a
listed codeword in `CORE_s(U)`, choose the first qualifying coset `B`. Put

```text
E=B\A_P,    e=|E|<=s,    q=q_e=max(0,k-N+e).
```

The codeword agrees with `U` on all `N-e` points of `B\E`. If `q>0`, then

```text
|A_P\B| >= a-(N-e) >= k+1-N+e=q+1.
```

Thus there are at least `q` outside agreement points. Let `J` be the first
`q` of them. If `q=0`, take `J` empty. The owner is

```text
I(P)=(B,E,J).
```

Suppose `P,P'` have the same owner. They both agree with `U` on

```text
(B\E) union J,
```

which has `N-e+q>=k` distinct points by the definition of `q`. Hence `P-P'`
has at least `k` roots while its degree is less than `k`, so `P=P'`. The
owner is injective. There are two choices for `B`, `binom(N,e)` choices for
`E`, and at most `binom(N,q_e)` choices for `J`. Summing over `e` proves
`(CORE)`.

Now specialize to the official grid and `s=4`. Here `k<=N`, so
`0<=q_e<=e<=4`. Every summand in `(CORE)` is at most `N^8`, giving

```text
#QOWN_core4 <= 10N^8.                                  (1)
```

Let `h=k/2+1` and `m=min(h,N-1-h)`. On the smallest official row,
`N=4096`; the smallest possible value of either side of the symmetric
binomial index is already at least `257`. Hence `12<=m<=(N-1)/2` on every
official row, and binomial monotonicity gives

```text
Q_2(k+2)=binom(N-1,h)=binom(N-1,m)>=binom(N-1,12).
```

Since `N>=4096`, every factor `N-i` for `1<=i<=12` is at least `N/2`.
Therefore

```text
binom(N-1,12)
 >= N^12/(2^12 12!).                                  (2)
```

The exact integer inequality

```text
4096^4 > 10*2^12*12!
```

and monotonicity in `N` show that the right side of `(2)` is greater than
`10N^8`. Combining with `(1)` proves `(FINITE-CORE)`.

Apply this owner after `QOWN_per`, so the classes are disjoint. The sharper
exact-periodic theorem gives

```text
#QOWN_per <= 4(1+epsilon)Q_2+3,    epsilon=2^-690.
```

Adding `#QOWN_core4<=Q_2`, using `Q_2>=1`, and enlarging coefficients gives

```text
#(QOWN_per union QOWN_core4)
 <= 5Q_2+4epsilon Q_2+3
 <= 8(1+epsilon)Q_2
 < 719(1+epsilon)Q_2.
```

This proves `(COMBINED)`.

Finally, the reciprocal-quadratic construction has core
`C=G\{b}` and defect triple `D subset C`. Its actual codeword agrees with the
source word on every point of `C\D=G\({b} union D)`. Thus it misses at most
four points of the index-two coset `G` and is in `QOWN_core4`. The owner uses
the full source agreement set before any sunflower presentation, so all chart
copies of that codeword receive one global charge.
