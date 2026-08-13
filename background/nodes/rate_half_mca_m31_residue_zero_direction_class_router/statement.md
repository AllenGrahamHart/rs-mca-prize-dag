# Mersenne residue-zero direction-class router

- **status:** PROVED
- **scope:** the first residue-zero full-lift support

Let `D` be one exact deficit-`H` layer on direction support `E`, `|E|=e`.
Every member has `H` inside agreements and `m-H>K-1` outside agreements.
Fix one member.  For every other member, its normalized codeword direction
agrees with the gauged received direction on at least

```text
A=2H-e
```

coordinates.  Distinct normalized directions agree with each other on at
most `c=K-1` coordinates.  If `A^2>ec`, the number of direction classes is
at most

```text
J=floor(e(A-c)/(A^2-ec)).                              (RZ1)
```

Each class and the anchor lie on one affine explanation line.  With

```text
Q=floor((N-e-c)/(m-H-c)),
```

outside-core packing therefore gives

```text
|D|<=1+J(Q-1).                                        (RZ2)
```

At Mersenne-31 `e=98232`,

```text
(s,q,H)=(32742,0,65489),   A=32746,   J=3,   Q=484,
|D|<=1450.
```

The prefix through `H-1` is `16432695`.  The synchronized top union `T`
is one pair-noncontained affine line, so

```text
|Z|<=16434145+|T|,       |T|<=981129.                 (RZ3)
```

Consequently an unsafe family at this support must satisfy

```text
|T|>=343071.
```

The line-packing inequality then forces its total common core to have size
at least `67452=m-2`.  This is the exact residue-zero terminal; `(RZ3)`
does not itself pay the support.
