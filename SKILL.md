---
name: genpark-personal-agent-cerebral-critical-closing-pressure-crpc-skill
version: 1.0.0
description: Zero-dependency sovereign personal agent skill for calculating Cerebrovascular Critical Closing Pressure (CrCP), effective cerebral perfusion pressure (CPP), arteriolar wall tension, and microvascular safety.
author: AlphaPark Inc.
license: Apache-2.0
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
metadata:
  openclaw_compatible: true
  hermes_compatible: true
  zero_dependency: true
---

# Cerebrovascular Critical Closing Pressure (CrCP) Skill

A sovereign personal agent capability for assessing downstream cerebral microvascular resistance, active arteriolar precapillary wall tension, effective cerebral perfusion pressure ($CPP_{effective} = MAP - CrCP$), and critical closing pressure ($CrCP$).

## Core Capabilities
- **Zero-Flow Pressure Extrapolation**: Computes the hemodynamic threshold at which cerebral flow velocity drops to zero ($CrCP = \frac{P_{sys} \cdot FV_{dia} - P_{dia} \cdot FV_{sys}}{FV_{sys} - FV_{dia}}$ in $\text{mmHg}$).
- **Effective Perfusion Pressure Formulation**: Measures the true driving pressure gradient traversing brain capillary beds ($CPP_{effective} = MAP - CrCP$, normative: $40 - 65\text{ mmHg}$).
- **Arteriolar Vasomotor Wall Tension**: Identifies precapillary vasospasm and intracranial compliance reduction when $CrCP > 55\text{ mmHg}$.
- **Cerebrovascular Postural Protection**: Recommends hydration buffers, head-of-bed angle corridors, and avoidance of extreme Valsalva strain.

## Fast Invocation
```python
from client import CerebralCriticalClosingPressureClient

client = CerebralCriticalClosingPressureClient()
res = client.evaluate_crcp(
    mean_arterial_pressure_mmhg=93.0,
    systolic_bp_mmhg=120.0,
    diastolic_bp_mmhg=80.0,
    mean_flow_velocity_cm_s=62.0,
    systolic_flow_velocity_cm_s=94.0,
    diastolic_flow_velocity_cm_s=44.0
)
print("Critical Closing Pressure:", res["critical_closing_pressure_mmhg"], "mmHg")
print("Effective CPP:", res["effective_cerebral_perfusion_pressure_mmhg"], "mmHg")
print("Safety Score:", res["cerebral_safety_score"], "/ 100")
```
