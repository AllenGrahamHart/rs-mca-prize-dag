# Audit

The proof counts all rank-drop slopes, a superset of slopes with a split
locator. It therefore does not need to count locators inside a kernel fiber.

Full rank means column rank `r+1` over the rational function field, not full
row rank. The strict inequality `r<R/2` is load-bearing: at `r=R/2` the
matrix has fewer rows than columns, and every slope has a nonzero ambient
kernel even when no locator splits over the domain.
