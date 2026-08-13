# Proof

## Lower-aware convex envelope

The parent theorem proves, for `r` distinct peeled parameterized lines,

```text
0<=ell_i<=g_i<=m-1,
sum_i g_i<=S_r:=min(r(m-1),e+C(r+1,2)c),           (LA1)
```

and bounds line `i` by

```text
f(g_i)=(N-g_i)/(m-g_i)=1+(N-m)/(m-g_i).           (LA2)
```

The function `f` is increasing and strictly convex.  Since line labels are
irrelevant to the sum, first sort the lower bounds decreasingly.  Any
feasible core vector can also be sorted decreasingly without violating the
sorted lower bounds: if `ell_i>=ell_j` but `g_i<g_j`, swapping `g_i,g_j`
preserves both lower constraints.

Now take two nonterminal coordinates `x_i>=x_j` and move as much mass as
possible from `x_j-ell_j` to `x_i`, stopping when `x_i=m-1` or
`x_j=ell_j`.  Convexity gives

```text
f(x_i+d)+f(x_j-d) >= f(x_i)+f(x_j).               (LA3)
```

Iterating `(LA3)`, and using monotonicity to spend all available mass, shows
that a maximizer is obtained by starting at the sorted lower-bound vector
and filling its coordinates successively to `m-1`.  Call this vector
`x(ell,S_r)`.  Therefore the integer number of removed slopes is at most

```text
L_r=floor(sum_i f(x_i)).                           (LA4)
```

Unlike the parent envelope, `(LA4)` cannot erase the forced lower bounds by
placing all core mass on unrelated coordinates.

## Recursive certificate

After `r` lines have been removed, unsafety forces the residual family to
have more than `B-L_r` slopes.  The parent exact-layer line bank has base
`C_e` and `G_e` slots, so it forces another slot of integer size

```text
lambda_r=ceil((B-L_r-C_e+1)/G_e).                 (LA5)
```

For `lambda_r>=2`, its total core is at least

```text
ell_r=max(ceil((lambda_r*m-N)/(lambda_r-1)),0),    (LA6)
```

and at least `u_r=max(ell_r-c,0)` of that core lies in the fixed
`e`-coordinate direction support.  Distinct lines have inside-core
intersections at most `c`, so `s` positive lower bounds obey

```text
sum_i u_i-C(s,2)c<=e.                             (LA7)
```

The strict reverse inequality contradicts unsafety.

## Official arithmetic

For both `e=130220` and `e=130221`, the guarded moving cutoff is `65515`.
At the start of the final peel there are 37 lower bounds.  Their sorted
runs and the maximizing allocations are

```text
e=130220:
  ell = 15816*4, 2046*33
  x   = 18769, 15816*3, 2046*33
  S_37=133735, floor(sum f(x_i))=609

e=130221:
  ell = 15816*4, 2046*33
  x   = 18770, 15816*3, 2046*33
  S_37=133736, floor(sum f(x_i))=609.
```

Equation `(LA5)` forces one final threshold `20`.  The resulting 38
inside-core lower bounds have runs `15811*5,2041*33`, hence

```text
5*15811+33*2041-C(38,2)*5 = 142893 > e.           (LA8)
```

This proves both supports.

At adjacent `e=130222`, the exact compiler reaches 288 removed lines.  The
only positive total-core lower bound is `9741`; `(LA4)` permits allocation
`67453*5,1037,0*282`, with charge `4910044`.  The residual target is then
`11867171`, below the certified base `12148280`, so `(LA5)` cannot force
another line.  This is only the exact wall of this envelope.
