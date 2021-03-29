##    Python codesnippets runner
##    Copyright (C) 2021  Michele Iarossi (micheleiarossi@gmail.com)
##
##    This program is free software: you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation, either version 3 of the License, or
##    (at your option) any later version.
##
##    This program is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License
##    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
examples.py
===========

Getting started
---------------

When ``examples.py`` runs, a menu like the one shown below is printed on the screen, allowing
the user to choose a code snippet to run: ::

    List of code snippets (features) to run:

      1: dir() on an integer variable
      2: Slicing strings
      3: Transforming a string into a list
      4: Formatting string expressions with the basic syntax
      5: Formatting string expressions with .format() syntax
      6: Formatting string expressions with f-strings syntax
      7: Changing lists in place
      8: List comprehension
      9: map() on the elements of a list

    Enter a number, 'l' for the list of features, 'u' for updating the list,
    'r' for renumbering, 't' for a complete test run, 'x' or 'q' for exiting...
    -> 

After running an example, you can enter ``l`` for having the list of features shown again.
Options ``u`` and ``r`` are useful when new features are being developed and added to the ``codesnippets``
package as explained in :doc:`Add your own codesnippet<expand>`.
Enter ``t`` if you want a complete run of all the features.
"""

import os
import importlib
import re
import shelve
import sys
import shutil

def load_snippets():
    """
    Returns the list of the *codesnippets* available by collecting the docstrings
    from the feature functions inside the feature modules belonging
    to the the ``codesnippets`` package.
    """

    # builds directory list from the 'codesnippets' folder
    try:
        dir_list = os.listdir('codesnippets')
    except FileNotFoundError as exc:
        raise RuntimeError("The required 'codesnippets' subfolder is missing!") from exc

    # filters the list: keeps only the feature files and removes the '.py' suffix
    features_list = [file[:-3] for file in dir_list if re.search(r'feature[0-9]+\.py',file)]

    # sorts the list according to the feature number
    # E.g. 'feature89' -> 89
    # The lambda function skips the first 7 characters of 'feature'
    features_list = sorted(features_list, key = lambda feature: int(feature[7:]))

    # stores the dictionary of modules already loaded
    sys_already_loaded_modules = sys.modules

    # loops over all features and collects the docstrings from the feature functions
    codesnippets = []

    for feature in features_list:
        # imports the feature as a module from the 'codesnippets' package
        module = importlib.import_module('.'+feature,'codesnippets')
        # checks if it needs to be reloaded
        if 'codesnippets.'+feature in sys_already_loaded_modules:
            importlib.reload(module)
        # gets the feature function
        feature_func = module.__dict__[feature]
        # adds the docstring to the doc codesnippets list
        codesnippets.append(feature_func.__doc__)

    # done
    return codesnippets

def show_list(codesnippets):
    """
    Prints the list of the available code snippets on the screen.
    The input parameter *codesnippets* is a list of one-line docstrings
    describing each feature item selectable from the menu.
    """
    print('\nList of code snippets (features) to run:\n')
    for (n_idx,doc_str) in enumerate(codesnippets,1):
        print(f"{n_idx:>3}: {doc_str}")

def run_feature(choice):
    """
    Runs the chosen code snippet given by the input parameter *choice* by calling
    the corresponding feature function after having imported the associated feature module
    from the ``codesnippets`` package.
    If the *choice* is out of range, prints an error message on the screen.
    """
    print()
    # stores the dictionary of modules already loaded
    sys_already_loaded_modules = sys.modules
    try:
        # imports the chosen feature as a module
        feature = 'feature'+choice
        module = importlib.import_module('.'+feature,'codesnippets')
        # checks if it needs to be reloaded
        if 'codesnippets.'+feature in sys_already_loaded_modules:
            importlib.reload(module)
        # gets the feature function
        feature_func = module.__dict__[feature]
        # calls the function
        feature_func()
    except ModuleNotFoundError:
        print("Feature '" + choice + "' does not exist!")
    print()

def run_all(codesnippets):
    """
    Runs all the code snippets.
    For testing purposes.
    """
    print()
    for (n_idx,doc_str) in enumerate(codesnippets,1):
        print(f"{n_idx:>3}: {doc_str}")
        # reuse of run_feature(choice) which needs an input string
        run_feature( str(n_idx) )
    print()

def update_list():
    """
    Returns the new list of *codesnippets* available and updates the database.
    """
    # loads the examples available in the 'codesnippets' package
    codesnippets = load_snippets()

    # updates the database
    codesnippets_db = shelve.open("codesnippets_db")
    codesnippets_db['codesnippets'] = codesnippets
    codesnippets_db.close()

    # done
    return codesnippets

def renumber_index(starting_feature_id,last_feature_id):
    """
    Renumbers the documentation table of contents.
    Adds new feature.rst file.
    """
    # relative path name to index.rst
    index_rst = '.'+ os.path.sep + 'sphinx' + os.path.sep + 'source' + os.path.sep + 'index.rst'
    # reads the file
    try:
        index_rst_lines = [a_line.rstrip() for a_line in open( index_rst )]
    except FileNotFoundError as exc:
        msg = "The required 'index.rst' file is missing!"
        raise RuntimeError(msg) from exc
    index_rst_text = '\n'.join(index_rst_lines)
    # loop over the feature ids
    for feature_id in range(last_feature_id,starting_feature_id-1,-1):
        # feature strings to find
        feature_str     = '<feature'+str(feature_id)+'.rst>'
        new_feature_str = '<feature'+str(feature_id+1)+'.rst>'
        # search and replace
        index_rst_text = index_rst_text.replace(feature_str,new_feature_str)
    # remove old index file
    os.remove(index_rst)
    # write the new index.rst file
    file = open(index_rst,"w")
    file.write(index_rst_text)
    file.close()
    # add new last feature.rst file
    feature_rst = '.'+ os.path.sep + 'sphinx' + os.path.sep + 'source' + os.path.sep + 'feature' + str(last_feature_id+1) + '.rst'
    file = open(feature_rst,"w")
    file.write('.. automodule:: codesnippets.feature' + str(last_feature_id+1))
    file.close()

def renumber_feature(starting_feature_id,last_feature_id):
    """
     Renumbers the feature files and functions when adding new features in between.
    """
    # loop over the feature ids from the end
    for feature_id in range(last_feature_id,starting_feature_id-1,-1):
        # feature strings
        feature_str = 'feature'+str(feature_id)
        new_feature_str = 'feature'+str(feature_id+1)
        # feature file name
        feature_py  = '.' + os.path.sep + 'codesnippets' + os.path.sep + feature_str + '.py'
        # read the feature file
        feature_id_lines   = [a_line.rstrip() for a_line in open( feature_py )]
        feature_id_text    = '\n'.join(feature_id_lines)
        # replace feature string
        feature_id_text    = feature_id_text.replace(feature_str,new_feature_str)
        # feature comment
        feature_comment_str     = '# Feature ' + str(feature_id)
        new_feature_comment_str = '# Feature ' + str(feature_id+1)
        # replace feature comment
        feature_id_text    = feature_id_text.replace(feature_comment_str,new_feature_comment_str)
        # search for references
        list_ref = re.findall(r'<feature[0-9]+>',feature_id_text)
        # update forward references
        for ref in list_ref:
            # get the referenced feature number
            ref_feature_id = int(ref[8:-1]) # e.g. '<feature87>' -> int('87')
            if ref_feature_id >= starting_feature_id:
                new_ref_feature_id  = ref_feature_id + 1
                new_ref_feature_str = '<feature' + str(new_ref_feature_id) + '>'
                # replace
                feature_id_text = feature_id_text.replace(ref,new_ref_feature_str)
        # write new feature file
        new_feature_py  = '.' + os.path.sep + 'codesnippets' + os.path.sep + new_feature_str + '.py'
        file = open(new_feature_py,"w")
        file.write(feature_id_text)
        file.close()
        # remove old feature file
        os.remove(feature_py)

    # loop from the beginning and update remaining forward references
    for feature_id in range(1,starting_feature_id):
        # feature strings
        feature_str = 'feature'+str(feature_id)
        # feature file name
        feature_py  = '.' + os.path.sep + 'codesnippets' + os.path.sep + feature_str + '.py'
        # read the feature file
        feature_id_lines   = [a_line.rstrip() for a_line in open( feature_py )]
        feature_id_text    = '\n'.join(feature_id_lines)
        # search for references
        list_ref = re.findall(r'<feature[0-9]+>',feature_id_text)
        # update forward references if required
        ref_updated = False
        for ref in list_ref:
            # get the referenced feature number
            ref_feature_id = int(ref[8:-1]) # e.g. '<feature87>' -> int('87')
            if ref_feature_id >= starting_feature_id:
                new_ref_feature_id  = ref_feature_id + 1
                new_ref_feature_str = '<feature' + str(new_ref_feature_id) + '>'
                # search and replace
                feature_id_text = feature_id_text.replace(ref,new_ref_feature_str)
                ref_updated = True
        if ref_updated:
            # remove old feature file
            os.remove(feature_py)
            # write new feature file
            file = open(feature_py,"w")
            file.write(feature_id_text)
            file.close()

def renumber(codesnippets):
    """
    Renumbers the feature files and functions when adding new features in between.
    Renumbers also the documentation table of contents.
    """
    print("\nStarting from...")
    choice = input("-> ")
    while not choice:
        choice = input("-> ")
    last_feature_id     = len(codesnippets)
    starting_feature_id = int(choice)
    if not (1 <= starting_feature_id <= last_feature_id):
        raise IndexError(f"Feature {starting_feature_id} does not exist!")
    print("Renumbering the documentation table of contents...")
    renumber_index(starting_feature_id,last_feature_id)
    print("\t-> Done")
    print("Renumbering the feature files...")
    renumber_feature(starting_feature_id,last_feature_id)
    print("\t-> Done")
    
def parse_license(start_line=None,end_line=None):
    """
    License parser. Parses the text between start line and end line.
    """
    try:
        lines = ["    " + a_line.rstrip() for a_line in open('COPYING')]
    except FileNotFoundError as exc:
        msg = "The required license file is missing!"
        raise RuntimeError(msg) from exc
    try:
        start_index = 0          if start_line is None else lines.index(start_line)
        end_index   = len(lines) if end_line   is None else lines.index(end_line)
    except ValueError as exc:
        msg = "The required license file is corrupt!"
        raise RuntimeError(msg) from exc
    license_text = '\n'.join(lines[start_index:end_index])
    return license_text

def show_warranty_disclaimer():
    """
    Shows the warranty disclaimer
    """
    # parse the warranty disclaimer
    start_line = '      15. Disclaimer of Warranty.'
    end_line   = '                         END OF TERMS AND CONDITIONS'
    warranty_disclaimer_text = parse_license(start_line,end_line)
    print()
    print(warranty_disclaimer_text)
    print(80*'-')

def show_GNU_GPL_v3_0():
    """
    Shows the GNU GPL license
    """
    # parse the whole license file
    license_text = parse_license()
    print()
    print(license_text)
    print(80*'-')

def show_copyright_notice():
    """
    Shows the short copyright and licence notice
    """
    # parse the copyright notice
    start_line = "        This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'."
    end_line   = "    The hypothetical commands `show w' and `show c' should show the appropriate"
    copyright_text = parse_license(start_line,end_line)
    # add first line with program name and author name
    copyright_text = "        Python codesnippets runner\n" + \
                     "        Copyright (C) 2021 Michele Iarossi (micheleiarossi@gmail.com)\n" + \
                     copyright_text
    print()
    print(copyright_text)

def menu(codesnippets):
    """
    Shows the user the menu of available code snippets and allows her or him to choose
    which code snippet to run.
    The input parameter *codesnippets* is a list of one-line docstrings
    describing each feature item selectable from the menu.
    """

    # loops over the menu choices
    choice = "l"
    while choice not in ("x","q"):
        # shows the code snippets list
        if choice == "l":
            show_list(codesnippets)

        # print copyright notice
        show_copyright_notice()

        # asks for user input
        print("Enter a number, 'l' for the list of features, 'u' for updating the list,\n"
              "'r' for renumbering, 't' for a complete test run, 'x' or 'q' for exiting...")
        choice = input("-> ")
        while not choice:
            choice = input("-> ")

        # runs one example
        if choice not in ("q","x","l","u","r","t","show w","show c"):
            run_feature(choice)

        # renumbers
        if choice == "r":
            renumber(codesnippets)
            choice = "x"

        # runs all
        if choice == "t":
            run_all(codesnippets)

        # updates the code snippets list and the database
        if choice == "u":
            codesnippets = update_list()
            # shows the list when while loop restarts
            choice = "l"

        # shows warranty disclaimer
        if choice == "show w":
            show_warranty_disclaimer()

        # shows GNU GPL license
        if choice == "show c":
            show_GNU_GPL_v3_0()

def main():
    """
    Starts the Python code snippets menu script.
    """
    # loads the available examples from the database
    codesnippets_db = shelve.open("codesnippets_db")
    codesnippets = codesnippets_db.get('codesnippets',[])
    codesnippets_db.close()

    # adds path for import
    sys.path.insert(1,os.getcwd()+os.path.sep+"codesnippets")
    print(sys.path)

    # checks whether the database has to be built
    if not codesnippets:
        # initial update for building the code snippets list
        codesnippets = update_list()

    # shows the menu to the user
    menu(codesnippets)

if __name__ == '__main__':

    main()
