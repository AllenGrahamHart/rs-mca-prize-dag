# Result

The strict `A=3` frontier has collapsed from an `O(m^2)` slope-slack table to
one exact corner. All moving degrees below `floor(rho/3)` are excluded, and
at the top degree every slope count above the minimum violation is excluded.
The only survivor has `delta=1`, `O<=1`, and `T=rho+2`.
