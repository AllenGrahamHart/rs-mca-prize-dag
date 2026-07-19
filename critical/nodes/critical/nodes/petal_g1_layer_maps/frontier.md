# G1 frontier after paid-atlas and source audit

Date: 2026-07-12.

## Closed locally

- fixed retained-zero sunflower layers inject into the auxiliary list;
- K4 bounds every full-petal chart by `m+1`;
- the weighted coefficient `121/128` is sufficient, and current plus all
  descendants costs `121/126<1`;
- a raw `n^5` chart count is not required;
- upstream slope-atlas `(CAT)/(UNIF)` is not a direct G1 input.

## Exact open content

The capf paper states that its layer results become theorems about an actual
sunflower decomposition only when such a decomposition supplies the layer
maps. No audited source constructs that decomposition for every received word.

The long full-list quotient program proves many bounds after fixing a special
sunflower received word with core `C`, petals `T_i`, and labels `c_i`. It does
not extract those data from an arbitrary received word and therefore does not
prove G1 coverage or quotient closure.

The next genuine theorem must be a paid sunflower extraction: from an
arbitrary received word and its top-band full-petal contributors, construct
fixed retained-zero layer keys whose first-match weighted sum is at most
`(121/128)n^6`, functorially on consumed quotient rows.

Fixed-layer estimates, special-sunflower counts, or upstream distinct-slope
payments do not advance this extraction unless they supply an explicit
consumer map. This route is source-stalled until such an extraction mechanism
is identified; further fixed-chart census work is not the next action.
