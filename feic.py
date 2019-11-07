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

import html2text
import messages
import requests

class Feic:

    def __init__(self):

        self.messages = messages.messages

    def get_address_from_input(self):
        # the user input parsing goes here

        address = ''
        while (address == ''):

            print(self.messages['warning'])
            print('Enter "quit" to quit.')
            address = input('feicim URL > ')
            print(address)

            # parse any user commands
            if (address == 'quit' or address == 'exit' or address == '"quit"'):
                print(self.messages['oktnxbye'])
                exit()

            elif (address == 'show c'):
                print(self.messages['gpl3_conditions'])
                exit()

            elif (address == 'show w'):
                print(self.messages['gpl3_warranty'])
                exit()
            
            # add missing schema
            if (address[:8] != 'https://' and address[:7] != 'http://'):
                # default to https
                address = 'https://' + address

        return address


    def get_contents(self, address):
        # requests library 
        # https://requests.readthedocs.io
        r = requests.get(address)

        return r.text


    def parse_content_to_md(self, content):
        # https://pypi.org/project/html2text/
        return html2text.html2text(content)


    def main(self):

        print(self.messages['greeting'])
        print(self.messages['description'])

        try:
            while True:

                print(self.parse_content_to_md(self.get_contents(self.get_address_from_input())))


        except KeyboardInterrupt:
            print(self.messages['oktnxbye'])


if (__name__ == '__main__'):
    app = Feic()
    app.main()
