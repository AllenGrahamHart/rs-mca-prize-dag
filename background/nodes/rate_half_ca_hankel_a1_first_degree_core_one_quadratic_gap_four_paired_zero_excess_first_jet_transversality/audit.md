# Audit

1. The nonincidence Forney identity is never extended to a support root.
   The incident calculation uses the minimum word `g_delta`; the difference
   from the full source is exactly the actual error `e_delta`.
2. The sign convention is fixed by
   `b=f-c^L=(f-c_delta)+(c_delta-c^L)=e_delta+g_delta`.
3. `Q_t`, `Q_X`, and `G_X` are nonzero at the selected support roots.
   `G_t` need not be nonzero and is not divided by.
4. A common component is excluded from a transverse smooth point before
   the padding count is used. Thus equation `(9)` counts only roots that can
   genuinely belong to the gcd.
5. At most `b` selected fibers lose the full `X`-degree `a`, because the
   leading `X`-coefficient of the gcd is a nonzero parameter polynomial of
   degree at most `b`.
6. The padding bounds are packet-wide upper bounds. No distribution or
   independence assumption is used.
7. The final strict count loses at most one classified row where the
   parameter-leading coefficient of the `X`-linear factor vanishes. It
   also uses the separately proved fact that every off-line specialization
   of `G` is nonzero.
