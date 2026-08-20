# Visualisation contract

Create diagrams only from observed metadata or clearly labelled inference.

## Required views

- Model topology: facts, dimensions, bridges, helpers and relationship cardinality.
- Filter-path map: cross-filter direction, bidirectional edges, inactive edges, loops and ambiguity.
- Dimension map: conformed dimensions and connected facts.
- Hierarchy trees: explicit, inferred and source-defined hierarchies labelled separately.
- Date-role map: active/inactive relationships and business date roles.
- Grain matrix: one-row meaning, key, dates, additivity and connected dimensions.
- Measure dependency map: base and derived measures where feasible.

Use Mermaid, Graphviz, SVG or HTML according to runtime capability. Give each issue a finding ID and preserve readable labels. Do not hide bidirectional or many-to-many relationships in generic arrows.
