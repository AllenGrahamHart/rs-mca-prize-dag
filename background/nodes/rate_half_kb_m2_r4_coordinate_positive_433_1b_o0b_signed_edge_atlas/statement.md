# KoalaBear m2 r4 positive `433-1b/O0b` signed-edge atlas

- **status:** PROVED
- **scope:** target-sign quotient for the residual route `433-1b -> O0b`
- **unit:** complete twelve-row target product/squared-sum lanes

The common graph has loop `A`, singleton pairs `AB,AC`, and pair `BC` of
multiplicity two. The outside graph has colored edges `BE,CF`, pairs `DE,DF`
of multiplicity two, and singleton `EF`:

```text
common: l=(1,0,0), m=(1,1,2)
outside: r=(0,1,1), l=(0,0,0), m=(2,2,1).
```

The loop spends one collision-defect unit. Each of `BC,DE,DF` is either
opposite-signed at zero further cost or repeated-signed at cost two. Since
the total defect is at most three, exactly four strata occur:

```text
S0:  BC,DE,DF all split              defect 1
SBC: BC repeated; DE,DF split        defect 3
SDE: DE repeated; BC,DF split        defect 3
SDF: DF repeated; BC,DE split        defect 3.
```

The 224 active-sign assignments have exactly ten target-gauge lanes:

```text
S0:  2 orbits of size 16
SBC: 4 orbits of size 16
SDE: 2 orbits of size 32
SDF: 2 orbits of size 32.
```

Every lane contains twelve target records and gives degree four at each of
`A,...,F`. The atlas does not assign source labels, prove a lane realizable or
empty, count distinct affine slopes, close K3, or prove a Prize endpoint.
