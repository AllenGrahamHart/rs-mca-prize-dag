# Proof

Write `F` for the number of full coordinates and `r` for the represented
projective directions. The parent bank proves

```text
2044<=K'<=5025,
F>=28396+204K',
r<=218.                                             (1)
```

For a represented pure-power direction `y`, its direction polynomial is
`X^e-y`. Since `e|N` and the characteristic is odd, this polynomial has
exactly `e` simple roots in `mu_N` whenever `y` lies in the image of the
power map. Full coordinates in that direction form a subset of those
roots. Therefore

```text
F<=re<=218e.                                        (2)
```

At the smallest possible `K'=2044`, the lower bound in (1) is `445372`.
Consequently (2) rules out every power of two `e<=1024`. The degree cap
`e<=K'-1<=5024` rules out every power of two `e>=8192`. This proves
`e in {2048,4096}`.

Suppose first that `e=2048`. The degree cap gives `K'>=2049`, while

```text
28396+204K'<=218*2048=446464                       (3)
```

gives `K'<=2049`. Thus `K'=2049`, and the full-coordinate floor is
`F>=446392`. Since `217*2048=444416`, equation (2) forces `r=218`.
The parent bank permits at most 218 distinct full affine lines and each
represented direction has at least one, so there are exactly 218 such
lines, one per direction. Finally

```text
re-F<=218*2048-446392=72.                           (4)
```

Now suppose that `e=4096`. The degree cap gives `K'>=4097`, and

```text
28396+204K'<=218*4096=892928                       (5)
```

gives `K'<=4237` because the lower bound is `892744` at 4237 and
`892948` at 4238. At the lower endpoint `F>=864184`, whereas
`210*4096=860160`, so `r>=211`; the parent bound gives `r<=218`.
There are at most 218 full lines, hence at most `218-r<=7` lines beyond
the first line in each represented direction.

For `e=4096`, direct capacity is sharper than the inherited aggregate
degree budget. Since `K'>=4097`,

```text
re-F<=218*4096-(28396+204*4097)=28744.             (6)
```

Together with (4), this gives the two missing-slot caps. QED.
