with open("input.txt") as f:
    input = f.read().splitlines()


def build_graph():
    graph = {}
    for edge in input:
        start, end = edge.split("-")
        if start not in graph:
            graph.update({start: [end]})
        else:
            ends = graph[start]
            ends.append(end)
            graph.update({start: ends})

        if end not in graph:
            graph.update({end: [start]})
        else:
            starts = graph[end]
            starts.append(start)
            graph.update({end: starts})
    return graph


graph = build_graph()


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node.lower() != node or node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def find_all_paths_part_2(graph, start, end, path=[], flag=True):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        # if uppercase or not already visited
        if node.lower() != node or node not in path:
            newpaths = find_all_paths_part_2(graph, node, end, path, flag)
            for newpath in newpaths:
                paths.append(newpath)
        # else if lowercase but not already visited and not visited twice
        elif node not in ["start", "end"] and flag:
            newpaths = find_all_paths_part_2(graph, node, end, path, flag=False)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def part_one():
    paths = find_all_paths(graph, "start", "end")
    print("Number of paths: ", len(paths))


def part_two():
    paths = find_all_paths_part_2(graph, "start", "end")
    print("Number of paths: ", len(paths))


part_one()
part_two()
