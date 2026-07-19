#!/usr/bin/env python3
"""F5 proof program P2 (Modal): the targeted live-syzygy hunt.

L3a (proved) forces any live dependence into RICH COVERING designs: every
point of every participating support covered >= 3 times, pairwise cores
<= k+t-2. This hunt searches exactly that corner: small triple-covering
designs, exact F_q linear algebra, adversarial freedom over domain points
AND slopes.

Per configuration: supports S_1..S_m (size A = k+sigma) on P points with
pairwise |S_i & S_j| <= k+t-2 and min point-coverage >= 3; assign domain
values x_1..x_P in F_q (random draws) and slopes z_i (random distinct);
build the dependence system: for each point column x and each of the two
moment rows, sum_i lambda_i * a_{S_i}(x) * (1 or z_i) = 0, where a_S(x) =
top