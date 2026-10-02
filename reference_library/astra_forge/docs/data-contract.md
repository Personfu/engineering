> Preserved ASTRA FORGE revision from commit 4026dd0. The [current ordered engineering records](../../../ENGINEERING_DOCUMENTATION.md) are the controlled A-I documentation. This earlier revision uses separate D03/D04 IDs for the two combined-title work packages; its D05-D08 map to current D04-D07.

# Data and provenance contract

All shipped numerical samples are synthetic educational reference outputs. No archive measurements are bundled. The connected Drive presentation was read for context only. Search/portal inspection is not dataset ingestion.

Every future measurement package must supply the fields below. Missing metadata is a validation failure, not an invitation to fabricate a value.

```json
{
  "project_id": "E03",
  "evidence_class": "MEASURED",
  "publisher": "required",
  "primary_url": "required",
  "dataset_id": "required",
  "product_version": "required",
  "observed_start_utc": "required",
  "observed_end_utc": "required",
  "retrieved_utc": "required",
  "sha256": "required 64 hexadecimal characters",
  "license_or_permission": "required",
  "calibration_id": "required or documented not applicable",
  "columns": [{"name": "required", "unit": "required", "uncertainty": "required", "missing_policy": "required"}],
  "quality_flags": "documented vocabulary",
  "coverage_limits": "required",
  "transforms": "ordered code/configuration/version receipts",
  "review_state": "unreviewed"
}
```

Keep raw inputs immutable and content-addressed; derived products receive their own hashes. Archive retrieval date does not replace observation date. Record nulls and rejection reasons. Do not silently join incompatible calibrations, time scales, coordinate systems or measurement units. For fitted parameters distinguish measured, published, inferred and invented reference values.

## Acquisition recipes

| Resource | Selection contract | QA before analysis |
|---|---|---|
| MAST | Target/program, instrument/filter, exposure/product ID and processing level | Exposure headers, bad pixels, gain, flats, darks, masks and calibration release |
| Exoplanet Archive | Table/release, planet/host ID, measurement provenance and uncertainty | Host grouping, upper limits, missing values, survey target denominator and completeness |
| CDAWeb/SPDF | Dataset/version, variables, time interval and quality fields | Cadence/gaps, coordinate frame, instrument response, units and fill values |
| PDS/NAIF | Bundle/collection/product ID, label, processing level and kernels | Calibration, observation geometry, frame/time scale, label units and mission-specific quality |
| GWOSC | Detector, run, GPS interval, sample rate and data-quality segment | Calibration uncertainty, nonoverlapping noise samples and injection labels |
| USGS Water | Station, parameter code, time window and qualifiers | Units, censoring, method changes, station coverage and provisional status |
| NOAA/USA-NPN | Product release, stations/phenophases, region and dates | Missing days, observation effort, calendar/time convention and climate baseline |
| Landsat/ALMA | Collection/product, observation date and reduction version | Spatial/spectral resolution, cloud/beam response, units and correlated errors |
| Public bio data | Dataset/accession/version, study metadata and allowed scope | Replicates, batch, organism identity, measurement method and confounding |
| Authorized mission logs | Channel definitions, clock origin, calibration and permission | Dropouts, sequence integrity, live time and raw-versus-corrected values |

## Asset provenance

All shipped SVGs are original programmatically generated schematics or mathematical reference plots. Dossier workflow diagrams are conceptual, not experimental measurements. The CubeSat drawing is an illustrative educational model, not manufacturer CAD. No mission image, copyrighted diagram, screenshot or private Drive photograph was copied. Future images need creator, primary URL, license/permission, date, edits, alt text and observation-versus-artist-concept labels.

## Publishable receipt

An evidence packet contains the exact original project title, proposed name, question, raw/derived manifest, model and code revision, calibration lineage, checks, result, uncertainty, competing interpretation and corrections. Sensitive ecological/community records remain protected and use generalized publication geometry only. Bioscience projects remain public-data/literature analysis; no pathogen manipulation or clinical recommendations are provided.
