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
import os
import sys
# sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('./_ext'))

# -- Project information -----------------------------------------------------

project = 'The Better Conversations Foundation'
copyright = '2020-2024, The Better Conversations Foundation Ltd.'
author = 'The Better Conversations Foundation'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
     'myst_parser', 
     'sphinx.ext.todo', 
     'sphinx_last_updated_by_git', 
     'sphinx.ext.intersphinx',
    #  'ablog', - note we conditionally add this in the following block
     # 'sphinx_external_toc',
     'sphinx_sitemap',
     'sphinx_reredirects',
     "sphinx_design",
     "sphinx_design_elements",
     "qms_header",
     ]
myst_enable_extensions = [
     "colon_fence",
     "html_image"
    ]

# Only include ablog extension for HTML builds 
if 'latexpdf' not in sys.argv:
    print("+++++++++++++ Adding ablog ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    extensions.append('ablog')
else:
    # Remove ablog from extensions if it's there
    if 'ablog' in extensions:
        print("+++++++++++++ Removing ablog ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        extensions.remove('ablog')

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# Add toc path
# external_toc_path = "_toc.yml"
#external_toc_exclude_missing = False  # If True, excludes files not in external toc file

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.git', 
                    'README.md', 'robots.txt', '_site'
                    'serve.sh', 'pyproject.toml', '_ignore', 'requirements.txt']


# Make the sitemap work see https://pypi.org/project/sphinx-sitemap/
# Ensure that PDFs are copied to the site by specifying the directories containing PDFs in the html_extra_path.
# This will copy the contents of the 'downloads' directory to the root of the build.

html_extra_path = ['robots.txt']


# Note everything in this folder will be copied to the root of the build
# Which is why there's another folder downloads in the extra-files folder
# html_extra_path = [] 
# Specifies additional directories to copy after the build is done, like 'extra-files' and 'documentation/downloads'.

# Allow markdown as well as rst files
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
    '.markdown': 'markdown',
}

# Be very picky 
nitpicky = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'

# Don't show the source link
html_show_sourcelink = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add the favicon and default logo
html_favicon = "_static/images/BCF-favicon.png"
html_logo = "_static/images/BCF-logo-light-no-border.png"

# See https://docs.readthedocs.io/en/latest/guides/adding-custom-css.html
html_css_files = [
    'css/custom.css',
    'css/cookieconsent.css',
]

html_js_files = [
    'javascript/cookieconsent.umd.js',
]

if 'BUILD_TYPE' in os.environ:
    if os.environ['BUILD_TYPE'] == "Production":
        print("Disabling TODO warnings and content as this is production")
        todo_include_todos = False
        todo_emit_warnings = False
    else:
        print("Allowing TODO warnings and content as this is not Production")
        todo_include_todos = True
        todo_emit_warnings = True
else:
        print("Allowing TODO warnings and content as there's no environment setting")
        todo_include_todos = True
        todo_emit_warnings = True

# This was for https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html
# Now we're using https://pydata-sphinx-theme.readthedocs.io/en/latest/user_guide/configuring.html
html_theme_options = {
    # "navbar_start": ["navbar-logo"],
    # "navbar_center": ["navbar-nav"],
    # "navbar_end": ["navbar-icon-links"],
    # "navbar_persistent": ["search-button"],
    # "content_footer_items": ["last-updated"],
    "github_url": "https://github.com/Better-Conversations/betterconversations.foundation",
    # "use_edit_page_button": True,
    "show_nav_level": 2,
    "header_links_before_dropdown": 5,
    "show_prev_next": True,
    "secondary_sidebar_items": [],
    "content_footer_items": ["last-updated"]   
    # "content_footer_items": ["last-updated", "utterances"]   
   # "logo": {
    #    "alt_text": "Better Conversations Foundation",
    #    "image_light": "_static/images/BCF-logo-light-non-border.png",
    #    "image_dark": "_static/images/BCF-logo-dark-no-border.png",
    #},
}

# Sidebars will pick up Ablog features
# Global pattern should be first on the list, however doesn't seem to work
# We don't want a sidebar on the home page

html_sidebars = {
    'blog/*': ['ablog/recentposts.html', 'ablog/tagcloud.html', 'ablog/categories.html', 'ablog/archives.html']
}

html_baseurl = "https://betterconversations.foundation/"

# Don't share the source 
html_copy_source = False

# -- Ablog -----------------------------------------------------------
# See here https://ablog.readthedocs.io/en/stable/manual/ablog-configuration-options.html
skip_injecting_base_ablog_templates = False

blog_title = "News from the BCF"
blog_baseurl = "https://betterconversations.foundation/blog"
post_date_format_short = "%b %d, %Y"
post_auto_image = 1 # Don't automatically add images, set to 1 to return the first image in the post
templates_path = ['_templates']

# -- Link Checking -----------------------------------------------------------

# Ignore anything which is localhost as the server may not be running
linkcheck_ignore = [r'http://localhost:\d+/']


html_last_updated_fmt = ""


# Define the current version document links to be added at the start of every rst file
# Use this to quickly update the current versions
# Changelogs will need to be constructed in the document tree as well

rst_prolog = """

.. _current-overview: https://betterconversations.foundation/downloads/BC%20Course%20Overview.pdf

.. _current-handbook: https://betterconversations.foundation/downloads/BC%20Course%20Handbook.pdf

"""

# rst_epilog = """
# .. raw:: html
#    <div>__GDPR__</div>

#    <p></p>

# """


# html_js_files = [
#     '_static/load_fathom.js',
# ]


# -- Redirects ----------------------------------------------------------------

redirects = {
    "documentation/200-the_course.index.html": "https://betterconversations.foundation/course/index.html",
    "documentation/800-resources/email-templates.html": "https://betterconversations.foundation/documentation/course-materials/email_templates.html",
    "2023/05/02/modelling-sales.html": "https://betterconversations.foundation/blog/2023-05-02-modelling-sales.html",
    "thanks/index.html": "https://betterconversations.foundation/about/appreciation.html",
}

# -- LaTeX ----------------------------------------------------------------
# For exporting to PDF

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    'preamble': r'''
\setcounter{secnumdepth}{0}
''',

    # Figure alignment
    'figure_align': 'htbp',
}


latex_documents = [
    ('index',  # Source start file (without .rst extension)
     'betterconversations-foundation.tex',  # Output .tex file name
     'About Better Conversations Foundation',  # Document title
     'The Better Conversations Foundation',    # Author name
     'report'),        # Document type (manual, howto, etc.)
]

