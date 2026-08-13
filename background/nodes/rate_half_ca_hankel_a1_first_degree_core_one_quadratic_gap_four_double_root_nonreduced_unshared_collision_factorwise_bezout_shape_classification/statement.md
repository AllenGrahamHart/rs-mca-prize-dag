# `A=1` nonreduced collision factorwise Bezout shape classification

- **status:** PROVED
- **closure:** the surviving `d_A=1` factor profile has only four shapes
- **consumer:** `rate_half_band_crossing_location`

Retain the unshared nonreduced collision with `d_A=1`. Thus

```text
G(t,X)=c Q_L(t,X) product_(j in O)Q_j(t,X),
deg_(t,X)G=(e-2,p-3),       2p=3e-1,              (FBS1)
```

where `Q_L` is the unique large-odd factor and every factor in `O` is
ordinary even. For a factor of bidegree `(m_j,n_j)`, let

```text
b_j=ord_tau Q_j(t,x_*),
ell_j=I_((tau,x_*))(Qbar,Q_j).                    (FBS2)
```

After the first copies of the `e-7` off-line padded-heavy points are
assigned factorwise, let `r_j` be their number on `Q_j`. Put

```text
t_j=m_j-r_j-b_j.                                  (FBS3)
```

Then every quantity in `(FBS2)--(FBS3)` is nonnegative and

```text
sum_j r_j=e-7,       sum_j b_j=2,       sum_j t_j=3,
ell_j=2b_j.                                          (FBS4)
```

The factorwise residual Bezout capacity is exhausted exactly:

```text
c_j:=e n_j+(3e-2-(3p-2))m_j=r_j+ell_j.            (FBS5)
```

For the large and ordinary factors this says respectively

```text
(3m_L-e)/2=r_L+2b_L,       m_L=e+2b_L-2t_L,
3m_j/2=r_j+2b_j,           m_j=2(b_j-t_j).         (FBS6)
```

Consequently the complete factorization has one of only four shapes:

```text
A. Q_L: (m,n;r,b,t;ell)
          =(e-2,(3e-7)/2; e-7,2,3;4),
   with no ordinary factor;

B. Q_L: (e-4,(3e-13)/2; e-8,1,3;2),
   plus one Q_2: (2,3; 1,1,0;2);

C. Q_L: (e-6,(3e-19)/2; e-9,0,3;0),
   plus one Q_4: (4,6; 2,2,0;4);

D. Q_L: (e-6,(3e-19)/2; e-9,0,3;0),
   plus two Q_2 factors, each (2,3; 1,1,0;2).      (FBS7)
```

Here the first pair is `(m,n)`, the next triple is `(r,b,t)`, and the
last entry is `ell`. For `e>=11` all four shapes satisfy every degree and
nonnegativity gate. At `e=7` only A remains, and at `e=9` only A and B
remain. In particular, at every relevant large row the unique
large factor has parameter degree at least `e-6`, and all ordinary-even
companions have total parameter degree at most four.

## Scope

The theorem classifies possibilities; it does not assert that any of the
four shapes occurs. It does not exclude the irreducible shape A or the
low-degree companions in B--D.
