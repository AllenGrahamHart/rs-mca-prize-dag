# E1 prize N=256 profile-(3,6) cofactor-16 once-divided exclusion

- **status:** PROVED
- **closure:** exact support branch, product ledger, dual radius census, and certified norm intervals
- **scope:** prize-envelope `N=256`, profile `(3,6,S=18)`, once-divided singleton supports
- **dependency:** energy-adaptive product windows

There is no profile-`(3,6,S=18)` prize collision with norm cofactor `m=16`
whose six-singleton binary support lies in one parity class but not in one
residue class modulo four.

After translation such a support is `2T` in `Z/128`, where the six-term
support polynomial of `T` in `Z/64` has exact multiplicity two at `X=1` and
contains both parities. A complete atlas contains 9,080 affine support orbits
in this branch.

Independent forward and reverse complete radius engines find 1,816,625,504
product-live signed vectors. Certified 48-bit root intervals put
1,816,625,308 strictly below the allowable `16p` interval and 196 strictly
above it; no interval is unresolved.

This proves only the once-divided m16 branch. The 39,936 primitive
multiplicity-four affine support orbits remain open.
