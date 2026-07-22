# Proof

Let `I,J` be the disjoint exponent supports of a primitive ordered top shift
pair at exact level `m`, and put

```text
f_t=1_(t in I)-1_(t in J),
z=sum_(t=0)^(m-1) f_t zeta_m^t in Z[zeta_m].        (1)
```

Top-shift equality and Newton identities give

```text
sum_t f_t omega^(kt)=0,       1<=k<h,               (2)
```

after reducing `zeta_m` to an element `omega` of order `m` modulo a prime
above `p`. The primitive-pair hypothesis makes `z` nonzero: if `z=0`, odd
Fourier inversion gives `f_t=f_(t+m/2)` for every `t`, so both supports have
the nontrivial stabilizer `-1`.

Because `p==1 mod n` and `m|n`, the prime splits completely in
`Q(zeta_m)`. For each odd `1<=k<h`, equation `(2)` places a distinct Galois
conjugate of `z` in a distinct prime above `p`. There are
`r=floor(h/2)` such odd indices. The cyclotomic-norm argument therefore gives

```text
p^r<=|Norm(z)|.                                     (3)
```

Put `g_t=f_t-f_(t+m/2)` for `0<=t<m/2`. Odd-frequency Parseval and AM--GM,
exactly as in the quarter-width theorem, give

```text
|Norm(z)|<=(sum_t g_t^2)^(m/4)<=(4h)^(m/4).         (4)
```

The official ambient order now remains in the estimate. Since `n>1`, the
prime `p>=n^2` cannot equal the composite integer `n^2`; hence `p>n^2`.
Combining `(3)` and `(4)` proves

```text
n^(2r)<p^r<=(4h)^(m/4),
```

which is `(AON1)`.

For the explicit cap write `m=2^a` and `n=2^s`. The proved quarter-width
theorem gives `4h<m`, so `(AON1)` implies

```text
2^(2sr)<2^(am/4),
r<ma/(8s).                                         (5)
```

As `r` is an integer, `(5)` gives

```text
r<=ceil(ma/(8s))-1=C(m,n)-1.
```

Since `h<=2r+1`, this is `h<=2C(m,n)-1`, proving `(AON3)`. If `m=n`, then
`a=s`, `C=m/8`, and the cap is `m/4-1`, as claimed.

## Parity sharpening

For `0<x<1`,

```text
1-x<2^(-36x/25).                                   (6)
```

Indeed `log(1-x)<-x`. Also

```text
exp(25/36)
 >1+25/36+(25/36)^2/2+(25/36)^3/6+(25/36)^4/24
 =80665009/40310784>2.
```

Hence `log 2<25/36`, so `(36/25)log 2<1`, which proves `(6)`.

Put `h=m/4-d`, `j=s-a`, and apply `(6)` with `x=4d/m`. The norm ceiling in
`(AON1)` sharpens to

```text
(4h)^(m/4)
 =2^(am/4)(1-4d/m)^(m/4)
 <2^(am/4-36d/25).                                 (7)
```

Since `m/4` is even, `h` and `d` have the same parity. If `d` is even, then
`2 floor(h/2)=h=m/4-d`. Equations `(AON1)` and `(7)` require

```text
s(m/4-d)<am/4-36d/25,
25jm<4(25s-36)d.                                   (8)
```

Thus the reverse weak inequality in the even line of `(AON4)` is impossible.
If `d` is odd, then `2 floor(h/2)=h-1=m/4-d-1`. The necessary inequality is

```text
s(m/4-d-1)<am/4-36d/25,
25jm<4(25s-36)d+100s.                              (9)
```

Again the reverse weak inequality is impossible. This proves `(AON4)`. QED.
