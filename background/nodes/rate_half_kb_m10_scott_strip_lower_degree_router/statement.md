# KoalaBear m10 Scott-strip lower-degree router

- **status:** PROVED
- **scope:** inner-degree-10 transverse branch of KoalaBear Q=6,s=6,u=2
- **dependency:** rate_half_kb_source_pencil_rank_transverse_compiler
- **consumer:** rate_half_band_closure

Let G be the geometric monodromy of the degree-60 endpoint map in an
inner-degree-10 decomposition. It has six original blocks of size ten, and
let N be the kernel of the action on those blocks.

The complete terminal degree-10 catalogue consists of nine almost-simple
groups with socles A5, A6, or A10. If the projection of N to a block is
trivial, then N is trivial and the full degree-60 action is the explicit A6
or S6 action on flags

~~~text
(i,A),  i in {1,...,6},  A a two-subset disjoint from i.
~~~

Neither flag action has subdegree four, contradicting the actual quartic
suborbit.

Otherwise D=[N,N] is a subdirect product of six copies of the simple inner
socle. Scott's lemma partitions the six coordinates into equal full
diagonal strips of size t in {1,2,3,6}. The independent case t=1 gives a
ten-point orbit in every other original block and is impossible. For
t>1, all automorphism twists of the degree-10 socle action are permutation-
equivalent and the action centralizer is trivial. The synchronized columns
inside every strip therefore form a G-invariant block system of block size
t. Hence the same endpoint map has a second geometric decomposition with
inner degree

~~~text
t in {2,3,6}.                                      (KB10-1)
~~~

Thus inner degree 10 has no terminal producer: every one of its four
transverse types routes strictly to inner degree 2, 3, or 6. The global
independent transverse frontier falls from 22 to 18 types, and the live
decomposition degrees are 2,3,4,6.

This is a strict lower-degree route, not a claim that no endpoint can also
admit a degree-10 decomposition. It constructs no owner, moves no ledger,
and does not close another degree, u=2, cap 68, the adjacent certificate, or
the KoalaBear row.

## Falsifier

A terminal degree-10 primitive group outside the nine-row catalogue; a
kernel-free degree-60 A6 or S6 flag action with subdegree four; a Scott
support size other than 1,2,3,6; an automorphism twist not realized in the
degree-10 action; a nontrivial action centralizer; or failure of the
synchronized size-t columns to give an inner-degree-t decomposition.
