# E06 · Data blueprint

[APOLLO THERMALIS](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![E06 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| node_id | string | 1 | Component/node and sensor mapping. | Location and lumped/spatial status required. |
| heat_capacity | float64 | J/K | Node thermal storage coefficient. | Positive; temperature dependence/source retained. |
| conductance_edges | array<record> | W/K | Reciprocal component connections. | Nonnegative; symmetry and uncertainty checked. |
| power_history | nullable<array<float64>> | W | Subsystem dissipated heat. | Clock/source required; missing not zero. |
| environment | record | K,Pa,W/m^2 | Air/radiative temperatures, pressure and solar. | Orientation/view-factor context retained. |
| surface_properties | record | 1,m^2 | Absorptivity/emissivity/area. | Spectral distinction and covariance required. |
| temperature_observed | nullable<float64> | K | Sensor/node temperature. | Sensor lag, bias and position uncertainty. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [NASA balloon thermal environment](https://lambda.gsfc.nasa.gov/product/websites/TOPHAT/topweb.gsfc.nasa.gov/balloon/inside.html) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [NASA Small Spacecraft Thermal Control](https://www.nasa.gov/smallsat-institute/sst-soa/thermal-control/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)

## Included evidence to explore

![E06 included data diagnostic](../../../../data/figures/11_thermal_power_and_response.svg)

Synthetic two-node balloon thermal model. Signed component powers sum to net wall power, with wall-to-payload conduction reversed for the wall balance. The payload has a prescribed 3 W internal source. Temperatures show the model response to imposed boundary histories; they are not balloon-flight measurements or qualification limits.

[Data atlas: tables, model definitions and provenance](../../../../data/README.md). Shared reduced-model evidence has a narrower domain than this project contract.
