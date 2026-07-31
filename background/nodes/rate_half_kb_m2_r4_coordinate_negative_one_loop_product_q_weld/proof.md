# Proof

The complete-fiber compiler gives a nonconstant Mobius product map
`p=N/D`.  Put

```text
Delta=N_1D_0-N_0D_1 !=0.
```

For distinct labels `r,s`, direct subtraction gives

```text
p_r-p_s=Delta(r-s)/(D(r)D(s)).                         (1)
```

The loop-stratified compiler writes

```text
A_1(W)=(W-h)C(W),       deg C<=1,
(s-h)C(s)+q_sD(s)=0                                    (2)
```

at every nonloop.  Combining `(1)` at `(h,s)` with `(2)` yields

```text
q_s/(p_h-p_s)=D(h)C(s)/Delta.                         (3)
```

The right side is linear in `s`, proving the rank bound `(KBN1W-3)`.
Expanding a `3 x 3` determinant and multiplying by
`d_i d_j d_k` gives exactly `(KBN1W-4)`.

Conversely, choose two nonloop labels `i_0,i_1`.  Their distinct first two
coordinates determine a unique affine-linear function `L`.  The two welds
with the remaining labels say that every `w_s` equals `L(s)`.  Set

```text
C=Delta L/D(h).
```

Equation `(3)` then reverses to every nonloop equation in `(2)`.  At the
loop, both `q_h` and `W-h` vanish, so its sum equation holds automatically.
This reconstructs all five common-`K` sum rows. QED.
