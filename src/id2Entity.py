"""Example of Python client calling Knowledge Graph Search API."""
# Author: Omar Sanchez

import json
import urllib.parse
import urllib.request

"""
This class is able to take entity id's and return the entity information using google's knowledge graph api
Input: entity id, google cloud platform api key enabled for used with google knowledge graph api
Output: The entity name and result score

Other Resources:
http://nlp.csai.tsinghua.edu.cn/~lzy/publications/aaai2015_transr.pdf
"""


class Id2Entity:

    def __init__(self, entity_id, api_key):
        self.api_key = api_key
        self.query = entity_id
        self.service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
        self.params = {
            'ids': entity_id,
            'indent': True,
            'key': api_key,
        }

    # Changes the query (entity_id) so that a new query result can be made
    def set_query(self, new_query):
        self.query = new_query
        self.params['ids'] = new_query

    # Makes a call to Google's knowledge graph api using the query input
    def query_results(self):
            url = self.service_url + '?' + urllib.parse.urlencode(self.params)
            print(url)
            response = json.loads(urllib.request.urlopen(url).read())
            print('Entity ID:', self.params['ids'])
            for element in response['itemListElement']:
                print(element['result']['name'] + ' (' + str(element['resultScore']) + ')')

            if len(response['itemListElement']) < 1:  # Entity missing from google database because it was deleted
                print("No such entity found.")

    # reads the relationship file and gets entity information from google knowledge graph api
    # input must be in the following format (Entity 1, Entity 2, Relationship)
    # entities are represented with unique id's in the form '/m/06rf7'
    def relationship_file(self, file_name, load_limit):
        from itertools import islice
        with open(file_name, 'r') as r:
            for line in islice(r, load_limit):
                line_columns = line.split("\t")

                first_entity = line_columns[0]
                second_entity = line_columns[1]
                entity_relationship = line_columns[2]

                self.set_query(first_entity)
                self.query_results()
                print()
                self.set_query(second_entity)
                self.query_results()
                print("Relationship:", entity_relationship)
                print("-----------------------------------------------------------------------------------------------")
                print()


def main():
    # set default entity_id parameter and load api key from file
    
    entity_id = input("Entity ID: ")
    # place your api key in a api_key.txt file in the same directory as this python file
    with open('api_key.txt', 'r') as r:
        api_key = r.read()

    # Create the entityLoader object
    entity_loader = Id2Entity(entity_id, api_key)
    entity_loader.query_results()

    # test on train.txt file
    # file_location = 'data/FB15k/test.txt'
    # entity_loader.relationship_file(file_location, 5)


if __name__ == "__main__":
    main()
