# Proof

The quotient-generated field `B=F_p(Q)` is a finite subfield of `F=F_q`.
Hence there is an integer extension degree `d=[F:B]>=1` with

```text
q=b^d.
```

If `B` is proper, then `d>=2`, so `b^2<=q`. The official field cap is strict:

```text
q<2^256.
```

Therefore

```text
b^2<2^256,
b<2^128.
```

The exact E1 allowance compiler prints six pair-feasibility thresholds with
bit lengths

```text
188,134,170,188,134,170.
```

In particular, every threshold is greater than `2^128`. Thus a proper
subfield has `b<b_pair_min` and cannot satisfy the pair-feasible premise.
Consequently every pair-feasible row has extension degree one and `B=F`.
