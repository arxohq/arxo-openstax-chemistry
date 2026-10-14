# Structural depth of the eleven chemistry models

The delivered classifier is a byte-identical snapshot of the corpus `boundaries.depth`, with an addressed `openstax_section` division convention. The adapter collects inputs, checks SHA-256 before parsing, and aggregates the existing classification. It is not a second classifier.

The denominator comes from literal publisher headings declared in `sources/**/articles.json`, checked against exact retained bytes. Numerical figures/examples do not invent divisions. Each snapshot uses its own publication hash and exact edition; no overlapping edition may lend anchors. Electro's denominator is the captured Table 17.1 excerpt only.

`EXECUTABLE` requires an anchored deriving rule. It establishes structural connection to selected claims, not completeness, correctness of every textbook statement, runtime acceptance of every input or an external scientific checker. SOURCE_ONLY and unanchored assumptions remain visible. All own publications are accounted for; imported nodes are excluded. Unsupported technical dependency units remain not_measured.

Run `python3.12 tools/measure_depth.py --check`. The per-unit JSON records hashes, editions, denominator, individual levels, unresolved/other-edition anchors and unmeasured publications. Six addressed regression tests run without private libraries. Thirty regressions of the shared implementation were checked separately during preparation.

Access for free at [OpenStax Chemistry 2e](https://openstax.org/books/chemistry-2e/pages/1-introduction). OpenStax/Rice University and content contributors; textbook content and adaptations: [CC BY-NC-SA 4.0](../licenses/CC-BY-NC-SA-4.0.txt).
