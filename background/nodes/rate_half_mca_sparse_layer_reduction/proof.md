# Proof

Fix a received pair `(f_1,f_2)`.

Suppose first that it is column-far: no pair `(p_1,p_2) in C^2` agrees with
`(f_1,f_2)` on at least `a` common coordinates. A slope is MCA-bad exactly
when its line word has an agreement witness of size at least `a`, because
every such witness necessarily fails mutual extension. This is exactly the
far-pair CA-bad condition. Its slope count is at most `B_ca^far(a)`.

Suppose instead that the pair is column-close. Choose `(p_1,p_2) in C^2`
whose common error set has size at most `r`, and put

```text
epsilon_i=f_i-p_i.
```

Then

```text
|supp(epsilon_1) union supp(epsilon_2)|<=r.
```

At slope `gamma`, translation by the codeword `p_1+gamma p_2` bijects
agreement witnesses for the original line with witnesses for
`epsilon_1+gamma epsilon_2`. Translating a proposed common explanation by
`(p_1,p_2)` also shows that a witness extends mutually before translation if
and only if it extends mutually afterwards. Hence the two pairs have exactly
the same MCA-bad slope set, whose size is at most `S_sparse(a)`.

The two cases prove

```text
B_mca(a)<=max(B_ca^far(a),S_sparse(a)).
```

Conversely, every far-pair CA-bad slope is MCA-bad, and sparse pairs are a
subclass of all received pairs. Therefore `B_mca(a)` is at least each term on
the right. This proves `(MS1)`. The budget equivalence `(MS2)` follows by
taking the maximum. QED.
