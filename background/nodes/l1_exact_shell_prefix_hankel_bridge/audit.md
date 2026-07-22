# Audit - L1 exact-shell prefix/Hankel bridge

## Checked axes

1. The prefix has exactly `a-k` coefficients, in degrees `k,...,a-1`.
2. Exact shells, rather than raw support fibers, are used in the list sum.
3. Agreement shells are disjoint by exact agreement size.
4. The missed-core convention is `D=C\A`, not the retained core.
5. `|X|=d+w+1` includes the required `+1`.
6. Multiplication by `L_(C\D)` is triangular only on the high coefficients;
   no claim is made about the complete coefficient vector.
7. The base polynomial `Q` disappears only because `deg Q<k`.
8. Both core and noncore no-extra-agreement guards are retained.
9. The zero target is preserved chartwise; arbitrary nonzero fibers are not
   identified across retained cores.
10. Toy power-sum Q and F2 growing-order Myerson are explicitly fenced from
    automatic consumption.

## Route effect

The former vague phrase "internal rechart payment" is no longer the only L1
route. A global exact-shell row-sharp Q theorem would pay the mixed bucket
directly. If that theorem is unavailable, the direct saturated-Hankel route
remains exactly the fixed-source problem already isolated in the DAG.
