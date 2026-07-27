# E1 N=256 E=34 nonquarter-diameter template exclusion

- **status:** PROVED
- **closure:** two independent complete finite censuses

No pair-feasible folded-profile `(3,4,0)` collision at `V=68` lies in the
nonquarter-diameter heavy-position template.

Two independent exact implementations exhaust every normalized vector in the
31 weld chambers:

```text
light supports                       28,368,875,
normalized signed vectors         1,815,608,000,
E=34 vectors                           1,518,816,
profile-(6,7) vectors                  1,044,528,
full-conductor profile vectors          899,456,
maximum M_3                                  1560.
```

The primary implementation groups unordered signed chords. The audit forms
the ordered negacyclic product directly and reconstructs weld eligibility
from circular distances. They agree on every count and maximum in each of the
31 normal forms.

Since `1560<1947`, the inherited rational cubic-Hermite certificate puts the
collision norm below the pair-feasible threshold. This theorem does not
exclude the progression or generic heavy templates.
