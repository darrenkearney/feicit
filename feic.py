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
import requests

messages = {
    'greeting': '# Feckit: Feic the internet.',
    'description': '''  Feic is a command-line web browser that fetches html pages from URLs and converts them to Markdown. Now you can read your favourite websites in a way never-before intended by the developers.
    
    Enjoy the purity of plaintext,  without all the clutter of advertising, modals, popups, and without executing the mass of javascript snippets used to track all over the modern web.
    
    Note, you are likey still being heavily tracked - but at least you are no longer doing it to yourself through your own browser.

Feckit.
    -- Darren
''',
    'warning': '''
------------------------------------
 WARNING - DANGER - Do NOT use this.
------------------------------------

This software is experimental.

This has a high potential to be very dangerous to your machine. Only use on a computer or virtual machine that you don't mind bricking or being hacked or corrupted.

Do not fetch anything from a URL you do not trust.

This is a super simple, basic and experimental script. Don't expect anything too clever.

If you know what you are doing, best used with a terminal multiplexer, or a terminal with nice scrolling so you can scroll back the content.

tl;dr - stop now and quit with Ctrl+C unless you understand the risks and wish to proceed anyway.

You have been warned.
''',
    'oktnxbye': '''Buíochas as féachaint ar an Idirlíon le "feckit", slán!
Thanks for feicing the internet, bye!''',
    'gpl3': '''feicit  Copyright (C) 2019  Darren Kearney
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.''',
    'gpl3_warranty': '''
      THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
      APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
      HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
      OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
      THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
      PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
      IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
      ALL NECESSARY SERVICING, REPAIR OR CORRECTION.
    ''',
    'gpl3_conditions':''' The conditions have yet to be added to interactive terminal in this software. Please see the license document that came with this software for more about the conditions.
    '''

}

def get_address_from_input():
    # the user input parsing goes here

    address = ''
    while (address == ''):

        print(messages['warning'])
        print('Enter "quit" to quit.')
        address = input("URL > ")
        print(address)

        if (address == 'quit' or address == 'exit' or address == '"quit"'):
            print(messages['oktnxbye'])
            exit()

        elif (address == 'show c'):
            print(messages['gpl3_conditions'])
            exit()

        elif (address == 'show w'):
            print(messages['gpl3_warranty'])
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

    print(messages)
    print(messages['greeting'])
    print(messages['description'])

    try:
        while True:

            print(parse_content_to_md(get_contents(get_address_from_input())))


    except KeyboardInterrupt:
        print(messages.oktnxbye)


main()
