# KoalaBear m4 A6 (5,4,2) pair-quotient normal form

- **status:** PROVED
- **scope:** rigid passport `A6: 5.1,2.2.1.1,4.2`
- **dependency:** `rate_half_kb_m4_a6s6_genus_zero_passport_reduction`
- **consumer:** `rate_half_band_closure`

Work over `E=Q(nu)`, where `nu^2-nu+4=0`. Put

```text
L =26828299u-7525603+3231308nu,
A2=63975032888671u^2+(-824138157082+7855063570280nu)u
   +245313368811+2125523128760nu,

P1=9994287u-315829-714826nu,
P2=1991382275400503u^2+(-417059633688806-83725261001260nu)u
   +132674139060063+26804277479260nu,
Q2=1132252914780903u^2+(-462396480179036+244927114639150nu)u
   +12231162711693-32963869775350nu,
Q4=89003185037860639199185563123u^4
   +(-126036323962081416795984038348
     +58730298647562103476728792872nu)u^3
   +(-11490078199717284397847774254
     -48409713450897291507014287016nu)u^2
   +(29110362047987136464064202740
     +305715256120089609322000856nu)u
   -1822586629728176676821274861
   +1518418512706836664928299688nu.
```

For the exact nonzero scalar `c` printed in the certificate, the rigid
degree-15 outer cover is

```text
T(u)=c L(u)^5 A2(u)^5/(P1(u)P2(u)Q2(u)^2Q4(u)^2).   (KBM4-A1)
```

Up to a nonzero scalar in `E`, its numerator minus denominator is

```text
R1 R2^2 S1^4 S2^4,                                  (KBM4-A2)

R1=80312277u-15954935+15312886nu,
R2=33120709u-7890011+5302214nu,
S1=875841u-133093+97604nu,
S2=360429781037043u^2+(-142615106443814+55888632283576nu)u
   +41237398279331-13362808229176nu.
```

The fibers over `0,1,infinity` have profiles

```text
(5,5,5),       (4,4,4,2,1),       (2,2,2,2,2,2,1,1,1).
```

This is the unordered-pair quotient of BelyiDB's degree-six companion
`6T15-[5,4,2]-51-42-2211-g0`.

For `K=F_(2130706433^6)`, both roots of `nu^2-nu+4` already lie in the base
field. Under both embeddings, `A2` remains a separable quadratic and is
coprime to `L`. Hence all three order-five points lie in `F_(p^2)`, and thus
in `K`. After replacing `T` by `1/T`, the required three-point pole divisor
splits over the challenge field.

## Falsifier

A failure of the pinned source factorization, pair-remainder determinant,
adjoint moving-factor derivation, identities `(KBM4-A1)`--`(KBM4-A2)`,
factor coprimality, branch profile, or either-embedding field descent.
