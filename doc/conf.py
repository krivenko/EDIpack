# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

import os
import sys
import subprocess
sys.path.insert(0, os.path.abspath('../python'))
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('./utils'))

import sphinx_rtd_theme
import sphinxfortran_ng
from sphinx.transforms import SphinxTransform
from docutils import nodes
from sphinx.application import Sphinx

# -- Project information -----------------------------------------------------

project = u'EDIpack'
copyright = u'2024, Lorenzo Crippa and Adriano Amaricci'
author = u'Lorenzo Crippa and Adriano Amaricci'

# The short X.Y version
version = u''
# The full version, including alpha/beta/rc tags
release = u'5.0.0'


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.mathjax',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.autodoc',
    'myst_parser',
    'breathe',
    'sphinx_rtd_theme',
    'sphinxfortran_ng.fortran_domain',
    'sphinxfortran_ng.fortran_autodoc'
]


# MyST configuration
myst_enable_extensions = [
    "dollarmath",      # Enable both block and inline math
    "amsmath",         # Adds AMS-style math features
    "deflist",         # Enable definition list syntax
    "colon_fence",     # Enable colon fences (alternative to triple backticks for code blocks)
    "html_admonition", # Admonitions like `.. note::` or `.. warning::`
    "html_image",      # Better control over image options
]

#intersphinx mapping
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'scifor': ('https://scifortran.github.io/SciFortran/', None),
#    'openmpi': ('https://docs.open-mpi.org/en/v5.0.x/', None),
}

# Enable auto-generation of ToC
myst_heading_anchors = 3  # To generate heading anchors for up to level 3

# Other options
myst_number_code_blocks = ['python']  # Example: auto-number Python code blocks
myst_default_language = 'python'      # Set default language for code blocks if not specified
myst_enable_html_img = True           # Allow using HTML <img> for better image control

# MyST settings related to the table of contents
myst_toc_tree = {
    "maxdepth": 3,
    "caption": "Contents",  # This replaces `auto_toc_tree_section`
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
#source_suffix = '.rst'
source_suffix = {'.rst': 'restructuredtext'}

fortran_src=[os.path.abspath('../src/singlesite/*.f90'),
                 os.path.abspath('../src/singlesite/revision.in'),
                 os.path.abspath('../src/singlesite/ED_IO/*.f90'),
                 os.path.abspath('../src/singlesite/ED_BATH/*.f90'),
                 os.path.abspath('../src/singlesite/ED_FIT/*.f90'),
                 os.path.abspath('../src/singlesite/ED_NORMAL/*.f90'),
                 os.path.abspath('../src/singlesite/ED_SUPERC/*.f90'),
                 os.path.abspath('../src/singlesite/ED_NONSU2/*.f90'),
                 os.path.abspath('../src/ineq/*.f90'),
                 os.path.abspath('../src/ineq/E2I_IO/*.f90'),
                 os.path.abspath('../src/ineq/E2I_BATH/*.f90'),
                 os.path.abspath('../src/ineq/E2I_FIT/*.f90'),
                 os.path.abspath('../src/c_bindings/*.f90'),
                 os.path.abspath('../src/c_bindings/edipack/*.f90'),
                 os.path.abspath('../src/c_bindings/edipack2ineq/*.f90')]
  
breathe_projects = { "edipack": os.path.abspath('../_build/doxygen/xml') }
breathe_default_project = "edipack"

def run_doxygen():
    doxyfile_in = os.path.join(os.path.dirname(__file__), 'Doxyfile.in')
    doxyfile_out = os.path.join(os.path.dirname(__file__), 'Doxyfile')
    with open(doxyfile_in) as f:
        template = f.read()
    with open(doxyfile_out, 'w') as f:
        f.write(template)
    subprocess.call(['doxygen', doxyfile_out])


#DEFAULT
fortran_ext=['f90', 'f95']

# fortran_subsection_type = "title"
# fortran_title_underline = "_"
# fortran_indent=4
# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


rst_prolog = """
.. |edipack| replace:: `EDIpack`
.. |edipack2ineq| replace:: `EDIpack2ineq`
.. |Nnambu| replace:: :f:var:`nnambu`
.. |Nspin| replace:: :f:var:`nspin`
.. |Norb| replace:: :f:var:`norb`
.. |Nbath| replace:: :f:var:`nbath`
.. |Nlat| replace:: :f:var:`nlat`
.. |bath_type| replace:: :f:var:`bath_type`
.. |ed_mode| replace:: :f:var:`ed_mode`
.. |Nsym| replace:: :f:var:`nsym`
.. |Nso| replace:: :f:var:`nspin` . :f:var:`norb`
.. |Nlso| replace:: :f:var:`nlat`. :f:var:`nspin` . :f:var:`norb`
.. |Nns| replace:: :f:var:`nnambu` . :f:var:`nspin`
.. |Nnso| replace:: :f:var:`nnambu` . :f:var:`nspin`. :f:var:`norb`
"""



# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
  'collapse_navigation': False,
  'prev_next_buttons_location': 'both',
  'navigation_depth': 4,
}

# html_theme = "sphinxawesome_theme"
# # Select theme for both light and dark mode
# # https://dt.iki.fi/pygments-gallery
# pygments_style = "emacs"


html_css_files = [
    'css/custom.css',
]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
html_sidebars = { '**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html'] }


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'test-docs'


# -- Options for LaTeX output ------------------------------------------------

latex_engine = 'xelatex'

latex_elements = {
    'fontpkg': r'''
\setmainfont{DejaVu Serif}
\setsansfont{DejaVu Sans}
\setmonofont{DejaVu Sans Mono}
''',
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}


latex_elements = {
    'preamble': [r'\usepackage{amsmath,amssymb,amsfonts}',r'\usepackage{mathtools}']
}
    
# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'EDIpack.tex', u'EDIpack documentation',
     u'io', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'EDIpack', u'EDIpack documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'EDIpack', u'EDIpack documentation',
     author, 'EDIpack', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# Fix quotes
class FixQuotesTransform(SphinxTransform):
    """Custom Sphinx transform to replace curly quotes with straight quotes."""
    default_priority = 750  # Run after smartquotes

    def apply(self):
        for node in self.document.traverse(nodes.Text):
            if isinstance(node, nodes.Text):
                node.parent.replace(node, nodes.Text(
                    node.astext()
                    .replace("“", '"')
                    .replace("”", '"')
                    .replace("‘", "'")
                    .replace("’", "'")
                ))


#workaround: use mathjax on all pages
def setup(app):
    app.add_transform(FixQuotesTransform)
    app.set_html_assets_policy('always')
    
def run_doxygen():
    docs_dir = os.path.dirname(__file__)
    build_dir = os.path.join(docs_dir, "../_build/doxygen")

    # Create the output directory if it doesn't exist
    os.makedirs(build_dir, exist_ok=True)

    doxyfile_in = os.path.join(os.path.dirname(__file__), 'Doxyfile.in')
    doxyfile_out = os.path.join(os.path.dirname(__file__), 'Doxyfile')

    with open(doxyfile_in) as f:
        template = f.read()
    with open(doxyfile_out, 'w') as f:
        f.write(template)
    subprocess.call(['doxygen', doxyfile_out])

run_doxygen()
