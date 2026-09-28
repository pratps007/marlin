from jinja2 import Template
from typing import Dict, Any

REPORT_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>MARLIN-X Evidence Report | {{ incident_id }}</title>
    <style>
        body { font-family: 'Helvetica Neue', Arial, sans-serif; color: #1e293b; line-height: 1.6; padding: 40px; background: #fff; }
        .header { border-b: 3px solid #0284c7; padding-bottom: 20px; margin-bottom: 30px; }
        .title { font-size: 24px; font-weight: bold; color: #0f172a; margin: 0; }
        .subtitle { font-size: 14px; color: #64748b; margin-top: 5px; }
        .section { margin-bottom: 30px; }
        .section-title { font-size: 16px; font-weight: bold; color: #0284c7; border-bottom: 1px solid #e2e8f0; padding-bottom: 5px; margin-bottom: 15px; }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
        .card { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 15px; }
        .badge { display: inline-block; padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: bold; background: #fef3c7; color: #92400e; }
        .badge-danger { background: #fee2e2; color: #991b1b; }
        .badge-success { background: #dcfce7; color: #166534; }
        table { width: 100%; border-collapse: collapse; margin-top: 10px; }
        th, td { border: 1px solid #e2e8f0; padding: 8px 12px; text-align: left; font-size: 12px; }
        th { background: #f1f5f9; font-weight: bold; }
        .footer { margin-top: 50px; border-t: 1px solid #e2e8f0; pt: 15px; font-size: 11px; color: #94a3b8; text-align: center; }
    </style>
</head>
<body>

    <div class="header">
        <div style="float: right;">
            <span class="badge badge-danger">SIMULATED INVESTIGATION SCENARIO</span>
        </div>
        <h1 class="title">MARLIN-X MARINE POLLUTION FORENSIC REPORT</h1>
        <div class="subtitle">NTRO Problem Statement SIH26143 | Incident ID: {{ incident_id }}</div>
    </div>

    <div class="section">
        <div class="section-title">1. INCIDENT OVERVIEW & SATELLITE EVIDENCE</div>
        <div class="grid">
            <div class="card">
                <strong>Target Location:</strong> {{ location }}<br>
                <strong>Satellite Source:</strong> Sentinel-1B SAR (IW GRD VV+VH)<br>
                <strong>Acquisition Time:</strong> {{ detected_at }}<br>
                <strong>Oil Slick Probability:</strong> 88% (Probable Oil Slick)
            </div>
            <div class="card">
                <strong>Slick Surface Area:</strong> 14.85 km²<br>
                <strong>Perimeter:</strong> 26.4 km<br>
                <strong>Orientation:</strong> 135.0° (NW-SE)<br>
                <strong>Estimated Release Window:</strong> 01:15 – 05:45 UTC (84% conf.)
            </div>
        </div>
    </div>

    <div class="section">
        <div class="section-title">2. CANDIDATE VESSEL ATTRIBUTION MATRIX</div>
        <table>
            <thead>
                <tr>
                    <th>Vessel Name</th>
                    <th>MMSI</th>
                    <th>Type</th>
                    <th>Distance</th>
                    <th>Time Fit</th>
                    <th>Plume Fit</th>
                    <th>AIS Reliability</th>
                    <th>Priority</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>OCEAN HYDRA</strong></td>
                    <td>413291000</td>
                    <td>Crude Oil Tanker</td>
                    <td>4.2 km</td>
                    <td>94%</td>
                    <td>89%</td>
                    <td><span class="badge">Suspicious (2.5h Gap)</span></td>
                    <td><span class="badge badge-danger">HIGH</span></td>
                </tr>
                <tr>
                    <td>MARITIME VOYAGER</td>
                    <td>352001240</td>
                    <td>Container Ship</td>
                    <td>18.6 km</td>
                    <td>62%</td>
                    <td>48%</td>
                    <td><span class="badge badge-success">Reliable</span></td>
                    <td>MEDIUM</td>
                </tr>
                <tr>
                    <td>UNMATCHED DARK TARGET</td>
                    <td>SAT-TARGET-09</td>
                    <td>Dark Vessel</td>
                    <td>6.8 km</td>
                    <td>81%</td>
                    <td>82%</td>
                    <td><span class="badge badge-danger">Dark Target</span></td>
                    <td><span class="badge badge-danger">HIGH</span></td>
                </tr>
            </tbody>
        </table>
    </div>

    <div class="section">
        <div class="section-title">3. MULTI-EVIDENCE EXPLAINABILITY & RECOMMENDATION</div>
        <div class="card">
            <strong>Key Evidence FOR Primary Candidate (Ocean Hydra):</strong>
            <ul>
                <li>Vessel trajectory intersects reverse drift origin corridor (-6h).</li>
                <li>Counterfactual plume simulation yields 89% physical compatibility with observed SAR slick.</li>
                <li>2.5-hour AIS signal gap precisely overlaps estimated release window (01:15–05:45 UTC).</li>
            </ul>
            <strong>Recommended Next Best Action:</strong><br>
            Task high-resolution optical/SAR satellite acquisition over Sector B (12.80°N, 74.16°E) to resolve Candidate A / Dark Target ambiguity.
        </div>
    </div>

    <div class="footer">
        Generated automatically by MARLIN-X Intelligence Engine v1.0 | Data Provenance: SIMULATED INVESTIGATION SCENARIO
    </div>

</body>
</html>
"""

class ReportGenerationEngine:
    def generate_html_report(self, incident_id: str = "MARLIN-X-DEMO-001") -> str:
        template = Template(REPORT_TEMPLATE)
        return template.render(
            incident_id=incident_id,
            location="Arabian Sea (12.85° N, 74.22° E)",
            detected_at="2026-09-28T08:30:00Z"
        )

report_engine = ReportGenerationEngine()
