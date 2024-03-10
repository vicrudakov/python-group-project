# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.insert(0, os.path.abspath("../wine_data_analysis"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Wine Data Analysis'
copyright = '2024, Elina Sukhanova, Viktor Rudakov, Maria Levina'
author = 'Elina Sukhanova, Viktor Rudakov, Maria Levina'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",     # Support automatic documentation
    "sphinx.ext.coverage",    # Automatically check if functions are documented
    "sphinx.ext.mathjax",     # Allow support for algebra
    "sphinx.ext.viewcode",    # Include the source code in documentation
    "numpydoc",               # Support NumPy style docstrings
    "sphinx.ext.autosummary", # Generates function/method/attribute summary lists
    "sphinx.ext.napoleon",    # Enables Sphinx to parse both NumPy and Google style docstrings
    "myst_nb",                # For compiling Jupyter Notebooks into high quality documentation formats
    "sphinx_design",          # For designing beautiful, view size responsive web components.
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

numpydoc_show_class_members = False

autodoc_default_options = { "members": "var1, var2", "special-members": "call,init", "undoc-members": True, "exclude-members": "weakref", "member-order": "bysource" }

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_title = "Wine Data Analysis"
html_static_path = ['_static']

# do not execute jupyter notebooks when building docs
nb_execution_mode = "off"

# download notebooks as .ipynb and not as .ipynb.txt
html_sourcelink_suffix = ""

suppress_warnings = [
    f"autosectionlabel._examples/{filename.split('.')[0]}"
    for filename in os.listdir("source/notebooks/")
    if os.path.isfile(os.path.join("source/notebooks/", filename))
]  # Avoid duplicate label warnings for Jupyter notebooks.

remove_from_toctrees = ["_autosummary/*"]
