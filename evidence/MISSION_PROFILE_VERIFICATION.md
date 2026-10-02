# Detailed mission profiles · Revision 4

[Mission control](../MISSION_CONTROL.md) · [Data notebook](../data/TABLES.md) · [Profile manifest](../assets/profile_manifest.json) · [Connection register](../registry/mission_connections.json)

This revision expands the visual library into **117 detailed engineering mission profiles**. Each retains its exact original investigation and complete engineering dossier, with an additional scientific identity, model cockpit, artifact wall, planned-work feed, resource connections and reading playlist. The nine sessions and all supplied projects remain in their original order.

## Source-bound profile content

The original navy, teal and copper design gains electric blue and magenta instrument accents. Each accessible SVG prints the full original title, scientific question, hypothesis, summary, model assumptions and limits; proposed field names, requirement/case IDs, cited-source titles and source-derived documentation counts are visible. The dashboard counts documented artifacts rather than readiness or scientific success.

The registry contains **471 derivation steps, 527 proposed requirements, 434 specified cases, 351 trade alternatives, 351 failure modes, 702 implementation work packages, 877 defined fields and 250 distinct cited resources**. The individual records now contain approximately **347,600 words**, including their browsing profiles and complete engineering dossiers. Proposed work and project empirical evidence remain distinguishable from included software demonstrations.

## Data visibility

The deterministic [table inventory](../data/DATA_INVENTORY.json) covers **12 actual CSVs, 98,759 stored rows and 61 column definitions**: one 200-row public catalog extract and 11 synthetic/reference tables. Every table exposes exact headers, units and their source, original preview rows, finite numeric ranges, missingness, parameters, domain limits, linked plots and hashes. Unknown units are explicitly labeled rather than inferred.

The inventory distinguishes **9 blank cells, 10,683 NaN cells and zero other non-finite numeric tokens**. These are descriptive storage counts across unlike tables. They do not represent independent observations, confidence bounds or physical validity. The table notebook explains numerical exceptions such as a Julia point that escapes while its derivative-based distance estimate is undefined.

The catalog wording is qualified against the saved response: it is a 200-row, query-ordered extract. The original sidecar records a `TOP 200 ... ORDER BY pl_name` request; the saved data do not independently establish global first-200 ranking. Original source bytes and the earlier numerical view are preserved as historical artifacts, with this qualification beside the current view.

## Resource connections and navigation

At most six connections per project are generated from actual cited-resource intersections, supplied session membership and shared included illustrations. Generic sources cited by more than 12 projects are excluded from the source-based ranking. Every connection carries its precise basis; these are reading/resource relationships rather than inferred scientific dependencies, collaborations or validated integrations.

The thematic playlists in mission control provide additional ways to read the collection. Handbook profile navigation resolves to the correct project section, avoiding ambiguous repeated heading anchors in combined documents.

## Verification execution

All **62 software/documentation tests pass**: 18 portfolio/profile/inventory/connection tests, eight schema fixtures, 22 ATLAS numerical tests and 14 supplementary archive tests. The [independent profile review](mission_profile_verification.json) verifies complete visible source facts, SVG accessibility, unique profile content, asset/input hashes, every actual CSV header/row/missingness/range/preview, all **692 reading-link bases/rankings**, and Markdown/HTML/fragment navigation. Exact original titles/order/names, 117 schemas, five controlled source files, 60 scientific assets and all original mathematical blocks remain preserved.

The [current data-gallery review](mission_data_gallery_verification.json) records **1,142 passing independent assertions**, with [primary-source and visual inspection](mission_data_gallery_source_review.json). It verifies the qualified catalog wording, unchanged scientific inputs/numerical summaries and all data-inventory diagnostics. The other eight new scientific figure pairs remain byte-identical to the earlier visual assembly.

[Documentation/artwork regeneration](mission_regeneration_verification.json) left **1,645 compared files byte-identical**. All **467 original display-LaTeX blocks** and their handbook copies match the published baseline; [KaTeX parsed all 467](mission_equation_rendering.json) without errors. Static front-page, Session B, data-observatory and D03 dossier previews loaded every embedded image; seven rendered profile/dashboard samples showed no viewport-clipped text.

The [staged Git byte check](mission_staged_asset_verification.json) verifies **557 asset files** against their versioned SHA-256 values, including all original scientific assets, 245 document-artwork SVGs, new scientific images and preserved architecture sources/renderings.

The [revision-3 verification](VISUAL_REVISION_VERIFICATION.md) remains as dated evidence for the earlier visual assembly. Its 59-test execution and original-asset proofs are retained. This profile revision adds inspection depth without claiming project experiments, clinical efficacy, flight readiness or NASA qualification.
