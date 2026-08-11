# Audit

1. The pole ideal is formed on `C`, so cancellation descends through
   singular points.
2. `2(floor(delta/2)+1)>delta` for both parities of `delta`.
3. The interpolant need not avoid every component. It only must avoid a
   component where the contact section is nonzero; degree `(1,e_i)` would
   make the contact line bundle negative there.
4. Three, not four, contact copies are used. The target has second degree
   `-e+ell+h+2`, while subtracting `C` leaves first degree exactly `-4`.
5. The official modular arithmetic is exhaustive over every integer
   `m<=e<=floor(rho/3)` and every allowed `h`.
6. The sole survivor has `delta=1`, `h=e-2`, and the minimum violating slope
   count `T=rho+2`; weakening any of these equalities changes the route.
