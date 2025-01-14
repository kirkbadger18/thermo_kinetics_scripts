class Node:
    def __init__(self, name, species, children):
        self.name = name
        self.species = species
        self.children = children

    def __repr__(self):
        return self.name

    def get_all_species(self):
        all_children = self.get_all_children()
        species = self.species
        for child in all_children:
            for spec in child.species:
                species.append(spec)
        return species

    def get_all_children(self):
        found_all = False
        all_children = self.children
        if isinstance(all_children,Node) and not isinstance(all_children,list):
            all_children = [all_children]
        while not found_all:
            new_children = []
            for children in all_children:
                if children.children:
                    gchildren = children.children
                    if isinstance(gchildren,Node) and not isinstance(gchildren,list):
                        gchildren = [gchildren]
                    for child in gchildren:
                        if child not in all_children:
                            new_children.append(child)
                            all_children.append(child)

            if len(new_children) == 0:
                found_all = True

        return all_children


