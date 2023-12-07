def boruvka(graph):
    num_vertices = len(graph)
    mst_cost = 0
    components = [i for i in range(num_vertices)]

    while len(set(components)) > 1:
        cheapest_edge = [float('inf')] * num_vertices
        cheapest_edge_info = [(None, None)] * num_vertices

        for u in range(num_vertices):
            for v, weight in graph[u].items():
                component_u = components[u]
                component_v = components[v]
                if component_u != component_v and weight < cheapest_edge[component_u]:
                    cheapest_edge[component_u] = weight
                    cheapest_edge_info[component_u] = (u, v)

        for u in range(num_vertices):
            if cheapest_edge[u] != float('inf'):
                u, v = cheapest_edge_info[u]
                component_u = components[u]
                component_v = components[v]
                if component_u != component_v:
                    mst_cost += cheapest_edge[u]
                    components[component_u] = component_v

    return mst_cost