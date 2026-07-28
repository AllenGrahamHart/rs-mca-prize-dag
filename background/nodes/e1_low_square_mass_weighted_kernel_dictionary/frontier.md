# Frontier

For the binding prize rate-`1/8` row, the exact target is now

```text
(1/2) sum_{d in D_p(33)} M_33(a(d),b(d))
    <= 65127585921474870475467050631501738502567.
```

A deliberately coarser sufficient statement is now

```text
|D_p(33)| <= 69541.
```

Here vectors are oriented and not orbit-normalized. The prize field floor
removes all four `S=16` profiles; the maximum live weight now comes from the
`(4,2,S=18)` profile. Existing profile exclusions should be imported as zero
contributions, then every surviving orbit should be charged by its exact
size, stabilizer, and `M_33(a,b)` weight.

The weighted route may close even when there are more than 69,541 vectors,
because multiplicities fall sharply away from `(4,2,18)` among the live
profiles. Do not replace the weighted target by a complete enumeration unless
the latter is demonstrably cheaper.
