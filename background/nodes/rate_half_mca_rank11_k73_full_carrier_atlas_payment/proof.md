# Proof

Use the exact cap system and dominance pruning already proved through
`K'=72`. The support-two/support-three position partition removes 1,024
impossible pairs and leaves 711 maximal ordinary vectors, together with the
full-completion carrier lanes recorded in the source contract.

The conservative replay covers 8,551,382 leaves. Exactly 218 distinct
support-two through support-five defect tuples have conservative premium
strictly above the exact safe ceiling. The largest conservative leaf already
below the ceiling is

```text
s2=41/s3=33/s4=33/s5=31/c6F/c7F/c8F/c9F/carrier32_plain,
```

with premium `(P73)` and margin `(M73)`.

For each of the 218 exceptional tuples, apply the exhaustive pairwise
carrier atlas at supports three, four, and five. Intersect every resulting
fixed-union charge with all exact same-support and cross-support caps. When
the fixed-union dimension is at least five, replace the separable support-4
and support-5 contribution by the proved joint flat-coupled charge. The
71,806 resulting exact evaluations are all safe. Their maximum is

```text
32133901221158725309935103349312670983455197672,
```

below the ceiling by
`8990475147539268350610906904422534588669227930`.

The branches routed before the conservative filter are replayed in seven
disjoint geometry lanes. Their exact evaluation counts sum to 118,892,669.
The largest geometry premium is the one-step value

```text
35688968442860327556985962346044983398767741600,
```

below the ceiling by
`5435407925837666103560047907690222173356684002`.
All other geometry maxima are smaller. Therefore the global premium is the
already-safe conservative leaf `(P73)`.

Let `R` be the unchanged record floor, `G` the rank-nine marks, and `Kern`
the inherited kernel capacity. Exact integral arithmetic gives

```text
Cap_full=floor((G+R P_73)/55),
Cap_total=Kern+Cap_full,
Demand=R C(67545,11)-C(1048649,11).
```

Substitution gives `(G73)`, so demand exceeds complete capacity and the row
closes. QED.
