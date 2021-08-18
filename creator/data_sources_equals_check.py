from owlready import *
from stix2 import parse
from utilities.shared_methods import *
from collections import *

directory_of_attack_patterns = os.path.join(os.getcwd(), "/enterprise-attack/attack-pattern")

same_list=[]
count=0
same=0
for attack_pattern_file in os.listdir(directory_of_attack_patterns):
    # open the file
    with open(os.path.join(directory_of_attack_patterns, attack_pattern_file), "r", encoding="utf-8") as file_handle:
        stix_object = parse(file_handle, allow_custom=True)
        if is_revoked(stix_object) == False and is_deprecated(stix_object) == False:
            id=get_id_of_attack_pattern(stix_object)
            data_sources=get_data_sources_in_list(stix_object)
            for attack_pattern_file2 in os.listdir(directory_of_attack_patterns):
                with open(os.path.join(directory_of_attack_patterns, attack_pattern_file2), "r",
                          encoding="utf-8") as file_handle2:
                    stix_object2 = parse(file_handle2, allow_custom=True)
                    if is_revoked(stix_object2) == False and is_deprecated(stix_object2) == False:
                        id2=get_id_of_attack_pattern(stix_object2)
                        data_sources2=get_data_sources_in_list(stix_object2)
                        if id!=id2:
                            count=count+1
                            if Counter(data_sources2)==Counter(data_sources):
                                same=same+1
                                if id+"-"+id2 not in same_list and id2+"-"+id not in same_list:
                                    same_list.append(id+"-"+id2)

print("The false positive rate is: "+ str(((same/count))*100)+ "%")
for x in same_list:
    print(x)


