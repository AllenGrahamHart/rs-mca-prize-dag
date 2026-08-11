# `A=1` core-one quadratic gap-four two-slope coefficient-rank spread

- **status:** PROVED
- **closure:** pair-union floor `rho+2` and half-size center-line cap
- **consumer:** `rate_half_band_crossing_location`

Retain either root pattern of the core-one scalar quadratic packet at
`u=4`. Let `S_gamma` be the exact support of the unique error at a supported
slope and let `r_gamma` be its residual rank loss, so

```text
|S_gamma|=rho-r_gamma.                              (QRS1)
```

In the double-root arm `r_gamma` is the indicator of the padded root `x_*`.
In the two-simple arm it is the number of padded roots among `x_1,x_2`.
The fixed core point `s_0` belongs to every `S_gamma`.

Write the residual primitive kernel as

```text
Qbar(U,V;X)=sum_(i=0)^e Q_i(X)U^(e-i)V^i.           (QRS2)
```

For distinct supported slopes put

```text
X_(alpha,beta)=S_beta\S_alpha,
j_(alpha,beta)=|S_alpha union S_beta|-rho.           (QRS3)
```

Then

```text
j_(alpha,beta)>=2,                                  (QRS4)

rank (Q_i(x))_(x in X_(alpha,beta),0<=i<=e)
 <=j_(alpha,beta)-1.                                (QRS5)
```

In particular,

```text
|S_alpha union S_beta|>=rho+2                       (QRS6)
```

for every pair. At equality in `(QRS6)`, all `r_alpha+2` nonzero residual
row forms `Qbar(-;x)` on `S_beta\S_alpha` are proportional.

If an affine codeword line contains assigned centers at a slope set `A` of
size `h>=2`, then

```text
2h<=rho+2-sum_(gamma in A)r_gamma.                  (QRS7)
```

Consequently, for any two supported slopes `alpha,beta`, at least

```text
ceil((rho+6+r_alpha+r_beta)/2)                       (QRS8)
```

other supported slopes `gamma` satisfy

```text
|E_alpha union E_beta union E_gamma|>=2rho+1,       (QRS9)
```

where `E_gamma` is the full padded degree-`rho` locator root set.

## Scope

The theorem does not exclude either quadratic packet or prove point
separation for the residual coefficient map. It supersedes the weaker
`rho+1` joint-support input in the earlier center-line caps. The abstract
cyclic design in Cycle 107 was checked only against the old three-expander
condition and therefore does not fence `(QRS8)`.
