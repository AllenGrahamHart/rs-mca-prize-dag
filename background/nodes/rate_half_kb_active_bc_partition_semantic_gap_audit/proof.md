# Proof

## 1. What the active partition proves

The partition proof writes `Z=Z_bad`, treats `Q` and `BC` as predicate sets,
and defines the four cells by intersections and successive set differences.
Equivalently, its formal first-owner kernel accepts `qCertified` and
`bcCertified` as arbitrary Boolean functions. Exact exhaustion, uniqueness,
and pairwise disjointness follow from the nested conditionals; no property of
those functions is used.

The frozen JSON records a predicate name and `predicate_available: true`, but
contains no witness schema, locator data, certificate relation, or semantic
constraint connecting that string to an endpoint record.

## 2. Finite countermodel

Take a one-element slope universe `{z}` and set

```text
bad(z)=true, tangent(z)=false, qCertified(z)=false,
bcCertified(z)=true, endpointRecords=empty.
```

The first owner of `z` is `BC`. Thus the four active cells are pairwise
disjoint, exhaust the bad set, and assign a unique owner, exactly as required
by the partition theorem. But `Z_BC={z}` admits no map to an endpoint record
because the codomain is empty. Hence no endpoint bridge is a logical
consequence of the partition contract.

## 3. The K3 chain does not fill the gap

The source-pencil rank compiler quantifies over every *supplied actual
endpoint record* and states that its 32,099 templates are per record rather
than a census of records. The decomposition source-pencil compiler also
states that the endpoint parameter line is not the evaluation carrier and
disclaims parameter-to-carrier, received-word, explaining-polynomial, slope,
owner, and charge descent. These theorems classify records after production;
they do not produce one from an active slope.

The countermodel is not a mathematical counterexample to the intended
balanced-core statement. It proves only that a new source-witness compiler
and either a K3 endpoint realization or another same-owner completion route
are indispensable. QED.
