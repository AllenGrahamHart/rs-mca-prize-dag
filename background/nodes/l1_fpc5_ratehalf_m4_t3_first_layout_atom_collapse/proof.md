# Proof: rate-half FPC5 `M=4,t=3` first-layout atom collapse

Apply `l1_general_first_layout_domination` to the selected post-owner class
and the first admissible maximal `M=4` source layout. Every selected codeword
not among the layout's four planted anchors is carried in this same layout in
its exact core-defect normal form. The four anchors contribute the first term
in (AC1); no later source layout contributes another non-planted member.

Classify the non-planted members by their exact full-petal profile in this
fixed layout. A `t=3` member has one unique touched subset of three petals,
and a four-petal layout has exactly

```text
binom(4,3)=4
```

such triples. For a fixed triple, the source labels are fixed, distinct, and
nonzero before affine normalization. The proved source cross-ratio reduction
normalizes them to `(0,1,lambda_T)`, where

```text
lambda_T=(c_3-c_1)/(c_2-c_1) notin {0,1}.
```

Thus `lambda_T` is data of the fixed source/triple, not a free summation
parameter.

The Johnson-nonpositive tail has the integer range

```text
1<=a<=floor((b-3)/4).
```

The exact complement-slice theorem identifies every member in a fixed
`(T,a)` cell bijectively with its guarded LS6 atom. These cells are disjoint
because the touched triple and exact defect are reconstructed from the
contributor. This proves (AC1).

There are at most four triples and fewer than `n` possible values of `a`.
If each atom is at most `B(n)`, summing (AC1) gives (AC2). QED.
