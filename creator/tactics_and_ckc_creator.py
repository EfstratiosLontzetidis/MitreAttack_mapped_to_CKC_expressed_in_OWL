from owlready import *


def create_tactics_and_ckc(attack):
    # att&ck tactics
    attack_tactic = types.new_class("attack_tactic", (Thing,), kwds={"ontology": attack})

    ma_reconnaissance = types.new_class("ma_Reconnaissance", (attack_tactic,), kwds={"ontology": attack})
    resource_development = types.new_class("ma_Resource_Development", (attack_tactic,), kwds={"ontology": attack})
    initial_access = types.new_class("ma_Initial_Access", (attack_tactic,), kwds={"ontology": attack})
    execution = types.new_class("ma_Execution", (attack_tactic,), kwds={"ontology": attack})
    persistence = types.new_class("ma_Persistence", (attack_tactic,), kwds={"ontology": attack})
    privilege_escalation = types.new_class("ma_Privilege_Escalation", (attack_tactic,), kwds={"ontology": attack})
    defense_evasion = types.new_class("ma_Defense_Evasion", (attack_tactic,), kwds={"ontology": attack})
    credential_access = types.new_class("ma_Credential_Access", (attack_tactic,), kwds={"ontology": attack})
    discovery = types.new_class("ma_Discovery", (attack_tactic,), kwds={"ontology": attack})
    lateral_movement = types.new_class("ma_Lateral_Movement", (attack_tactic,), kwds={"ontology": attack})
    collection = types.new_class("ma_Collection", (attack_tactic,), kwds={"ontology": attack})
    ma_c2 = types.new_class("ma_Command_and_Control", (attack_tactic,), kwds={"ontology": attack})
    exfiltration = types.new_class("ma_Exfiltration", (attack_tactic,), kwds={"ontology": attack})
    impact = types.new_class("ma_Impact", (attack_tactic,), kwds={"ontology": attack})

    # ckc phases
    ckc_phase = types.new_class("ckc-phase", (Thing,), kwds={"ontology": attack})

    ckc_reconnaissance = types.new_class("ckc_Reconnaissance", (ckc_phase,), kwds={"ontology": attack})
    weaponization = types.new_class("ckc_Weaponization", (ckc_phase,), kwds={"ontology": attack})
    delivery = types.new_class("ckc_Delivery", (ckc_phase,), kwds={"ontology": attack})
    exploitation = types.new_class("ckc_Exploitation", (ckc_phase,), kwds={"ontology": attack})
    installation = types.new_class("ckc_Installation", (ckc_phase,), kwds={"ontology": attack})
    ckc_c2 = types.new_class("ckc_Command_and_Control", (ckc_phase,), kwds={"ontology": attack})
    actions_on_objective = types.new_class("ckc_Actions_on_Objective", (ckc_phase,), kwds={"ontology": attack})

    ma_reconnaissance.equivalent_to = [ckc_reconnaissance]
    resource_development.equivalent_to = [weaponization]
    initial_access.equivalent_to = [delivery]
    execution.equivalent_to = [exploitation]
    persistence.equivalent_to = [installation]
    ma_c2.equivalent_to = [ckc_c2]
