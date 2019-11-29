
def max_network_rank(src_array, dst_array, node_count):
    # first count the edge count for each node
    edge_count = {}
    for i in xrange(node_count):
        if src_array[i] in edge_count:
            edge_count[src_array[i]] += 1
        else:
            edge_count[src_array[i]] = 1

        if dst_array[i] in edge_count:
            edge_count[dst_array[i]] += 1
        else:
            edge_count[dst_array[i]] = 1

    # now for each edge, check max edge count
    max_count = 0
    for i in xrange(node_count):
        max_count = max(max_count, edge_count[src_array[i]]
                + edge_count[dst_array[i]] - 1)
    
    # print edge_count, max_count
    return max_count


assert 4 == max_network_rank([1,2,3,3], [2,3,1,4], 4)

