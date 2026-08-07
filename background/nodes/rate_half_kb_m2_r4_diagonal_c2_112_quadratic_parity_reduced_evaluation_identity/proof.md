# Proof

For an even index `i=2j`, the corresponding direct term differs from the
claimed term by

```text
a_(2j) V^(d-2j) ((U^2)^j - (VZ)^j).
```

The difference of powers is divisible by `U^2-VZ` through

```text
X^j-Y^j = (X-Y) sum_(r=0)^(j-1) X^(j-1-r)Y^r.
```

For an odd index `i=2j+1`, factor `-U V^(d-2j-1)` and apply the same
identity to `(U^2)^j-(VZ)^j`. Every direct term is therefore congruent to
its displayed parity-reduced term modulo `R`. Summing over `i` proves the
identity. No localization or field assumption is used. QED.
