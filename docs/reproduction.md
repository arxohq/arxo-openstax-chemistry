# Rebuild only the selected models

Use the exact npm CLI `@arxo/cli@0.2.5` and semantics `law.core/0.2.11`. `registry/original` preserves input IR; `registry/package` contains native freshly compiled own IR; `registry/world` contains linked dependencies. The canonical `contentHash`, the raw file SHA-256 and evaluation `resultHash` are different identities.

For a selected root, the compiler can read pinned dependency IR from the delivered `deps/*.lawir.json`. Run in a disposable copy so compilation caches do not enter the release inventory:

```sh
law engine imports-context packages/openstax.chemistry_kinetics --clir registry/package > imports.json
law engine lower packages/openstax.chemistry_kinetics --imports imports.json --exact-release law.core/0.2.11
```

The context operation prints the dependency context. For a scripted rebuild, save it and pass it using `--imports <context.json>` to lower. Canonicalize the resulting JSON with `law engine canon <lowered.json>`, generate the package lock with `law engine lock <package-root> --clir registry/package --write`, then link with `law engine link <own-ir> --package <package-root>`. Lower one existing suite with `law engine lower-test <json-array-of-suite-paths> --lawtest-list --program <world-ir>`; preserve its canonical case/query/expectations. Run `law eval` for the new request. No formula is implemented in maintenance scripts.

New source sections were fetched from their official URLs with the existing OpenStax extractor. `sources/**/manifest.json` and publication nodes retain URLs, UUIDs, retrieval times and raw/extracted hashes. The missing solutions 3.3 snapshot is an exact section span reused from the already pinned stoichiometry snapshot. The retained kinetics 12.4 bytes equal the newly fetched extraction. Older comments that say 12.6 for Arrhenius are historical; source anchors in this delivery correctly point to 12.5.

The exact public file allowlist is `publication.toml`. `tools/canon_publication.py export` creates a fresh archive directory, checks resources and hashes, and does not copy Git history. Verification reports are scoped to this kit; source changes require a new snapshot and renewed addressed checks.

Access for free at [OpenStax Chemistry 2e](https://openstax.org/books/chemistry-2e/pages/1-introduction). OpenStax/Rice University and content contributors; textbook content and adaptations: [CC BY-NC-SA 4.0](../licenses/CC-BY-NC-SA-4.0.txt).
