# Deep joint completion payment closes K'=46..53

- **status:** PROVED
- **closed residual rows:** `K'=46..53`
- **new closed component prefix:** `K'=10..53`

Refine the support-four and support-five completion maxima to exact defects
`s_4,s_5 in 0..q`, retain every other support branch, and apply the joint
support-four external charge exactly when `s_4+s_5<q`.

For each row `K'=46..53`, the other-support product has `8640` raw branches,
`1182` distinct cap vectors, and exactly `9` componentwise maximal vectors.
Exhausting every exact defect pair against those nine vectors gives the
active branch

```text
c2F/c3F/c4d floor((q-1)/2)/c5d floor((q-1)/2)/c6F/c7F/c8F/c9F.
```

Every row `K'=46..53` is safe.  The smallest positive gap is at `K'=53`:

```text
2503373059664320603163477388007627909210651834842589498907998.
```

The same payment first fails at `K'=54`, where complete capacity exceeds
demand by

```text
2477882110233058360154706764229180240778698202487636349407165.
```

## Falsifier

A missing exact defect pair; a discarded non-dominated other-support vector;
an active premium above the certified maximum; a nonpositive endpoint cross
on `46..53`; or closure of `K'=54` by this payment.
