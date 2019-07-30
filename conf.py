import sys, os, subprocess

from sphinx.highlighting import lexers
from pygments.lexers.web import PhpLexer
from recommonmark.transform import AutoStructify
from recommonmark.parser import CommonMarkParser

sys.path.insert(0, os.path.abspath(os.path.join('../..', 'sphinx-bootstrap-directives')))

# -----------------------------------------------------------------------------
# GENERAL CONFIGURATION
# -----------------------------------------------------------------------------

project = u'Resume'
copyright = u''
authors = u"Boris Budini"
master_doc = 'index'
templates_path = ['_templates']
extensions = ['m2r', 'rst2pdf.pdfbuilder', 'sphinxprettysearchresults']
source_suffix = ['.rst', '.md']
version = '1.0.0'
exclude_patterns = ['_build']
# -----------------------------------------------------------------------------
# HTML THEMES SETTINGS
# -----------------------------------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_theme_path = ["_themes"]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'display_version': False,
    'style_external_links': True,
    'sticky_navigation': True,
    'canonical_url': '',
    'logo_only': True
}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.
# "<project> v<release> documentation" by default.
#
html_title = u'Boris Budini'

# A shorter title for the navigation bar.  Default is the same as html_title.
#
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#
# html_logo = None

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Insert custom js and css locations here
def setup(app):
    app.add_javascript('_static/js/custom.js')

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#
# html_extra_path = []

# If not None, a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# The empty string is equivalent to '%b %d, %Y'.
#
html_last_updated_fmt = '%H:%M:%S %m/%d/%y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#
# html_additional_pages = {}

# If false, no module index is generated.
#
# html_domain_indices = True

# If false, no index is generated.
#
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#
# html_split_index = False



# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr', 'zh'
#
# html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# 'ja' uses this config value.
# 'zh' user can custom change `jieba` dictionary path.
#
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#
# html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'SphinxExampleProjectdoc'



# ------------------------------------------------------------------------------
# OPTIONS FOR: PDF Output
# ------------------------------------------------------------------------------
pdf_documents = [('index', u'documentation', u'School Resume', u'Boris Budini'),]
pdf_use_index = False
pdf_use_coverpage = False
pdf_stylesheets = ['sphinx','kerning','a4']
