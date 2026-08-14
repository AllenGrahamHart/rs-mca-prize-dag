# Cycle 277: rate-half Shape-A three-source-class rank amplification (2026-08-13)

The dominant-component rank theorem uses an earlier residual parameter and
does not transfer to Shape A. The correct input is the later first-degree
marked-source frame: its degree-`e` primitive locator has `e+1` independent
coefficient vectors, for the same `e=(2^39+1)/3` used in Shape A.

Because `d_A=1`, every `x in U_0` lies in one of three source classes. On
each class the evaluated locator row is a fixed quadratic parameter
multiple of the corresponding evaluated split-biform row. Injective
evaluation on `U_0` therefore gives

```text
sr(Qbar)=e+1<=3sr(G),
sr(G)>=ceil((e+1)/3)=61083979322.
```

```text
rank-three branch:       excluded
all ranks <61083979322:  excluded
surviving rank interval: [61083979322,e-1]
critical status effect:  none
hostile mutations:       7/7
```

The rank-three incidence/genus router remains a valid conditional theorem,
but it is no longer a live Shape-A branch. Future work should attack the
macroscopic-rank interval directly.
