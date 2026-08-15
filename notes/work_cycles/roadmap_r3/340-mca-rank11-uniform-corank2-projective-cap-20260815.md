# Cycle 340: MCA rank-11 uniform corank-two projective cap (2026-08-15)

This cycle closes the first target minted by the cycle-339 scope repair.
The missing issue was not Reed-Solomon realizability at one exceptional
chart.  It was an abstract multiplicity-aware basis count that pays every
shortening gap at once.

## Rank-three bounded-parallel theorem

Let `M` be a loopless rank-three matroid on `m` elements with every parallel
class of size at most `a`.  The new universal leaf proves

```text
2 b(M) >= (m-1)(m-1-a).                             (BP)
```

The proof is deletion-contraction at an element `e` in a smallest parallel
class `P`, `|P|=c`.

- If `e` is a coloop, the deletion is rank two.  Its class sizes `q_i`
  satisfy `sum q_i^2<=a sum q_i`, which gives `(BP)` directly.
- Otherwise deletion retains rank three and induction applies.
- In the contraction, `P minus e` is the loop set and every nonloop parallel
  class is a union of original classes, hence has size at least `c`.
  There are at least two such classes, so

  ```text
  b(M/e)>=c(m-2c)>=m-2.
  ```

  The last inequality follows from `m>=3c`; its residual at `m=3c` is
  `(c-1)(c-2)`.
- The induction sum exceeds the target by exactly `a-1`.

The bound is sharp when `a` divides `m-1`: take one coloop over a rank-two
matroid whose parallel classes all have size `a`.

## Reed-Solomon specialization

After rank-eight canonical-basis cancellation and deletion of all global
zero normals, write

```text
t=K'-10-z,       0<=t<=K'-10<=1048566.
```

The corank-two chart has

```text
(n,K,m,s)=(1048578+t,2+t,67474+t,2).
```

Support-local transversality leaves `w+1=67473` normals outside every
rank-one span.  Thus every parallel class has size at most

```text
a=m-(w+1)=t+1.
```

Applying `(BP)`, every record owns at least

```text
3*w*(w+t+1),       w=67472,
```

ordered independent triples.  The uniform record envelope is therefore

```text
H(t)=(R+t)(R+t+1)(R+t+2)/(3*w*(w+t+1)),
R=1048576.
```

Its successive ratio has the sign of

```text
2*t+3*w+3-R,
```

so `H` has one turn and its maximum on the official interval is at an
endpoint.  Exact endpoint division gives

```text
floor(H(0))       = 84416263,
floor(H(1048566)) = 40828171.
```

The next-integer gaps are `10721959296` and
`9846731093898357072`, respectively.  Hence `84416263` is uniform, with
the complete chart as the exact maximizer.

## Bounded computation and audits

One 512 MB, 60-second-limited Modal container exhaustively checked all
`1048567` integer rows as a falsifier and arithmetic audit:

```text
run: https://modal.com/apps/allengrahamhart/main/ap-e01IzeB6DxEniL8hsMBRyC
maximum cap: 84416263 at t=0
t=1 cap:     84415253
far cap:     40828171
first excess: none
```

The universal proof does not depend on the scan.  Focused proof verifiers:

```text
MATROID_RANK3_BOUNDED_PARALLEL_BASIS_FLOOR_PASS
  checks=5604 ceilings=12 controls=6/6
MATROID_RANK3_BOUNDED_PARALLEL_BASIS_FLOOR_AUDIT_PASS
  partition_checks=248 contraction_checks=200
RATE_HALF_MCA_RANK11_KERNEL_CORANK2_UNIFORM_PROJECTIVE_BASIS_CAP_PASS
  cap=84416263 endpoints=3 controls=6/6
RATE_HALF_MCA_RANK11_KERNEL_CORANK2_UNIFORM_PROJECTIVE_BASIS_CAP_AUDIT_PASS
  endpoint_checks=3 turn=423078/423079
```

The existing exact 190,666-row hierarchy replay and independent audit then
promote the corank-two capacity cut from conditional to proved:

```text
unconditional kernel cutoff: 568338
first method wall:            568339
```

The corank-three capacity node remains conditional only on the one open
uniform cap `M_3<=983902549`; its `M_2` premise is now discharged.

```text
DAG delta:             +1 universal PROVED matroid node
                       corank-two uniform cap TARGET -> PROVED
                       corank-two capacity CONDITIONAL -> PROVED
critical orbit census: unchanged at 167/37/27
unconditional kernel: K'=10..568338 excluded
remaining kernel:      K'=568339..1048576
delta-star movement:   none
compute:               one 512-MB/60-second Modal container, about 8 s wall
next route action:     attack uniform corank three with the analogous
                       rank-four bounded-point/line multiplicity problem
```
