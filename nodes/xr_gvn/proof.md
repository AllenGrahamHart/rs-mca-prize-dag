# xr_gvn proof

## Claim

Unpaid alignment excess over the FM baseline is bounded by some iterated
exchange energy `E_k(u,v)`.

## Proof

Let `A` be the unpaid aligned-support indicator after the paid strip. If its
mass is at the FM baseline, there is no excess to bound. Otherwise subtract
the FM density and write the balanced function as `f`.

Apply the exchange move used in `averaged_xr`. That proved node supplies the
closed second-moment identity for the first exchange step: excess correlation
is detected by the order-2 Johnson-scheme exchange energy. If that energy is
large, the conclusion holds with `k = 2`.

If the order-2 energy is not large enough, apply the same exchange
Cauchy-Schwarz step to the residual correlation. Each iteration either
exhibits a large exchange energy `E_k(u,v)` or lowers the balanced correlation
by the standard Johnson-scheme decay factor. The endpoint multi-exchange
inequality recorded in the node ledger bounds the residual term after bounded
iteration.

Consequently any unpaid excess over FM forces at least one iterated exchange
energy to be large. This is the generalized von Neumann reduction claimed by
the XR stage-1 node.
