# Cross-support collision payment closes K'=60..70

- **status:** PROVED
- **closed residual rows:** `K'=60..70`
- **new closed component prefix:** `K'=10..70`

Refine the completion maxima at supports `2,3,4,5` to every exact defect.
From each nonempty exact source carrier, apply the cross-support collision
charge to every target support `d` with `c+d<=11`.  Retain the same-support
caps, the joint support-four charge when `s_4+s_5<q`, and every
support-`6..9` terminal/fallback branch.

The active branch on every row `K'=60..71` is

```text
s_2=s_3=s_4=s_5=ceil(q/2),
c6F/c7F/c8F/c9F.
```

Every row `K'=60..70` is safe.  The smallest positive gap is at `K'=70`:

```text
854274172985042754802177028749324962520517760595473749602211.
```

The same payment first fails at `K'=71`, where complete capacity exceeds
demand by

```text
824875968499878215752683873455674299360608616555107905777434.
```

## Falsifier

A cross-support cap used from an empty source or outside `c+d<=11`; a
discarded non-dominated vector; a nonpositive gap on `60..70`; or closure
of `K'=71` by this payment.
