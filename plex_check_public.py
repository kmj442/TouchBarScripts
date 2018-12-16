#!/usr/bin/python2
from requests import ConnectionError
from plexapi.server import PlexServer
import yaml
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--config_loc",
                    help="Location file - neccessary")

args = parser.parse_args()

class Plex_Handler():

    def __init__(self, config):
        """ __init__ """
        token = config["Plex"]["token"]
        baseurl = "http://{0}:32400".format(config["Plex"]["ip"])
        try:
            self.plex = PlexServer(baseurl, token)
            movie_continue = True
        except ConnectionError as e:
            print("No Connection")
            movie_continue = False
        if movie_continue:
            self.get_avail_movies()

    def get_avail_movies(self):
        """ Queries movie list to see if it retrieves index """
        movies = self.plex.library.section("Movies")
        avail_movies = len(movies.search())
        if avail_movies > 0:
            print("Up")
            return "Up"
        else:
            print("Down")
            return "Down"

def get_config():
    """ Reads Config file to pass in """
    file_stream = open(args.config_loc, "r")
    config = yaml.load(file_stream)
    file_stream.close()
    return config

def main():
    config = get_config()
    server = Plex_Handler(config)

if __name__ == '__main__':
    main()
