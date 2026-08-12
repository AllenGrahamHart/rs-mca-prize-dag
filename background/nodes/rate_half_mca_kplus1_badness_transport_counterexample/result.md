# Result

The shared K-adapter probe returns an exact counterexample:

```text
actual code dimension k:       slope 0 is MCA-bad on S
substituted dimension k+1:     slope 0 is pair-contained on S
cause:                         X^k enters the enlarged code
verdict on silent transport:   REFUTED
verdict on guarded adapter:    OPEN
```

The source-dimension bridge remains possible only if it carries the original
degree-`<k` guard and rechecks badness on the identical support.
