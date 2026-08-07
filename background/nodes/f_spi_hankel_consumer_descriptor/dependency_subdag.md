# Dependency sub-DAG

```text
spi_component_control [PROVED exact incidence components] --req--+
                                                                +--> f_spi_hankel_consumer_descriptor [PROVED]
payment_completeness [PROVED first-owner classification] --req--+

f_spi_hankel_consumer_descriptor [PROVED]
  --req--> f_prize_consumer_flat_scope [CONDITIONAL]
```
