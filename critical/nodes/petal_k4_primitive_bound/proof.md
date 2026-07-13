# Proof

The G1/E22 dictionary supplies petal size `ell`, petal count `m`, missed
degree `d`, and canonical retained remainder `r<ell`. P1 gives
`d>=ell(m-2)`.

`petal_retained_zero_effective_degree` factors the actual chart image and
preserves its exact support. `petal_full_touched_set_injection` then injects
the consumed full-petal list into touched sets of size at least
`ceil((ell+d-r)/ell)`. Finally `petal_top_band_tail_collapse` proves that this
tail is at most `m+1<=n` on every official row. This is a bound for the
complete full-petal list, so it also bounds the primitive sublist. Taking
`b4=1` proves K4.

Mixed-petal lists are not asserted here; the `petal_growth` packet explicitly
keeps them outside this full-petal consumer.
