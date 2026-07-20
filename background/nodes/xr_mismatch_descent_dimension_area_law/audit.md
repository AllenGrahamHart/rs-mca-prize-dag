# Audit

- Counted transitions `j<L`; the final live state supplies the endpoint
  `N_L>=K_L+h>=h+1`.
- Kept ambient loss and dimension loss separate. The first gives `(XDA1)`;
  the second telescopes exactly to `(XDA2)`.
- Used `K_j+h=(K_j-1)+(h+1)`, preserving the load-bearing `+1`.
- Applied the threshold bound only to indices with `K_j>=kappa`; no claim is
  made about nodes in other branches.
- Checked every official table entry with exact integers.
- The theorem is pathwise. It does not multiply, sum, or otherwise pay branch
  widths, and it does not promote the consumer.
- No computation or unproved premise is used.

