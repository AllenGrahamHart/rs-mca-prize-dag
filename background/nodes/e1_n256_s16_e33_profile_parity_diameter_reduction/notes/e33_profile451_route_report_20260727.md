# E33 profile-(4,5,1) route report

The abstract nested-layer cap is 1918, above the exact V=66 cubic cutoff
1732. The sharp same-set target-fiber improvements alone lower it only to
1836, so a coupled quotient calculation is required.

Route-selection probes were deliberately bounded:

- `ap-P1zhpQPMyh32aGipdWKBO2`: exact 3,783,780-row `Z/32Z` nested-set census
  and deterministic `Z/128Z` hill search both found maximum 1608;
- `ap-YPwBdbkAdSXjalYqUMCEW5`: pure pseudo-Boolean threshold shards 0,1,2
  timed out without a witness; shards 3,4,5 were infeasible. This is evidence
  only and is not used in the proof;
- `ap-XlApOnmQmoX3P5Gd6qsVXb`: complete mod-16 quotient census found exact
  maxima 1732 and 1670;
- `ap-BnCaKbLKE6f99c19iKJ1D5`: the pinned-wrapper replay reproduced both
  allocation totals and maxima.

The load-bearing result is the quotient census, not the hill search or SAT
resistance. It covers 5,421,301 order-128 allocations and 3,086,861 divided
order-64 allocations. The remaining outer-`4Z` chamber is paid analytically
by the degree-32 norm bound `50^32<2^250`.

All runs used at most 1 GiB per container and 60-second hard timeouts. The
combined campaign stayed conservatively below `$0.30`; no continuation is
authorized or needed.
