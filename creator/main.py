from database_service.clear_db import clear_db
from utilities.shared_methos import *
import os


# general initialization - do not delete it
directory_of_attack_patterns = os.path.join(os.getcwd(), "enterprise-attack\\attack-pattern")
clear_db()


# test for only one file
# file_handle = open(os.path.join(directory_of_attack_patterns, "attack-pattern--0a3ead4e-6d47-4ccb-854c-a6a4f9d96b22.json"))
# stix_object = parse(file_handle, allow_custom=True)
# # print(type(stix_object))
# # print(len(stix_object.objects[0]['kill_chain_phases']))
# get_data_sources_of_attack_pattern(stix_object)



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



