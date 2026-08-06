# Proof

The branch order laws and field cap give `e<=6`, `k|e`, and
`k in {1,2,4}` on the plus branch, `k in {2,4}` on the minus branch.
Before applying the field cap, divisibility gives

```text
k=1: e in {1,2,3,4,5,6},
k=2: e in {2,4,6},
k=4: e=4.
```

Only `e=6,k=2` needs removal. If `p^6<2^256`, then `p^3<2^128`.
On the plus branch `p=c*2^40+1` with `c` odd. The cube bound leaves only
`c=1,3,5`, but the three candidates have divisors `257,7,3` respectively.

On the minus branch write `p=c*2^b-1`, `b>=40`, with `c` odd. The cube
bound leaves only

```text
b=40: c=1,3,5;
b=41: c=1,3;
b=42: c=1.
```

They are composite, with respective displayed divisors

```text
3, 144899, 179; 13367, 5; 3.
```

For `b>=43`, already `(2^43-1)^3>2^128`. This excludes order two at
degree six and proves exhaustiveness.

Nonemptiness reuses the five certified generating witnesses. The plus
order-one witness supports every `e<=6`; the plus and minus order-two
witnesses support `e=2,4`; each order-four witness supports `e=4`. Their
largest indicated powers remain below `2^256`. Comparing `k` and `e` gives
the seven non-generating types. QED.
