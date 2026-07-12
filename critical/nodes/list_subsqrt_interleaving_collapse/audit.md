# Audit: sub-square-root interleaving collapse

## Construction read: NO ISSUE

For every projection, its image is an ordinary list because linear
combinations preserve every common agreement coordinate. Cauchy-Schwarz gives
the stated lower bound on projection-fiber collisions. A fixed distinct tuple
pair solves the vector equation for at most `|F|^(m-2)` coefficient vectors;
this remains true when several row differences are dependent. Double counting
and rearranging gives the printed rational upper bound with positive
denominator. Integrality and `L^2<|F|` give equality, including `L=1`.

The diagonal lower bound uses only a maximizing ordinary received word, which
exists because the spaces are finite. The case `m=1` is separate and immediate.

## Consumer-backward read: NO ISSUE

At the base safe point, `L<=B*=floor(q/2^128)` and `q<2^256` imply
`L^2<q`, so the theorem supplies the required safe inequality for every arity
with no denominator change. At the preceding base unsafe point, diagonal
embedding supplies the required strict lower witness for every arity. The same
adjacent indices are therefore valid.

This audit does not prove the base adjacent crossing. That exact premise remains
in the red ancestry of `list_adjacency_closing`.
