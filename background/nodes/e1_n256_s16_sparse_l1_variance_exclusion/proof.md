# Proof

Write the positive-half negacyclic autocorrelation coefficients as
`A_1,...,A_63`. There are only 21 unordered support pairs, so at
most 21 of these integer coefficients are nonzero. Put

```text
E=sum_d A_d^2=V/2,       L=sum_d |A_d|.
```

For every positive integer `a`,

```text
a^2>=3a-2.
```

Summing over the at most 21 nonzero coefficients gives

```text
E>=3L-42,       L<=floor((E+42)/3).                    (1)
```

The coefficient magnitudes are `2,2,2,1,1,1,1`, so the 21 raw
chord-product magnitudes comprise three `4`s, twelve `2`s, and six
`1`s. Their total magnitude and square mass are

```text
W=42,       Q=102.
```

Fix a non-diameter distance class. Write its signed chord products as
`w_j`, put `a_j=|w_j| in {1,2,4}`, and define

```text
W_d=sum_j a_j,                 H_d=W_d-|sum_j w_j|,
Q_d=sum_j a_j^2-(sum_j w_j)^2.
```

We claim

```text
Q_d<=4H_d.                                             (2)
```

After reversing every sign if necessary, let `P` and `N` be the total
positive and negative magnitudes with `P>=N`, and put `S=P-N`.
Then `H_d=2N`. Since `a_j^2<=4a_j`, the claim follows immediately
when `S=0` or `S>=4`:

```text
Q_d<=4(P+N)-S^2=8N+4S-S^2<=8N.
```

For `S=1,2,3`, the maximum square sum of parts in `{1,2,4}` with
total `x` is

```text
g(x)=16 floor(x/4)+h_(x mod 4),       h=(0,1,4,5).
```

Because `g(x+4)=g(x)+16`, it suffices to inspect `N mod 4`.
The exact slacks

```text
8N-[g(N+S)+g(N)-S^2]

S=1:  0,4,8,4
S=2:  0,6,0,6
S=3:  4,0,4,8
```

are nonnegative, proving (2).

Let `W_64` be the raw magnitude and `D_64` the square mass of diameter
chords, and put `H=sum_d H_d` over non-diameter classes. Since every raw
chord magnitude is at most four,

```text
D_64<=4W_64,
L=42-W_64-H,
102-E=D_64+sum_d Q_d<=4(W_64+H)=4(42-L).
```

Therefore

```text
4L<=E+66,       L<=floor((E+66)/4).                    (3)
```

If `y_u=|F(zeta^u)|^2` for odd `u`, then the mean of the
`y_u` is 16. Autocorrelation antisymmetry gives

```text
|y_u-16|<=2L.                                          (4)
```

Apply (3) to the two new low-variance blocks and (1) to the five existing
upper blocks:

```text
V range    E upper    L upper    y upper B    denominator C
106           53         29          74             1607
108--110      55         30          76             1643
112          56         32          80             1714
114--118     59         33          82             1749
120--124     62         34          84             1785
126--130     65         35          86             1820
132--134     67         36          88             1855
```

For each row define, on `0<x<=B`,

```text
g(x)=log 16+(x-16)/16-(x-16)^2/C-log x.
```

Its derivative factors exactly:

```text
g'(x)=(x-16)(C-32x)/(16 C x).
```

In every row `16<C/32<B`. Thus the only minima are `x=16`
and the endpoint `x=B`. We have `g(16)=0`. Put

```text
r=(B-16)/16-(B-16)^2/C.
```

For each table row, the degree-12 positive Taylor truncation verifies by exact
rational arithmetic that

```text
sum_(j=0)^12 r^j/j! > B/16.
```

Hence `exp(r)>B/16`, so `g(B)>0` and the pointwise
majorant is valid.

Average it over the 128 odd conjugates. The linear deviations have mean zero
and their mean square is `V`, giving

```text
log G<=log 16-V/C,
|Norm(F(zeta))|=G^64<=2^256 exp(-64V/C).               (5)
```

For each row use its minimum `V` and put `q=32V/(3C)`.
The degree-nine positive Taylor truncation verifies exactly that

```text
sum_(j=0)^9 q^j/j! > 2.
```

Therefore `q>log 2`, so `64V/C>6 log 2`. Equation (5)
is strictly below `2^250`. The collision-norm criterion excludes
every listed variance. Since `V` is even, only
`0<V<=104` remains.
