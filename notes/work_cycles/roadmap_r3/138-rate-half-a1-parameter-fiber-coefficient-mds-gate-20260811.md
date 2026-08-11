# Cycle 138: rate-half `A=1` parameter-fiber coefficient-MDS gate (2026-08-11)

## Transposed realizability matrix

Write every selected full-degree parameter fiber as

```text
G(delta,X)=zeta_delta F_delta(X),
```

with `F_delta` monic and split. Every scaled root-coefficient vector is an
evaluation of a parameter polynomial of degree at most `m`. Equivalently,
one explicit parameter-barycentric matrix has the full-support kernel vector
`zeta`. The official guaranteed matrices are

```text
extremal: 50371909150609548946088 rows x 366503875926 columns;
strict:   25185954575671278348969 rows x 274877906946 columns.
```

This is the parameter-direction counterpart of Cycle 134's fixed-domain
gate. Both constrain one common biform; neither row count is itself a rank
proof.

## Verification and burn-down

```text
result:                  PROVED parameter-fiber coefficient-MDS gate
DAG delta:               +1 PROVED, +2 nodes total this cycle group
DAG after compile:       2291 nodes, 6733 edges, 2050 PROVED
critical status delta:   none; 28 every-route TARGETs remain
node replay:             normal/-O/audit/tamper all pass
DAG/manifests/crosswalk: pass
full composed replay:    preflight blocked by a pre-existing failed WCL
                         row in the historical baseline; new scripts pass
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

The next closure test must combine the fixed-domain and fixed-parameter
coefficient systems with the retained Hankel/source identities. A survivor
of one matrix alone is not a valid pair-boundary realization.
