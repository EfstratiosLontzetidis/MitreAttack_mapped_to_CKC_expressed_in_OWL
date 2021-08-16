from database_service.clear_db import clear_db
from utilities.shared_methos import *
import os, yaml
from owlready import *

# A new empty ontology is created. The ontology is called attack. The IRI of the ontology is also given
attack = Ontology("https://raw.githubusercontent.com/EfstratiosLontzetidis/AttackOWL/master/attack.owl")

# # create the class data_sources_class with the OWL name "data-sources" dynamically
# data_sources_class = types.new_class("data-sources", (Thing,), kwds={"ontology": attack})
#
# # set the path of the yaml file that contains the data sources and their components
# yaml_data_sources_file_path = os.path.join(os.getcwd(),"..\\enterprise-attack\\data-sources\\attack-data-sources.yaml")
#
# # open yaml file
# with open(yaml_data_sources_file_path, "r", encoding="utf-8") as data_sources_file:
#     # for each data source in the data_sources_file
#     for data_source in yaml.safe_load(data_sources_file):
#         # create the class a_data_source_class. Use the -name field to set the name
#         a_data_source_class = types.new_class(data_source['name'], (data_sources_class,), kwds={"ontology": attack})
#         # for each data component of the specific data source
#         for data_component in data_source['data_components']:
#             # print(data2['name'])
#             # create the class a_data_component_class. Use the -name field to set the name
#             # this is a data component that belongs to the data source - so it is a subclass - here it is declared
#             a_data_component_class = types.new_class(data_component['name'], (a_data_source_class,), kwds={"ontology": attack})
#         #print("============================================================================")


# somewhere inside attack pattern there will be the relationships (object properties) and properties (data properties) beside classes
# set the directory of the attack-patterns
directory_of_attack_patterns = os.path.join(os.getcwd(), ".\\enterprise-attack\\attack-pattern")

# create an attack pattern class
attack_pattern_class=types.new_class("attack-pattern", (Thing,), kwds={"ontology": attack})


# read all attack-pattern stix files
# for each attack pattern file that exists in the directory
for attack_pattern_file in os.listdir(directory_of_attack_patterns):
    # open the file
    with open(os.path.join(directory_of_attack_patterns, attack_pattern_file), "r", encoding="utf-8") as file_handle:
        # parse the file as a stix object and create the class
        stix_object = parse(file_handle, allow_custom=True)
        # if the attack pattern is not revoked and not deprecated
        if is_revoked(stix_object)==False and is_deprecated(stix_object)==False and is_subtechnique(stix_object)==False:
            techniqueclass = types.new_class(
                get_name_of_attack_pattern(stix_object).replace(" ", "_").replace("/", "_"),
                (attack_pattern_class,), kwds={"ontology": attack})
            for attack_pattern_file2 in os.listdir(directory_of_attack_patterns):
                with open(os.path.join(directory_of_attack_patterns, attack_pattern_file2), "r",
                          encoding="utf-8") as file_handle2:
                    stix_object2 = parse(file_handle2, allow_custom=True)
                    # if the attack pattern is not revoked and not deprecated
                    if is_revoked(stix_object2)==False and is_deprecated(stix_object2)==False and is_subtechnique(stix_object2)==True:
                        if get_id_of_attack_pattern(stix_object) in get_id_of_attack_pattern(stix_object2):
                            subtechniqueclass = types.new_class(
                                get_name_of_attack_pattern(stix_object2).replace(" ", "_").replace("/", "_"),
                                (techniqueclass,), kwds={"ontology": attack})

# # properties example, in owlready object properties and data properties are the same ( in data -> range = str )
# domainlist=[]
# domainlist.append(attack_pattern_class)
# # rangelist=[]
# # rangelist.append(data_sources_class)
# class has(Property):
#     # domain and range must be lists
#     ontology = attack
#     domain = domainlist
#     # range = rangelist
# # print(attackpatternclass)

attack.save(filename=".\\attack.owl")




