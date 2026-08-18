# C2 first depth-two CRT falsifier: report

## Verdict

The first exact row with a genuine tail survives the preregistered
square-root falsifier:

```text
(n,t,q) = (64,4,193),
log2 J_prim = 3.6594639436676833741082921356213505185771e-7,
log2 sqrt(2n) = 3.5.
```

Thus `J_prim` is strictly above one, but the candidate retains
`3.4999996340` bits of slack.

## Exact factor balance

The proved support-overlap factorization separates the result into

```text
log2 K_0^prim = -0.0000049382958030039211597098455567791399,
log2 K_tail   =  0.0000053042421973706894971206747703412749,
log2 J_prim   =  0.0000003659463943667683374108292135621351.
```

The primitive first junction contracts, the unreduced tail expands by a
slightly larger amount, and their exact product lands extremely close to
one. This is direct evidence that separate one-sided estimates on the two
factors discard the relevant cancellation.

## Exact counts

```text
Z_0 = 13295206688
C_1 = 116512
Z_1 = 495229865162016
Z_2 = 95579012297974912
B_0 = 495228544669824
B_1 = 95578985107762144
```

`Z_0-C_1=13295090176` is positive and divisible by `64`.

## Method and controls

A first-nonzero-coefficient gauge reduced the four-dimensional Fourier sum
to `21,791,257` normalized tuples. Three 60-bit modular shards returned the
same literal counts because every value is already below one modulus. The
analyzer nevertheless reconstructs from two moduli and checks the third
independently. The same executable reproduces the frozen `(32,2,97)` control
exactly. All tasks returned in at most `10.219` seconds.

## Interpretation

This row is the first direct test of depth transport rather than scale. It
does not prove the square-root candidate and does not justify monotonicity in
`m`, `n/t`, or `q`. It does show that the tail can reverse first-junction
contraction while leaving the full ratio close to one. More isolated toy
rows are now lower value than an analytic theorem coupling those factors.

## Replay

```text
tools/ramguard modal -- modal run notes/pilots_20260818/c2_first_depth2_crt/modal_run.py --output notes/pilots_20260818/c2_first_depth2_crt/results.json
tools/ramguard tiny -- python3 notes/pilots_20260818/c2_first_depth2_crt/analyze.py
tools/ramguard tiny -- python3 notes/pilots_20260818/c2_first_depth2_crt/analyze.py --tamper-selftest
```

Modal run: `ap-Xv3PG5iFZZ94Z09Qedpmko`. Frozen SHA-256 values:

```text
preregistration  676f96c1b59d1e4a9e3ad813383c0e993cc83af73db12e5a3eb598aeeef1bbc3
executed C++     2f24a4bf408429156ea80a6f56c790d726e5a3851cc4f95544da3d1f8fc75258
launcher         d1622b2ba064252b6e82c7616dae7a9d25d516bc88c206f1a45d8dacb5755ace
results          bf9593294593327ebdb186d7575a1fdf0bbb6c74d7296c3a52d384b3519f9e91
```

