from database_service.clear_db import clear_db
from utilities.shared_methos import *
import os, yaml, owlready

# read all data-sources yaml files and get data sources and their data components
with open("enterprise-attack/data-sources/attack-data-sources.yaml","r") as datasourcesfile:
    for data in yaml.safe_load(datasourcesfile):
        # parent class data source name
        print(data['name'])
        # subclasses (data components)
        for data2 in data['data_components']:
            print(data2['name'])
        print("============================================================================")

# somewhere inside attack pattern there will be the relationships (object properties) and properties (data properties) beside classes
# general initialization - do not delete it
directory_of_attack_patterns = os.path.join(os.getcwd(), "enterprise-attack\\attack-pattern")

# read all attack-pattern stix files
# count=0
for attackpatternfile in os.listdir(directory_of_attack_patterns):
    file_handle = open(os.path.join(directory_of_attack_patterns, attackpatternfile))
    stix_object = parse(file_handle, allow_custom=True)
    if is_revoked(stix_object) or is_deprecated(stix_object):
        print(get_name_of_attack_pattern(stix_object) + "    " +get_id_of_attack_pattern(stix_object))
    # get_data_sources_of_attack_pattern(stix_object)
    # count=count+1
    # print(count)



