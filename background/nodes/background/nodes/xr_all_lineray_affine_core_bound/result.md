# Replay certificate

The strengthened standalone verifier was shipped by content to Modal and
replayed in app `ap-0uXY2xxIKcCf0u16t4mJTD`. It returned

```text
XR_ALL_LINERAY_AFFINE_CORE_BOUND_PASS small_lines=702 max_pairs=5
selectors=990 max_slopes=3
rowc-r1_4:sigma<=3 rowc-r1_8:sigma<=3 rowc-r1_16:sigma<=3
prize-r1_4:sigma<=3 prize-r1_8:sigma<=3 prize-r1_16:sigma<=3
```

The exhaustive replay checks all 702 nonempty nonconstant syndrome lines for
the length-four ternary repetition code. It verifies the weighted set-pair
charge and cardinality bound on every transverse sparse family, then
enumerates all 990 one-per-slope selectors and verifies `(SEL)` at the exact
minimum selector rank. Removing transversality produces a seven-pair tangent
line exceeding the claimed bound, so the hypothesis is load-bearing. Peak
worker RSS was `56 MB`.

The separate P9 collision-profile replay in Modal app
`ap-EC3OVO0F8gifH3co7fMcj9` retained all original T1--T4 identities. Every
`n=16,k=8` conservative post-deletion high-core family had complete-family
and canonical-selector rank `9=k+1`, and exact search found no selector of
rank at most three. The raw near-pencil controls had rank-one selectors that
were removed by the tangent deletion. This does not challenge the theorem;
it certifies that the open high-transversal-rank branch is already populated
in toy rows and that the strip hypothesis changes the rank conclusion.

After manifest refresh, the repository-wide Modal replay passed `126/126`
verifiers with no failures, timeouts, hash mismatches, or remote errors in app
`ap-CjPRwq11iMq0L6nqBWPyQG`. The five integration gates passed in
`ap-NY6cp85J71Zo8rqvQLNFUv`, retaining exactly nine open critical truth leaves.
The critical orbit was rebuilt remotely in `ap-8QsNCW9ju10c9oDmDnp7LX`.
