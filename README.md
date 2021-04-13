# PySimpleCanvas
PySimpleCanvas is a library built on PyGame that makes certain things easier. Here are some of the things you can do:

 - 

This library is meant to imitate Processing Java closely, but with some simpler things and built on PyGame for easier installation.

Mostly made this for fun, but also because prototyping is easy with Python, and I wanted to combine Processing's graphics capabilities with the simplicity of the Python language.

_Fun fact:_
  _This library does some cheaty things to make init easier to use. For example, many functions in the main module (and the draw submodule) use the inspect module to gain access to the caller's global variables. Because of this, you don't need to pass your setup, loop, or any functions to init for them to be called by the library._
