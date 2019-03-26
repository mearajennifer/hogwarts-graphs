class Node():
    """Node in a graph."""

    def __init__(self, data, adjacent=None):
        self.data = data
        if adjacent:
            self.adjacent = adjacent
        else:
            self.adjacent = set()

    def __repr__(self):
        return f'{self.data}'


class Graph():
    def __init__(self):
        self.nodes = set()

    def add_node(self, node):
        """
        Adds a node to the graph.
        """
        self.nodes.add(node)

    def add_connection(self, node1, node2):
        """
        Adds a connection between 2 existing nodes.
        """
        node1.adjacent.add(node2)
        node2.adjacent.add(node1)

    def print_groups(self):
        """
        Prints all groups of connected nodes in the graph (without repeats).
        """

        seen = set()
        groups = []
        to_visit = []

        for node in self.nodes:

            if node not in seen:
                group = set()
                seen.add(node)
                group.add(node)
                to_visit.extend(node.adjacent)

                while to_visit:
                    connection = to_visit.pop()

                    if connection not in seen:
                        seen.add(connection)
                        group.add(connection)
                        to_visit.extend(connection.adjacent)

                groups.append(group)

        print('Groups in Hogwarts:')
        for group in groups:
            print('-', group)

    def are_connected(self, node1, node2):
        """
        Returns True if two nodes are connected and False if they are not.
        Breadth-first search.
        """
        to_visit = []
        seen = set()
        to_visit.append(node1)
        seen.add(node1)

        while to_visit:
            current = to_visit.pop(0)
            if current == node2:
                return True
            else:
                for connection in current.adjacent:
                    if connection not in seen:
                        to_visit.append(connection)
                    seen.add(connection)
        return False

    def are_connected_rec(self, node1, node2):
        """
        Returns True if two nodes are connected and False if they are not.
        Recursive search.
        """
        pass

    def is_well_formed(self):
        """
        Verifies that all node connections in an undirected graph are
        bi-directional.
        """
        for node in self.nodes:
            for connection in node.adjacent:
                if node not in connection.adjacent:
                    return False
        return True


# set up graph, nodes, and connections
hogwarts = Graph()

# group one
harry = Node('Harry')
hermione = Node('Hermione')
ron = Node('Ron')
lavender = Node('Lavender')

hogwarts.add_node(harry)
hogwarts.add_node(hermione)
hogwarts.add_node(ron)
hogwarts.add_node(lavender)

hogwarts.add_connection(harry, hermione)
hogwarts.add_connection(harry, ron)
hogwarts.add_connection(hermione, ron)
hogwarts.add_connection(ron, lavender)

# group two
nick = Node('Nearly Headless Nick')
baron = Node('Bloody Baron')
lady = Node('Grey Lady')
myrtle = Node('Moaning Myrtle')

hogwarts.add_node(nick)
hogwarts.add_node(baron)
hogwarts.add_node(lady)

hogwarts.add_connection(nick, baron)
hogwarts.add_connection(nick, lady)
hogwarts.add_connection(baron, lady)
hogwarts.add_connection(lady, myrtle)

# call graph methods
hogwarts.print_groups()

if hogwarts.are_connected(nick, myrtle):
    print(f'{nick} and {myrtle} are connected!')
else:
    print(f'{nick} and {myrtle} aren\'t connected.')

if hogwarts.are_connected(lady, hermione):
    print(f'{lady} and {hermione} are connected!')
else:
    print(f'{lady} and {hermione} aren\'t connected.')

if hogwarts.is_well_formed():
    print('Hogwarts is a well-formed graph!')
else:
    print('Hogwarts is not a well-formed graph.')




