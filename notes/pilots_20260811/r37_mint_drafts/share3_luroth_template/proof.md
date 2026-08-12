# Proof (of the PROVED components)

## 1. The Lüroth degree arithmetic and the waste law

If the sharing is realised as a pullback along a degree-`k` map `x -> w`,
then `deg_x = k * deg_w` for any factor pulled back from the `w`-line. The
(BIV-G) budget allows `deg_x <= 3(m-1)`. Maximal sharing takes `k = m-1`,
whence `deg_w = 3(m-1)/(m-1) = 3` **exactly**: the budget is met with
equality and nothing is wasted. For general `k` the unusable remainder is
`3(m-1) mod k`, which at `k = 2` reproduces the one lost unit of the
involution ansatz at even `m` (there `3m-3` is odd, so an invariant factor,
having even `x`-degree, cannot use the last unit).

## 2. The demand calibrations

Direct arithmetic: `3m(m-1) - (rho-1)` with `rho = 4m-1` gives `8, 22, 42`
at `m = 3,4,5`; `D_max = (8m-9) - (4m-1) = 4m-8`; `25 = 36 + 4 - 15` at
`m = 4, k = 2`. Best-achieved supply `8, 12, 9` exceeds the corrected demand
only at `m = 3`. All verified as exact integers.

## 3. Lemma 1 and the flat-supply threshold

Möbius injectivity requires `6m > rho = 4m-1`, i.e. `2m > -1`, which holds
for every `m >= 1`; so no degree-1 factor arises in pencil-image classes.
Combined with AM-HM and Cauchy-Schwarz this yields a required
cross-coincidence growing like `m` minus a constant, hence vacuous at small
`m` and binding from `m = 7`. The constant is soft (`~`) and, as printed, is
off by one against the stated vacuity range; the verifier asserts the literal
form and flags the inconsistency rather than adopting either reading.

## 4. The constant-norm mechanism

Let `nu` be a fixed element of `mu_64` and consider monic cubics
`x^3 + ax^2 + bx + c` whose roots are three distinct elements of `mu_64` with
product `-c` fixed. Since two such cubics share the same `c`, every line
joining them lies in the plane `c = const`, so **the whole line has constant
norm**. Existence of a line with many split members is then forced, not
accidental: fix one root `r`, let the other two roots `s, t` vary subject to
`st = nu/r`, and put `u = s + t`. Then

```text
a = -(r + u),        b = r u + nu/r,
```

which is a line parametrized linearly by `u`. Its split members are exactly
the `u` for which `y^2 - uy + nu/r` has both roots in `mu_64`, of which there
are `~32`.

The verifier enumerates all `C(64,3) = 41664` split cubics at `q = 193`,
confirms `64` equidistributed norm classes of `651`, and scans every class
exhaustively by hashing the line through each pair. It finds a maximum of
`31` collinear split cubics and `9152` lines carrying at least `8`, and it
checks that every line multiplicity is a binomial coefficient `C(t,2)` (so
the counts are consistent).

This proves the mechanism the source asserts, and prices it: the sharing
supply is `Theta(1/N)`, not `Theta(1/q)`.

## 5. What is NOT proved

No `G`, no completion, no bivariate system, and no structurally verified
`m = 4` witness. The `31` and `9152` above count RAW lines, not
structurally-verified complete fibres, and therefore do not supersede the
source's `12/9/9` census. The flat-supply law's conditional death regime for
`q >~ 10^4` and `8 <= m <= 128` is carried from the source, unverified here;
the `o(m^2)` supply bound is not delivered anywhere, and `m = 4` is untouched
by that theorem.
