# Result

The rich-fiber cutoff is proved uniformly for every dyadic order. It improves
the earlier single-collision estimate

```text
p<=6^(phi(n))=36^(n/4)
```

to

```text
P(t)>=19 => p<=6^(n/4).
```

The gain uses all ten unordered product representations forced at the C36'
cutoff, plus the facts that one product fiber has at most two diagonal
representations and at most one representation containing the root `-1`.

This proves C36' for the complete large-field branch `p>6^(n/4)`. It does not
bound the weighted rich locus in the remaining range
`n^2<=p<=6^(n/4)`, so the critical node remains TARGET.

The exploratory coefficient searches are in
`experiments/prize_resolution/h3_norm_parseval_search.py` and
`experiments/prize_resolution/h3_rich_parseval_packing.py`. Modal runs
`ap-v0bUbi2376aquny83Mgihi` and `ap-drEoxyyrlyY2pioSWGwMsQ` supplied
route checks only; the proof above no longer depends on bounded search.

## Verification

- theorem replay: `ap-siNdQHOJy0zqNpqAFdJZxn`, PASS on 43,434 coefficient
  vectors and 130,293 distance-parity pairs;
- constrained route replay: `ap-U5dzx35TfeUfnyRCf8KLKb`, PASS;
- full manifest replay: `ap-0NJsnJMsYJxFhQzppsGQyR`, 130/130 PASS;
- five integration gates: `ap-jBvpnlB8oU1kaI6P7gKhOY`, PASS; and
- critical-orbit rebuild: `ap-wDtanQSzWdMQWOqVy6T7RJ`, PASS with all nine
  open truth leaves unchanged.
