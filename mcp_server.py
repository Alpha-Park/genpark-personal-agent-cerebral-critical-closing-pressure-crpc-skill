"""
MCP Server for Cerebrovascular Critical Closing Pressure (CrCP) Skill.
Exposes JSON-RPC Model Context Protocol tools for evaluating CrCP, effective CPP, arteriolar wall tension, and cerebral safety.
"""

import sys
import json
from typing import Dict, Any
from client import CerebralCriticalClosingPressureClient


def get_tools_manifest() -> Dict[str, Any]:
    return {
        "tools": [
            {
                "name": "evaluate_crcp",
                "description": "Calculates Cerebrovascular Critical Closing Pressure (CrCP in mmHg), effective cerebral perfusion pressure (CPP), wall tension, and hemodynamic safety score.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "mean_arterial_pressure_mmhg": {
                            "type": "number",
                            "description": "Systemic mean arterial pressure in mmHg (e.g. 93.0 mmHg)."
                        },
                        "systolic_bp_mmhg": {
                            "type": "number",
                            "description": "Systolic blood pressure in mmHg (e.g. 120.0 mmHg)."
                        },
                        "diastolic_bp_mmhg": {
                            "type": "number",
                            "description": "Diastolic blood pressure in mmHg (e.g. 80.0 mmHg)."
                        },
                        "mean_flow_velocity_cm_s": {
                            "type": "number",
                            "description": "MCA mean flow velocity in cm/s (e.g. 62.0 cm/s)."
                        },
                        "systolic_flow_velocity_cm_s": {
                            "type": "number",
                            "description": "MCA peak systolic flow velocity in cm/s (e.g. 95.0 cm/s)."
                        },
                        "diastolic_flow_velocity_cm_s": {
                            "type": "number",
                            "description": "MCA end-diastolic flow velocity in cm/s (e.g. 42.0 cm/s)."
                        }
                    },
                    "required": [
                        "mean_arterial_pressure_mmhg",
                        "systolic_bp_mmhg",
                        "diastolic_bp_mmhg",
                        "mean_flow_velocity_cm_s",
                        "systolic_flow_velocity_cm_s",
                        "diastolic_flow_velocity_cm_s"
                    ]
                }
            }
        ]
    }


def handle_request(client: CerebralCriticalClosingPressureClient, req: Dict[str, Any]) -> Dict[str, Any]:
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": get_tools_manifest()
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "evaluate_crcp":
            res = client.evaluate_crcp(
                mean_arterial_pressure_mmhg=float(args.get("mean_arterial_pressure_mmhg", 93.0)),
                systolic_bp_mmhg=float(args.get("systolic_bp_mmhg", 120.0)),
                diastolic_bp_mmhg=float(args.get("diastolic_bp_mmhg", 80.0)),
                mean_flow_velocity_cm_s=float(args.get("mean_flow_velocity_cm_s", 62.0)),
                systolic_flow_velocity_cm_s=float(args.get("systolic_flow_velocity_cm_s", 95.0)),
                diastolic_flow_velocity_cm_s=float(args.get("diastolic_flow_velocity_cm_s", 42.0))
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(res, indent=2)
                        }
                    ]
                }
            }
        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method not found: {name}"
                }
            }
    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32600,
                "message": f"Invalid Request: Unsupported method {method}"
            }
        }


def main():
    client = CerebralCriticalClosingPressureClient()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(client, req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {
                    "code": -32700,
                    "message": f"Parse error or exception: {str(e)}"
                }
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
