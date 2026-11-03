"""
Example Usage: Cerebrovascular Critical Closing Pressure (CrCP) & Perfusion Driving Engine.
Demonstrates zero-dependency calculation of CrCP, effective cerebral perfusion pressure (CPP), and wall tension.
"""

from client import CerebralCriticalClosingPressureClient


def main():
    client = CerebralCriticalClosingPressureClient()
    print("=== Cerebrovascular Critical Closing Pressure (CrCP) Demo ===")

    # Test Case 1: Healthy resting cerebral perfusion hemodynamics
    res1 = client.evaluate_crcp(
        mean_arterial_pressure_mmhg=93.0,
        systolic_bp_mmhg=120.0,
        diastolic_bp_mmhg=80.0,
        mean_flow_velocity_cm_s=62.0,
        systolic_flow_velocity_cm_s=94.0,
        diastolic_flow_velocity_cm_s=44.0
    )
    print("\nTest Case 1: Normal CrCP & Perfusion Pressure Profile")
    print(f"  Systemic BP: {res1['systolic_bp_mmhg']}/{res1['diastolic_bp_mmhg']} mmHg (MAP: {res1['mean_arterial_pressure_mmhg']} mmHg)")
    print(f"  MCA Velocity: {res1['systolic_flow_velocity_cm_s']}/{res1['diastolic_flow_velocity_cm_s']} cm/s (Mean: {res1['mean_flow_velocity_cm_s']} cm/s)")
    print(f"  Critical Closing Pressure (CrCP): {res1['critical_closing_pressure_mmhg']} mmHg")
    print(f"  Effective CPP: {res1['effective_cerebral_perfusion_pressure_mmhg']} mmHg | Wall Tension Ratio: {res1['wall_tension_ratio']}")
    print(f"  Cerebral Safety Score: {res1['cerebral_safety_score']} / 100")
    print(f"  Classification: {res1['classification']}")
    print(f"  Physiological Interpretation: {res1['physiological_interpretation']}")
    print(f"  Actionable Guidance: {res1['actionable_guidance']}")

    # Test Case 2: Elevated CrCP (high vasomotor wall tension / risk of low effective CPP)
    res2 = client.evaluate_crcp(
        mean_arterial_pressure_mmhg=105.0,
        systolic_bp_mmhg=148.0,
        diastolic_bp_mmhg=84.0,
        mean_flow_velocity_cm_s=55.0,
        systolic_flow_velocity_cm_s=102.0,
        diastolic_flow_velocity_cm_s=31.0
    )
    print("\nTest Case 2: Elevated CrCP / High Wall Tension Pattern")
    print(f"  Critical Closing Pressure (CrCP): {res2['critical_closing_pressure_mmhg']} mmHg")
    print(f"  Effective CPP: {res2['effective_cerebral_perfusion_pressure_mmhg']} mmHg")
    print(f"  Cerebral Safety Score: {res2['cerebral_safety_score']} / 100")
    print(f"  Classification: {res2['classification']}")
    print(f"  Actionable Guidance: {res2['actionable_guidance']}")


if __name__ == "__main__":
    main()
