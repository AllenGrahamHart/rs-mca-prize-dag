# Source and route audit

Date: 2026-07-12.

1. The migrated claim that survey “Theorem 4.7” identifies interleaved MCA
   with base MCA is incorrect and irrelevant to the list challenge. In the
   survey source, Lemma 4.7 gives
   `eps_mca(C^{==s},delta)<=s eps_mca(C,delta)`.
2. Survey Lemma 2.10 is the list statement. It bounds every `m`-interleaved
   list by a fixed power of the base list, uniformly in `m`, but the exponent
   and combinatorial factor do not automatically fit the finite `2^-128|F|`
   budget at the candidate corridor.
3. The proved codegree Theorem C is valid for every `m`. Its recursion admits
   the finite-depth closed form proved in `list_codegree_closed_form`; this
   removes the need to expand a binary tree separately for each arity.
4. A global “all words are a-regular” route is false. The upstream overlap
   packet contains an explicit finite-field `K_(2,2)` over-agreement witness
   where the interleaved list exceeds both participating row lists. Only a
   theorem pricing the irregular stratum, not an assertion that it is absent,
   can use that route.

The remaining direct work is now precise: provide exact base-list envelopes
`B_j` at the finitely many doubled agreements, evaluate the closed form against
the challenge-field budget for the input `m`, and match the resulting safe
index with an explicit lower staircase at the preceding index.
