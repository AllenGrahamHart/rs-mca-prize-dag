# Result

DSP8 now has a class-sensitive factorial-moment route:

```text
25(10F_25^0+17F_25^A)<=48536n^2
```

is sufficient, where `F_25^c` is the retained
`P(t)(P(t)-2)R(t)` moment. A simpler unweighted sufficient target is

```text
M_21<=48536n^2/425=114.202352...n^2.
```

Thus the existing `FM69` conjecture would close DSP8 but is substantially
stronger than necessary. This compiler itself does not estimate either
moment.
