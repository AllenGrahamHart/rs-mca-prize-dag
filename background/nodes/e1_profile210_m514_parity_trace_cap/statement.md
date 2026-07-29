# E1 profile-(2,10) cofactor-514 parity and trace cap

- **status:** PROVED
- **closure:** local parity multiplicity and distinct-conjugate trace bound
- **scope:** binding prize rate-`1/8` row, profile `(2,10,S=18)`, cofactor `514`

Two of the 17 autocorrelation magnitude profiles surviving the middle-shape
router are impossible:

```text
E=8:  (n_1,n_2,n_3)=(0,2,0),
E=13: (n_1,n_2,n_3)=(13,0,0).
```

The energy-eight profile has identically zero parity autocorrelation, which
contradicts local multiplicity two. In the energy-thirteen profile, every
conjugate deviation is a signed sum of 13 distinct folded traces. Their
maximum is strictly below `2551/100`; this sharpened logarithm majorant forces

```text
Norm(F(zeta_256))<514*p_min.
```

Exactly 15 magnitude profiles remain in the cofactor-`514` branch, and no
energy-thirteen profile remains.
