# Dependency sub-DAG

```text
dli_fixed_weight_ambient_q_bridge (PROVED)
                    |
                    | req
                    v
dli_ambient_q_sqrt_route_no_go (PROVED)
                    |
                    | ev
                    v
dli_c2pp_joint_reserve (TARGET)
```

The supplier identifies ambient Q as a sufficient upper bound. This node
proves that imposing the same square-root scale on that upper bound is false.
The evidence edge records a route cut, not a premise of C2''.

