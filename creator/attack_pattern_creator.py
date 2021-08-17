from utilities.shared_methods import *
import os, yaml
from owlready import *


def create_attack_patterns(attack):
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


    # set the directory of the attack-patterns
    directory_of_attack_patterns = os.path.join(os.getcwd(), str(get_global_path())+"\\enterprise-attack\\attack-pattern")

    # create an attack pattern class
    attack_pattern_class = types.new_class("attack-pattern", (Thing,), kwds={"ontology": attack})

    # create objectproperty for the attack_pattern and attack_tactic parent classes
    ap_to_at_object_property = types.new_class("has_ap", (Property,),
                                               kwds={"ontology": attack})
    ap_to_at_object_property.ontology=attack
    attack_pattern_list=[attack_pattern_class]
    attack_tactic_list=[attack_tactic]
    ap_to_at_object_property.domain=attack_tactic_list
    ap_to_at_object_property.range=attack_pattern_list

    # read all attack-pattern stix files
    count=0
    # for each attack pattern file that exists in the directory
    for attack_pattern_file in os.listdir(directory_of_attack_patterns):
        # open the file
        with open(os.path.join(directory_of_attack_patterns, attack_pattern_file), "r", encoding="utf-8") as file_handle:
            # parse the file as a stix object and create the class
            stix_object = parse(file_handle, allow_custom=True)
            # if the attack pattern is not revoked and not deprecated
            if is_revoked(stix_object) == False and is_deprecated(stix_object) == False and is_subtechnique(stix_object) == False:
                techniqueclass = types.new_class(
                    get_name_of_attack_pattern(stix_object).replace(" ", "_").replace("/", "_"),
                    (attack_pattern_class,), kwds={"ontology": attack})
                tactics=get_kill_chain_phases_of_attack_pattern(stix_object)
                for tactic in tactics:
                    count = count + 1
                    specific_attack_pattern_to_specific_attack_tactic_property = types.new_class(
                        "has_ap_" + str(count),
                        (ap_to_at_object_property,),
                        kwds={"ontology": attack})
                    specific_attack_pattern_to_specific_attack_tactic_property.ontology = attack
                    attack_patterns = [techniqueclass]
                    if "defense-evasion" in tactic:
                        attack_tactics = [defense_evasion]
                    elif "privilege-escalation" in tactic:
                        attack_tactics=[privilege_escalation]
                    elif "persistence" in tactic:
                        attack_tactics=[persistence]
                    elif "initial-access" in tactic:
                        attack_tactics=[initial_access]
                    elif "impact" in tactic:
                        attack_tactics=[impact]
                    elif "execution" in tactic:
                        attack_tactics=[execution]
                    elif "exfiltration" in tactic:
                        attack_tactics=[exfiltration]
                    elif "credential-access" in tactic:
                        attack_tactics=[credential_access]
                    elif "command-and-control" in tactic:
                        attack_tactics=[ma_c2]
                    elif "collection" in tactic:
                        attack_tactics=[collection]
                    elif "discovery" in tactic:
                        attack_tactics=[discovery]
                    elif "resource-development" in tactic:
                        attack_tactics=[resource_development]
                    elif "lateral-movement" in tactic:
                        attack_tactics=[lateral_movement]
                    elif "reconnaissance" in tactic:
                        attack_tactics=[ma_reconnaissance]
                    specific_attack_pattern_to_specific_attack_tactic_property.domain = attack_tactics
                    specific_attack_pattern_to_specific_attack_tactic_property.range = attack_patterns
                for attack_pattern_file2 in os.listdir(directory_of_attack_patterns):
                    with open(os.path.join(directory_of_attack_patterns, attack_pattern_file2), "r",
                              encoding="utf-8") as file_handle2:
                        stix_object2 = parse(file_handle2, allow_custom=True)
                        # if the attack pattern is not revoked and not deprecated
                        if is_revoked(stix_object2)==False and is_deprecated(stix_object2) == False and is_subtechnique(stix_object2) == True:
                            if get_id_of_attack_pattern(stix_object) in get_id_of_attack_pattern(stix_object2):
                                subtechniqueclass = types.new_class(
                                    get_name_of_attack_pattern(stix_object2).replace(" ", "_").replace("/", "_"),
                                    (techniqueclass,), kwds={"ontology": attack})
                                tactics2=get_kill_chain_phases_of_attack_pattern(stix_object2)
                                for tactic2 in tactics2:
                                    count=count+1
                                    specific_attack_pattern_to_specific_attack_tactic_property2 = types.new_class(
                                        "has_ap_" + str(count),
                                        (ap_to_at_object_property,),
                                        kwds={"ontology": attack})
                                    specific_attack_pattern_to_specific_attack_tactic_property2.ontology=attack
                                    attack_patterns2=[subtechniqueclass]
                                    if "defense-evasion" in tactic2:
                                        attack_tactics2 = [defense_evasion]
                                    elif "privilege-escalation" in tactic2:
                                        attack_tactics2 = [privilege_escalation]
                                    elif "persistence" in tactic2:
                                        attack_tactics2 = [persistence]
                                    elif "initial-access" in tactic2:
                                        attack_tactics2 = [initial_access]
                                    elif "impact" in tactic2:
                                        attack_tactics2 = [impact]
                                    elif "execution" in tactic2:
                                        attack_tactics2 = [execution]
                                    elif "exfiltration" in tactic2:
                                        attack_tactics2 = [exfiltration]
                                    elif "credential-access" in tactic2:
                                        attack_tactics2 = [credential_access]
                                    elif "command-and-control" in tactic2:
                                        attack_tactics2 = [ma_c2]
                                    elif "collection" in tactic2:
                                        attack_tactics2 = [collection]
                                    elif "discovery" in tactic2:
                                        attack_tactics2 = [discovery]
                                    elif "resource-development" in tactic2:
                                        attack_tactics2 = [resource_development]
                                    elif "lateral-movement" in tactic2:
                                        attack_tactics2 = [lateral_movement]
                                    elif "reconnaissance" in tactic2:
                                        attack_tactics2 = [ma_reconnaissance]
                                    specific_attack_pattern_to_specific_attack_tactic_property2.domain=attack_tactics2
                                    specific_attack_pattern_to_specific_attack_tactic_property2.range=attack_patterns2
