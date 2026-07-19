# Frontier

There is no independent large-arity truth leaf. The proved
`list_subsqrt_interleaving_collapse` theorem shows that whenever the ordinary
worst list has size below `sqrt(|F|)`, every common-support interleaving has
exactly the same worst list size.

At the prize-safe point the ordinary list is at most
`floor(|F|/2^128)`, whose square is strictly below `|F|` under the official
cap `|F|<2^256`. At the preceding unsafe point, diagonal tuples preserve the
ordinary witness. Therefore all arities share the base adjacent crossing.

The frontier has moved entirely to the base adjacent theorem represented by
the existing red ancestry below `list_adjacency_closing`.
