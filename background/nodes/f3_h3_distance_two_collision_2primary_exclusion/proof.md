# Proof

A half-basis coefficient vector of squared norm two has exactly two nonzero
coordinates, each equal to `1` or `-1`. Hence

```text
beta_E-beta_F = u zeta^a (1 +/- zeta^d)              (1)
```

for a sign unit `u`, distinct half-basis coordinates, and some `d mod n`.
Replace the plus sign, when present, by

```text
1+zeta^d=1-zeta^(d+n/2).
```

The resulting exponent is nonzero modulo `n`; otherwise `(1)` would vanish,
contrary to the proved shifted-product Sidon theorem. If `zeta^e` has order
`2^r`, then

```text
|Norm_Q(zeta_n)/Q(1-zeta^e)|
  = Phi_(2^r)(1)^[Q(zeta_n):Q(zeta_(2^r))]
  = 2^[Q(zeta_n):Q(zeta_(2^r))].                    (2)
```

The monomial and sign in `(1)` have absolute norm one. Equation `(2)` proves
that the collision norm is a power of two. An odd row prime dividing every
same-fiber collision norm therefore cannot support a distance-two pair.

For the packing refinement, take the seven distinct vectors of squared norm
at most three from the rich-fiber norm-cutoff proof. Let `e` count distances
at most six. Distance two is now impossible, so every counted distance is at
least four; every uncounted even distance is at least eight. The centroid
identity gives

```text
4e+8(21-e)
  <= sum_(i<j)||v_i-v_j||_2^2
  <= 7*21=147.
```

Thus `168-4e<=147`, so `e>=6`. QED.
