# Engineering interface control procedure

An interface-control record (ICD) specifies the contract between a measurement, archive product, code/model, mechanical component or downstream decision. Each project owns a separate ICD associated with its stable project ID. The [NASA interface requirements outline](https://www.nasa.gov/reference/appendix-l-interface-requirements-document-outline/) supplies the systems-engineering reference for this procedure.

## Minimum controlled record

| Item | Content required before ingestion or integration |
| --- | --- |
| Identity and configuration | Project and interface IDs, revision, producer/consumer, intended use, owner, approval record, exact code/model and source-product versions |
| Representation | Field/member names, scalar precision, array ordering/rank/shape, categorical codes, enum vocabulary, record nesting, serialization, lossless integer/time transport |
| Physical semantics | SI or declared source units, quantity versus proxy, signed direction, reference frame, origin, axes, epoch/time scale, bandpass/spectral convention, spatial/temporal support |
| Measurement and inference | Calibration version and uncertainty, response/filter/window, saturation/nondetection/limit qualifiers, extraction/selection rule, fitted versus observed status |
| Joint uncertainty | Covariance basis and units, variable order, dependence groups, cross-covariance, PSD/rank tests, systematic and model-discrepancy treatment |
| Missingness and quality | Null meaning, masks, detection/quantification limits, excluded records and reason, data gaps, clock drift, stale calibration and invalid-domain flags |
| Provenance and authority | Original URL/product ID/query, retrieval/version time, raw-content hash, rights/access restrictions, governance, permitted uses and release constraints |
| Physical integration | Mating interfaces, dimensions/tolerances, material/state, datum/keep-out, connector/pin definitions, power/thermal budget, supported load envelope and source |
| Failure and change control | Invalid-input response, degraded output behavior, compatibility checks, migration/reprocessing rule, notification owner and backward-compatibility decision |

## Structural representation and domain validation

The 117 [project schemas](../data/CONTRACTS.md) implement initial field, container and nullability contracts. A matrix is a nested row/column array. Known dimensions such as B24's 2×2 covariance are constrained. Complex values use `{real, imag}` records. C02's sparse operator uses COO `{shape, row, col, data}`; equal array lengths, index bounds, duplicate-index policy and row normalization are domain checks. A posterior/distribution uses an explicit empirical/parametric/summary/unidentified representation, rather than substituting a point estimate without notice.

Generic structured fields deliberately preserve a pending member-level ICD requirement. A structural-schema pass does not establish a complete engineering interface: resolve the permitted subfields, units, shapes and required metadata before accepting populated records. Distribution sample dimensions and weights, covariance validity, array length consistency, physical bounds and frame/time conventions need project-specific validation beyond JSON Schema. A null remains unknown or missing and must be explained in its sidecar; zero is a physical value, not a substitute.

For large integer timestamps, preserve integer precision during JSON/CSV transport; JavaScript's floating representation cannot exactly represent every 64-bit integer. Select an exact source encoding and declared epoch/time scale, or use validated lossless integer-string transport in the ingestion ICD. Never silently equate floating epoch seconds, UTC strings and TT2000-like integers.

## Controlled changes and review evidence

1. Freeze the ICD and acquisition query with the model baseline and requirement revision.
2. Validate a known-good fixture and independent invalid fixtures: wrong units/frame, absent mandatory calibration, incorrect shape, timestamp loss and invalid covariance.
3. Reconcile conservation, timing and sensor-response ledgers between producer and consumer. Log rejected records and the reason.
4. Record an interface review with uncertainty and any unresolved TBD. Accept an integration only inside the supported envelope.
5. For a changed source product, calibration, schema or hardware interface, identify affected requirements and rerun the corresponding fixtures and model correlation checks.

The project requirements, verification cases and failure-mode tables provide the traceability hooks. Store executed interface-test inputs, outputs, hashes and pass/fail rationale with the project evidence package.
