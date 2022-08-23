# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "psweep"
copyright = "2022, Steve Schmerler"
author = "Steve Schmerler"

# The full version, including alpha/beta/rc tags
release = "0.8.0"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "myst_parser",
]

# ----------------------------------------------------------------------------
# auto stuff
# ----------------------------------------------------------------------------

autosummary_generate = True

intersphinx_mapping = {
    "sklearn": ("https://scikit-learn.org/stable", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/reference", None),
    "numpy": ("https://numpy.org/doc/stable", None),
}

autodoc_default_options = {
    "members": True,
    "show-inheritance": True,
    # :inherited-members: seems to get applied to all autoXXX directives, not
    # just autoclass? Need to use :no-inherited-members: in all automodule
    # directives, else all module content (classes, functions, ...) end up on a
    # single page. We do that in https://github.com/elcorto/sphinx-autodoc .
    "inherited-members": True,
    "no-special-members": True,
}

napoleon_google_docstring = True
napoleon_numpy_docstring = True

# ----------------------------------------------------------------------------

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"

html_theme_options = {
    "fixed_sidebar": True,
    }

sidebar_collapse = True

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# make gh-pages happy
master_doc = "index"
