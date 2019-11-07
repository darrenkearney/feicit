#!/usr/env/python3
"""'feicit' is a minimal terminal-based web browser, to view websites as plain text.
Copyright (C) 2019 Darren Kearney

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import click
import html2text
import messages as m
import requests

def get_address_from_input():
    # the user input parsing goes here

    address = ''
    while (address == ''):

        print(m.messages['warning'])
        print('Enter "quit" to quit.')
        address = input("URL > ")
        print(address)

        if (address == 'quit' or address == 'exit' or address == '"quit"'):
            print(m.messages['oktnxbye'])
            exit()

        elif (address == 'show c'):
            print(m.messages['gpl3_conditions'])
            exit()

        elif (address == 'show w'):
            print(m.messages['gpl3_warranty'])
            exit()
        
        # add missing schema
        if (address[:8] != 'https://' and address[:7] != 'http://'):
            # default to https
            address = 'https://' + address

    return address


def get_contents(address):
    # requests library 
    # https://requests.readthedocs.io
    r = requests.get(address)

    return r.text


def parse_content_to_md(content):
    # https://pypi.org/project/html2text/
    return html2text.html2text(content)


def main():

    print(m.messages['greeting'])
    print(m.messages['description'])

    try:
        while True:

            print(parse_content_to_md(get_contents(get_address_from_input())))


    except KeyboardInterrupt:
        print(messages.oktnxbye)


main()
