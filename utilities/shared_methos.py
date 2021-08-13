from stix2 import parse

from database_service.database import ClientDB


def is_revoked(stix_object):
    revoked = False
    try:
        revoked = stix_object.objects[0].revoked
    except Exception:
        pass
    return revoked


def is_deprecated(stix_object):
    deprecated = False
    try:
        deprecated = stix_object.objects[0].x_mitre_deprecated
    except Exception:
        pass
    return deprecated


def get_id_of_attack_pattern(stix_object):
    external_id = "None"
    for x in range(len(stix_object.objects[0]['external_references'])):
        try:
            external_id = stix_object.objects[0]['external_references'][x].external_id
            break
        except Exception:
            continue
    return external_id


def get_name_of_attack_pattern(stix_object):
    name = "None"
    try:
        name = stix_object.objects[0].name
    except Exception:
        pass
    return name


def get_description_of_attack_pattern(stix_object):
    description = "None"
    try:
        description = stix_object.objects[0].description
    except Exception:
        pass
    return description


def get_kill_chain_phases_of_attack_pattern(stix_object):
    kill_chain_phases = []
    try:
        kill_chain_phases = stix_object.objects[0]['kill_chain_phases']
    except Exception:
        pass
    return kill_chain_phases


def get_data_sources_of_attack_pattern(stix_object):
    collection = ClientDB.db['data_sources']
    unique_data_sources = []
    auxiliaryList = []
    try:
        # get data-sources
        data_sources = stix_object.objects[0]['x_mitre_data_sources']
        # for each data source
        for x in range(len(data_sources)):
            a_data_source = data_sources[x]
            # check if it is contain : => this means that we have 2 data sources
            if ":" in a_data_source:
                # we have 1 class and one subclass
                parent_data_source = a_data_source.split(":", 1)[0].lstrip()
                subclass_data_source = a_data_source.split(":", 1)[1].lstrip()
                auxiliaryList.append(parent_data_source)
                auxiliaryList.append(subclass_data_source)

            else:
                # the data source will be one class
                auxiliaryList.append(a_data_source)
                print("Not found!")
        # remove duplicate values
        for dsource in auxiliaryList:
            if dsource not in unique_data_sources:
                unique_data_sources.append(dsource)
    except Exception:
        print("exception in "+stix_object.objects[0].id)
        # it means that the attack-pattern does not have any data source
        pass
    # print(unique_data_sources)
    return unique_data_sources




