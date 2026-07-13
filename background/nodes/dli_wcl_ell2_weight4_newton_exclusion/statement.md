# DLI ell=2 weight-4 Newton exclusion

- **status:** PROVED
- **closure:** proof

## Statement

Let `q` be an official DLI production prime and let `omega in F_q` have exact
order 1024. There is no reduced signed weight-4 polynomial

```text
P(X) = sum_(i=1)^4 s_i X^e_i,
```

with distinct `e_i in {0,...,511}` and `s_i in {+1,-1}` satisfying both

```text
P(omega) = 0,
P(omega^3) = 0.
```

Consequently no official DLI production row contains a weight-4 odd-trade at
the `ell=2` level. This conclusion is field-uniform: it uses only
`char(F_q) notin {2,3}` and the exact order of `omega`, not the field-size cap
or a norm-factor census.

## Nonclaims

This closes only weight 4 at `ell=2`. Weights 5 through 7 there, every other
unpaid weight window, and WCL-ZONE remain open. No primitivity assumption is
needed because the theorem excludes every reduced weight-4 relation.

## Falsifier

Four distinct nonzero elements with no antipodal pair in a field of
characteristic other than 2 or 3 whose first and third power sums both vanish.
