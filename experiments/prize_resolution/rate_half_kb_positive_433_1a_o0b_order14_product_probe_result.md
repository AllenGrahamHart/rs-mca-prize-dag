# Positive 433-1a/O0b order-14 product probe

## Scope

This is exact finite-field evidence on the aligned order-14 subgroup
fixture.  It tests only the positive complete-fiber product rows.  It does
not test source-sum rows and does not prove a universal-field or packet
exclusion.

For each prime, the script chooses the seven antipodal pairs of an
order-14 subgroup, exhausts all `7P6=5040` assignments to `a,...,f`, both
five-cycle signs, and every distinct assignment of

```text
-c^2, ab, ab, -ab, ac
```

to the five common source labels.  The common rows determine the unique
quadratic-over-quadratic product map whenever their rank is five.  The
probe enforces leading support, permits any internal outside product at
`eta`, and permits an arbitrary assignment of the remaining six products
to `L^c`.  This is an enlargement of the source-facet placement set.

## Exact results

```text
prime  sigma  common rows  lead fail  K+eta pass  full pass  max overlap  max e-prefix
 29      -      300960       100572      33199        0           5             2
 29      +      300960       100572      33150        0           5             3
 43      -      296640        82436      23655        0           5             2
 43      +      296640        82436      23864        0           4             3
 71      -      302400        71586      15158        0           4             2
 71      +      302400        71586      15360        0           4             1
113      -      298080        53398      11598        0           3             1
113      +      298080        53398      11662        0           3             1
```

`max overlap` is the largest multiset intersection between the six
predicted and required `L^c` products.  `max e-prefix` is the largest
number of consecutive elementary symmetric equations `e_1,e_2,...` that
any separator survivor satisfies.  No common five-row matrix had rank
below five.

The six-fiber separator is therefore far from sufficient, but the complete
twelve-row product gate rejects every tested placement in all eight cases.
The first four elementary symmetric equations already reject every case;
usually the first two or three suffice.

## Runs

- Initial `F_29` replay: `ap-M9gh2mPNg6cBLSyIyQcIM8`.
- Four-prime census: `ap-JjNfWGTF3R7CdJlZyrGpKQ`.
- Elementary-symmetric diagnostic: `ap-DOi4tbfs0TgGBL5lEl52m7`.
- Every task stopped internally before 50 seconds; observed maxima were below 16 seconds.
- Eight diagnostic containers used `0.5` CPU and `256 MB`; estimated cost is well below one cent.

## Next theorem target

Seek a low-order complete-product moment obstruction for the aligned
source placement, preferably from the first four elementary symmetric
rows.  Do not promote this finite fixture result to deletion of the
universal `433-1a -> O0b` route.
