## Preregistered K'=87 exact component payment

- **decision:** insert the larger of the certified ordinary and nonordinary
  premiums into the pinned rank-nine component ledger and require a strict
  positive incidence gap
- **certified premium:**
  `41460899125475443837881046685022762331499044695`
- **payment script SHA-256:**
  `1e154be116c33854af85a5a01fd03e4a3c4e0b66d1e24bc1fe58c9f2f9c62713`
- **Modal dispatcher SHA-256:**
  `c8e111c4c1bdc4f62f56598f3a7fa56615f4ca09d1c9bbf580c29b7e9ea483ab`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** one Modal container, one CPU and 256 MB, 30-second wall;
  projected cost below `$0.01`
- **local safety:** one synchronous client under the `modal` RAMguard profile
  and a 2 MB inherited thread-stack limit; no local calculation

The script independently derives the row marks, kernel capacity, record floor,
safe premium ceiling, full-rank capacity, required incidence, and strict gap
from the pinned ledger. It accepts only the exact K'=87 row and asserts both
the known ceiling margin
`15543567623247423995536789673894577398694` and a strictly positive component
gap. No rounded or floating-point quantity is used.

`PASS` authorizes construction and adversarial replay of the K'=87 proof node.
`INCOMPLETE` or a nonpositive gap leaves the row open.

**Outcome:** `PASS`. Modal app `ap-JAw6W5GHktZA9TXLxcpMUY` reconstructed the
exact row; capture SHA-256:
`883f659486162495750adbc80c97d3224cdae6b3bdebf3429492a33189d95312`.
The certified premium is below the exact safe ceiling by
`15543567623247423995536789673894577398694`. Total capacity is
`921060890011284709657056363808900069597352462765767795701103981`
against required incidence
`921060967723676391242250303252610946492991464556444164407248882`,
leaving strict component gap
`77712391681585193939443710876895639001790676368706144901`.
