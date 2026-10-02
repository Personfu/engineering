# Engineering data contracts

Every project has three companion files:

- `<ID>.schema.json`: the proposed JSON record shape with types, units and documented quality rules.
- `<ID>.csv`: an **empty, header-only acquisition template**. It contains no invented observations.
- `<ID>.dictionary.csv`: descriptions, units, original source types and quality rules for each field.

The contracts are derived from the project-specific engineering annexes. Null means missing or unknown, with its cause recorded in a provenance sidecar. Zero is a physical/statistical value and must not be substituted for missingness. JSON Schema validates structure; domain code must additionally validate physical bounds, frames, calibration applicability, covariance dimensions/positive semidefiniteness, conservation, selection and the human-readable quality rules.

Follow the [data management plan](../../docs/DATA_MANAGEMENT.md) for a populated record set. Retain product identifier, archive/query version, retrieval timestamp, original file hash, calibration reference, coordinate/time frame, exclusion/censoring rule and transformation history. Array dimensions and covariance ordering must be defined by an instrument or analysis interface before use; unspecified array dimensions in a discovery-stage contract are an unresolved design input.

Actual acquired/generated data included in this repository are under [`models/data/`](../../models/data/). That collection includes explicitly labeled synthetic demonstrations and a separately labeled 200-row NASA Exoplanet Archive snapshot with query and hash provenance. A URL in any other design record is a data/resource pointer, not proof that a dataset has been acquired or an investigation executed.

The [requirement inventory](../../catalog/requirements.csv) and [verification-case inventory](../../catalog/verification_cases.csv) connect these contracts to engineering decisions. Empty templates are intended to make future acquisition reviewable, not to substitute for the original student-team measurements.
