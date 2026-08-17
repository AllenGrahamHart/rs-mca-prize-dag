## Preregistered K'=87 residual-witness adjacent payment

- **decision:** print every support-disjoint adjacent-edge price on the exact
  best-single counterexample and identify the minimal edge set in both the
  primary and independent atlas
- **scope:** offset 1, `m2=27`, `s4=48`, `s5=47`, case
  `F23__N4_t2__N5_t0`, charges `(32,7),(36,5)`
- **K'=87 adapter SHA-256:**
  `a66f4235d0651bd35d3ccbe749beb6ea5f52c6b2198bc1460bf13f3fe7907a00`
- **base paired analyzer SHA-256:**
  `44faccd0305d374557650c8bfc3b40f3aaa97717e46b154568cbadb3ec77bf3a`
- **dispatcher SHA-256:**
  `64bca2a9e0ce3d6b0f69ed664db3a18e01e8348dcde9bc3e046ec6c4116c506e`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** one CPU, 256 MB, 20-second child wall and 30-second container
  wall; projected cost below `$0.01`
- **local safety:** one RAM-guarded Modal client; no local mathematical run

The adapter changes only `K'=87`, `q=77`, `m'=67559`, the exact safe ceiling,
and the raw-safe leader. The base analyzer enumerates all support-disjoint
subsets of the available edges and independently reconstructs every adjacent
pair cap.

`PASS` prints both exact option tables. A best price above the leader is a
current adjacent-router wall; a lower price identifies the next compressed
edge family. `INCOMPLETE` changes no status. This one-witness calculation
cannot promote `K'=87`.

**Outcome:** `PASS`. Modal app `ap-wLdIVTwSfqoHqcbrTReo02` completed the
paired exact option table. Primary and independent values agree entry by
entry. Capture SHA-256:
`9edcb2b46da5f9cb3aa97bcc8f230e0725bc7b2cd72e214477f4c5ece34ba82b`.

The minimizing valid choice is the support-disjoint edge set `4+6`, with
price `37213564927666895824914633823577105351210858112`, below the exact
raw-safe leader by `4247334197808548012966412861445656980288186583`.
Every single edge remains above the leader:

```text
edge 4  41697268189301188466486299088841700382091277312
edge 5  41535717484613459403166619514559682376379208865
edge 6  41597760943556546045632267199456263836264023265
```

This repairs the single witness but not the row. It authorizes an exhaustive
paired offset-1 falsifier using the proved support-disjoint optimizer.
