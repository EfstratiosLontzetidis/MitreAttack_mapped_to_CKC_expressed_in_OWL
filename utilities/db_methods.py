

# def store_in_database(json_as_string):
#     for x in range(len(data_sources)):
#         a_data_source = data_sources[x]
#         # check if it is contain : => this means that we have 2 data sources
#         if ":" in a_data_source:
#             # we have 1 class and one subclass
#             parent_data_source = a_data_source.split(":", 1)[0].lstrip()
#             subclass_data_source = a_data_source.split(":", 1)[1].lstrip()
#             # check if we have already used the parent class data source data source
#             if collection.find({"name": parent_data_source}).count() == 0:
#                 # if we have not used it then insert it to the database
#                 parentclass = {"name": parent_data_source}
#                 collection.insert_one(parentclass)
#                 unique_data_sources.append(parent_data_source)
#
#             # check if we have already used the subclass source
#             if collection.find({"name": subclass_data_source}).count() == 0:
#                 # if we have not used it...
#                 # get its parent class id
#                 parentclass_id = collection.find({"name": parent_data_source})[0]["_id"]
#                 print(parentclass_id)
#                 subclass = {"name": subclass_data_source}
#                 collection.insert_one(subclass)
#                 unique_data_sources.append(subclass_data_source)
#         else:
#             # the data source will be one class
#             print("Not found!")