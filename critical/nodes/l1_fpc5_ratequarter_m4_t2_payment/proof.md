# Proof: rate-quarter pair uniqueness

From (RQ1) and `b<ell`,

```text
3k+1=4ell+b<5ell.
```

Hence `2ell>k-1`. Suppose two degree-`<k` codewords `P` and `P'` touch the
same pair of full petals in the fixed layout. Both equal the received word on
the union of those petals, so `P-P'` has `2ell>k-1` distinct roots. But
`deg(P-P')<k`, forcing `P=P'`.

There are six unordered pairs among four petals. Thus the complete
non-planted `M=4,t=2` contribution in the fixed first layout is at most six.
Apply `l1_general_first_layout_domination` to the selected source-admissible
class. Every member not carried non-planted in this first layout belongs to
its anchor set, which has size four. This gives the global bound `6+4=10`.
QED.
