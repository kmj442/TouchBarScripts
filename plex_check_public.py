#!/usr/bin/python2
from requests import ConnectionError
from plexapi.server import PlexServer

class Plex_Handler():

    def __init__(self):
        token = "<input_token_here"
        baseurl = "<input_ip_address_here>:32400"
        try:
            self.plex = PlexServer(baseurl, token)
            movie_continue = True
        except ConnectionError as e:
            print("No Connection")
            movie_continue = False
        if movie_continue:
            self.get_avail_movies()

    def get_avail_movies(self):
        movies = self.plex.library.section("Movies")
        avail_movies = len(movies.search())
        if avail_movies > 0:
            print("Up")
        else:
            print("Down")


def main():
    server = Plex_Handler()

if __name__ == '__main__':
    main()
