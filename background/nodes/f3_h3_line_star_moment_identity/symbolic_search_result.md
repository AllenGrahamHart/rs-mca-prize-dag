# Bounded canonical-target search

Modal app `ap-lCcgXz0Mo33iwbvN53Jfap` ran the exact SymPy search over all
`81^2=6561` ordered pairs of source-coordinate Laurent monomials whose four
exponents lie in `{-1,0,1}`. It returned exactly one identity:

```text
z=(0,0,0,0), w=(0,0,0,0),
```

namely `z=w=1`. This is the base point of every quotient line and contributes
nothing to `R(t)`. No non-base target point is forced in the tested ansatz.

Replay remotely:

```bash
tools/ramguard modal -- uvx modal run tools/modal_run_script.py \
  --script experiments/prize_resolution/h3_chord_target_identity_search.py
```

The completed worker reported `55 MB` peak RSS. The result is a finite
symbolic no-go fence, not a classification of arbitrary rational target maps.

