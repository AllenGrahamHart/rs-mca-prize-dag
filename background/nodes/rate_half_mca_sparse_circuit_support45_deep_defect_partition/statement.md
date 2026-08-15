# Deep support-four/support-five defect partition

- **status:** PROVED
- **source supports:** `4,5`

For one record, let `M_4,M_5` be the maximum completion counts of an
independent deletion at supports four and five, with `M_c=0` when the
support-`c` circuit stratum is empty.  With `q=K-10`, define

```text
s_4=q-M_4,       s_5=q-M_5.
```

Then `0<=s_4,s_5<=q`, and the `(q+1)^2` exact defect pairs form a disjoint
exhaustive partition.  On pair `(s_4,s_5)`:

1. every inherited cap is retained;
2. the source-`c` deletion cap uses ceiling `q-s_c`;
3. every valid cross-support carrier cap is retained; and
4. if `s_4+s_5<q`, the joint zero-carrier and support-four external charge
   apply.

Thus the former fallback/fallback leaf can be refined without a new premise.
For any nonnegative weighted premium, a branch vector componentwise dominated
by another branch vector may be discarded when taking the maximum.

## Falsifier

A completion maximum outside `0..q`; two exact defect pairs classifying the
same maximum tuple; loss of an inherited cap; use of the joint charge when
`s_4+s_5>=q`; or deletion of a branch vector not componentwise dominated by
a retained vector.
