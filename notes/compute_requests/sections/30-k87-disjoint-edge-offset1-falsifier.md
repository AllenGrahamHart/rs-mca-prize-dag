## Preregistered K'=87 support-disjoint offset-1 falsifier

- **decision:** exhaust the complete offset-1 residual lane using the best
  support-disjoint subset of available adjacent edges
- **scope:** paired primary and independent traversals of offset 1; no other
  offset is launched in this campaign
- **primary adapter SHA-256:**
  `9aa4ff7e6d71face083b427d06519486ec50a6c6554203007a7f9be07abdb5c8`
- **independent-pricing adapter SHA-256:**
  `f4d447913771dde26e085d56fbfdef0fec6ba702183f99f403dccfe2f2a98e22`
- **K'=87 best-single primary base SHA-256:**
  `f2ef06960e42febe620dcfa7ecddf2d7207532462e764e0b767a98416f45de53`
- **K'=87 best-single audit base SHA-256:**
  `d4c6baed6e30a3acea25b808a6320589fc1b7aadd401da1a4fac0566b17df627`
- **K'=87 traversal core SHA-256:**
  `53b1d80cabff9cf1995043195b91e8b1e96013ffcb8aaacf5642591a88cd3e0a`
- **dispatcher SHA-256:**
  `964a08d370022a2ce6fde495346e3bed3c3b8ed2907cc8ab9b0a8a210399ac6c`
- **checker SHA-256:**
  `8dd3942479fdcb34b93908629039ed1e33484015de07a314fcc55fef1950c02f`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** two jobs, one CPU and 256 MB each, 480-second child wall and
  495-second container wall; projected total cost below `$0.10`
- **local safety:** one `modal`-profile RAMguard client; no local enumeration

The primary adapter calls the proved `priced_all_adjacent` optimizer; the
independent adapter calls its separately implemented `price` reconstruction.
Both enumerate only edge sets with pairwise disjoint support pairs. No
overlapping adjacent charges are composed.

`FALSIFIED` requires a paired exact over-leader witness and blocks a complete
support-disjoint campaign. `SURVIVED` requires exact agreement on all 462,384
offset-1 source units and every deduplicated carrier profile. `INCOMPLETE`
retains partial checkpoints and changes no status. Offsets 9, 23, and 43
already inherit survival because this optimizer includes every best-single
choice. This campaign alone cannot promote `K'=87`.
