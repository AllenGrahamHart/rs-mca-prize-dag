# Proof: official two-petal codimension sieve

The list threshold for two full petals gives

```text
2ell+r>=d+ell=2ell+s,
```

so `s<=r<=b`. Put `j=ell-b>=1`.

At rate `1/2`, the source equation is `k+1=4ell+b`, hence

```text
5ell=k+1+j.
```

The official `k=2^40` satisfies `k==1 mod 5`. Therefore `j==3 mod 5`.
Since `j>=1`, actually `j>=3`. From `s<=b=ell-j`,

```text
c_slice=ell-s-1>=j-1>=2.
```

At rate `1/4`, exact core defect gives `d=ell+s<=k-1`, so

```text
c_slice=ell-s-1>=2ell-k.
```

The source equation `3k+1=4ell+b` becomes

```text
5ell=3k+1+j.
```

Consequently

```text
2ell-k=(k+2+2j)/5 >= (k+4)/5,
```

because `j>=1`. This proves both bounds. QED.
