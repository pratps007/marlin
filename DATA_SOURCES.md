# MARLIN-X Data Provenance & Data Sources Registry

> **System Status:** DEMO MODE / SIMULATED INVESTIGATION SCENARIO  
> **Last Audit Date:** September 28, 2026

---

### 1. Data Provenance Overview

MARLIN-X is designed to ingest multimodal satellite, environmental, and maritime vessel data. During the current development phase (Phase 1–3 Prototype), **no live external satellite or commercial AIS API calls are made**.

All incident telemetry, slick geometries, vessel tracks, and environmental vector fields are generated within a self-contained, reproducible demonstration dataset (`MARLIN-X-DEMO-001`).

---

### 2. Dataset Inventory & Provenance Breakdown

| Data Category | Target Real-World Source | Current Status | Data Provenance |
| :--- | :--- | :--- | :--- |
| **SAR Imagery** | Copernicus Sentinel-1 (IW GRD VV/VH) via Copernicus Data Space Ecosystem | **SIMULATED** | Pre-packaged synthetic backscatter raster array (`MARLIN-X-DEMO-001`). |
| **Optical Imagery** | Copernicus Sentinel-2 MSI | **NOT YET CONNECTED** | Degraded graceful fallback (No optical imagery loaded). |
| **Surface Wind Vectors** | ECMWF ERA5 Reanalysis / GFS ($10\text{m}$ wind) | **SIMULATED** | Constant vector field ($12.5\text{ kn}, 240^\circ$). |
| **Surface Currents** | NOAA OSCAR / HYCOM ($0\text{m}$ surface current) | **SIMULATED** | Constant vector field ($0.45\text{ m/s}, 115^\circ$). |
| **AIS Telemetry** | Spire / MarineTraffic / ExactEarth AIS | **SIMULATED** | Synthesized 4-vessel trajectory series (`413291000`, `352001240`, `563098110`, `SAT-TARGET-09`). |
| **Offshore Infrastructure** | Global Fishing Watch / Petroleum Platform Databases | **SIMULATED** | Offshore platform locations off Mangalore coast. |
| **Coastline Vectors** | OpenStreetMap / Natural Earth Coastlines | **GEOJSON EMBEDDED** | Local vector LineString representation for Karnataka coast. |

---

### 3. Verification & Guardrail Compliance

- **No Unsubstantiated Claims**: No real-world vessel is accused of actual marine pollution. All vessel names (`Ocean Hydra`, `Maritime Voyager`, `Arabian Express`) are synthetic designations for algorithm testing.
- **Explicit Demo Labeling**: Every dashboard view, API response, and generated report explicitly flags data as `"SIMULATED INVESTIGATION SCENARIO"`.
