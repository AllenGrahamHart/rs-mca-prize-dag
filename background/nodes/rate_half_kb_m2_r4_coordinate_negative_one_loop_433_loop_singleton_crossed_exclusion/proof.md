# Proof

Assign the two source antipodal pairs roots `(1,epsilon_1 i)` and
`(r,epsilon_2 i r)`, with the loop root `t`.  Their squared labels are
pairwise distinct.  Insert these roots, `(KB431X-1)`, and the corresponding
edge sums into the two denominator-cleared q welds from the parent theorem.

For either cell, each weld contains only products of the following known
guards:

```text
b,c,r; b+/-1,c+/-1,b+/-c,bc+/-1,r+/-1,r^2+/-1.
```

Divide these factors whenever they occur.  The two residuals are linear in
`r`.  Exact elimination gives `(KB431X-2)` for both cells.  Before monic
normalization the scalar is `+/-4i`, which is nonzero in the deployed odd
characteristic.

If the root signs agree, a common solution would force `b=0` or `c^2=1`.
If they differ, it would force `c=0` or `b^2=1`.  These are respectively
product-zero or target signed-pair collisions, all excluded by the parent
guards.  Thus no q-compatible common packet exists in either cell. QED.
