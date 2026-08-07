# Proof

For two generic quadratics, direct expansion proves

```text
Res_w(Aw^2+Bw+C,Dw^2+Ew+F)
  =(AF-CD)^2-(AE-BD)(BF-CE).
```

The linear combination `DP-AQ=-(Vw+U)` proves the generic reconstruction.
The auxiliary identity `AZ-BU+CV=0` gives

```text
V^2 P(-U/V)=A(U^2-VZ),
V^2 Q(-U/V)=D(U^2-VZ),
```

so compatibility is also sufficient on `V!=0`. If `V=0`, the same linear
combination forces `U=0` at every common root, establishing the retained
rank-drop branch.

The upstream compiler at exact commit
`55ac3e07477bd7a768190a3e755f22b0d44354b0` reconstructs each literal
q-slice system from the pinned 36-cell atlas, performs the quadratic
compression over `QQ`, and
records the resultant and terminal factor fingerprints of `U,V,Z`. An
independent official SageMath 10.9 Modal review ran all twelve cells in
separate processes. Every shard matched the exact PR #1149 certificate:

```text
PASS=12, FAIL=0, TIMEOUT=0, REMOTE_ERROR=0.
```

The `R02/R20` resultants have degree 42 and 3,679 terms; the `R11`
resultants have degree 38 and 2,464 terms. Grouping the exact resultant and
three core hashes produces exactly the six pairs in `(KBFQ-3)`, each of
size two and covering all twelve cells.

The pinned objects are:

```text
certificate raw SHA-256  1b4e7b8c6c284f5bdfa1634d54bfc6aafc188adea21c9c4578e21d766ca6125b
certificate payload      4adc4187bb5794ed70fce122055fb94916974c1adacf9451237aff002ebfd63e
Sage compiler             d64dfd1a2806eec3d4788eb3c4b990f87bb8655fa9cf91d83393bd217dd7fddb
Python verifier           4c66a081e4fe0a821c96326489698df6a22e4c1281efc34005cbdf5b525a8b04
theorem note              a1fa5172dc1643cc9b72894fa2110f2e90a54558a2975b9519a25328f9b4057b
Modal review ledger       473710b935f7866f185e6ad9a0938a3a49215031c30c54e19a023a22dcacd6d5
```

The fail-closed upstream Python verifier independently passes all 11 hostile
mutations and the five generic symbolic identities. Thus the exact
dichotomy and six-orbit literal compression are proved. QED.
