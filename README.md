# Cerebrovascular Critical Closing Pressure (CrCP) Skill

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/zero--dependencies-standard--lib-brightgreen.svg)](requirements.txt)
[![MCP Protocol Ready](https://img.shields.io/badge/mcp-protocol--ready-orange.svg)](mcp_server.py)
[![OpenClaw Certified](https://img.shields.io/badge/openclaw-certified-purple.svg)](SKILL.md)

Zero-dependency sovereign personal agent skill for non-invasive evaluation of Cerebrovascular Critical Closing Pressure (CrCP), effective cerebral perfusion pressure (CPP), and precapillary arteriolar wall tension.

```mermaid
flowchart TD
    TCD_Flow["MCA Systolic & Diastolic Flow Velocities (FVsys, FVdia)"] & BP_Stream["Continuous Arterial Blood Pressure (Psys, Pdia, MAP)"] --> ZeroFlow["Zero-Flow Pressure Intercept Formulation"]
    ZeroFlow --> CrCP_Calc["Critical Closing Pressure (CrCP in mmHg)"]
    CrCP_Calc --> CPP_Eff["Effective Perfusion Driving Pressure (CPP = MAP - CrCP)"]
    CPP_Eff --> WallTension["Arteriolar Precapillary Wall Tension & ICP Safety Index"]
    WallTension --> Agent["OpenClaw / Hermes Personal Agent Hemodynamic Shielding"]
```

## Features
- **Deterministic Math**: Pure Python standard library implementation with zero external dependencies.
- **Cerebrovascular Hemodynamic Standards**: Formulates zero-flow pressure intercept, effective cerebral perfusion pressure, and arteriolar wall tension ratios.
- **Intracranial Pressure Transmission & Hypoperfusion Shield**: Early detection of compromised effective perfusion pressure and excessive microvascular tone.
- **Model Context Protocol (MCP)**: Native JSON-RPC tool integration for LLMs and autonomous agents.

## Quickstart

```python
from client import CerebralCriticalClosingPressureClient

client = CerebralCriticalClosingPressureClient()
result = client.evaluate_crcp(
    mean_arterial_pressure_mmhg=93.0,
    systolic_bp_mmhg=120.0,
    diastolic_bp_mmhg=80.0,
    mean_flow_velocity_cm_s=62.0,
    systolic_flow_velocity_cm_s=94.0,
    diastolic_flow_velocity_cm_s=44.0
)
print("Critical Closing Pressure:", result["critical_closing_pressure_mmhg"], "mmHg")
print("Effective CPP:", result["effective_cerebral_perfusion_pressure_mmhg"], "mmHg")
print("Safety Score:", result["cerebral_safety_score"])
print("Classification:", result["classification"])
```

## License
Apache-2.0
