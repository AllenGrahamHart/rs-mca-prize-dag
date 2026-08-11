# `A=1` core-one quadratic gap-four abstract incidence design

- **status:** PROVED
- **closure:** explicit support-only realization of the exact degree sequence
- **consumer:** `rate_half_band_crossing_location`

For every integer `e>=7`, put

```text
rho=3e-1,       b=T=rho+4=3e+3.                      (AID1)
```

There is an explicit family of `b` subsets `E_t` of an `N=4rho` element
set satisfying exactly the locator degree data in `(ICS2)--(ICS5)`:

```text
|E_t|=rho                                      for every t;
one core point s_0 has degree b;
3rho+5 light points have degree e;
one point x_* has degree e-6;
rho-7 inactive points have degree zero.              (AID2)
```

## Construction

Work on the cyclic start set `Z/bZ`. Let

```text
sigma_j=floor(7(j+1)/b)-floor(7j/b) in {0,1}.         (AID3)
```

At start `j`, create `3-sigma_j` distinct light points. Put each such point
in the `e` consecutive blocks

```text
j,j+1,...,j+e-1 mod b.                               (AID4)
```

Every cyclic interval of `e` starts contains either two or three marked
positions `sigma_j=1`. A block therefore contains either `3e-2` or `3e-3`
light points. Exactly `e-6` blocks have the latter size. Add `x_*` to those
blocks, add `s_0` to every block, and add `rho-7` unused points to the
ambient set. The resulting blocks satisfy `(AID2)`.

## Route fence

The exact support degree sequence of the retained `u=4` packet is
combinatorially consistent for every relevant `e`. It cannot be excluded by
handshake, divisibility, or block-degree arguments alone.

No RS word pair, codeword-center assignment, Hankel pencil, resultant cube,
or field-valued realization is constructed.
