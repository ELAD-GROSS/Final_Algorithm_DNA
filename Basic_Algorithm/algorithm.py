from Basic_Algorithm.Induced_Graph import InducedGraphAux
from Basic_Algorithm.FinalDirectedGraph import FinalDirectedGraph
from Basic_Algorithm.DynamicProgramming import create_guesses


def final_algorithm(strand_len, read_size, real_edge_length, original_strand, reads_lst):
    # build induced graph
    data_for_induced_graph = InducedGraphAux(read_size, real_edge_length, reads_lst)
    induced_graph = data_for_induced_graph.build_induced_graph_from_data()

    # build final directed graph
    final_directed_graph = FinalDirectedGraph(induced_graph, original_strand)

    candidate_strings = create_guesses(final_directed_graph, strand_len)

    return len(candidate_strings) == 1 and original_strand == list(candidate_strings)[0]
