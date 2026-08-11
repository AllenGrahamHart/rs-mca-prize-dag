# Audit

1. The auxiliary field `F_257` constructs a finite set system; it is not an
   official challenge field and is not presented as one.
2. The witness uses `m=64`, a power of two, and violates the `2m` conclusion
   by `m-3`, avoiding a one-point-only diagnosis.
3. The quartic difference-family identity proves the block sizes, degree
   profile, and pairwise-union bound without relying on the searched `W`.
4. The Modal search selected only `W`. Its output is reduced to a fixed
   1024-bit certificate and replayed independently; search success is not
   itself the proof.
5. The theorem rules out only derivations for an arbitrary distinguished
   `W`. The witness `W` is not a pair union. When `W` is a minimum pair union,
   the omitted combinatorial structure proves the corrected canonical bound.
6. The two verifiers construct cosets and block membership differently and
   fail closed on mask and deletion mutations.
