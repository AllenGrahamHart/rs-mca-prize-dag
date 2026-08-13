# Mersenne core-dichotomy capped-charge payment

- **status:** PROVED
- **scope:** Mersenne-31 full-lift supports `130222<=e<=130225`
- **adjacent route wall:** `e=130226`

Fix the weighted-prefix absorption cutoff

```text
b_abs=65450.
```

For any line selected by the recursive exact-layer bank, let `g` be its
actual total core.  If

```text
g>=e+10-b_abs,
```

then every explanation of deficit at least `b_abs+1` lies on that line;
the low explanations are bounded by the exact weighted prefix through
`b_abs`.  Otherwise every selected line has

```text
g<=G_e:=e+9-b_abs.
```

In the second branch, maximize the lower-aware joint charge subject also to
the individual cap `G_e`.  This exhaustive dichotomy proves all four printed
supports.  The first two terminate after 14 lines and the last two after 70
lines.  At `e=130226`, the initial forced threshold is only 14 and has zero
forced core; the capped compiler eventually reaches threshold one without a
packing contradiction.  No unsafe conclusion is claimed there.
