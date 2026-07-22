# Upstream crosswalk - L1 complement Toeplitz normal form

## Shared divisor object

Both programs count monic split divisors of `Z^n-beta`. Upstream
`prop:q-boundary-divisor` represents one locator-prefix fiber by divisors in
an affine space `Q_z+A` with `deg A<=omega-w-1`. The local exact-shell theorem
represents one arbitrary received-word shell by complement divisors satisfying
the convolution window `C_(U,a)(M)=0` and the primitive gcd guard.

## Remaining difference

Upstream fixes the top `w` coefficients of a locator. Locally, multiplication
by the high-degree tail of `U` gives `w` Toeplitz linear forms on all
coefficients of the complement locator. Codeword shifts do not change those
forms, but no split-divisor-preserving reduction to a top-prefix projection is
known.

## Portable target

A useful upstream theorem would extend row-sharp Q from prefix-affine divisor
sections to realized Toeplitz sections, with effective-image normalization,
first-match quotient payment, and the exact cofactor gcd retained. A weaker
portable result would classify the Toeplitz sections that are prefix-
equivalent and route every other rank profile to an already paid cell.

## List-interior alignment

Grande Finale v3 keeps `U_list-int`, the arbitrary-word interior codeword-ray
term, separate from locator Q, but gives it no comparably explicit algebraic
definition. The Toeplitz exact-shell divisor census is a strong candidate
model for that list-interior object: it is arbitrary-word, exact-support,
split-divisor, and retains the primitive cofactor guard. This is an alignment,
not a proved cross-tree identification, until upstream states the owner map
from `U_list-int` to these divisors and its row budget.

The later `l1_exact_shell_fixed_cofactor_prefix_transport` resolves the
boundary between the two upstream terms: scalar cofactor is literally
locator Q, bounded cofactor is a bounded union of deeper locator-Q atoms, and
only growing cofactor remains a candidate for `U_list-int`.
