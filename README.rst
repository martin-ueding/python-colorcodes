.. Copyright © 2012-2014, 2016-2017 Martin Ueding <dev@martin-ueding.de>

#################
python-colorcodes
#################

This class supplies color codes for use in terminals. They are created using
the ``tput`` facility. You can get color output in a Python program like this::

    import colorcodes

    _c = colorcodes.Colorcodes()

    print(_c.red + "This is red text" + _c.reset)
    print(_c.red + _c.bold + "This is bold red text" + _c.reset)
