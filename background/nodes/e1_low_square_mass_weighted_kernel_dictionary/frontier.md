# Frontier

For the binding prize rate-`1/8` row, the exact target is now

```text
(1/2) sum_{d in D_p(33)} M_33(a(d),b(d))
    <= 62622678770648913918718317914905517790930.
```

A deliberately coarser sufficient statement is

```text
|D_p(33)| <= 27520.
```

Here vectors are oriented and not orbit-normalized. The maximum weight comes
from the still-open `(3,4,S=16)` profile. Existing profile exclusions should
therefore be imported as zero contributions, then every surviving orbit
should be charged by its exact size, stabilizer, and `M_33(a,b)` weight.

The weighted route may close even when there are more than 27,520 vectors,
because multiplicities fall sharply away from `(3,4,16)`. Do not replace the
weighted target by a complete enumeration unless the latter is demonstrably
cheaper.
