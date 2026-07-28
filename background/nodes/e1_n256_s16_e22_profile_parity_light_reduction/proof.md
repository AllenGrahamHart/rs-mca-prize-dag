# Proof

The general chord inequality gives `L<=22`.  Put `Delta=22+66-4L`.  The
proved relaxed slack recurrence gives

```text
L       22  21  20  19  18  17  16  15  14
Delta    0   4   8  12  16  20  24  28  32
min E   54  50  46  42  38  34  30  26  22.
```

Thus `L<=14`.  Exact enumeration of `sum j^2 n_j=22` and
`sum j n_j<=14` gives the following profile/odd-count pairs:

```text
(6,4) 6; (9,1,1) 10; (2,5) 2; (5,2,1) 6; (1,3,1) 2;
(4,0,2) 6; (0,1,2) 2; (6,0,0,1) 6; (2,1,0,1) 2.
```

The signed-chord identity is

```text
22=102-D_64+2C.
```

Hence `D_64` is even.  Diameter edges form a matching, so the four light
vertices have zero or two light-light diameters.  Two diameters make the light
support two antipodal pairs and produce zero odd classes.  With no light
diameter, the six light-light edges generate every odd autocorrelation class
modulo two, so there are at most six.  Therefore `(9,1,1)` is impossible;
every surviving profile has zero light-light diameters.  The exact diameter
ledger is

```text
d_1=0: (D_64,C)=(0,-40),(4,-38),(8,-36),(12,-34),(16,-32),(20,-30);
d_1=2: (D_64,C)=(2,-39),(18,-31).
```

The proved exhaustive even-parity atlases contain exactly 8,168 normalized
two-odd supports in 87 affine orbits and 280,720 normalized six-odd supports
in 1,234 affine orbits.  Every template leaves `binom(124,3)` heavy supports
and 64 relative signs, yielding the printed floor.  The source-pinned Modal
derivation and a separately structured checker agree on every slack value,
profile, diameter ledger, atlas count, and route total.
