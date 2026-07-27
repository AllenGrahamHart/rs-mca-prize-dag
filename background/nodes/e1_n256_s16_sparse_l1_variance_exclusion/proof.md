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

For the two endpoint energies we can sharpen (3). In a non-diameter class,
let `b,r,t` count raw chord magnitudes `4,2,1`, respectively, and
retain `S=|A_d|`. Define its nonnegative charging slack

```text
delta_d=4H_d-Q_d.
```

Since `4b+2r+t=S+2N`, direct substitution gives

```text
delta_d=(S-2)^2+4r+3t-4.                              (4)
```

The parity `S=t mod 2` shows that every `delta_d` is even. Equation
(4) also classifies the two smallest values:

```text
delta_d=0:
  (r,t,S)=(0,0,0),(0,0,4),(1,0,2),(0,1,1),(0,1,3);

delta_d=2:
  (r,t,S)=(0,2,2).
```

For a diameter chord of magnitude `a`, use the slack
`delta_64(a)=4a-a^2`, which is `0,4,3` for
`a=4,2,1`. Summing every class gives the exact global slack identity

```text
Delta=4(42-L)-(102-E)
     =sum_d delta_d+sum_(diameters e) delta_64(a_e).   (5)
```

Suppose first that `E=52`. Bound (3) gives `L<=29`. If
`L=29`, then (5) gives `Delta=2`. Hence there is no unit or
magnitude-two diameter, exactly one non-diameter class has slack two, and
every other class has slack zero. The slack-two class consumes exactly two of
the six unit chords, no magnitude-two chord, and contributes energy four.
Each of the twelve magnitude-two chords lies in a distinct zero-slack class
with `S=2`, contributing total energy 48. The four remaining unit chords
lie in distinct zero-slack classes with positive odd `S`, contributing at
least four more. Thus `E>=56`, a contradiction, and

```text
E=52 implies L<=28.                                   (6)
```

Now suppose `E=51`. If `L=29`, then (5) gives the impossible
value `Delta=1`. If `L=28`, then `Delta=5`. The only
decomposition of five into the allowed nonnegative charges is one unit
diameter of charge three and one slack-two class. All twelve magnitude-two
chords again lie in distinct zero-slack classes and contribute energy 48.
The slack-two class contributes four, and the three remaining unit chords
contribute at least three, so `E>=55`, again a contradiction. Therefore

```text
E=51 implies L<=27.                                   (7)
```

If `y_u=|F(zeta^u)|^2` for odd `u`, then the mean of the
`y_u` is 16. Autocorrelation antisymmetry gives

```text
|y_u-16|<=2L.                                          (8)
```

Apply (6)--(7) to the two new endpoint rows, (3) to the next two
low-variance blocks, and (1) to the five existing upper blocks:

```text
V range    E upper    L upper    y upper B    denominator C
102           51         27          70             1568
104           52         28          72             1600
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
|Norm(F(zeta))|=G^64<=2^256 exp(-64V/C).               (9)
```

For each row use its minimum `V` and put `q=32V/(3C)`.
The degree-nine positive Taylor truncation verifies exactly that

```text
sum_(j=0)^9 q^j/j! > 2.
```

Therefore `q>log 2`, so `64V/C>6 log 2`. Equation (9)
is strictly below `2^250`. The collision-norm criterion excludes
every listed variance. Since `V` is even, only
`0<V<=100` remains.
