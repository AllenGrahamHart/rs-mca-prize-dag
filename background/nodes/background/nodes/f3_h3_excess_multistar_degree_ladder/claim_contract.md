# Claim contract

- **claim id:** `f3_h3_excess_multistar_degree_ladder`
- **mathematical statement:** product excess `e=P(t)-18` forces at least
  `7+ceil(e/2)` small representations and the explicit weighted-center degree
  `L(7+ceil(e/2))`
- **scope:** every nonzero product target in an odd-characteristic dyadic row;
  the excess specialization applies when `P(t)>=19`
- **consumer:** `f3_h3_mobius_excess_half`, truncated rich-fiber candidate
  sieve
- **status:** `PROVED`
- **proved dependencies:** rich-fiber norm cutoff and weighted multistar
  router
- **new open content:** count the resulting degree-stratified ideals with
  quotient weights
- **falsifier:** a rich product fiber violating `(EML1)`, `(EML2)`, or the
  center-degree ladder
- **proof route:** swap-orbit count, exact exceptional-representation ledger,
  centroid deficit, and weighted handshake
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/f3_h3_excess_multistar_degree_ladder/verify.py`
- **upstream mapping:** primitive shift-pair control / truncated excess ledger
