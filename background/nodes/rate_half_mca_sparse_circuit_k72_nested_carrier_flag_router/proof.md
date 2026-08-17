# Proof

Write `F_c` for the span of an attaining independent deletion and `H_c` for
its annihilator in the ten-dimensional correction space. Full completion
relative to the support-two point gives `H_c<=H_2`. Maximal overlap gives
`F_3<=F_4,F_5`, hence `H_4,H_5<=H_3`. The carrier-size identity
`|B_c|=M_c+c-1` gives `32,34,35`, and therefore the residual sizes are two
and three.

Assume first that `R_4 subset R_5`. Then `B_4 subset B_5`. The rank-three
flat `F_4` contains 34 of the 35 ground points in `B_5`; the omitted point
must be outside `F_4`, since `B_5` spans the rank-four flat `F_5`. Thus an
attaining support-five basis has exactly three anchors in `F_4` and one
outside it. Every point of the nonempty `B_2` class is an exact support-five
completion and lies in `F_4`. Its support-five circuit therefore contains
four points in the rank-three flat `F_4`, a dependent proper subset. This
contradicts minimality. Hence residual overlap two is impossible.

Suppose the residuals share exactly one ground point `z`. If `v_z` is
outside `F_3`, then `F_4=span(F_3,v_z)<=F_5`. Consequently `H_5<=H_4`, and
the six-dimensional `H_5` vanishes on `B_4 union B_5`, whose size is
`34+35-33=36`.

If `v_z` lies in `F_3`, then `H_3` also vanishes at `z`. Since `z` is not
in `B_3`, this gives a fixed 33-point set. Independently, Grassmann inside
the eight-dimensional `H_3` gives

```text
dim(H_4 intersect H_5) >= 7+6-8=5,
```

and this intersection vanishes on the 36-point carrier union.

Finally, disjoint residuals give union size `32+2+3=37`; the same Grassmann
bound gives dimension five. If `F_4<=F_5`, then `H_5<=H_4` and dimension six
is available instead. The fixed-union charge and exact arithmetic verifier
give the printed premiums. QED.
