# Result

Primitive odd swap pairs satisfy the exact necessary norm inequality

```text
m^(h-1)<h^(m/4).
```

For `h=m/4-d`, the simpler band `s(d+1)<=m/2`, `m=2^s`, is therefore
swap-empty. At `m=2^41` this removes the swap class for
`1<=d<=26,817,356,774`.

The narrower cyclotomic-Haar band already routes every pair to the swap
class. It is consequently completely empty at every width, not merely empty
on even widths. At the top official level this gives full emptiness for
`1<=d<=9223`; the simpler constant-`64` sub-band reaches `d=6521`.

This theorem alone leaves only the free class between the Haar and swap
cutoffs. The downstream Vandermonde-defect theorem deletes a much larger
initial part of that region. Between its cutoff and the swap cutoff only the
free class remains; below the swap cutoff both classes remain open.
