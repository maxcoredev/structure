Downsides:
-----------

1. manage.py not in git
2. Not possible to migrate whole pit or smth (but can everything, or submodule)
3. INSTALLED_APPS:

.. code-block:: bash

    INSTALLED_APPS = [
        ...
        'pit.trucks',
        'pit.workers',
    ]

Pros:
-----------

0. Clean isolated architecture
1. Everything in git (but unwanted modules are hided)
2. One small dir to work in
3. No pip install -e module_name
4. Less migration conflicts