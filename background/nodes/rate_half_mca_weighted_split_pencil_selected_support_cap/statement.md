# Weighted split-pencil selected-support capacity

- **status:** PROVED
- **scope:** finite weighted points and distinct affine lines

Let affine-plane points `p` have integer weights

```text
0<=s_p<=A-1,       sum_p s_p<=S,       A>=3.
```

For every line `L` in a finite set of distinct affine lines, choose integers
`0<=x_(L,p)<=s_p`, supported on points of `L`, with

```text
sum_(p in L) x_(L,p)=A.
```

Put

```text
Q_L=sum_(p in L) C(x_(L,p),2),       W=sum_L Q_L,
h=floor(S/(floor(A/2)+1)).
```

Then

```text
W <= floor((A-2)S^2/8)+C(S,2)+C(h,2)C(A-1,2).       (SP1)
```

The three terms pay, respectively, lines with one selected dominant owner
and no second globally heavy owner, balanced selected partitions, and lines
containing at least two globally heavy owners.

## Nonclaim

The bound is not asserted sharp. It does not count slopes, infer a
split-pencil representation, or control charges that are not attached to
one exact selected-support partition of mass `A` on each line.

## Falsifier

A weighted affine-plane instance satisfying every displayed hypothesis with
`W` larger than `(SP1)` refutes the theorem.
