# Proof (of the PROVED components only; Statement U itself is a TARGET)

## 1. The fibre cap (FIB) — pigeonhole

Let `W = S_1 u S_2` be the common support of the two syndromes, `|W| = r+f`
with `f >= 1`. A structural (fibre) slope `gamma` is by definition witnessed
by a locator `S_gamma` of size `r` contained in `W`, and the error vector
`e_0 + gamma e_1` vanishes off `S_gamma`. Two distinct structural slopes
cannot share a locator: if `S_gamma = S_gamma'` then `(gamma - gamma') e_1`
vanishes off a set of size `r` while `e_1` has support of size `> r` inside
`W` (column-farness), forcing `gamma = gamma'`.

Each `S_gamma` omits exactly `f` points of `W`, and the omitted `f`-sets of
two distinct structural slopes are disjoint: a point omitted by both carries
`e_0 + gamma e_1 = e_0 + gamma' e_1 = 0`, hence `e_0 = e_1 = 0` there, hence
it is not in `W`. Disjoint `f`-subsets of an `(r+f)`-set number at most
`floor((r+f)/f)`, so

```text
T_fib <= floor((r+f)/f) = floor(r/f) + 1.
```

The two displayed forms are equal for every `r >= 0`, `f >= 1` (integer
identity; the verifier checks it on a wide range and at the razor value of
`r`). At `f = 1` the cap is exactly `r+1`.

## 2. The floor and the equality case

If the ratio `chi = e_1/e_0` has degree `d` on the common support, its fibres
have size at most `d`, so the number of distinct values — each of which is a
structural slope — is at least `ceil((r+1)/d)`. Equality with `r+1` demands
`d = 1`, which forces `|W| = r+1` (hence `f = 1`) and `chi` injective, in
which case every value of `chi` is a slope and the floor meets the cap. This
is exactly the LB1 configuration.

## 3. (U-SYM): the razor kill

Let `D` be invariant under a `mu_M` action and let the locator be
orbit-invariant, `sigma(X) = L_B(X) G(X^M)`. On such a domain the Hankel rows
whose index is not `0 mod M` collapse on the orbits that the error support
does not meet; killing those orbits with the locator leaves only the rows
indexed `0 mod M` as genuine conditions. There are `ceil(rho/M)` of them, and
they constrain the single unknown `gamma`. Hence the carrier is generically
empty as soon as `ceil(rho/M) >= 2`, i.e. as soon as `M < rho`.

At razor `rho = 2^34` and `M = 2` (negation closure, which the official
power-of-two multiplicative subgroup has) the system is over-determined by

```text
ceil(rho/2) - 1 = 2^33 - 1 = 8589934591 conditions.
```

The count contains no `q`: **it is a rho-threshold, not a field threshold.**
This is why the measured excess at `rho = 2` (one condition, one unknown —
a solution per invariant locator) does not survive to razor rho, and why any
far-CA counting argument that treats `D` as a generic point set is unsound at
small `rho`.

## 4. What is NOT proved here

`T_rand` is unpriced: no bound, no mechanism, no measurement. Statement U is
`T_sym = T_rand = 0`, so U remains a TARGET and `(U-VAL)` remains conditional
on it. The `rho = 3` symmetric-T variant is unmeasured. The `C(128,63)` /
`C(127,64)` identification is refuted (ratio exactly `128/65`), so `T_sym`
does not inherit the qcore cap by identification.
