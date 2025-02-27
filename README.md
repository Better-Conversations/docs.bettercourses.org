# Website Sources for betterconversations.foundation 

This is the source code for the https://betterconversations.foundation web site. 

It is built using Sphinx and the PyData theme.

Note the repository is public, as is the built site which is served up via GitHub Pages. 

## Handbook

This is in the `source/course/handbook` directory. Add new pages as Markdown and into the _toc.yml at the root level. 

TODO make this build a PDF for download and put it in the right place e.g. source/downloads/BC Course Handbook.pdf

## Building the PDF of the Site

This is done as part of the main build and can be downloaded in source/documentation/fullsite-pdf.rst


## Controlled Document Details

In Markdown files, you can add a dropdown with the controlled document details like this:

```{dropdown} Controlled Document Details
```{qms_header}

In RST files, you can add a dropdown with the controlled document details like this:

.. dropdown::
    Controlled Document Details

    .. qms_header::
