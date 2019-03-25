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
        self.nodes.add(node)
    
    def add_connection(self, node1, node2):
        node1.adjacent.add(node2)
        node2.adjacent.add(node1)

    def print_groups(self):
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

        for group in groups:
            print(group)


harry = Node('Harry')
hermione = Node('Hermione')
ron = Node('Ron')

hogwarts = Graph()
hogwarts.add_node(harry)
hogwarts.add_node(hermione)
hogwarts.add_node(ron)

hogwarts.add_connection(harry, hermione)
hogwarts.add_connection(harry, ron)
hogwarts.add_connection(hermione, ron)

nick = Node('Nearly Headless Nick')
baron = Node('Bloody Baron')
lady = Node('Grey Lady')
friar = Node('Fat Friar')

hogwarts.add_node(nick)
hogwarts.add_node(baron)
hogwarts.add_node(lady)
hogwarts.add_node(friar)

hogwarts.add_connection(nick, baron)
hogwarts.add_connection(nick, lady)
hogwarts.add_connection(nick, friar)
hogwarts.add_connection(baron, lady)
hogwarts.add_connection(baron, friar)
hogwarts.add_connection(lady, friar)

hogwarts.print_groups()
