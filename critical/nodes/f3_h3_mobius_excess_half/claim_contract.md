# Claim contract: C36' cutoff-18 weighted excess

- **claim id:** `f3_h3_mobius_excess_half`
- **statement:** for every official row, `17X_18<=300n^2` with the exact
  `P`, `R`, and `X_18` definitions in `statement.md`
- **scope:** all `n=2^s`, `13<=s<=41`, and all official primes
  `p=1 mod n`, `p>=n^2`
- **consumer:** `f3_h3_three_to_one_c36`, nonidentity rich-fiber tail
- **status:** `TARGET`
- **proved dependencies:** quotient-block identity, paired PGL2 identity,
  cutoff-18 compiler, rich-fiber norm cutoff, and exact C36' arithmetic
- **new open content:** on the proved-reduced range
  `n^2<=p<=6^(n/4)`, a joint product/quotient correlation estimate; the
  preferred sufficient aggregate target is `S_ns^rich<=1200n^2`, restricted
  to the actual rich locus `P(t)>=19`
- **falsifier:** one exact official row with `17X_18>300n^2`
- **current proof route:** constants-explicit joint block moment or oriented
  character/Stepanov estimate retaining product/quotient correlation
- **replay:** `python3 critical/nodes/f3_h3_mobius_excess_half/verify.py`
- **upstream mapping:** primitive shift-pair control / exact residual ray
  compiler

Do not replace the joint target by a marginal shifted-energy bound, and do not
consume a pointwise constant-fiber conjecture as a theorem.
