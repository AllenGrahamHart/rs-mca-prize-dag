# Proof

At `tau=1679`, put

```text
A=1114369,  A-K=65793,  c=2A-n=131586,  n-A=982783.
```

For `h=38384`, PR `#1173`'s ordered-basis count gives

```text
N_1=5061797488,  N_2=422717509.
```

The dimension-two pair-type cap is `M_2=253`, so
`R_2=(n-A)M_2=248644099`. The complete paid transverse ledger is

```text
near                                      134944
high tail                    63463433414902515
anchor                                    982783
rank-one transverse          41243110864829984
rank-two transverse         105106214156829391
------------------------------------------------
E_transverse                209812758437679617.             (1)
```

Thus an unsafe line leaves at least

```text
E_nt=B*+1-E_transverse=65167969673715471                    (2)
```

nontransverse slopes. Dividing by `R_2` forces `262093370` represented row
spaces. Canonical promotion and merge give dimension-two or dimension-three
containers. Since

```text
M_3=4047,  R_3=(n-A)M_3=3977322801,
```

(2) forces at least `ceil(E_nt/R_3)=16384884` distinct containers, each with
at least `h+1=38385` common actual zero coordinates.

Suppose now that `r=dim(V_nt)<=9`. Every nontransverse pair differs from the
fixed anchor in both coordinates by an element of `V_nt`, so the complete
nontransverse family lies in one common-support two-fold affine `V_nt` list.
The ordinary affine-span theorem bounds the corresponding ordinary list by

```text
M_r=floor(C(n-K+r,r)/C(A-K+r,r)) <= M_9=66298487937.
```

The exact cap is monotone over `0<=r<=9` at this row. Moreover
`M_9^2<2130706433^6`, so sub-square interleaving leaves at most `M_9` ordered
pair types. Fixed-pair ownership contributes at most `n-A` slopes per type,
giving

```text
R_9=(n-A)M_9=65157026870188671.                            (3)
```

Adding (3) to (1) yields `274969785307868288`, below `B*`; this contradicts
unsafety. Hence `dim(V_nt)>=10`. But `V_nt<=C'` and `dim(C')<=10`, proving
`dim(V_nt)=dim(C')=10`.

An exact scan of every legal cutoff shows that `h=38384` is the global
maximum paid by the dimension-nine formula, at cutoffs `1676..1679`; cutoff
`1679` has the largest slack. At `h+1`, the total exceeds `B*` by
`2062328934603`. For dimension ten, the formula increases with `h`; scanning
all cutoffs at `h=0` finds the minimum at `tau=872`, where the total is
`1048057349706085243`, over budget by `773076621594690156`.
