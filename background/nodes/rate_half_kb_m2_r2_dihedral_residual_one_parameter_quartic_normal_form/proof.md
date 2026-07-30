# Proof

Normalize the regular dihedral action on the rational outer component by

```text
u(r)=1/r,       v(r)=lambda/r,
```

where `lambda` has order `n`. The first reflection quotient is
`Y=r+1/r`. Its sibling under the second reflection is

```text
Y(vr)=lambda/r+r/lambda.
```

Eliminating `r` gives

```text
x^2+y^2-a*x*y+(a^2-4)=0,       a=lambda+lambda^(-1). (1)
```

For primitive third and sixth roots, respectively, `a=-1` and `a=1`.

It remains to place the endpoint quadratic relative to `(1)`. Pulling
`h(T)=Y` back to `C` gives a quadratic cover. Its branch places are the
places where a branch value of `h` has odd pullback multiplicity under
`Y`. The source V4 passports give, on the base `C`,

```text
source genus 0: one inertia-a place plus one inertia-ac place;
source genus 1: two inertia-ac places.
```

In either case this quadratic subcover has exactly two branch places. The
map `Y` has branch values `2,-2`. A branch value of `h` outside this pair
has two simple preimages and contributes two branch places; a value in the
pair has one double preimage and contributes none. Since `h` has two
distinct branch values, exactly one lies in `{2,-2}`. Simultaneous sign
change in `(1)` lets us call it `2`; call the other `b`, with
`b notin {2,-2}`.

Put

```text
X=(x-2)/(x-b),       Ynew=(y-2)/(y-b).
```

Solving for the old coordinates gives

```text
x=(bX-2)/(X-1),       y=(bYnew-2)/(Ynew-1).        (2)
```

Substitute `(2)` into `(1)` and clear
`(X-1)^2(Ynew-1)^2`. Rewriting the resulting symmetric bidegree-`(2,2)`
equation in

```text
sigma=X+Ynew,       pi=X*Ynew
```

gives exactly the six coefficients `(KBMN-2)`. This is a direct expansion;
no pole or source equation has been discarded.

Finally choose a source coordinate in which `m composed h(t)=t^2` and
apply the preceding coefficient-quartic pin. Its exact substitution gives
`(KBMN-3)`. The only continuous geometric datum left in the normal form is
`b`; irreducibility and actual source realization remain to be imposed.
QED.
