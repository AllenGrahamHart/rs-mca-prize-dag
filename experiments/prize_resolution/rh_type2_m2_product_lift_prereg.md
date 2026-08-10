# Preregistration: strict-A=3 m=2 product-code lift hunt

Date: 2026-08-10

## Exact forced incidence shape

At `m=2`, an `O=0`, `T=rho+2` endpoint failure has

```text
N=32, rho=7, T=9,
```

with 31 domain rows of supported-slope degree two and one row of supported
degree one. The 31 double-root rows form `K_9` with five missing edges. The
singleton vertex has missing degree two; the other eight vertices have
missing degree one. Up to relabelling, the missing graph is a two-edge path
centered at the singleton vertex plus a perfect matching on the remaining
six vertices.

## Registered test

Over `F_97`, put `D=mu_32`. For random choices of nine distinct finite
slopes, one unsupported residual root, and a random assignment of the 31
edge rows plus singleton row to `D`, test whether nonzero row scales make the
three quadratic coefficient vectors members of `RS[D,8]`. Equivalently,
test the exact stacked parity-check matrix for a full-support null vector.

For every product-code lift, reconstruct the three degree-at-most-seven
locator coefficient polynomials and test the four coefficient layers of
the `9 x 8` Hankel compatibility system for a nonzero syndrome pair.

## Outcomes

- **Strong falsifier:** a full-support product-code lift with a nonzero
  Hankel-compatible syndrome pair. Preserve the complete assignment and
  coefficients for exact follow-up; this is not yet a column-far
  counterexample until the joint-support condition is checked.
- **Intermediate survivor:** a full-support product-code lift that fails the
  Hankel system. This proves that the product-code constraint alone is too
  weak and names the Hankel equations as load-bearing.
- **No survivor:** evidence only. Random placements do not prove universal
  non-liftability; record the rank histogram and total trials.

## Compute envelope

Eight independent Modal workers, one CPU and 512 MB each, stop after 52
seconds inside a 60-second container timeout and return partial histograms.
No local numerical computation.
