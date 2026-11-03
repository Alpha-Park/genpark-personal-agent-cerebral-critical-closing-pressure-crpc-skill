"""
Cerebrovascular Critical Closing Pressure (CrCP) & Perfusion Driving Engine.
Provides deterministic, zero-dependency modeling of cerebral arteriolar critical closing pressure,
effective cerebral perfusion pressure (CPP_effective), and precapillary vasomotor wall tension.
"""

from typing import Dict, Any, List, Optional


class CerebralCriticalClosingPressureClient:
    """
    Deterministic client for calculating Cerebrovascular Critical Closing Pressure (CrCP).
    Assesses active arteriolar smooth muscle tone, intracranial pressure transmission,
    effective cerebral blood flow driving pressure, and microvascular resistance vessel patency.
    """

    def __init__(self):
        pass

    def evaluate_crcp(
        self,
        mean_arterial_pressure_mmhg: float,
        systolic_bp_mmhg: float,
        diastolic_bp_mmhg: float,
        mean_flow_velocity_cm_s: float,
        systolic_flow_velocity_cm_s: float,
        diastolic_flow_velocity_cm_s: float
    ) -> Dict[str, Any]:
        """
        Calculates CrCP and effective CPP via zero-flow pressure extrapolation.
        Formulas:
        CrCP = (systolic_bp * diastolic_fv - diastolic_bp * systolic_fv) / (diastolic_fv - systolic_fv)
        Effective CPP = MAP - CrCP
        Normative values:
        - CrCP: 30.0 - 50.0 mmHg (elevated in intracranial hypertension or high vasomotor tone)
        - Effective CPP: 40.0 - 65.0 mmHg
        """
        if systolic_bp_mmhg <= diastolic_bp_mmhg or diastolic_bp_mmhg <= 0:
            return {"error": "Systolic blood pressure must exceed diastolic pressure and both must be positive"}
        if systolic_flow_velocity_cm_s <= diastolic_flow_velocity_cm_s or diastolic_flow_velocity_cm_s <= 0:
            return {"error": "Systolic flow velocity must exceed diastolic velocity and both must be positive"}
        if mean_flow_velocity_cm_s <= 0 or mean_arterial_pressure_mmhg <= 0:
            return {"error": "Mean blood pressure and mean flow velocity must be strictly positive"}

        # 1. Critical Closing Pressure (CrCP in mmHg)
        delta_fv = systolic_flow_velocity_cm_s - diastolic_flow_velocity_cm_s
        crcp_mmhg = round((systolic_bp_mmhg * diastolic_flow_velocity_cm_s - diastolic_bp_mmhg * systolic_flow_velocity_cm_s) / (diastolic_flow_velocity_cm_s - systolic_flow_velocity_cm_s), 1)

        # Ensure realistic clamp if artifactual noise
        crcp_clamped = max(5.0, min(85.0, crcp_mmhg))

        # 2. Effective Cerebral Perfusion Pressure (CPP_eff = MAP - CrCP)
        cpp_effective_mmhg = round(mean_arterial_pressure_mmhg - crcp_clamped, 1)

        # 3. Arteriolar Wall Tension Index (relative)
        wall_tension_ratio = round(crcp_clamped / mean_arterial_pressure_mmhg, 2)

        # 4. Cerebral Hemodynamic Safety Score (0 - 100)
        score = 80.0
        if 30.0 <= crcp_clamped <= 48.0:
            score += 15.0
        elif 22.0 <= crcp_clamped < 30.0 or 48.0 < crcp_clamped <= 56.0:
            score += 5.0
        elif crcp_clamped > 65.0:
            score -= 30.0  # Excessive wall tension / ICP elevation
        elif crcp_clamped > 56.0:
            score -= 15.0
        elif crcp_clamped < 18.0:
            score -= 20.0  # Vasomotor collapse

        if 45.0 <= cpp_effective_mmhg <= 65.0:
            score += 5.0
        elif cpp_effective_mmhg < 35.0:
            score -= 20.0

        crcp_score = round(min(100.0, max(5.0, score)), 1)

        if crcp_score >= 85.0 and 30.0 <= crcp_clamped <= 50.0:
            tier = "OPTIMAL_CEREBROVASCULAR_CLOSING_PRESSURE"
            interp = f"Ideal critical closing pressure (CrCP {crcp_clamped} mmHg, effective CPP {cpp_effective_mmhg} mmHg); balanced precapillary vasomotor tone and intracranial compliance."
            guidance = "Optimal microvascular perfusion reserve. Cerebral blood flow is well-shielded against systemic pressure fluctuations."
        elif crcp_clamped > 58.0:
            tier = "ELEVATED_CRITICAL_CLOSING_PRESSURE"
            interp = f"Elevated critical closing pressure (CrCP {crcp_clamped} mmHg > 50 mmHg, Wall Tension Ratio {wall_tension_ratio}); indicates increased arteriolar tone or elevated intracranial pressure."
            guidance = "High downstream microvascular resistance. Monitor for headache, visual obscurations, or sustained arterial hypertension."
        elif cpp_effective_mmhg < 40.0:
            tier = "COMPROMISED_EFFECTIVE_PERFUSION_PRESSURE"
            interp = f"Reduced effective cerebral perfusion pressure (CPP {cpp_effective_mmhg} mmHg < 40 mmHg); risk of regional cerebral hypoperfusion."
            guidance = "Low cerebral driving pressure. Maintain adequate hydration and avoid excessive pharmacological blood pressure lowering."
        else:
            tier = "MODERATE_CEREBROVASCULAR_PRESSURE_PROFILE"
            interp = f"Moderate CrCP profile (CrCP {crcp_clamped} mmHg, CPP {cpp_effective_mmhg} mmHg); stable perfusion hemodynamics."
            guidance = "Maintain regular aerobic conditioning to preserve arteriolar elasticity and nitric oxide responsiveness."

        return {
            "mean_arterial_pressure_mmhg": mean_arterial_pressure_mmhg,
            "systolic_bp_mmhg": systolic_bp_mmhg,
            "diastolic_bp_mmhg": diastolic_bp_mmhg,
            "mean_flow_velocity_cm_s": mean_flow_velocity_cm_s,
            "systolic_flow_velocity_cm_s": systolic_flow_velocity_cm_s,
            "diastolic_flow_velocity_cm_s": diastolic_flow_velocity_cm_s,
            "critical_closing_pressure_mmhg": crcp_clamped,
            "effective_cerebral_perfusion_pressure_mmhg": cpp_effective_mmhg,
            "wall_tension_ratio": wall_tension_ratio,
            "cerebral_safety_score": crcp_score,
            "classification": tier,
            "physiological_interpretation": interp,
            "actionable_guidance": guidance
        }
