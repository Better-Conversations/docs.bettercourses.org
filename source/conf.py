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
from datetime import datetime
copyright = f"2020-{datetime.now().year}, The Better Conversations Foundation Ltd."
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
     "sphinx_tags",
     "sphinxcontrib.mermaid",
     "sphinx.ext.graphviz",
     "qms_header",
     "llms",
     ]
myst_enable_extensions = [
     "colon_fence",
     "html_image"
    ]

# Blog removed - ablog extension no longer needed

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

# Add the favicon and default logo (using new BCF branding files)
html_favicon = "_static/images/bcf-symbol.png"
html_logo = "_static/images/bcf-logo.png"

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
        build_env = "production"  # html variable

    else:
        print("Allowing TODO warnings and content as this is not Production")
        todo_include_todos = True
        todo_emit_warnings = True
        build_env = "development"  # html variable

else:
        print("Allowing TODO warnings and content as there's no environment setting")
        todo_include_todos = True
        todo_emit_warnings = True
        build_env = "development"  # html variable

# Pass build_env to templates
html_context = {
    "build_env": build_env  # Now accessible in Jinja templates
}

# This was for https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html
# Now we're using https://pydata-sphinx-theme.readthedocs.io/en/latest/user_guide/configuring.html
html_theme_options = {
    # Remove top nav, use left sidebar for navigation (docs site pattern)
    "navbar_start": ["navbar-logo"],
    "navbar_center": [],  # Empty - no top nav links
    # Header right side: BCF link, GitHub, then search (rightmost)
    "navbar_end": ["navbar-icon-links", "search-button"],
    "navbar_persistent": [],  # Empty - search moved to navbar_end
    # External links in header (order: BCF site first, then GitHub)
    "icon_links": [
        {
            "name": "BCF",
            "url": "https://betterconversations.foundation",
            "icon": "fa-solid fa-arrow-up-right-from-square",
            "attributes": {"title": "BCF main site"},
        },
        {
            "name": "GitHub",
            "url": "https://github.com/Better-Conversations/docs.bettercourses.org",
            "icon": "fa-brands fa-github",
        },
    ],
    "show_nav_level": 1,  # Show only first level initially, expand current section
    "navigation_depth": 4,  # Allow deep navigation tree
    "collapse_navigation": False,  # Allow collapsible sections (click to expand)
    "show_prev_next": True,
    # Secondary sidebar (right side) - empty
    "secondary_sidebar_items": [],
    # Primary sidebar configuration
    "primary_sidebar_end": [],
    # Show toc tree in primary sidebar
    "show_toc_level": 2,
}

# Sidebars configuration for pydata theme
# Using custom sidebar-nav for full navigation tree on all pages
html_sidebars = {
    "**": ["sidebar-nav.html"],
}

html_baseurl = "https://docs.bettercourses.org/"

# Don't share the source
html_copy_source = False

# Templates path
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

.. _current-flipcharts: https://betterconversations.foundation/downloads/BC%20Course%20Flipcharts.pdf

.. raw:: html

    <script type="text/javascript">!function(e,t,n){function a(){var e=t.getElementsByTagName("script")[0],n=t.createElement("script");n.type="text/javascript",n.async=!0,n.src="https://beacon-v2.helpscout.net",e.parentNode.insertBefore(n,e)}if(e.Beacon=n=function(t,n,a){e.Beacon.readyQueue.push({method:t,options:n,data:a})},n.readyQueue=[],"complete"===t.readyState)return a();e.attachEvent?e.attachEvent("onload",a):e.addEventListener("load",a,!1)}(window,document,window.Beacon||function(){});</script>
    <script type="text/javascript">window.Beacon('init', 'befb95fb-5fe3-47ac-8ff6-20d83acd09d6')</script>

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
# -- Graphviz ---------------------------------------------------------------

graphviz_output_format = 'svg'  # Clearer than PNG, scales better

# -- LaTeX ----------------------------------------------------------------
# For exporting to PDF

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
    'geometry': r'\usepackage[margin=1in]{geometry}',
    
    'preamble': r'''
        % Add page numbers
        \usepackage{fancyhdr}
        \pagestyle{fancy}
        % For UK date format
        \usepackage{datetime}
        \renewcommand{\dateseparator}{~}  % Space between day and month
        \newcommand{\uktoday}{\the\day~\monthname[\month]~\the\year}
        \renewcommand{\familydefault}{\sfdefault}
    ''',

    'maketitle': r'''
        \makeatletter
        \begin{titlepage}
            \centering
            \vspace*{40mm}
            {\huge\textbf{\@title}} 
            \vspace{15mm}\par
            {\Large \textit{\@author}}
            \vspace{15mm}\par
            {\large \uktoday}
        \end{titlepage}
        \makeatother
    ''',
}

latex_documents = [
    ('index',  # Source start file (without .rst extension)
     'betterconversations-foundation.tex',  # Output .tex file name
     'The Better Conversations Foundation',  # Document title
     'The Better Conversations Foundation',    # Author name
     'report',     # Document type (simple article format)
     True),          # Generate TOC
    ('documentation/design-patterns/index',  # Source start file for design patterns
     'design-patterns.tex',  # Output filename 
     'Better Conversations Design Patterns',  # Document title
     'The Better Conversations Foundation',  # Author
     'report',     # Document type (full report format)
     True),         # Generate TOC
    ('documentation/delivery-patterns/index',  # Source start file for delivery patterns
     'delivery-patterns.tex',  # Output filename
     'Better Conversations Delivery Patterns',  # Document title
     'The Better Conversations Foundation',  # Author
     'report',      # Document type
     True),        # Generate TOC
    ('documentation/delivery-guidance/index',  # Source start file for delivery guidance
     'delivery-guidance.tex',  # Output filename
     'Better Conversations Delivery Guidance',  # Document title
     'The Better Conversations Foundation',  # Author
     'report',     # Document type
     True)        # Generate TOC
]

# Document class options
latex_docclass = {
    'manual': 'report',
    'article': 'article'  # Use article class for Articles of Association
}

# Add specific article settings
latex_elements.update({
    'extraclassoptions': 'openany',
    'papersize': 'a4paper',
    'pointsize': '10pt',  # Smaller text for legal documents
    'babel': '\\usepackage[english]{babel}',
    'figure_align': 'htbp',
})

# Make tags work
tags_create_tags = True
tags_intro_text = "Tags"
tags_page_title = "Tag"
tags_create_badges = True
