import scapi
from soundcloud_oauth import init_scope

root = init_scope()
user = root.users("bfields")
for friend in user.followings():
    print "Following %s" % friend["username"]
