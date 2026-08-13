# Cycle 199: MCA pole-line typed witness certificate (2026-08-12)

The upstream `#1159` actual-record packet already contained a strict
certificate manifest and four replay paths.  A fresh primary replay at exact
head `e603e0cedc5220ec2f29bd53836e732e3ec14934`, with this DAG supplied for
its external pins, passes:

```text
d1=67473; actual record=1; actual owner=not-established
62 semantic mutations rejected; 3 parser mutations rejected
```

A replay on the later `#1163` stack correctly fails its source-drift gate
because intervening `#1160/#1163` changes modify a pinned manuscript.  The
exact-head replay is the valid provenance check.

The imported certificate is an actual witness, not a schema label.  Over the
deployed subgroup and degree-six challenge extension, the pole line

```text
v=-1/(X-alpha),
u=1_E+alpha/(X-alpha),
gamma=alpha
```

has slope word `1_E`.  The zero polynomial explains it on the exact following
support of size `m`.  The direction word has no degree-`<k` explanation there:
otherwise `(X-alpha)g+1` would have `m>k` roots and degree at most `k`.
The support-complement locator with numerator zero passes the Cycle-198 guard
and reconstructs the identical support and explanation.

The minimum is exactly `67473` under both shifts by the upstream and local
root-count proof.  The record therefore verifies the full typed witness
substrate while retaining

```text
Q owner:      UNASSIGNED
BC owner:     UNASSIGNED
U_new owner:  UNASSIGNED.
```

This closes the concrete certificate-parsing criticism in `#1159` for one
deployed record and demonstrates the repaired adapter on its boundary case.
The remaining obstacle is genuinely owner-level: define executable frozen Q
and BC predicates, prove slope-global Q exclusion, and prove both projection
directions.  Another witness parser will not solve that theorem.

```text
start:                   3f626c84d
result:                  PROVED typed deployed actual witness import
DAG delta:               +1 PROVED background node, +2 edges
critical status delta:   none
upstream terminal delta: one actual certificate parses and passes the guard;
                         frozen-owner equivalence remains open
delta-star movement:     none
compute:                 exact Python replays only; no Modal spend
next route action:       use this fixed record to adjudicate candidate Q and
                         BC predicates, then attack slope-global Q exclusion
```
