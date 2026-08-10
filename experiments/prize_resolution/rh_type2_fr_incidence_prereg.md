# Preregistration: type-2 FR incidence-only route test

## Question

Does the proposed max-intersection input `(FR)` follow from the numerical
support facts currently used by `(NEWCAP)` alone?

The test is deliberately narrower than the algebraic Hankel-pencils problem.
It asks for a finite set system satisfying the exact endpoint parameters and
all of the following incidence statements:

```text
m=4, N=16m=64, rho=4m-1=15, T=rho+2=17,
|S_gamma|=rho,
sum_x (m-d_x)=1,
|S_gamma union S_gamma'|>=a=7m-1=27,
|S_gamma \ W|>=R+1-a=m+2=6,
|W|=a.
```

The registered route falsifier is one such system with

```text
max_gamma |S_gamma intersect W|>2m=8.
```

This would prove only that the cardinality, saturation, pairwise-union, and
individual-distance inequalities do not imply `(FR)`. It would not refute
`(FR)` for realizable strict-`A=3` Hankel pencils, because the test does not
construct the corresponding vectors, syndromes, or apolar generators.

## Construction frame

Let `H` be the quartic-residue subgroup of `F_17^*`, and let
`A_0,...,A_3` be its four multiplicative cosets. On

```text
D={0,1,2,3} x F_17^*
```

define one block for every `gamma in F_17` by

```text
B_gamma={(i,gamma+a): a in A_i, gamma+a != 0}.
```

Delete `(0,1)` from `B_0`. The four cosets form a disjoint difference
family: for every nonzero additive difference, the total number of ordered
within-coset representations is `|H|-1=3`. Therefore every block has size
15, every point has degree 4 except `(0,1)`, which has degree 3, and every
pair of blocks intersects in at most 3 points.

The Modal task searches only for the distinguished 27-set `W`: it chooses
9 points of `B_0` and 18 points outside `B_0`, accepting exactly when every
block meets `W` in at most 9 points. The accepted `B_0` then violates the
registered `2m` bound by one.

## Decision rule

- `WITNESS`: all displayed identities pass and the maximum intersection is
  at least 9. Bank a route-fence theorem and move the positive attack to the
  generalized locator polynomials or the Hankel pencil.
- `NO_WITNESS`: no witness is found before the bounded search ends. This is
  evidence only and changes no status.
- Any failed construction identity voids the run.

## Compute envelope

One Modal container, one CPU, 256 MB, 60-second hard timeout. The search
checkpoints its trial count in the returned payload and has no local fallback.

## Registered scale follow-up

The first run returned a valid `m=4` witness on its first trial, with maximum
intersection `9>8`. After recording that output, register the same construction
at

```text
m=64, 4m+1=257, N=1024, rho=255, T=257, a=447.
```

Here `3` is a primitive root modulo the Fermat prime `257`. Accept only if the
same identities hold and some block meets `W` in `3m-3=189` points, versus
`2m=128`. This follow-up distinguishes a linear incidence gap from the
one-point gap at `m=4`. It has the same nonclaim: no Hankel pencil is built.
