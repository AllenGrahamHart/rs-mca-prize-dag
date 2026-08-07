# KoalaBear fixed R02/R20 rank-drop exclusion

- **status:** PROVED
- **cells:** `{F04,F05,F06,F07} x {R02,R20}`
- **chart:** `V=AE-BD=0`
- **field:** `F_2130706433`, hence `F_(2130706433^6)`

After removing only factors inverted by the original four-variable named
open, `V` has exactly two retained factors in every literal cell. The first
has degree 2 and 6 terms. The second has degree 11 and 116 terms on `R02`, or
degree 14 and 225 terms on `R20`.

For every literal cell and retained factor, adjoin the factor to the four
original q-slice rows. The resulting exact deployed-prime ideal has original
named localizer nilpotence index 2. Therefore all sixteen factor charts, and
hence all eight `V=0` rank-drop charts, are empty.

This does not close the generic `V!=0` charts.
