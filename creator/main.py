from creator.attack_pattern_creator import create_attack_patterns
from creator.data_source_creator import create_data_sources
from utilities.shared_methods import *
from owlready import *

# A new empty ontology is created. The ontology is called attack. The IRI of the ontology is also given
attack = Ontology("https://raw.githubusercontent.com/EfstratiosLontzetidis/AttackOWL/master/attack.owl")
# this is used so that we do not have conficts between our PCs. Remove or add a dot.
set_global_path(".")

# no need to create data sources  but if you want you can add it
# create_data_sources(attack)

create_attack_patterns(attack)


attack.save(filename=str(get_global_path())+"\\attack.owl")




