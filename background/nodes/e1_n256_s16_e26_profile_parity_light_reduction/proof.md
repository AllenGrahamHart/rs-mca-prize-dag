# Proof

## Slack and profiles

The general chord inequality gives `L<=floor((26+66)/4)=23`. Put
`Delta=26+66-4L`. The proved relaxed slack recurrence gives

```text
L       23  22  21  20  19  18  17  16
Delta    0   4   8  12  16  20  24  28
min E   54  50  46  42  38  34  30  26.
```

Therefore `L<=16`. Exact enumeration of

```text
sum_j j^2 n_j=26,       sum_j j n_j<=16
```

gives 13 profiles. For the rational cubic Hermite majorant with double
contacts 14 and 57, the raw moments at `V=52` are

```text
(1,16,308,6592+M_3).
```

Exact substitution at the sign boundary gives

```text
M_3=228: (73379/79507, 6128/79507, -9755/245917),
M_3=229: (73381/79507, 6126/79507, -58459/1475502).
```

Eight-term rational atanh bounds certify opposite signs at 228 and 229, so
the exact cutoff is 228. All 13 profiles exceed it. Their
cap/profile/odd-count ledger is

```text
1452 (6,5)        6       1328 (9,2,1)     10
1308 (2,6)        2       1180 (5,3,1)      6
1076 (8,0,2)     10       1064 (1,4,1)      2
 956 (4,1,2)      6        948 (10,0,0,1)  10
 868 (0,2,2)      2        820 (6,1,0,1)    6
 724 (2,2,0,1)    2        584 (1,0,1,1)    2
 308 (1,0,0,0,1)  2.
```

## Parity, diameter, and route size

The signed-chord identity is

```text
26=102-D_64+2C.                                      (2)
```

Thus `D_64` is even. Diameter edges form a matching, so the four light
vertices contain zero or two light-light diameters. Two diameters make the
light support a union of two antipodal pairs, so every remaining light chord
is doubled and there are zero odd classes. This matches no surviving profile.
With zero light diameters, the six light-light chords generate every odd
autocorrelation class modulo two, so at most six odd classes are possible. This removes the
three ten-odd profiles and leaves exactly (1).

The proved light-support atlases are exhaustive: 8,168 normalized two-odd
supports in 87 affine odd-unit orbits and 280,720 normalized six-odd supports
in 1,234 such orbits. An independent orbit expansion rechecks both atlases.
Each template has `binom(124,3)` heavy supports and 64 relative sign vectors,
giving the direct-census floor in the statement. QED.
