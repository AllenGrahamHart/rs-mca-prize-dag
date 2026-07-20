# DSP8 nodal target-divisor pruning

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_dsp8_correlation_bound`
- **dependency:** `f3_h3_dsp8_nodal_trace_parameter_router`

Use the nonnode parameterization from `(NTP1)`, suppress its common nonzero
cube-root scale, and write

```text
q(a)=a(a+1),
T(a)=(R(a),U(a),V(a))
    =(-1/q(a),-a^2/(a+1),(a+1)^2/a).                (NDP1)
```

The admissible parameters have `a notin {0,-1}` and
`a^2+a+1!=0`. Define the six-value Mobius orbit

```text
S(a)={a,-a-1,a^(-1),-(a+1)/a,-a/(a+1),-1/(a+1)}.  (NDP2)
```

For any two admissible parameters `a,b`, the unordered root multisets in
`T(a)` and `T(b)` are equal, and equivalently have a common positive root,
if and only if

```text
b in S(a).                                          (NDP3)
```

The nodal DSP8 target has both exact forms

```text
t(a,b)=((ab-1)(ab+a+1)(ab+a+b)(ab+b+1))
       /(q(a)^2q(b)^2),                              (NDP4)

t(a,b)-1=-(q(a)+q(b)+3q(a)q(b))/(q(a)^2q(b)^2).    (NDP5)
```

Consequently `t=0` is contained in the positive-overlap orbit and is already
removed by signed disjointness. The excluded identity target is exactly

```text
q(a)+q(b)+3q(a)q(b)=0.                              (NDP6)
```

Thus a complete nodal packet generator may canonicalize `(NDP2)` while
retaining exact decoration multiplicities, reject `b in S(a)`, reject every
one of the nine tests `T_i(a)+T_j(b)=0`, and reject `(NDP6)` before computing
richness or the quotient-line weight. These are exact pruning rules. They do
not bound the remaining signed-disjoint, nonidentity pair correlation and do
not promote DSP8.
