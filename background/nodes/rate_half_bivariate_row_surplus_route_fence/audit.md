# Audit

1. All ten unordered pairs of the five supported slopes are checked.
2. The unique deficient coordinate is established from the generic locator,
   not inferred only from the support partition.
3. Rank at most five uses an explicit all-nonzero kernel vector.
4. Rank at least five uses a printed nonzero minor for every matrix.
5. `verify.py` reuses the exploratory reconstruction. `verify_audit.py`
   independently reconstructs each support word by Cramer's rule from the
   first three moments, verifies all eight syndrome moments, and checks the
   hard-coded minors.
6. The witness is a genuine Hankel/apolar pencil but has `m=1`. The official
   scale is not covered.
