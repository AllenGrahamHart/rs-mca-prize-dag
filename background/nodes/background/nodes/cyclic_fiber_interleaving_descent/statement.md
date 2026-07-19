# Cyclic-fiber agreement descends to an interleaved quotient list

- **status:** PROVED
- **consumer:** `petal_small_scale_staircase_census`

Let `H<=F^*` be cyclic of order `n`, let `M|gcd(n,k)`, and let `K<=H`
have order `M`. Put

```text
C  = RS[F,H,k],
C' = RS[F,H^M,k/M].
```

For a received word `U` and an integer `A` divisible by `M`, let
`N_M(U,A)` count degree-`<k` codewords whose exact agreement set with `U`
is `K`-invariant and has size `A`. Then

```text
N_M(U,A) <= L_M(C',A/M),
```

where the right side is the worst common-support `M`-interleaved list size
at agreement `A/M`. Consequently, if `L=L_1(C',A/M)<|F|`, then

```text
N_M(U,A) <= floor(L(|F|-1)/(|F|-L)),
```

and `N_M(U,A)<=L` whenever `L^2<|F|`.

If `K` is the exact stabilizer of the agreement support, its quotient support
in `H/K` is aperiodic. Applying `exact_support_interleaving_projection` with
the aperiodic-support property gives the corresponding explicit bound in
terms of the ordinary **aperiodic** quotient-row list, without discarding the
primitive structure.
