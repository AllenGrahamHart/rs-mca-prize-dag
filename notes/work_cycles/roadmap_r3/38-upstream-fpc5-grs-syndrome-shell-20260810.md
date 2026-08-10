### 2026-08-10 upstream FPC5 GRS syndrome-shell import

Przemek's proved syndrome-catalecticant-shell theorem now has an exact FPC5
specialization in the critical support chain. If a rational Hankel chart has
locator degree `d` and `c` rows, put `D=d+c`. Its primitive core-split
locators are canonically the weight-`d` vectors in one syndrome fiber of the
`D`-row weighted Vandermonde parity check on the `N` core points.

For `D<N`, the local object is therefore the exact radius-`d` shell of

```text
RS[F,Core,N-D].
```

For `D>=N`, the check is injective and the fixed chart has at most one
primitive locator. The MDS distance also gives support overlap at most
`d-c-1`; in a fixed-background chart this is the already sharp `d-ell` cap.

This is a useful route pin, not a critical closure. Below the injective range,
the generic split-support count is literally an ordinary RS list-size
problem, so invoking an unproved max-to-mean statement under Hankel language
would be circular. The remaining possible extra saving lies in the FPC5
background/chronology filters or in a LIST theorem strong enough for this
derived parameter family. Required-background coalescence also remains open.
