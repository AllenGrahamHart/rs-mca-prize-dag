## Preregistered K'=87 ordinary-lane payment

- **decision:** replay the complete ordinary lane through the pinned primary
  and independent K'=83 routers after substituting only the K'=87 row data
- **primary adapter SHA-256:**
  `a9382db987ce51906dedd510d028ebf688a141455c147f617bda60a7c9b334c9`
- **audit adapter SHA-256:**
  `338d35ca79a5a54e6c869f913bf4a25f52e1cd0351b20ce3df3142494c735af3`
- **single-call dispatcher SHA-256:**
  `fce317eda0003bef6d515484f636b54d497cb6158a26907de13f7de4d3674565`
- **checker SHA-256:**
  `60fde0ea89ffccb94f61c9fd824faa5656ad2689af4c532d6aaea62a7131cdff`
- **hash-pinned K'=83 code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** one Modal container, one CPU and 1 GB; fresh primary and
  audit subprocesses execute sequentially with 900-second child walls and an
  1815-second container wall; projected cost below `$0.20`
- **local safety:** one synchronous client under the `modal` RAMguard profile
  and a 2 MB inherited thread-stack limit; no local enumeration

The adapters set `K'=87`, `q=77`, `m'=67559`, and `n'=1048663`, then derive
the exact safe premium ceiling from the pinned ledger. The checker requires
both subprocesses to finish below 128 MB RSS and to agree exactly on source
units, raw rows, raw-safe units, expanded units, geometry rows, premium,
margin, and normalized active branch. It independently checks the seven-row
high-stratum multiplicity and recomputes safety from the printed ceiling.

```text
PASS:       paired exact agreement and nonnegative ordinary margin;
UNSAFE:     paired exact agreement but negative ordinary margin;
INCOMPLETE: timeout, resource breach, malformed output, or disagreement.
```

Only `PASS`, combined with the completed clipped nonordinary wave and a
strict exact component gap, permits a K'=87 proof-node promotion.

**Outcome:** `PASS`. Modal app `ap-t1IWAsyDidGwq0ZwwYO6yI` completed both
fresh subprocesses at peak RSS `33..37` MB. Capture SHA-256:
`06a550c1f65be3c2a7c4d96590188f5de6ca792c1f87e638f2fa7d5163b43519`.
The checker reports exact paired agreement on 542,840 source units, 3,799,880
raw rows, 121,895 raw-safe units, 4,385 expanded units, and 2,940,875 geometry
rows per implementation. The ordinary premium is
`41460244206367810395288131753780101229368111530`, below the safe ceiling by
`670462675256690016910468032334996708331859`. It is also strictly below the
clipped-wave leader, so it does not change the candidate global premium.
