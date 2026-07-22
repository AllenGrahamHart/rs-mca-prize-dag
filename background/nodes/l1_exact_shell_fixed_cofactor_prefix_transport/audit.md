# Audit - L1 fixed-cofactor prefix transport

## Checked axes

1. Codeword shifts preserve exact agreement sets, not only list size.
2. The zero normalized word has only the full-agreement codeword shell.
3. The cofactor leading coefficient equals that of `U` because `L` is monic.
4. The product recursion starts with `l_0=1`.
5. The `t=0` equation fixes no new locator coefficient.
6. The number of nontrivial product equations is `h-k=w+e`.
7. Prefix depth is capped by the full locator degree `a`.
8. Prescribed leading coefficient leaves exactly `e` free cofactor
   coefficients and hence `q^e` choices.
9. The complement gcd is retained for positive cofactor degree.
10. Scalar cofactor makes exactness automatic outside the locator roots.

## Route effect

This theorem identifies the exact portion of arbitrary-word L1 represented
by locator-prefix fibers. The follow-on accounting theorem separates three
issues that this node does not decide: depth-uniform row-sharp constants,
effective-image collapse/divisor-section transversality, and payment above
the `e=k` cap. The formal `q^e` count alone is not described as an
unavoidable loss; the full-locator section gives the exact above-cap object.
