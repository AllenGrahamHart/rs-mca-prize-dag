# Claim contract

- **claim id:** `f3_h3_dsp8_unit_product_trace_normal_form`
- **mathematical statement:** every decorated DSP8 primitive cubic shift pair
  has a unique product-one normalization with forced scale `q=rs`, common
  trace `sigma`, target `t=1+rs(r+s-sigma)`, and two exact quadratic split
  tests
- **scope:** every official dyadic H3 row and every retained DSP8 record
- **consumer:** `f3_h3_dsp8_correlation_bound`
- **status:** `PROVED`
- **proved dependency:** the DSP8 primitive cubic shift-pair adapter
- **new open content:** bound the normalized trace/split/line incidence in
  `(UTN7)--(UTN8)` with the exact class weights
- **falsifier:** one decorated record with two normalizing scales, one record
  for which `q!=rs` or `(UTN5)` fails, or one admissible normalized record
  that does not reconstruct through the adapter
- **nonclaims:** no point count, no rich-target cap, and no DSP8 promotion
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/f3_h3_dsp8_unit_product_trace_normal_form/verify.py`
- **upstream mapping:** a strict equal-constant subcase of primitive `SP`;
  generic `thm:sp-proper` all-pairs counting discards the forced scale and is
  only a route audit here
