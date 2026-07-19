# ATTACK — xr_eliminant_vanishing_class (medium; post-census Bezout)

## Sharpened form (already in statement.md)
The eliminant is NONZERO on every light profile, so identical vanishing means
lying on a PROPER hypersurface inside the profile cell. So the obligation is
NO LONGER a classification — it is: "per pair (u,v), aligned light triples on
an explicit proper hypersurface are RATIONED (<= poly(n))" — a Bezout/SPI
counting statement.

## What to do
Run E32-extended census (notes/modal_xr_eliminant...py) at n=9..13 FIRST to
fix the observed vanishing classes, THEN write the Bezout bound: the proper
hypersurface has bounded degree (the eliminant's degree), so aligned triples
on it are degree-bounded => poly(n) by Bezout. Likely shares the deep-link
staircase / SPI budget machinery. Cite only proved incidence inputs. If a new
identically-vanishing class appears at toys, report it (falsifier).
