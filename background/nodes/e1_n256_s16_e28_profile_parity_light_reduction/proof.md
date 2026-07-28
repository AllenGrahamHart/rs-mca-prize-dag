# Proof

## Slack and profiles

The general chord inequality gives `L<=floor((28+66)/4)=23`. Put
`Delta=28+66-4L`. The proved relaxed slack recurrence gives

```text
L       23  22  21  20  19  18  17  16
Delta    2   6  10  14  18  22  26  30
min E   56  52  48  44  40  36  32  28.
```

Therefore `L<=16`. Exact enumeration of

```text
sum_j j^2 n_j=28,       sum_j j n_j<=16
```

gives 14 profiles. For the rational cubic Hermite majorant with double
contacts 14 and 57, the raw moments at `V=56` are

```text
(1,16,312,6784+M_3).
```

Exact substitution at the sign boundary gives

```text
M_3=658: (73771/79507, 5736/79507, -8052/245917),
M_3=659: (73773/79507, 5734/79507, -2539/77658).
```

Eight-term rational atanh bounds certify

```text
-(605625/2544224)log 2 +(73771/79507)log(8/7)
 +(5736/79507)log(64/57)+8052/245917 > 0,

-(605497/2544224)log 2 +(73773/79507)log(8/7)
 +(5734/79507)log(64/57)+2539/77658 < 0.
```

Thus the exact cutoff is 658. Thirteen profiles exceed it. Their
cap/profile/odd-count ledger is

```text
1592 (4,6)        4       1456 (7,3,1)      8
1456 (0,7)        0       1344 (10,0,2)    12
1316 (3,4,1)      4       1208 (12,0,0,1)  12
1200 (6,1,2)      8       1088 (2,2,2)      4
1056 (8,1,0,1)    8        936 (4,2,0,1)    4
 908 (1,0,3)      4        848 (0,3,0,1)    0
 764 (3,0,1,1)    4.
```

## Parity and light supports

The signed-chord identity is

```text
28=102-D_64+2C.                                      (3)
```

Hence `D_64` is even. Heavy-heavy and heavy-light diameter edges contribute
16 and 4, so the number `d_1` of light-light diameter edges is even. Four
light vertices allow only `d_1=0` or `d_1=2`.

If `d_1=2`, the light support is two antipodal pairs. Its other four chords
form two doubled folded classes, so it contributes no odd class. If `d_1=0`,
the six non-diameter light chords generate every odd class modulo two; the
complete light-support ledger has only 2, 4, or 6 odd classes. Therefore a
surviving profile has 0, 2, 4, or 6 odd classes. Deleting the ledger entries
with 8 or 12 odd classes leaves exactly (1), and none has 2 or 6.

The two-diameter supports are exactly `{0,a,64,a+64}` for `1<=a<=63`.
Canonicalization under translation and odd units leaves the six representatives
with `a in {1,2,4,8,16,32}`. For the four-odd branch, the independently proved
atlas has 28,800 normalized supports in exactly 148 affine orbits; every orbit
has the repeated-wedge geometry. This gives the complete 154-template router.

Finally, direct matching enumeration with `d_1=0` or `d_1=2` gives the two
sets of square masses in (2). Substitution in (3) gives the collision sums.
QED.
