# proof: ef_component_control_alignment

The extension-fiber alignment incidence has the same algebraic form as the
incidence controlled by `spi_component_control`:

```text
I_{u,v} = { (Z,[l]) : M(Z) l = 0 },
```

where `M(Z)` is the Hankel pencil attached to the B-rational pair `(u,v)`.

The proved `spi_component_control` packet applies to this Hankel
slope-incidence variety: one horizontal scroll over the generic-rank locus and
at most `t` rank-drop fibers, with controlled Segre degree. Removing the
base-descended section and restricting to already-paid strata are closed
sub-incidence operations; they cannot create new irreducible components beyond
the controlled components of the ambient incidence.

Therefore the EF horizontal-component classification problem is finite and
degree-controlled exactly as required by `ef_ru`.
