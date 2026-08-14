# Kernel multi-basis capacity cut

- **status:** PROVED
- **scope:** the dominant rank-deficient lane in every residual shortening
  `10<=K'<=11641`
- **units:** `(record, eleven-subset)` incidences

Put

```text
n'=1048576+K',       m'=67472+K'.
```

For corank `d=1,...,9`, let `M_d` be the support-local record cap from the
canonical-basis globalizer. The multi-basis decoration theorem gives total
kernel capacity

```text
A_multi(K') = sum_(d=1)^9 floor(
  C(n',10-d) M_d C(K'-10,d+1)/(d+2)).                (1)
```

Exact integer replay proves, for every `10<=K'<=11641`,

```text
A_multi(K')
  < ceil((495405467/10^9) N_min C(m',11)),
N_min=274980728111260126.                            (2)
```

At `K'=11641`, the exact gap in (2) is

```text
17769453550459149385453824948016076737082337523706893862084.
```

Therefore the kernel lane cannot be the dominant component-incidence lane
through `K'=11641`. At `K'=11642`, the capacity exceeds demand by

```text
187031323586740190878769118921060658362307444191332937452616,
```

so this method stops there.

## Falsifier

An arithmetic mismatch in (1); a row in the closed interval with
`A_multi(K')` at least the ceiling in (2); failure of the `d+2` decoration
divisor; or an assertion that the comparison remains paying at
`K'=11642`.
