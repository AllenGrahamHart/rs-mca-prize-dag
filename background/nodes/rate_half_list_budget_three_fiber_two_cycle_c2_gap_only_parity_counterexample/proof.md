# Proof

For `E=sum_(j=0)^4 E_jz^j`, `E_0=1`, the coefficients of `E^(-1/4)` obey

```text
4n a_n=-sum_(j=1)^min(4,n)(4n-3j)E_j a_(n-j).       (1)
```

Every denominator `4n` used below is invertible in `F_53`. Iterating `(1)`
through degree 23 gives

```text
(a_0,...,a_23)=
(1,13,9,6,14,27,50,39,27,20,16,11,
 19,0,0,0,2,9,22,23,46,31,11,11).                  (2)
```

The entries at indices 14, 15, and 16 prove `(GPC2)`. The two windows from
`(2)` are

```text
L=(1,13,9,6,14,27,50,39),
T=(2,9,22,23,46,31,11,11).                          (3)
```

Their normalized truncated product is

```text
LT/2 mod z^8=(1,44,52,42,21,44,40,43).              (4)
```

Direct squaring of the polynomial in `(GPC3)` gives the same eight
coefficients. Its coefficients in degrees five, six, and seven are zero, so
in particular it satisfies the required degree bound `deg C<=H-3=5`.

Substitution shows that `2,24,46,48` are the four roots of `E` in `F_53`.
They are distinct, so `E` is split and squarefree. None is the negative of
another member of the set, proving that the root set is not two-antipodal.
The nonzero odd coefficients `E_1=1` and `E_3=34` give the same conclusion.

Finally, repeated multiplication gives respective root orders
`52,13,13,52`. Euler's criterion gives nonsquare, square, square, nonsquare.
Thus neither the order-56 torsion condition nor the common square class
required by the official normalization holds. This isolates exactly why the
example refutes gap-only parity forcing without touching the official
torsion-and-square statement. QED.
