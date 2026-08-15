# Proof

Fix an independent `(c-1)`-set `A` with `q-1` completions.  Their labels
have private completion coordinates, so they are independent and span a
hyperplane `Lambda_0` of the `q`-dimensional annihilator `Lambda`.  All lie
on

```text
U=A union {the q-1 completions},       |U|=q+c-2.    (1)
```

Every support-`c` label in `Lambda_0` is supported inside `U`: compare its
representation on its circuit with its representation on `U`.  Their union
has size at most `q+2c-2<=K`, so evaluation independence forces the two
representations to agree coordinatewise.

If every support-`c` label lies in `Lambda_0`, (1) is already the claimed
carrier.  Otherwise choose one outside label with support `D`.  It and
`Lambda_0` span `Lambda`, so

```text
Lambda <=E_(U union D),       |U union D|<=q+2c-2.  (2)
```

For any other support-`c` label, compare its circuit representation with
the representation supplied by (2).  The union has size at most

```text
q+3c-2<=q+10=K
```

exactly for `c<=4`.  Vandermonde independence forces its support into
`U union D`, proving the carrier alternative.

If no deletion has `q-1` completions, every deletion has at most `q-2`.
As in the parent completion ladder, one selected eleven-set cannot contain
two completion labels.  Summing

```text
max_(0<=b<=q-2) b C(m-c+1-b,11-c)
```

over all `(c-1)`-deletions and dividing by the `c` charges of every circuit
gives the second term in `(NS)`.  On the `K'=22` specialization, the parent
ratio test is increasing through `b=q-2=10`, giving the printed caps.
