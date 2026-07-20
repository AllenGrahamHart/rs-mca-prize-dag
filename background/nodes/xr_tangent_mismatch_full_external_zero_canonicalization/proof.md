# Proof

Let `W=S_z\T`. The witness equation and vanishing of the recovered-pair
errors outside `T` give `W subseteq Z_z`. The nonzero polynomial `q_z` has
degree below `K`, so `d_z<=K-1` and the locator of its full external zero set
divides it.

Let

```text
I_z={x in T:q_z(x)=e_0(x)+z e_1(x)}.
```

The internal part of the selected witness lies in `I_z`, hence

```text
|I_z| >= |S_z intersect T|
      = A-|W|
      >= A-d_z.
```

Division by the full locator is valid on `T` and converts these equalities
to agreement with a degree-below-`K-d_z` polynomial. Subtracting the new
dimension from the guaranteed agreement gives `A-K`.

The selected witness/codeword pair is chosen once per slope by a fixed total
order on the finite witness set. Therefore the resulting `Z_z` is a function
of the slope under that first-match convention. No summation or count over
the possible values of `Z_z` is asserted.
