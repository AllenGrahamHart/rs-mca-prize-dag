# proof: aqb_deficit_arithmetic

The deficit is affine increasing in `Q`:

```text
B_I(Q) = d Q - 40 - log2 C(2^40, 2^39 + d),
```

with `d > 0`. Hence the worst admissible value is `Q = 256`.

The script

```bash
python3 nodes/aqb_averaged_quotient_box/verify.py
```

certifies the binomial term with Robbins Stirling bounds:

```text
log(n!) in [(n+1/2)log n - n + (1/2)log(2pi) + 1/(12n+1),
            (n+1/2)log n - n + (1/2)log(2pi) + 1/(12n)]
```

applied to `n = 2^40`, `m = 2^39 + d`, and `n-m`.

The resulting certified interval is:

```text
B_I(256) in
[429645546.773407953684577335517,
 429645546.773407953684577335517]
```

with interval width below `1e-24` bits. Therefore

```text
429,645,547 - B_I(256) > 0.2265 bits.
```

Thus the claimed `429,645,547`-bit AQB gain clears the finite deficit. The same
run gives

```text
Qcrit in [255.900000020976959686266378250,
          255.900000020976959686266378250],
```

matching the recorded threshold.
