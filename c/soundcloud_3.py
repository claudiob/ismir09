import sys
import igraph
import scapi
from soundcloud_key import soundcloud_key, soundcloud_secret, API_HOST

def init_scope():
    soundcloud_token = "nvFKBw83bTfDjIFPiRCxGw" # Already retrieved
    soundcloud_token_secret = "BNGdRSiimWgxrfPDmWkHza1roy77EwQ1mvT8JoeE"
    return scapi.Scope(scapi.ApiConnector(API_HOST, authenticator = \
        scapi.authentication.OAuthAuthenticator(soundcloud_key, \
        soundcloud_secret, soundcloud_token, soundcloud_token_secret)))

def populate(root, graph, user, depth):
    graph.add_vertices(1)
    idx = graph.vcount() - 1
    user = root.users(user)
    graph.vs[idx]['name'] = user.username
    print "created vertex %d for %s" % (idx, user.username)
    
    if depth > 1:
        followingUsers = list(user.followings()) # only first page
        for following in followingUsers:
            try:
                next_idx = [v['name'] for v in graph.vs].index(following['username'])
            except ValueError:
                next_idx = populate(root, graph, following['id'], depth-1)
            graph.add_edges((idx, next_idx))
    return idx

def main(user, depth=2):
    root = init_scope()
    graph = igraph.Graph(n=0, directed=True)
    populate(root, graph, user, depth) 
    graph.write_svg("%s_%d.svg" % (user, depth), layout=graph.layout("kk"), \
        labels="name", vertex_size=20, width=800, height=600)

if __name__ == "__main__":
    sys.exit(main(sys.argv[1], int(sys.argv[2])))
