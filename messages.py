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

# This file just contains an object full of strings
# These strings are used in the program at various points.
# Hopefully this will make it easier to localize later
messages = {
    'greeting': '# Feckit: Feic the internet.',
    'description': '''  Feic is a command-line web browser that fetches html pages from URLs and converts them to Markdown. Now you can read your favourite websites in a way never-before intended by the developers.
    
    Enjoy the purity of plaintext,  without all the clutter of advertising, modals, popups, and without executing the mass of javascript snippets used to track all over the modern web.
    
    Note, you are likey still being heavily tracked - but at least you are no longer doing it to yourself through your own browser.

Feckit.
    -- Darren
''',
    'warning': '''
 __________________________________________________________________
|                                                                  |
| This software is experimental.                                   |
|                                                                  |
| This has a high potential to be very dangerous to your machine.  |
| Only use on a computer or virtual machine that you don't mind    |
| bricking or being hacked or corrupted.                           |
|                                                                  |
| Do not fetch anything from a URL you do not trust.               |
|                                                                  |
| This is a super simple, basic and experimental script.           |
| Don't expect anything clever. Really, I made this in an hour.    |
|                                                                  |
| If you know what you are doing, best used with a terminal        |
| multiplexer, or a terminal with nice scrolling so you can        |
| scroll back the content. Planned features include paged output,  |
| and invoking it from the command line.                           |
|                                                                  |
| tl;dr - stop now and quit with Ctrl+C unless you understand      |
| the risks and wish to proceed anyway.                            |
|                                                                  |
| You are considered warned.                                       |
|__________________________________________________________________|
 ------------------------------------------------------------------
| WARNING!                                                         |
| DANGER! - Do NOT use  without understanding the risk.            |
 ------------------------------------------------------------------
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
