FROM lonli078/go-irc-server
MAINTAINER muffinx <muffinx@openmailbox.org>

# import
ADD import/ /

# run irc
USER irc
ENTRYPOINT ./go-irc-server -d
