# WCL `(1,6)` unsigned sign-product router pilot

- **consumer:** `dli_wcl_slot_1_6_emptiness`
- **purpose:** count the exact affine-Galois quotient after aggregating all 32
  sign lifts of a six-subset of `mu_256`
- **status effect:** route selection only

For six distinct squared roots `y_i` choose square roots `r_i` and put

```text
Psi_6(y_1,...,y_6)
  = product_(s_2,...,s_6 in {+1,-1})
      (r_1+s_2r_2+...+s_6r_6).
```

Changing a chosen square root permutes the factors, so `Psi_6` is a symmetric
integer polynomial in the `y_i`. In odd characteristic it vanishes exactly
when one of the 32 reduced sign lifts sums to zero.

The computation will count six-subset orbits of `Z/256` under
`x -> ax+b`, with `a` odd, by exact Burnside enumeration. It will separately
track the parity of the exponent sum; this parity is invariant because the
subset size is six. The two sectors are the precise obstruction to a single
sixth-root product normalization.

## Predictions and stopping rule

1. The total fixed-point sum is divisible by `256*128`.
2. Each parity-sector sum is separately divisible by the group order.
3. The quotient is materially below `185,569,028`, but no target is promoted.

One Modal container, one CPU, 512 MiB, and a 60-second cap. No support list,
norm, or factorization is generated. A successful exact count authorizes a
proof node for the router; a timeout ends this implementation without retry.

## Result

Modal app `ap-lVlwqd9Jq78L9k2fCosqa3` completed in 1.173965 seconds. The
two orbit counts are `6,025,357` and `5,624,703`, totaling `11,650,060`.
The exact fixed-point sums are `197,438,898,176` and `184,310,267,904`;
both divide by the group order `32,768`. The successful branch promotes only
the router theorem, not the slot.
