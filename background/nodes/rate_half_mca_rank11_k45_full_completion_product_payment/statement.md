# Full completion product pays K'=45

- **status:** PROVED
- **closed residual row:** `K'=45`
- **new closed component prefix:** `K'=10..45`

At `K'=45`, refine every completion maximum at supports `2..9`.  The
Cartesian branch product has

```text
9*8*7*6*5*4*3*2=362880
```

disjoint exhaustive leaves.  On the `259200` leaves where supports four and
five are both terminal, also intersect the support-four cap with the proved
external-carrier charge.

The worst final premium is the all-fallback leaf:

```text
40126324034612056409620566967689123241580103372.
```

This is below the exact safe premium ceiling by

```text
323417025195949241219620287627046670164885155.
```

Complete component demand exceeds complete capacity by

```text
1616971801308361526826641488053709685917408248376428345137933.
```

The same payment fails at `K'=46`, where the all-fallback leaf exceeds the
safe premium ceiling and complete capacity exceeds demand by

```text
5057508862309072579343840146913199075599800084788396842011438.
```

## Falsifier

A completion-maximum tuple outside the Cartesian product; loss of an
inherited cap; use of the joint support-four cap on a fallback source; a
branch premium above the streamed maximum; a nonpositive `K'=45` endpoint
cross; or closure of `K'=46` by this payment.
