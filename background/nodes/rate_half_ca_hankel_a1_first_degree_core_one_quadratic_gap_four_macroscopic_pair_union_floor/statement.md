# `A=1` quadratic gap-four macroscopic pair-union floor

- **status:** PROVED
- **closure:** every pair union jumps from `rho+4` to `3rho/2-1`
- **consumer:** `rate_half_band_crossing_location`

Retain either core-one quadratic `u=4` arm. Put

```text
j_0=rho/2-1=(3e-3)/2.                                (MPF1)
```

Then every two distinct supported slopes satisfy

```text
|S_alpha union S_beta|>=rho+j_0=3rho/2-1.           (MPF2)
```

For the official row this is

```text
rho=549755813888,
j_0=274877906943,
|S_alpha union S_beta|>=824633720831.               (MPF3)
```

If an affine codeword line contains assigned centers at a supported-slope
set `A` of size `h>=2`, then

```text
j_0 h+sum_(gamma in A)r_gamma
 <=rho+j_0-1=3rho/2-2.                              (MPF4)
```

In particular,

```text
h<=3,
h=3  =>  sum_(gamma in A)r_gamma<=1.                (MPF5)
```

For every fixed pair `alpha,beta`, at least `rho+1` other supported slopes
`gamma` have

```text
|E_alpha union E_beta union E_gamma|>=2rho+1.       (MPF6)
```

## Scope

The theorem uses only the exact support design and minimum-distance center
geometry after the quadratic profile has been reached. It does not exclude
either root pattern or determine the adjacent crossing.
