# Proof

Fix a record with exact support `S`, `|S|=m'`, and a corank `d`. Decorate
every rank-`(10-d)` eleven-subset `T subset S` by every rank basis
`B subset T`. The loopless-matroid exchange lemma gives at least `d+2`
decorations for each `T`.

Now fix one independent `(10-d)`-subset `B subset S` and put
`H=ker(ev_B)`. Then `dim H=d`. If a decorated eleven-set `T` uses `B` and
has the same evaluation rank, all `d+1` coordinates of `T minus B` are
common zeros of `H`. Generalized MDS bounds the complete common zero set
of `H` by `K'-d`; the `10-d` coordinates of `B` are already common zeros.
Thus at most

```text
K'-d-(10-d)=K'-10
```

coordinates remain, and `B` has at most `C(K'-10,d+1)` extensions.

There are at most `C(m',10-d)` candidate bases inside `S`. Hence the
decorated incidence count is at most

```text
C(m',10-d) C(K'-10,d+1).
```

Dividing by the `d+2` decorations per eleven-set and taking the integer
floor proves (RS). No quotient synchronization across different records is
used.
