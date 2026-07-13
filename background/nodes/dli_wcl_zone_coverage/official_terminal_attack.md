# Official terminal-block attack ledger

## Exact terminal obligations

The actual schedule ends in

| `ell_j` | `N_j` | WCL weights | smallest one-orbit charge in window |
|---:|---:|---:|---:|
| 1 | 256 | 2..6 | `512*2^-6 = 8` |
| 2 | 512 | 3..7 | `1024*2^-7 = 8` |
| 4 | 1024 | 5..9 | `2048*2^-9 = 4` |
| 8 | 2048 | 9..13 | `4096*2^-13 = 1/2` |
| 16 | 4096 | 17..21 | `8192*2^-21 = 1/256` |

Thus WCL-ZONE requires **zero** primitive orbits throughout the full windows
at `ell in {1,2,4,8}`. At `ell=16`, one weight-17 orbit already
violates the bound, one weight-18 orbit saturates it, and higher-weight orbits
must be counted exactly. Deeper levels are genuinely weighted rather than
zero-event obligations.

The ledger is raw: multiplier shadows, additive clusters, and level lifts are
charged at their own level and weight. Ownership metadata cannot delete their
mass from C1'. At the four zero-event levels this repair does not change the
obligation, because any ownership class is nonempty exactly when its raw
ledger is nonempty.

## Two exact scope controls

1. `dli_wcl_scope_guardrail` proves that an isolated order-512 row can have a
   primitive weight-3 orbit of charge `64`. It fails the ambient split.
2. `dli_wcl_engineered_terminal_scope` recovers the strongest banked
   engineered weight-6 witness. Its exact norm is `2q` with a 256-bit prime
   factor satisfying `v_2(q-1)=9`, so this construction also fails the ambient
   split by 32 powers of two.

These are not evidence that official WCL is true; they prove only that both
known attacks were terminal-level constructions and cannot be transported
silently to the production tower.

## Exact weight-3 and weight-4 exclusions at `ell=1`

At `ell=1`, shift and odd Galois dilation preserve the cyclotomic norm. A
complete search quotients reduced signed supports by the
affine action

```text
e -> a e + b mod 512,  a odd,
```

before factoring norms. `dli_wcl_weight3_ambient_exclusion` certifies the
complete result:

```text
11,054,080 reduced signed supports
       254 affine-Galois norm classes
       439 distinct certified prime factors
         0 factors q<2^256 with v_2(q-1)>=41
        18 maximum v_2(q-1) below the cap
```

`dli_wcl_weight4_ambient_exclusion` applies the same norm principle through a
normalized-section compiler:

```text
1,398,341,120 reduced signed supports
    1,014,080 normalized-section keys
       24,979 affine-Galois norm classes
       44,599 distinct certified prime factors
            0 factors q<2^256 with v_2(q-1)>=41
           29 maximum v_2(q-1) below the cap
```

Therefore no official production row has a primitive weight-3 or weight-4
relation in either `ell=1` level. Weight 2 is elementary. Weights 5 and 6
remain open, so WCL-ZONE remains open.

## Bounded weight-5 falsification

`dli_wcl_weight5_first64_mitm_exclusion` checks the first 64 primes of the
form `q=k*2^41+1`, in increasing positive `k`. The exact range is

```text
3 <= k <= 996,
6,597,069,766,657 <= q <= 2,190,227,162,529,793.
```

Proper-divisor witnesses certify all 932 intervening values composite, and
direct Pocklington witnesses certify the 64 selected values prime. On every
prime row, an exact pair/triple meet-in-the-middle search checks all 130,560
legal pairs and 22,108,160 legal triples. No reduced weight-5 relation is
found. This is an exact finite no-hit theorem, not an exhaustive weight-5
exclusion.

## Exact weight-3 exclusion at `ell=2`

At `ell=2`, the first odd-index vanishing equation already forces a signed
weight-3 polynomial to vanish at an order-1024 root. The normalized-section
norm census `dli_wcl_ell2_weight3_ambient_exclusion` gives

```text
88,954,880 reduced signed supports
   521,220 normalized-section keys
       510 affine-Galois norm classes
     1,329 factor records, 1,141 distinct certified prime roots
         0 roots q<2^256 with v_2(q-1)>=41
        21 maximum v_2(q-1) below the cap
```

Thus weights 2 and 3 are absent at the official `ell=2` level. Since this is
an emptiness level, weights 4 through 7 must still be excluded before that
level is closed.

## Algebraic weight-4 exclusion at `ell=2`

The second odd-index equation removes weight 4 without a norm census. For the
four signed roots `r_i=s_i omega^e_i`, the equations are

```text
sum_i r_i = sum_i r_i^3 = 0.
```

Newton's identities make the monic root polynomial even, so its roots occur
in antipodal pairs. A reduced signed support with distinct base exponents
contains no antipodal pair. The proved node
`dli_wcl_ell2_weight4_newton_exclusion` therefore excludes every weight-4
relation over every official field. Weights 5 through 7 remain at this level.

## Global Newton cutoff

The same argument works uniformly. If the first `ell` odd power sums vanish,
Newton's identities kill every odd elementary symmetric coefficient through
degree `2ell-1`. Therefore a relation of weight `w<=2ell` is impossible at
odd weight and antipodal at even weight. The proved node
`dli_wcl_newton_short_window_exclusion` gives the complete tower reduction

```text
ell=1:  weights 2--6; Newton excludes 2; prior norms exclude 3,4; residual 5,6
ell=2:  weights 3--7; Newton excludes 3,4; residual 5,6,7
ell=4:  weights 5--9; Newton excludes 5,6,7,8; residual 9
ell>=8: weights ell+1--ell+5; Newton excludes the entire window
```

Thus only six weight slots remain across all 34 production levels:

```text
(1,5), (1,6), (2,5), (2,6), (2,7), (4,9).
```

## Next attack

The preferred next target is `(ell,w)=(2,5)`; its two moment equations should
be used together before any norm sweep. At the terminal `ell=1` levels,
weight 5 is likewise unresolved. Directly
extending the normalized section would require choosing three free tail terms
and is much larger than the completed weight-4 computation. The pair/triple
compiler is now validated, but extending its prime range indefinitely cannot
prove the ambient theorem. The global route still needs an algebraic
obstruction from the `2^41` splitting requirement, or a rigorous orbit/norm
reduction with a feasible class and storage bound. A separately preregistered
small weight-6 round is useful as a falsification probe because a six-term
isolated-row witness is already known, but it must not be confused with
closure.
