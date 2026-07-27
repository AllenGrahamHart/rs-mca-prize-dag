# Audit

- The primary vertex-triple enumeration checks all 333,375 normalized
  four-light supports.
- The independent positive-gap enumeration reconstructs the same 28,800 valid
  supports without importing the primary list.
- All valid supports have zero light-light diameters, distance multiplicities
  `2,1,1,1,1`, and a repeated wedge rather than a matching.
- Affine canonicalization yields 148 representatives with orbit histogram
  `4,16,40,88` at normalized sizes `32,64,128,256`.
- The independent replay expands every printed orbit, checks pairwise
  disjointness, and recovers the complete valid-support set.
- Omitting the last orbit fails the coverage equality.

Both exact classifiers run under the 256 MiB RAM guard in less than ten
seconds combined. No Modal computation is load-bearing.
