# Cycle 367: MCA K'=72 flat-circuit coupling closes the split-section census (2026-08-16)

Cycle 366 isolated the leading `(33,8)<(36,5)` flag and left a weighted
support-four/support-five target.  A direct circuit-minimality coupling now
closes that target without classifying individual degree-34 split cores.

## Cycle pins

```text
our start:       e1c3640c0
our end:         cycle commit containing this record
canonical prize: 28a62b400
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
open upstream:   #1170 at 1ca90d4c570e3630b62c4cca084549282f1d7418
```

## Flat-circuit coupling theorem

Let a finite matroid on `N` labelled elements have every rank-three flat of
size at most `B` and every rank-four flat of size at most `B+1`.  If `C_4`
and `C_5` count four- and five-circuit supports, then

```text
5 C_5 <= (B-3) C(N,4) - (N-B) C_4.                (FC)
```

For a rank-three flat `F` of size `b`, every independent triple in `F` and
point outside `F` gives an independent four-set.  Its rank-four closure has
at most `B+1` points, and a five-circuit completion cannot return to `F`
without containing a dependent proper subset.  Relative to the unrestricted
`B-3` completion ceiling, this loses at least `b-3` completions.  Each
independent four-set has only four triples.  Summing these witnesses and
using

```text
sum_F t_F(b-3) >= 4 C_4
```

proves `(FC)`.  The theorem is matroidal; representability is not needed.

## K'=72 specialization

Divide the 36-point flag locator from the five-dimensional correction
space.  Residual degree is at most 35 on

```text
N=67544-36=67508
```

outside points.  An independent triple in the original outside evaluation
matroid leaves a two-dimensional residual annihilator and therefore a closure
of at most 34 points; an independent four-set leaves one residual section
and therefore a closure of at most 35 points.  Thus `(FC)` applies to the
original restricted matroid and gives

```text
5 C_5 <= 31 C(67508,4) - 67474 C_4.
```

The independent-triple cap is

```text
C_4 <= floor(31 C(67508,3)/4)=397371647886059.
```

The exact selected-incidence objective is increasing in `C_4`: one extra
four-circuit can reduce the integer five-circuit cap by at most 13,495, while

```text
21 C(m-4,7) - 15*13495 C(m-5,6)
 = 195 C(m-5,6) > 0.
```

At the endpoint, `C_5<=2463704216893565`.  Keeping ordinary `C(36,r)` caps
for every lower inside/outside stratum, with no parallel-class refinement,
gives

```text
I_4 <= 506389674857089789010503158660245768712830400,
I_5 <=   2212036714331204501716306860191372678671248,

21 I_4 + 15 I_5
 <= 10667363722713853636746310934768031733149507120.
```

This is below the required split-section cap by

```text
9885600480815705838297234461816703140525428870.
```

The previously red K72 split-section census is therefore `PROVED`.

## Atlas boundary

Exploratory atlas replay confirmed that paying the original two-step flag
reveals the same carrier-size trichotomy at the adjacent one-step cell.  More
generally, whenever `(M_3,M_4,M_5)=(30,31,31)` and `1<=M_2<=29`, the carrier
sizes remain `(32,34,35)` and maximal overlaps have residual sizes two and
three.  This is a route compression opportunity, not yet a promoted row
closure.

A broad replay expanding the full invariant family exceeded the 270-second
Modal subprocess ceiling.  It produced no counterexample, but its truncated
diagnostic is not used as evidence.  The next replay must Pareto-compress the
family before geometry expansion and emit only the maximal branches.

Primary and independent Modal checks pass for the generic theorem and K72
specialization, including sharp uniform-matroid controls and 12 hostile
contract mutations.  Peak RSS was 60 MB.  The manifest replay compiled
2,548 nodes and 7,582 edges with SHA-256
`78a5003244e09c68b8f41775714465665c7c005132746194dd0073c9b43ef646`.

```text
result:                PROVED K'=72 weighted split-section census
newly closed rows:     none
closed prefix:         10..71
remaining rank nine:  72..15528
new nodes:             1 PROVED
status promotion:      1 TARGET -> PROVED
new premise:           none
critical status delta: none; one background route node promoted green
upstream delta:         none; flat-circuit theorem is a future #1170 export
delta-star movement:   none
compute:               exact Modal arithmetic, <=61 MB; one atlas timeout
next route action:     build a Pareto-compressed complete K'=72 atlas replay,
                       then close the row or isolate its next exact survivor
```

