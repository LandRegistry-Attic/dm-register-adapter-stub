# regad_stub

A Stub for  the Register Adapter.

## Running


1. Setup the virtualenv::

    $ pyvenv3 venv
    $ . venv/bin/activate
    $ pip install -r requirements.txt

2. Run the service::

    $ python run.py -p 5011


## Editing the names on the title

Instructions for Test Engineers to alter the names on the tile.

1. Clone the repository with git.

2. Edit the names with your preferred Text Editor.

   The proprietor names are accessed from a [Dictionary] (https://docs.python.org/3/tutorial/datastructures.html#dictionaries) in regad_stub/__init__.py.

   The title numbers are mapped to lists of names and the default value is provided as a second argument in the `get` accessor.

3. Commit the changes with git.

4. Push the changes to the remote with git.

5. Restart the service.
