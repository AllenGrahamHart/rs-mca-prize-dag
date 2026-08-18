# Proof

The verifier exhausts all `2^16` binary words over the printed order-16
domain and independently evaluates every listed Fourier coefficient. It
certifies the two marginal counts and the `20=4+16` joint owner split in
`(SH1)`. Substitution gives `8192/485`, and exact squaring proves it exceeds
`sqrt(32)`.

For `(SH2)`, first consider one order-16 local block. The same exhaustive
certificate gives

```text
|E_{1}|=3856,       |E_{2,6}|=1296,       |E_4|=5124,
|E_{1,2,4,6}|=20,   |Owner intersect E_{1,2,4,6}|=4.     (1)
```

Now write each global index as `i=s+ra`, with `0<=s<r`, `0<=a<16`.
Fourier inversion over the complete residues `f_0+16l`, `0<=l<r`, localizes
each global event to the corresponding order-16 equation at every `s`.
The `r` local blocks are independent, so the three marginals have counts

```text
3856^r,       1296^r,       5124^r,
```

the joint has count `20^r`, and its antipodally invariant owner has count
`4^r`. The binary sample space has size `2^(16r)`. Thus the primitive
joint-to-product ratio is

```text
(20^r-4^r) 2^(32r)/(3856*1296*5124)^r
 = [20*2^32/(3856*1296*5124)]^r (1-5^(-r)),
```

which is `(SH2)` after reducing the bracket.

The required fields exist for every power-of-two `r=2^d`: 2-adic LTE gives

```text
v_2(17^r-1)=d+4,
```

so `16r` divides `17^r-1`. The `r`th-power map from the order-`16r` roots
onto the order-16 roots lets us choose the global root with `r`th power `3`.

At `r=2`, direct rational substitution gives the printed fraction, whose
square exceeds `64`. QED.
