# Proof

## Slack and profiles

The general chord inequality gives `L<=floor((24+66)/4)=22`.  Put
`Delta=24+66-4L`.  The proved relaxed slack recurrence gives

```text
L       22  21  20  19  18  17  16  15  14
Delta    2   6  10  14  18  22  26  30  34
min E   56  52  48  44  40  36  32  28  24.
```

Thus `L<=14`.  Exact enumeration of

```text
sum_j j^2 n_j=24,       sum_j j n_j<=14
```

gives the following nine profile/odd-count pairs:

```text
(4,5) 4; (7,2,1) 8; (0,6) 0; (3,3,1) 4; (6,0,2) 8;
(2,1,2) 4; (8,0,0,1) 8; (4,1,0,1) 4; (0,2,0,1) 0.
```

The fixed cubic-Hermite majorant is deliberately absent: the proved route
boundary says its optimistic margin is negative already at `M_3=0` here.

## Parity and atlas

The signed-chord identity is

```text
24=102-D_64+2C.
```

Hence `D_64` is even.  Diameter edges form a matching, so the four light
vertices have zero or two light-light diameters.  Two diameters make the light
support two antipodal pairs, leaving zero odd classes.  With no light
diameter, the six light-light edges generate every odd autocorrelation class
modulo two, so there are at most six.  Therefore none of the three eight-odd
profiles can occur.

The previously proved exhaustive even-parity atlases contain exactly 63
normalized zero-odd supports in 6 affine orbits and 28,800 normalized four-odd
supports in 148 affine orbits.  The former all have two diameters and the
latter none.  Each template leaves `binom(124,3)` heavy supports and 64
relative sign vectors, giving the printed router floor.  The Modal derivation
and a separately structured exact checker agree on every slack value,
profile, atlas count, and route total.
