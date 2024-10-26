# Website Sources for betterconversations.foundation 

This is the source code for the https://betterconversations.foundation web site. 

It is built using Sphinx and the PyData theme.

Note the repository is public, as is the built site which is served up via GitHub Pages. 

## Handbook

This is in the `source/course/handbook` directory. Add new pages as Markdown and into the _toc.yml at the root level. 

TODO make this build a PDF for download and put it in the right place e.g. source/downloads/BC Course Handbook.pdf

## Building the PDF of the Articles of Association

We need a PDF of the articles of association for Companies House and B-Corp certification. 

To build the PDF, run `make latexpdf` in the root of the repository. 

This requires a local installation of LaTeX. 


