from Constructors.Multilabel import *

class Multilabelling:
    def __init__(self, initial_mapping=None):
        self.labelling_map = initial_mapping if initial_mapping else {}

    def get_multilabel_for_name(self, variable_name):
        return self.labelling_map.get(variable_name, Multilabel([]))

    def update_multilabel_for_name(self, variable_name, new_multilabel):
        self.labelling_map[variable_name] = new_multilabel

    def __str__(self):
        return "\n".join([f"{variable_name}: {multilabel}" for variable_name, multilabel in self.labelling_map.items()])
