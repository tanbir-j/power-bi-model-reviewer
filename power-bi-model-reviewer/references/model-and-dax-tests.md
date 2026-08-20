# Model and DAX tests

## Relationship tests

Assess bidirectional relationships, many-to-many joins, ambiguous paths, loops, fact-to-fact joins, dimension-to-dimension joins, inactive relationships, orphan risks and RLS propagation.

For every issue state why the pattern matters in this model, not merely that generic guidance discourages it.

## Grain tests

Infer table grain, identify mixed-grain tables, list candidate keys and specify the row-level test needed to confirm uniqueness or fan-out.

## Dimensional tests

Assess star-schema quality, conformed dimensions, role-playing dates, SCD readiness, surrogate keys, hierarchy usability, unknown members and snowflaking.

## DAX tests

Review context transition, filter removal, iterators, distinct counts, ratios, semi-additive measures, active/inactive dates, blank handling, totals, repeated logic, implicit measures, calculated columns and performance patterns.

## Falsification

Each finding must include a practical test that could disprove it. Metadata-only evidence cannot prove duplicate keys, reconciliation, fan-out or orphaned members.
