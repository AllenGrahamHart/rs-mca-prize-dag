# paid_ext_fn proof

There are two cases.

On generating rows, the node `generating_escape` proves that the extension
escape column is zero: the generator field is already the row field, so there
is no nontrivial intermediate extension contribution to price.

On non-generating rows, `ext_import` proves that the extension-pole witness
count crosses the gate exactly at the imported S7 list window. Therefore the
extension paid column is computed by applying that imported list-window rule
to the base row.

Combining these two cases gives the stated function `Paid_ext(A)`: zero on
generating rows, and the imported extension-pole/list-window count otherwise.
