# Data management and reproducibility

The portfolio links scientific archives and relevant papers, and specifies project-specific prospective fields. Most original student-team data were not supplied. A bibliography entry is not a claim that raw data were obtained or that a product exists for every historical project.

## Three distinct data classes

1. **External observational data:** acquired through a documented query, with retrieval timestamp and hash. The model toolkit’s exoplanet sample is an explicitly selected observational sample.
2. **Synthetic data:** generated from stated equations, parameters and seeds. Label plots and files as synthetic or illustrative. Synthetic agreement verifies implementation behavior; it does not validate environmental realism.
3. **Prospective data contracts:** fields required to execute a dossier. These are schemas and acquisition plans, not measurements.

## Minimum manifest

```json
{
  "project_id": "C05",
  "data_class": "observational | synthetic | prospective",
  "source_url": "verified source or documented query",
  "product_id": "exact archive identifier when obtained",
  "retrieved_utc": "ISO timestamp for obtained files",
  "sha256": "hash of raw bytes when obtained",
  "version": "product release and processing revision",
  "units": {"field": "unit"},
  "reference_frame": "explicit frame or not applicable",
  "time_scale": "UTC/TDB/other plus conversion method",
  "calibration": "document and revision",
  "selection": "query, missingness and exclusions",
  "license": "checked product-level terms",
  "access": "public/restricted/consented/synthetic",
  "transformations": ["ordered script/configuration hashes"]
}
```

Raw observations remain immutable. Derived products include source hashes and transformation configuration. Missing values are not zeros; nondetections are not discarded without a selection model. Keep upper limits, quality flags, measurement uncertainties and original units.

## Archive-specific constraints

- MAST, PDS, ALMA and IRSA links identify resource discovery or products. Confirm release, calibration level, instrument response, proprietary period and acknowledgements for each acquired dataset.
- NOAA profiles have calibration scales and geographic/temporal representativeness constraints. Regional comparison data are not simultaneous ground truth for an Arizona balloon.
- Exoplanet discovery catalogs are shaped by detection methods and follow-up. The included alphabetically selected sample is useful for plotting and ingestion tests, not occurrence-rate inference. Composite parameters may combine distinct references.
- Ground telemetry, laboratory records, biomedical assays and field wildlife tracks may require collaborator access or institutional review. No access is asserted from a title or publication alone.
- Indigenous knowledge and tribal planning data follow community governance. Do not infer authorization from public climate maps, and do not release sensitive locations or interviews.

## Reproducible run record

Record Python/library versions, input hashes, parameter configuration, random seeds, tolerances and output hashes. Do not put credentials or access tokens into notebooks or data manifests. Use a small public test case before a large archive download. Every numerical result should be traceable to a committed script and a retained configuration.

## Publication package

Release source-linked figures with axes/units, uncertainty definition, processing history, selection/censoring decisions, and a concise methods statement. Distinguish observational points from model curves. Keep a claim-to-source ledger and disclose unresolved disagreement. If data cannot be released, publish a consent-compatible schema and an explicitly synthetic demonstration.
