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

Finally suppose `E=50`. Bound (3) gives `L<=29`. If
`L=29`, then (5) gives `Delta=0`. Thus every
non-diameter class has zero slack, and every diameter has magnitude four.
The twelve magnitude-two chords lie in distinct classes with `S=2` and
contribute energy 48. The six unit chords lie in distinct classes with
positive odd `S` and contribute at least six more. This contradicts
`E=50`, so

```text
E=50 implies L<=28.                                   (8)
```

For `E=49`, (3) gives `L<=28`. Equality would make
`Delta=3`, so (5) forces exactly one unit diameter and zero slack in
every non-diameter class. The twelve magnitude-two classes contribute 48,
while the five remaining unit classes contribute at least five. This
contradicts `E=49`, and hence

```text
E=49 implies L<=27.                                   (9)
```

For `E=48`, (3) again gives `L<=28`. Equality would make
`Delta=2`, forcing one slack-two class and otherwise zero slack. Its
energy together with the twelve magnitude-two and four remaining unit
classes is at least `4+48+4=56`, so `L<=27`.

It remains to rule out `L=27`, which would give `Delta=6`.
Equation (4) gives the following additional exact class patterns:

```text
delta_d=4:
  (r,t,S)=(1,1,1),(1,1,3);

delta_d=6:
  (r,t,S)=(0,2,0),(0,2,4),(1,2,2),(0,3,1),(0,3,3).
```

Class slacks are even, while the only positive diameter charges are three
and four. Up to zero-charge magnitude-four diameters, every decomposition of
six and its minimum possible energy is

```text
positive charges                 energy lower bound
3+3  (two unit diameters)              52
4_64+2  (magnitude-two diameter plus class)  52
2+2+2                                   60
4+2  (two positive classes)             52
6  (one positive class)                 52
```

The bounds follow directly from the displayed patterns, with all remaining
chords in zero-slack classes. Every case exceeds 48, so

```text
E=48 implies L<=26.                                  (10)
```

For `E=47`, (3) gives `L<=28`. The value `L=28`
would give the impossible `Delta=1`; the value `L=27` gives
`Delta=5`, forcing one unit diameter and one slack-two class. Their
energy plus the twelve magnitude-two and three remaining unit classes is at
least `4+48+3=55`, so `L<=26`.

If `L=26`, then `Delta=9`. Diameter chords form a matching on
the four light vertices, so there are at most two unit diameters. Parity then
forces exactly one unit diameter, leaving total charge six. The possibilities
are a magnitude-two diameter plus a slack-two class, one slack-six class, a
slack-four plus a slack-two class, or three slack-two classes. The last would
consume six unit chords after the unit diameter and is impossible; the first
three have energy at least 51 by the displayed local patterns. Hence

```text
E=47 implies L<=25.                                  (11)
```

For `E=46`, equality in (3), namely `L=28`, has
`Delta=0` and energy at least 54. If `L=27`, then
`Delta=4`. The positive charge is either one magnitude-two diameter,
one slack-four class, or two slack-two classes. Their respective energy lower
bounds are 50, 50, and 58. Thus

```text
E=46 implies L<=26.                                  (12)
```

For `E=45`, (3) gives `L<=27`. Equality has
`Delta=3`, forcing a unit diameter and energy at least 53. If
`L=26`, then `Delta=7`, forcing one unit diameter together with
one magnitude-two diameter, one slack-four class, or two slack-two classes.
The corresponding energy lower bounds are 49, 49, and 57. Therefore

```text
E=45 implies L<=25.                                  (13)
```

For the next two energies, record the exact minimum-energy slack ledger in a
compact recurrence. Let `T` contain every attainable positive class type
`(delta,r,t,S)` from (4), retaining at most the profile's three
magnitude-four, twelve magnitude-two, and six unit chords within one class.
Define

```text
P(0,0,0)=0,
P(d,r,t)=min_(e,a,b,S in T) [P(d-e,r-a,t-b)+S^2].
```

Missing states have value infinity. We deliberately forget cumulative
magnitude-four usage across classes, enlarging the feasible universe. If
`d_2,d_1` count magnitude-two and unit diameters, the matching
constraints are

```text
d_2+2d_1<=4,       d_1+d_2<=3.
```

The resulting relaxed minimum energy at global slack `Delta` is

```text
m(Delta)=min [P(Delta-4d_2-3d_1,r,t)
              +4(12-d_2-r)+(6-d_1-t)].
```

This is a lower-bound relaxation, not an exact reconstruction of the
class partition. Indeed, a zero-slack non-diameter class has either
`(r,t)=(0,0)`, `(r,t)=(1,0)` with `S=2`, or `(r,t)=(0,1)` with
`S in {1,3}`. Charging its magnitude-two and unit chords separately
therefore costs respectively `0`, `4`, or `1`, never more than its
actual energy `S^2`. The formula also omits the nonnegative energy of
diameters and of zero-slack classes made only from magnitude-four chords.
Together with the forgotten global magnitude-four budget, every omission
can only lower the minimum relative to an actual support.

Direct substitution in this finite recurrence gives

```text
Delta       0   1   2   3   4   5   6   7   8   9  10  11  12  13
m(Delta)   54 inf  56  53  50  55  52  49  46  51  48  45  42  47.
```

For `2<=Delta<=13`, the same table is summarized by

```text
m(Delta)=54-Delta  if Delta=0 mod 4,
         58-Delta  if Delta=2 mod 4,
         56-Delta  if Delta=3 mod 4,
         60-Delta  if Delta=1 mod 4.
```

The exceptional entries are `m(0)=54` and `m(1)=infinity`.

Every actual support has energy at least this relaxed minimum. For
`E=44`, (3) gives `L<=27`; the candidates `L=27,26,25`
have slacks `2,6,10` and minimum energies `56,52,48`, all too
large. Hence

```text
E=44 implies L<=24.                                  (14)
```

For `E=43`, the candidates `L=27,26,25,24` have slacks
`1,5,9,13`, with no feasible first case and lower bounds
`55,51,47` for the rest. Therefore

```text
E=43 implies L<=23.                                  (15)
```

If `y_u=|F(zeta^u)|^2` for odd `u`, then the mean of the
`y_u` is 16. Autocorrelation antisymmetry gives

```text
|y_u-16|<=2L.                                         (16)
```

We first exclude `V=100` and `V=98`. Equations (8)--(9) give
`0<y_u<=72` in both rows. On `0<x<=72`, define

```text
h(x)=log 16+1/150+(23/336)(x-16)-(x-16)^2/1344-log x.
```

Its derivative factors exactly as

```text
h'(x)=-(x-14)(x-48)/(672x).
```

Hence the only minima are `x=14` and `x=72`. At the first,

```text
h(14)=log(8/7)+1/150-47/336>0;
```

the degree-four even alternating truncation of `log(1+1/7)` is
strictly greater than `47/336-1/150=373/2800`. At the endpoint,

```text
h(72)=113/75-log(9/2)>0;
```

the degree-six positive Taylor truncation of `exp(113/75)` is strictly
greater than `9/2`. Thus `h(x)>0` throughout the interval. Averaging
over the 128 conjugates gives

```text
log G<=log 16+1/150-V/1344.
```

For the two rows put

```text
V=100: q=(32/3)(25/336-1/150)=1138/1575,
V=98:  q=(32/3)(49/672-1/150)=53/75.
```

In both cases the degree-three positive Taylor truncation of `exp(q)` is
strictly greater than two. Therefore `q>log 2`, equivalently the norm
decay exceeds six bits. Both variances are excluded.

For `V=96`, equation (10) gives `0<y_u<=68`. Define on
this interval

```text
h_2(x)=log 16+1/150+(11/161)(x-16)-(x-16)^2/1288-log x.
```

Its derivative is

```text
h_2'(x)=-(x-14)(x-46)/(644x),
```

so its only minima are 14 and 68. Exact rational Taylor comparisons give

```text
h_2(14)=log(8/7)+1/150-45/322>0,
h_2(68)=35261/24150-log(17/4)>0.
```

The first uses the degree-four alternating logarithm truncation; the second
uses the degree-five positive exponential truncation. Averaging gives

```text
log G<=log 16+1/150-V/1288.
```

At `V=96`,

```text
q=(32/3)(12/161-1/150)=26224/36225.
```

Its degree-three positive exponential truncation exceeds two, so the norm is
strictly below `2^250`. This excludes `V=96`.

For `V=94`, equation (11) gives `0<y_u<=66`. On this
interval use

```text
h_3(x)=log 16+1/150+(43/630)(x-16)-(x-16)^2/1260-log x.
```

The derivative is `-(x-14)(x-45)/(630x)`, so the minima are
14 and 66. Exact rational comparisons give

```text
h_3(14)=log(8/7)+1/150-44/315>0,
h_3(66)=1507/1050-log(33/8)>0.
```

Degree-four Taylor truncations certify both inequalities. After averaging,

```text
q=(32/3)(47/630-1/150)=3424/4725;
```

its degree-three exponential truncation exceeds two. Hence `V=94` is
excluded.

For `V=92`, equation (12) gives the same ceiling 68 used by
`h_2`, but the allowance must be tightened from `1/150` to
`1/160`. The derivative roots remain 14 and 46, while

```text
h_2(14)=log(8/7)+1/160-45/322>0,
h_2(68)=37601/25760-log(17/4)>0.
```

Degree-four logarithm and degree-five exponential truncations certify the
minima. The averaged decay is

```text
q=(32/3)(23/322-1/160)=73/105,
```

whose degree-four exponential truncation exceeds two. Thus `V=92` is
excluded.

Finally `V=90` has ceiling 66 by (13). Use the root pair
`(14,45)` from `h_3`, again with allowance `1/160`. The
two minimum checks become

```text
log(8/7)+1/160-44/315>0,
1607/1120-log(33/8)>0.
```

Both use degree-four truncations, and the averaged decay is again
`q=73/105`. This excludes `V=90`.

For `V=88`, equation (14) gives `0<y_u<=64`. Use allowance
`1/160` and derivative roots `(14,44)`:

```text
h_4(x)=log 16+1/160+(3/44)(x-16)-(x-16)^2/1232-log x.
```

The two minimum checks are

```text
log(8/7)+1/160-43/308>0,
17357/12320-log 4>0.
```

Degree-four truncations certify both, and the averaged decay is
`q=73/105`. Thus `V=88` is excluded.

For `V=86`, equation (15) gives `0<y_u<=62`. With allowance
`1/160` and roots `(14,43)`, use

```text
h_5(x)=log 16+1/160+(41/602)(x-16)-(x-16)^2/1204-log x.
```

The minimum checks are

```text
log(8/7)+1/160-42/301>0,
66541/48160-log(31/8)>0.
```

Again degree-four truncations suffice, and the averaged decay is
`q=73/105`. This excludes `V=86`.

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
|Norm(F(zeta))|=G^64<=2^256 exp(-64V/C).               (17)
```

For each row use its minimum `V` and put `q=32V/(3C)`.
The degree-nine positive Taylor truncation verifies exactly that

```text
sum_(j=0)^9 q^j/j! > 2.
```

Therefore `q>log 2`, so `64V/C>6 log 2`. Equation (17)
is strictly below `2^250`. The collision-norm criterion excludes
every listed variance. Since `V` is even, only
`0<V<=84` remains.
