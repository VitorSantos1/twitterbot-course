#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import post_to_mastodon, post_to_twitter, download_file
import csv, random

def generate_name():
    names = []
    adjectives = []

    with open('nomes.txt', newline='') as namesFile:
        for row in csv.reader(namesFile):
            names.append(row[0])
        
    with open('adjectivos.txt', newline='') as adjectivesFile:
        for row in csv.reader(adjectivesFile):
            adjectives.append(row[0])

    name = random.choice(names)
    adjective = random.choice(adjectives)

    corporate_name = "{} {}".format(name, adjective)
    return corporate_name

POST_TO_MASTODON = True
POST_TO_TWITTER = False

post_content = generate_name()

print(post_content)

if POST_TO_MASTODON:
    post_to_mastodon(post_content)

if POST_TO_TWITTER:
    post_to_twitter(post_content)
