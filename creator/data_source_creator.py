from owlready import *
import os, yaml

from utilities.shared_methods import get_global_path


def create_data_sources(attack):
    # create the class data_sources_class with the OWL name "data-sources" dynamically
    data_sources_class = types.new_class("data_source", (Thing,), kwds={"ontology": attack})
    # create data_component_class with the name of "data-component"
    data_component_class = types.new_class("data_component", (Thing,), kwds={"ontology": attack})

    # create objectproperty for the data source and data component parent classes
    ds_to_dc_object_property = types.new_class("has_dc", (Property,),
                                               kwds={"ontology": attack})

    ds_to_dc_object_property.ontology = attack
    data_source_list = [data_sources_class]
    data_component_list = [data_component_class]
    ds_to_dc_object_property.domain = data_source_list
    ds_to_dc_object_property.range = data_component_list
    # future improvement
    # # create source_data_element_class with the name of "source-data-element"
    # source_data_element_class = types.new_class("source-data-element", (data_component_class,), kwds={"ontology": attack})
    # # create target_data_element_class with the name of "target_data_element"
    # target_data_element_class = types.new_class("target_data_element", (data_component_class,), kwds={"ontology": attack})

    # set the path of the yaml file that contains the data sources and their components
    yaml_data_sources_file_path = os.path.join(os.getcwd(),
                                               str(
                                                   get_global_path()) + "\\enterprise-attack\\data-sources\\attack-data-sources.yaml")

    # open yaml file
    with open(yaml_data_sources_file_path, "r", encoding="utf-8") as data_sources_file:
        # for each data source in the data_sources_file
        count = 0
        for data_source in yaml.safe_load(data_sources_file):
            # create the class a_data_source_class. Use the -name field to set the name
            a_data_source_class = types.new_class(data_source['name'].replace(" ", "_").replace("/", "_"),
                                                  (data_sources_class,), kwds={"ontology": attack})
            # for each data component of the specific data source
            data_components = []
            for data_component in data_source['data_components']:
                count = count+1
                # create the class a_data_component_class. Use the -name field to set the name
                # this is a data component that belongs to the data source - so it is a subclass - here it is declared
                a_data_component_class = types.new_class(data_component['name'].replace(" ", "_").replace("/", "_"),
                                                         (data_component_class,), kwds={"ontology": attack})
                specific_data_source_to_specific_data_component_property = types.new_class(
                    "has_dt_" + str(count),
                    (ds_to_dc_object_property,),
                    kwds={"ontology": attack})

                specific_data_source_to_specific_data_component_property.ontology = attack
                data_components = [a_data_component_class]
                data_sources = [a_data_source_class]
                specific_data_source_to_specific_data_component_property.domain = data_sources
                specific_data_source_to_specific_data_component_property.range = data_components

                # future improvement
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

                # relationship try
                # relationship_object_property = types.new_class("has_data_component", (Property,), kwds={"ontology": attack})
                # source_data_element_list = [a_data_source_class]
                # target_data_element_list = [a_data_component_class]
                # relationship_object_property.ontology = attack
                # relationship_object_property.domain = source_data_element_list
                # relationship_object_property.range = target_data_element_list
