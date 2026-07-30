# Proof

## 1. The degree-10 catalogue and the block kernel

Write the six original blocks as B_0,...,B_5. Let H_i be the block
stabilizer induced on B_i and let P_i be the image of N on B_i. The complete
terminal catalogue is

~~~text
H_i              |H_i|       simple socle     subdegrees
A5                   60       A5               1,3,6
S5                  120       A5               1,3,6
PSL(2,9)            360       A6               1,9
PGL(2,9)            720       A6               1,9
PSigmaL(2,9)        720       A6               1,9
M10                 720       A6               1,9
PGammaL(2,9)       1440       A6               1,9
A10             10!/2        A10              1,9
S10             10!          A10              1,9.                 (1)
~~~

The quotient H_i/P_i is a quotient of the stabilizer of one point in the
outer degree-six action. Consequently

~~~text
|H_i/P_i| <= 5! = 120.                              (2)
~~~

If P_i is nontrivial, almost simplicity makes it contain the simple socle
S_i of H_i, and [P_i,P_i]=S_i. Conjugacy of the six blocks makes the same
alternative hold in every coordinate.

## 2. The kernel-free exceptions have no quartic suborbit

Assume P_i=1. Then (1)-(2) leave only H_i=A5 or S5. Since every coordinate
projection of N is trivial, N=1. The full group acts faithfully on the six
blocks, and its block stabilizer G_(B_i)<=S5 maps onto H_i. If H_i=S5,
orders force this map to be an isomorphism. If H_i=A5, the only possible
orders for G_(B_i) are 60 and 120. The order-120 case would be S5 and would
require a quotient S5 onto A5 with kernel of order two, impossible because
S5 has no normal subgroup of order two. Thus this map is again an
isomorphism, and

~~~text
|G|=6|H_i|=360 or 720.
~~~

Thus G=A6 or S6 in its natural degree-six action. The unique degree-10
actions of its point stabilizer A5 or S5 are the actions on two-subsets of
the other five points. The resulting degree-60 G-set is

~~~text
Omega={(i,A): i in {1,...,6}, A subset {1,...,6}-{i}, |A|=2}.       (3)
~~~

The exact flag-stabilizer orbit calculation gives

~~~text
A6: 1,2,3,3,3,6,6,6,6,6,6,6,6
S6: 1,2,3,3,3,6,6,6,6,6,6,12.                      (4)
~~~

Neither row has subdegree four. The actual irreducible bidegree-(4,4)
component supplies a G-point-stabilizer suborbit of size four, contradicting
(4). Hence P_i is nontrivial.

## 3. Scott strips

Put D=[N,N]. By Section 1,

~~~text
D <= S_0 x ... x S_5,      projection_i(D)=S_i,
~~~

so D is subdirect in six isomorphic nonabelian simple groups. Scott's lemma
writes it as a direct product of full diagonal strips whose supports
partition the six coordinates. Since D is characteristic in N and N is
normal in G, the support partition is G-invariant. The outer action is
transitive, so all support parts have one common size

~~~text
t in {1,2,3,6}.                                     (5)
~~~

If t=1, D is the independent product. Fix alpha in B_0. The stabilizer
D_alpha contains the full transitive factor S_j on every other B_j. Since
the actual quartic suborbit is transverse, it meets some B_j other than
B_0, where its D_alpha-orbit would have size ten. This contradicts its size
four. Therefore t>1.

## 4. Untwisting each strip

Every automorphism of each simple socle in (1) is realized by a permutation
in its degree-10 action:

- S5 in its two-subset action realizes Aut(A5);
- Aut(A6)=PGammaL(2,9) of order 1440 acts on the same ten points;
- S10 realizes Aut(A10).

Moreover, each socle point stabilizer has exactly one fixed point, as the
subdegree rows in (1) show. The action centralizer is therefore trivial. To
see this, a centralizer element sends alpha to a point fixed by S_alpha; the
only such point is alpha. Transitivity then makes the centralizer element
the identity.

For each Scott support T, untwist its actions and identify every B_i,
i in T, with one common ten-point set X_T. The strip socle then acts by

~~~text
(x,i) -> (s*x,i).                                    (6)
~~~

Take g in G carrying T to another support T'. Conjugation by g induces one
isomorphism of the two strip socles. If n_i is the restriction of g from
B_i to B_{g(i)} in the chosen coordinates, all n_i implement that same
isomorphism. Hence n_j^(-1)n_i centralizes the common socle action for every
i,j in T. Triviality of the centralizer gives n_i=n_j.

It follows that g maps synchronized columns to synchronized columns:

~~~text
C_(T,x)={(x,i):i in T},       |C_(T,x)|=t.           (7)
~~~

As T ranges over the Scott supports and x over X_T, (7) is a G-invariant
partition of all 60 sheets into blocks of size t.

## 5. Strict lower-degree routing

By the monodromy/intermediate-field correspondence and Luroth's theorem,
the block system (7) gives a geometric functional decomposition of the same
endpoint map with inner degree t. Equations (5) and t>1 give

~~~text
t in {2,3,6}<10.                                    (8)
~~~

The source-pencil/transverse compiler applies again to this strictly
smaller decomposition. Thus no m=10 case remains terminal: all four of its
transverse types route into the already-live m=2,3,6 rows. Removing those
four independent producers from the 22-type frontier leaves 18 types in
degrees 2,3,4,6. QED.
