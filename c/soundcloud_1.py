import sys
import scapi
import igraph
from soundcloud_oauth import init_scope

def populate(root, graph, user, levels):
    graph.add_vertices(1)
    idx = graph.vcount() - 1
    user = root.users(user)
    graph.vs[idx]['name'] = user.username
    print "created vertix %d for %s" % (idx, user.username)
    
    if levels > 1:
        followingUsers = list(user.followings()) # only first page
        for following in followingUsers:
            try:
                next_idx = [v['name'] for v in graph.vs].index(following['username'])
            except ValueError:
                next_idx = populate(root, graph, following['id'], levels-1)
            graph.add_edges((idx, next_idx))
    return idx

def main(user, levels=2):
    root = init_scope()
    graph = igraph.Graph(n=0, directed=True)
    populate(root, graph, user, levels) 
    graph.write_svg("%s_%d.svg" % (user, levels), layout=graph.layout("kk"), \
        labels="name", vertex_size=20, width=800, height=600)

if __name__ == "__main__":
    sys.exit(main(sys.argv[1], int(sys.argv[2])))
