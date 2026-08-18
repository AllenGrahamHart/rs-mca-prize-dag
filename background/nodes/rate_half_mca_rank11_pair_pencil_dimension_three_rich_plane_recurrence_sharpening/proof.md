# Proof

The parent affine-plane theorem gives 520 selected scalar points in a
three-dimensional scalar polynomial space, affine-line occupancy at most 15,
and affine-plane occupancy at most 218. Let `J` be their complete common
received-pair core and shorten by it. The reversible shortening preserves all
520 residual pair cores, each of size

```text
s'=m-2-|J|=67470+K',
```

on a residual domain of size `n'=1048576+K'`, where `K'=K-|J|`.
The shortening preserves a three-dimensional scalar polynomial space inside
the polynomials of degree below `K'`, so necessarily `K'>=3`. It also
preserves the affine-line occupancy cap 15.

At a residual coordinate, either evaluation vanishes on the complete scalar
difference space, in which case the coordinate belongs to no residual pair
core, or the owners lie in one affine scalar plane. Thus every residual owner
multiplicity is at most 218.

## At most two 189-rich planes

Two distinct affine planes in a three-dimensional affine space intersect in
either the empty set or an affine line. Their selected-type intersections
therefore have size at most 15. If three distinct affine planes each contained
at least 189 selected types, their union would contain at least

```text
3*189-3*15=522
```

selected types. This exceeds the complete population 520. Hence at most two
affine planes are 189-rich.

## Recurrence of one rich plane

Fix a 189-rich affine plane `A`. Its selected points do not lie on one affine
line, because line occupancy is at most 15. The direction space of `A`
therefore contains two linearly independent residual scalar polynomials
`T_1,T_2`, both of degree below `K'`.

Whenever a residual coordinate has owner fiber `A`, evaluation is constant
on `A`; hence

```text
T_1(x)=T_2(x)=0.
```

Put `G=gcd(T_1,T_2)`. If `deg G>=K'-1`, both quotients `T_i/G` are constants,
contradicting the linear independence of `T_1,T_2`. Therefore

```text
deg G<=K'-2.
```

The residual domain has distinct coordinates, so `A` can recur at at most
`K'-2` coordinates. With at most two rich planes this proves `(RP-1)`.

## Exact incidence ledger

Let `d_x` be the residual owner multiplicity. Coordinates outside the
`N_189` rich set have `d_x<=188`; all other coordinates have `d_x<=218`.
Counting the 520 pair-core incidences gives

```text
520s'=sum_x d_x
     <=188n'+(218-188)N_189
     <=188n'+60(K'-2).                              (1)
```

Substitute the residual parameters into `(1)`:

```text
520(67470+K')
 <=188(1048576+K')+60(K'-2).
```

After collecting terms,

```text
272K'<=188*1048576-520*67470-120
      =162047768.                                   (2)
```

Exact division gives

```text
162047768=272*595763+232,
```

so `K'<=595763`. Since `K=1048576`, this is equivalent to

```text
|J|=K-K'>=452813.
```

At `K'=595763`, capacity minus demand is 232. Increasing `K'` by one changes
the difference by `248-520=-272`, so the adjacent difference is `-40`.
This proves all claims. QED.
