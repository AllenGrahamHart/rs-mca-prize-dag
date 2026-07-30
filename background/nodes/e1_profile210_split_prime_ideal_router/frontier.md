# Frontier

The profile is no longer an unstructured support-12 search. Its pure
cofactor contribution is at most ten orbits. Exact low-variance resultants
remove `m=1538`, so all remaining uncertainty is the occupancy of the
split-prime pairs

```text
(m,Q_s),
m in {514,1028},
s one of 128 primitive roots modulo 257.
```

The current coarse envelope is `T_210<=266`, or `68096` oriented vectors.
The `m=1028` branch has the shorter moment window `V<=12` and should be
attacked before `m=514`.

The next attack must couple the two reductions

```text
F(r)=0 mod p,       F(s)=0 mod q
```

for a profile-`(2,10)` polynomial `F`, or derive a split-prime occupancy
bound directly from the resultant/ideal geometry. Counting all support-12
vectors without fixing `(m,Q_s)` is rejected.
