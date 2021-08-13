from database_service.clear_db import clear_db
from utilities.shared_methos import *
import os, yaml
from owlready import *


attack = Ontology("https://raw.githubusercontent.com/EfstratiosLontzetidis/AttackOWL/master/attack.owl")

# read all data-sources yaml files and get data sources and their data components
datasourceclass=types.new_class("data-sources", (Thing,), kwds = { "ontology" : attack })
#print(datasourceclass)
with open("enterprise-attack/data-sources/attack-data-sources.yaml","r") as datasourcesfile:
    for data in yaml.safe_load(datasourcesfile):
        # parent class data source name
        # print(data['name'])
        datasourceclassdata=types.new_class(data['name'], (datasourceclass,), kwds={"ontology": attack})
        # subclasses (data components)
        for data2 in data['data_components']:
            # print(data2['name'])
            datacomponentclass=types.new_class(data2['name'], (datasourceclassdata,), kwds={"ontology": attack})
        #print("============================================================================")


# somewhere inside attack pattern there will be the relationships (object properties) and properties (data properties) beside classes
# general initialization - do not delete it
directory_of_attack_patterns = os.path.join(os.getcwd(), "enterprise-attack\\attack-pattern")
attackpatternclass=types.new_class("attack-pattern", (Thing,), kwds = { "ontology" : attack })
# read all attack-pattern stix files
# count=0
for attackpatternfile in os.listdir(directory_of_attack_patterns):
    file_handle = open(os.path.join(directory_of_attack_patterns, attackpatternfile))
    stix_object = parse(file_handle, allow_custom=True)
    if not is_revoked(stix_object) and not is_deprecated(stix_object):
        # problem with utf-8 -> b'VNC' instead of VNC
        techniqueclass=types.new_class(str(get_name_of_attack_pattern(stix_object).encode('utf-8')), (attackpatternclass,), kwds = { "ontology" : attack })
        # print(get_name_of_attack_pattern(stix_object) + "    " +get_id_of_attack_pattern(stix_object))
    # get_data_sources_of_attack_pattern(stix_object)
    # count=count+1
    # print(count)

# print(attackpatternclass.__subclasses__())
attack.save(filename="attack.owl")


