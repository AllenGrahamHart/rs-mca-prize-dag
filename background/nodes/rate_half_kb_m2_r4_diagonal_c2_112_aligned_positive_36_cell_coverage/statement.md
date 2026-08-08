# KoalaBear aligned-positive 36-cell coverage

- **status:** PROVED
- **scope:** every literal aligned-positive unramified `c2(1,1,2)` cell
- **field:** `F_(2130706433^6)`
- **consumer:** source-line literal-assignment coverage

The literal registry consists of twelve source assignments and three residual
root distributions. Every one of the resulting 36 named-open systems is
empty:

```text
F00,F01,F02,F03,F04,F05,F06,F07 x R02,R11,R20
M00,M01,M02,M03                 x R02,R11,R20.
```

This is a census theorem assembled from seven proved, disjoint packets. It
does not classify aligned-negative, near-aligned, ramified, or boundary
source-line assignments outside this registry.

## Falsifier

A duplicate or missing literal cell, a non-PROVED supplier, a cell conclusion
that omits its complete named open or full quotient gates, or any surviving
point in one of the 36 systems.
