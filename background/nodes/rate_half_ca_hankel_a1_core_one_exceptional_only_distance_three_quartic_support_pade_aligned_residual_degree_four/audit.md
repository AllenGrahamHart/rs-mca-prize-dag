# Audit

1. Selection frequency uses row blocks: a block with `2e+1` rows can meet at
   most that many disjoint outside orbit-pairs.
2. A nonaligned actual relation meets the static relation class in at most
   `2t` points. Base points are absent because the class pair is primitive.
3. Alignment identifies primitive rational relations. The actual row gcd and
   complement are coprime, so no extra polynomial multiplier is hidden.
4. Every root outside `H` gives a nonzero polynomial of degree at most two in
   `U`; an identically zero specialization would enlarge `H`.
5. The first incidence pass yields degree at most six. The second pass is
   necessary to obtain degree at most four and the printed alignment counts.
6. The exact verifier checks the monotone endpoint inequalities with integer
   arithmetic. Rounded asymptotics are not used.
7. Degree zero is excluded by calibrated internal evaluations, not by merely
   assuming the complements are distinct. The comparison uses three good
   square-norm indices; it does not impose square norms on the tails.
