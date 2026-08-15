# Proof

Put

```text
n=1048618,       m=67514,       q=32,
R_min=274980728111260126.
```

Use the preceding full-deficit capacity for every support stratum.  Every
independent support-five deletion has at most `q` completions.  There are six
exhaustive cases.

Choose a deletion with the maximum completion count.  If that maximum is
`q-s` for `0<=s<=4`, its direct
support-five deletion count uses exactly `q-s`, while the cross-support
theorem caps each target support `d` satisfying

```text
5+(s+1)d-s-1<=10
```

by

```text
C(q+4+s(d-1),d) C(m-d,11-d).                       (1)
```

Intersect these caps with the preceding supportwise caps and weight support
`d` by its full-shadow deficit `C(11-d,2)`.  For defects zero through four,
the exact premiums are

```text
s=0  3982795567806168516229316108688140450163630384
s=1  32010916243694499800320717073630461749362242674
s=2  38248686795246707324552098975684990817633239548
s=3  37909212899522784820182461169606692027883637848
s=4  37569681406601825198675563099275312923276993433.
```

Otherwise the maximum is at most `q-5`, so every support-five deletion has
at most `q-5` completions.  The
ordinary deletion count then gives

```text
39561073029598078809344868550502487135515187669.    (2)
```

Taking the maximum of the six branches gives (2).  This saves

```text
1358455685574599016032497232831377276386431865
```

from the uncoupled premium.

The all-core chart is maximized at core `41` with value
`9275468231667667`.  Retaining all kernel coranks gives

```text
K_cap=17118437512304869669174162767031044097864380317587792249408.
```

The rank-nine marks and full-rank capacity are respectively

```text
39184442698700870613155525220929985265240350768921233121073054790,
910235915731681560754887897376310981744678105658368636509811656.
```

Adding the kernel yields the capacity in the statement.  Sharp isolated
incidence gives demand `R C(m,11)-C(n,11)`, producing the printed gap at
`R_min`.  The variable-record coefficient and exact floor-record cross are

```text
55 C(m,11)-premium
=143327002558240027109345932105933013269257449851>0,

224456707837460696716722330982796481350734785231787345508364676>0.
```

Thus the inequality persists for every `R>=R_min`.  Repeating all six
branches at `K'=43` gives capacity excess

```text
2590504432899371163130658487199612335023802688487478696166262,
```

so `K'=43` is retained as the first wall.  QED.
