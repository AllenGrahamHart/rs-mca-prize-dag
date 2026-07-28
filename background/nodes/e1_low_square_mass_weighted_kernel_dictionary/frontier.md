# Frontier

For the binding prize rate-`1/8` row, the exact target is now

```text
(1/2) sum_{d in D_p(33)} M_33(a(d),b(d))
    <= 62622678770648913918718317914905517790930.
```

A deliberately coarser sufficient statement is now

```text
|D_p(33)| <= 66866.
```

Here vectors are oriented and not orbit-normalized. The prize field floor
removes all four `S=16` profiles; the maximum live weight now comes from the
`(4,2,S=18)` profile. Existing profile exclusions should be imported as zero
contributions, then every surviving orbit should be charged by its exact
size, stabilizer, and `M_33(a,b)` weight.

The weighted route may close even when there are more than 66,866 vectors,
because multiplicities fall sharply away from `(4,2,18)` among the live
profiles. Do not replace the weighted target by a complete enumeration unless
the latter is demonstrably cheaper.
