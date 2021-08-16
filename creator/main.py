from database_service.clear_db import clear_db
from utilities.shared_methods import *
import os, yaml
from owlready import *

# A new empty ontology is created. The ontology is called attack. The IRI of the ontology is also given
attack = Ontology("https://raw.githubusercontent.com/EfstratiosLontzetidis/AttackOWL/master/attack.owl")

# create the class data_sources_class with the OWL name "data-sources" dynamically
data_sources_class = types.new_class("data-source", (Thing,), kwds={"ontology": attack})
# create data_component_class with the name of "data-component"
data_component_class = types.new_class("data-component", (Thing,), kwds={"ontology": attack})
# # create source_data_element_class with the name of "source-data-element"
# source_data_element_class = types.new_class("source-data-element", (data_component_class,), kwds={"ontology": attack})
# # create target_data_element_class with the name of "target_data_element"
# target_data_element_class = types.new_class("target_data_element", (data_component_class,), kwds={"ontology": attack})

# set the path of the yaml file that contains the data sources and their components
yaml_data_sources_file_path = os.path.join(os.getcwd(),"..\\enterprise-attack\\data-sources\\attack-data-sources.yaml")

# open yaml file
with open(yaml_data_sources_file_path, "r", encoding="utf-8") as data_sources_file:
    # for each data source in the data_sources_file
    for data_source in yaml.safe_load(data_sources_file):
        # create the class a_data_source_class. Use the -name field to set the name
        a_data_source_class = types.new_class(data_source['name'].replace(" ", "_").replace("/", "_"), (data_sources_class,), kwds={"ontology": attack})
        # for each data component of the specific data source
        for data_component in data_source['data_components']:
            # create the class a_data_component_class. Use the -name field to set the name
            # this is a data component that belongs to the data source - so it is a subclass - here it is declared
            a_data_component_class = types.new_class(data_component['name'].replace(" ", "_").replace("/", "_"), (data_component_class,), kwds={"ontology": attack})
            # for relationship in data_component['relationships']:
            #     a_source_data_element_class = types.new_class(relationship['source_data_element'].replace(" ", "_").replace("/", "_"),
            #                                              (source_data_element_class,), kwds={"ontology": attack})
            #     a_target_data_element_class = types.new_class(
            #         relationship['target_data_element'].replace(" ", "_").replace("/", "_"),
            #         (target_data_element_class,), kwds={"ontology": attack})
            #     relationship_object_property = types.new_class("test_relationship", (Property,), kwds={"ontology": attack})
            #     source_data_element_list = [a_source_data_element_class]
            #     target_data_element_list = [a_target_data_element_class]
            #     relationship_object_property.ontology = attack
            #     relationship_object_property.domain = source_data_element_list
            #     relationship_object_property.range = target_data_element_list
            relationship_object_property = types.new_class("has_data_component", (Property,), kwds={"ontology": attack})
            source_data_element_list = [a_data_source_class]
            target_data_element_list = [a_data_component_class]
            relationship_object_property.ontology = attack
            relationship_object_property.domain = source_data_element_list
            relationship_object_property.range = target_data_element_list




# # somewhere inside attack pattern there will be the relationships (object properties) and properties (data properties) beside classes
# # set the directory of the attack-patterns
# directory_of_attack_patterns = os.path.join(os.getcwd(), "..\\enterprise-attack\\attack-pattern")
#
# # create an attack pattern class
# attack_pattern_class=types.new_class("attack-pattern", (Thing,), kwds={"ontology": attack})
#
# # read all attack-pattern stix files
# # count=0
# # for each attack pattern file that exists in the directory
# for attack_pattern_file in os.listdir(directory_of_attack_patterns):
#     # open the file
#     with open(os.path.join(directory_of_attack_patterns, attack_pattern_file), "r", encoding="utf-8") as file_handle:
#         # parse the file as a stix object and create the class
#         stix_object = parse(file_handle, allow_custom=True)
#         # if the attack pattern is not revoked and not deprecated
#         if is_revoked(stix_object)==False and is_deprecated(stix_object)==False and is_subtechnique(stix_object)==False:
#             techniqueclass = types.new_class(
#                 get_name_of_attack_pattern(stix_object).replace(" ", "_").replace("/", "_"),
#                 (attack_pattern_class,), kwds={"ontology": attack})
#             for attack_pattern_file2 in os.listdir(directory_of_attack_patterns):
#                 with open(os.path.join(directory_of_attack_patterns, attack_pattern_file2), "r",
#                           encoding="utf-8") as file_handle2:
#                     stix_object2 = parse(file_handle2, allow_custom=True)
#                     # if the attack pattern is not revoked and not deprecated
#                     if is_revoked(stix_object2)==False and is_deprecated(stix_object2)==False and is_subtechnique(stix_object2)==True:
#                         if get_id_of_attack_pattern(stix_object) in get_id_of_attack_pattern(stix_object2):
#                             subtechniqueclass = types.new_class(
#                                 get_name_of_attack_pattern(stix_object2).replace(" ", "_").replace("/", "_"),
#                                 (techniqueclass,), kwds={"ontology": attack})



# properties example, in owlready object properties and data properties are the same ( in data -> range = str )
# attack_pattern_list=[]
# attack_pattern_list.append(attack_pattern_class)
# data_source_list=[]
# data_source_list.append(data_sources_class)
#
#
# class detected_with(Property):
#     # domain and range must be lists
#     ontology = attack
#     # domain = attack_pattern_list
#     range = data_source_list


attack.save(filename="..\\attack.owl")




