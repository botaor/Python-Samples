# Python Samples #

## What is it? ##
I learned [Python][py] a few years ago and I really like the language.

The problem is that I am really a C/C++ developer and thus only use Python from time to time. This makes it impossible to always remember the proper syntax,  language constructs and library calls.

Because of this I am making this simple repository. It will have examples of the main Python constructs I use. So that when I need to do something, I can just look it up here, instead of having to remember which was the last project where I used it.

By definition this will always be a work in progress.

## Components ##
The project is divided into several files. Each file deals with a particular aspect of the language. The name of the file should be indicative of what is inside. There will be help strings in the files and in the functions, so that it will be possible to use the Python `help` function to get the necessary information.

Just do the following:

    >>>import <module>
    >>>help( '<module>' )
    >>>help( '<module>.<function>' )

Some modules might have other dependencies. If this is the case, then it is clearly marked in the documentation string of the module.

The file `Template.py` is just what I use to start a new module. It has no real use by itself.

Some modules need sample files to show their purpose. All these sample files are kept in the `Samples` directory.

## Environment ##
Unless otherwise specified all example code is for Python 2.7.

All testing is done in Windows, but it should work just as well in other operating systems. Modules that are known to only work in windows, are marked as such in the documentation string.

## Licensing ##
This code is distributed under the [MIT][mit] license. See the [LICENSE][license] file in the root of this repository.

## Contacts ##
Contact the developer at: [rui@ruibotao.com][rui]

## Author ##
Developed by Rui Botão (computer programmer and enthusiast orienteer).


[rui]: mailto:rui@ruibotao.com "Rui"
[py]:  http://www.python.org/  "Python"
[mit]:  https://opensource.org/licenses/MIT/  "MIT"
[license]: LICENSE "LICENSE"

