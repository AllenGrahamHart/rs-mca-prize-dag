# Audit - L1 m=4 positive-valuation value-coset certificate

1. The product of roots equals the depressed value only when `R(0)=0`; this
   is why the theorem is restricted to `nu>0`.
2. Products of points in one domain coset lie in one value coset, so value
   ratios lie in the subgroup even when the domain itself is not a subgroup.
3. `N=p+1` and `n=4N`; hence every ratio has an `N`th power in `mu_4`.
4. Frobenius gives `w^p=w^N/w`, with no assumption that the domain coset is
   Frobenius-stable.
5. All 16 ordered quarter pairs are checked.
6. Quotient remainders are exact large-integer finite-field arithmetic, not
   floating point or random search.
7. A zero pair of remainders means both roots satisfy both power equations;
   a linear remainder is checked at its unique candidate.
8. Surviving quadratics have nonzero discriminant five and no degenerate
   value among `0,1,u,v`.
9. The three surviving quarter pairs times two roots are one six-element
   permutation orbit, not three projectively different triples.
10. The invariant is `a^3+8b^2=0`; signs follow from
    `Y^3-2s^2Y+s^3`.
11. The two no-pair rows close only positive valuation; `nu=0` remains.
12. The theorem does not close the latter two positive rows or L1.
