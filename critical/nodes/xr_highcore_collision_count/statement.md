# XR high-core collision count

- **status:** see `dag.json` (single source of truth)

At each of the six clean-rate candidates and for every generic-branch
received pair `(u,v)`, the number of post-strip live slopes whose agreement
support shares a size-`k` core with another live member is at most

```text
8 n^3.
```

The count is on distinct slopes, not raw supports or the W-collision moment.
Pairs jointly `A`-close to a codeword pair are tangent-paid and outside this
generic branch. Dihedral-symmetric and extension-type slopes remain inside
the predicate allocation.

