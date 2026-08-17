## Preregistered cell-3 guarded global common basis

- **decision:** replace the failed raw seven-variable Gröbner endpoint by a
  cached one-dimensional common basis before adding any outside equation
- **scope:** four source-sign rows, common variables `(t,r,c,b)` only
- **launcher SHA-256:**
  `c344181eecbec17bc6677a2751a31dc025035a714f3dff57dd50380e2a4116a6`
- **checker SHA-256:**
  `9a64da492f10fc051cd8b0748d7227c02a8210c954406f62818ec2ddc24949e6`
- **cached common input SHA-256:**
  `28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8`
- **envelope:** four one-CPU workers, 4 GiB each, 240-second Singular
  child wall and 270-second container wall; projected cost below `$0.20`
- **local safety:** one RAM-guarded Modal client under a 330-second external
  hard stop; no local CAS

For each sign row, Singular starts from the three pinned compact equations,
saturates all sixteen route guards, and then saturates by the ideal generated
by all six product cofactors. The latter restricts to the union of the six
rank-five charts, rather than requiring every cofactor nonzero. The complete
reduced basis is printed and checkpointed. Acceptance requires four ordered
rows, dimension one, nonempty complete bases with exact internal hashes,
sign-packet custody, clean transcripts, and three hostile mutations rejected.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 330s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_cell3_global_common_basis_modal.py
```

A checked result is a reusable algebraic representation of the already
proved guarded common curve. It authorizes one preregistered outside-case
diagnostic from the reduced basis; it does not authorize a 24- or 1,416-case
campaign and excludes no outside system by itself.

**Outcome:** `COMPLETE`. Modal app `ap-e7skPdzRi1PIPNxBo3VKdw` returned four
dimension-one bases, each of size 21, in about two minutes. Result SHA-256:
`bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e`.
Basis SHA-256 values in sign order `--,-+,+-,++` are

```text
20d4032b93acc1f0918efea258978bf830a4a7de389442b519e9496f9b6e9df4
a27da16ead59ce535f5fd5017a97c7459de63fab60b1b27456cc82e7cbe20202
f9e7054412eae0ecbd2d0369bbd4ddb9e7ba80b29e59f02ca86cb24ef7a9725e
11e2e6e5abde49d1887ea4b677bcdbb0aefb02b9e7cf696f93e8b04f7b06b0b5
```

The checker accepts four distinct programs and bases and rejects 3/3 hostile
mutations. The known nonfatal Modal async-generator close warning occurred
after the complete checkpoint; the app exited zero.
