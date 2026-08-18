# Cycle 516: endpoint design upstream export

## Result: BANKED in draft PR #1170

The two exact `q=3170` endpoint reductions have been added to the existing
conditional `(Q)` / base-field-normalized split-pencil packet.

```text
PR:                         przchojecki/rs-mca #1170
parent extension commit:    6186c7b1
endpoint extension:         dab75a23
plane-line source commit:   f0a13cc6e33399aa8192bf4879b9a9e7941371e3
plane-line source tree:     1763c945b9e4031424099486ecf7d44a9bc021a2
direction source commit:    1db90bbbef8c8e31b881de04dc9cedb387728c0f
direction source tree:      ddcb65d9d490042a6215457db9c1214246d2b456
PR comment:                 issuecomment-5334889900
```

The packet now verifies, under its complete-family endpoint hypothesis,

```text
339<=number of full 218-point planes<=358,
number of saturated plane pairs>=22752,
number of saturated 15-point lines>=217,
41746<=number of represented saturated directions<=47836,
minimum roots per represented line or direction>=2351,
aggregate unused direction degree<=30203244.
```

Normal and optimized primary and independent replays pass, optional source
replay checks both separately pinned nodes, and 40/40 hostile mutations are
rejected.

## Burn-down

```text
starting local pin:       1db90bbbe
canonical prize pin:      0dd5b3244
upstream PR #1170 pin:    dab75a23
DAG status delta:         none
crosswalk delta:          +2 proved conditional route-cut rows
compute spend:            none
next action:              quotient-periodic classification or common-factor forcing
```

## Nonclaims

- the complete-family source hypothesis remains conditional upstream;
- aggregate direction saturation is not an individual splitting theorem;
- no endpoint family, rank-eleven row, or prize problem is paid.
