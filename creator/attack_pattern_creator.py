from utilities.shared_methods import *
import os, yaml
from owlready import *


def create_attack_patterns(attack):
    # set the directory of the attack-patterns
    directory_of_attack_patterns = os.path.join(os.getcwd(), str(get_global_path())+"\\enterprise-attack\\attack-pattern")

    # create an attack pattern class
    attack_pattern_class = types.new_class("attack-pattern", (Thing,), kwds={"ontology": attack})

    # read all attack-pattern stix files
    # count=0
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
