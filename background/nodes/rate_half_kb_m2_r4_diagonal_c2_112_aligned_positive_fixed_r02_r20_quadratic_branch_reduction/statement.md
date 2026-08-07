# KoalaBear fixed R02/R20 generic route reduction

- **status:** PROVED structural reduction
- **representatives:** `{F04,F05} x {R02,R20}`
- **chart:** `V!=0`
- **nonclaim:** no literal cell is proved empty here

After exact reconstruction `w=-U/V` and transported-unit cancellation, the
generic resultant has exactly three retained factors, of degrees `3,3,12`.
For every representative one cubic branch is empty, the other survives as a
dimension-one named-open curve, and the degree-12 branch reaches its bounded
420-second basis cap.

For `F04`, coefficient 0 of the full `J` quotient mismatch is compiled by
truncated convolution rather than full product expansion. After exact source
named cancellation and symmetric descent it factors as

```text
w^4 * J8a^2 * J8b^2 * J11 * J12.               (KBGR-1)
```

On both surviving cubic curves, the intersections with `J8a`, `J8b`, and
`J12` are empty after transported localization. The `J11` intersection
survives. Coefficient 1 has one nonunit degree-70 factor with 182,336 terms;
the coefficient-0 full-`I` truncated product reaches the memory/time fence.
