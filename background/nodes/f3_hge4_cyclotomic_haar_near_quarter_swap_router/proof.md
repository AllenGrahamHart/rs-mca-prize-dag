# Proof

Put `M=m/2`, choose `omega in F_p` of order `m`, and label the reciprocal
root supports of a hypothetical primitive exact-level pair by disjoint
`h`-subsets `I,J` of `Z/mZ`. Define

```text
f_t=1_(t in I)-1_(t in J).                          (1)
```

Top-shift equality and Newton identities give

```text
sum_t f_t omega^(kt)=0,       1<=k<h.               (2)
```

As in the quarter-width norm theorem, the cyclotomic integer

```text
z_0=sum_t f_t zeta_m^t
```

is nonzero: otherwise odd Fourier inversion makes both supports invariant
under `-1`, contradicting primitivity.

## First antipodal defect

For `0<=t<M`, put

```text
g_t=f_t-f_(t+M),       q_t=f_t+f_(t+M),
D_0=sum_t g_t^2,       L=sum_t q_t^2.                (3)
```

The orthogonal identity `(a-b)^2+(a+b)^2=2a^2+2b^2` gives

```text
D_0+L=4h.                                           (4)
```

Let `r_0=floor(h/2)`. Complete splitting of `p` in `Q(zeta_m)`, followed by
odd-frequency Parseval and AM--GM, gives

```text
p^r_0<=|Norm(z_0)|<=D_0^(m/4).                      (5)
```

Because `p>m^2` and `h=m/4-d`, both parity cases imply

```text
D_0>m^(1-4(d+1)/m).
```

Using `exp(-x)>=1-x` in `(4)--(5)` yields the strict defect bound

```text
0<=L<4(d+1)log m.                                   (6)
```

## Dyadic Haar tower

For `v>=0`, put `m_v=m/2^v` and collapse `f` onto `Z/m_vZ`:

```text
f_v(t)=sum_(j=0)^(2^v-1) f_(t+j m_v).
```

Thus `f_0=f`, `f_1=q`, and

```text
z_v=sum_t f_v(t)zeta_(m_v)^t,
D_v=sum_(t=0)^(m_v/2-1)(f_v(t)-f_v(t+m_v/2))^2,
D_v+||f_(v+1)||_2^2=2||f_v||_2^2.                  (7)
```

If `z_v=0`, divisibility by
`Phi_(m_v)(X)=X^(m_v/2)+1` gives

```text
f_v(t)=f_v(t+m_v/2),       D_v=0,
||f_(v+1)||_2^2=2||f_v||_2^2.                      (8)
```

If `z_v!=0`, let

```text
H_v=floor((h-1)/2^v),       r_v=ceil(H_v/2).
```

The odd integers through `H_v` index distinct primes above `p`, because
their original exponents `2^v k` still lie below `h` in `(2)`. The same norm
argument gives

```text
p^r_v<=|Norm(z_v)|<=D_v^(m_v/4).                   (9)
```

## Exact last-stage repetition contradiction

Write `R=log m`, set

```text
X=4(d+1)R,       T=ceil(log_2 X),       B=2^T.
```

Then `X<=B<2X`. Assume `(CHQ2-exact)`. We prove successively that

```text
z_1=z_2=...=z_T=0.                                 (10)
```

Suppose the earlier terms vanish but `z_v!=0` for some `1<=v<=T`. Since
`2^v<=B<h`, the moment rank in `(9)` is positive. Equations `(6)--(8)` give

```text
D_v<=2^v L<2^v X<=BX.                              (11)
```

On the other hand `r_v>h/2^(v+1)-1`, so `(9)` and `p>m^2` give

```text
D_v>m^(1-(4d+8*2^v)/m).                            (12)
```

Since `2^v<=B`, equation `(12)` gives

```text
D_v>m^(1-(4d+8B)/m)>BX,
```

contradicting `(11)`. This proves `(10)`.

Repeated use of `(8)` now says that `f_1` consists of `B=2^T` identical
blocks. Hence either `L=0` or the positive integer `L` is at least `B`. But
`(6)` gives `L<X<=B`, so necessarily

```text
L=0.                                                (13)
```

Therefore `f_t+f_(t+M)=0` for every `t`: the antipode exchanges `I` and `J`.
The primitive swap router proves that such a top shift pair has odd `h` and
is exactly an instance of its half-order support problem. Even widths are
empty, and the free class is absent.

## Closed-form corollary

It remains to show that `(CHQ2)` implies the exact hypotheses. It gives

```text
B<2X=8(d+1)R<sqrt(m).
```

The condition is vacuous at `m=16`; otherwise `m>=32`, and it also gives
`d<sqrt(m)/(8R)<sqrt(m)/8`. Hence

```text
h=m/4-d>m/4-sqrt(m)/8>sqrt(m)>B.                   (14)
```

Moreover,

```text
BX<2X^2=32(d+1)^2R^2<m/2.                          (15)
```

Finally `B<8(d+1)R`, so

```text
((4d+8B)R)/m<68(d+1)R^2/m
                  <68/(64(d+1))
                  <=17/32<log 2.                  (16)
```

Here `d+1>=2`, and `log 2>2/3>17/32` follows from the first positive term in
`log 2=2 atanh(1/3)`. Therefore

```text
m^(1-(4d+8B)/m)>m/2>BX.                            (17)
```

Equations `(14)` and `(17)` are `(CHQ2-exact)`. QED.

For fixed `m`, the exact band is an initial interval in `d`: as `d`
increases, `X` and `B` are nondecreasing, `h` decreases, `BX` is
nondecreasing, and `m^(1-(4d+8B)/m)` is nonincreasing. Thus an adjacent exact
PASS/FAIL boundary certifies the whole printed interval.
