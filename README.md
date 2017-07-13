# druml

Unified Modeling Language (UML) Class Diagram generator for
multiple Drupal / PHP projects, written in Python 2.7.


## Usage


    $ python druml.py -p PATH/TO/PROJECTS


### Sample Usages

1. Generating Class Diagrams for Drupal Core modules.

    ```
    $ python druml.py -p ~/drupal-8.3.5/core/modules/
    ```

2. Generating Class Diagrams for Drupal Contrib modules.

    ```
    $ python druml.py -p ~/drupal-8.3.5/modules/
    ```



## Purpose

If you need a Class Diagram for each of your modules on a Drupal site, this is
for you.

Class Diagrams are very useful in the evaluation of how a Drupal module was
designed.

This program will read through the code of every single project in your
specified directory, and spit out nicely made Class Diagrams for each module.

One reason you may want to use druml would be if you're ever tasked with
performing a security evaluation
on multiple Drupal Contrib modules, or even Drupal Core modules. You'd get all
the Class Diagrams you'd need in seconds.


## Dependencies

druml requires two dependencies:

 - [phUML](https://github.com/jakobwesthoff/phuml) (downloaded during runtime)
 - [graphviz](http://graphviz.org/) (required prior to running)


 ### phUML

 phUML is a program that uses graphviz to generate a UML Class Diagram for a
 single project. druml runs phUML on every project in a directory, and stores
 its output in a nicely made folder.

 **Note:** phUML must be installed in the same directory as druml.py in order for
 druml to find it. Fortunately, you don't have to install it manually; if
 druml can't find it, you will be prompted to install it automatically.

 **Note:** phUML can use a lot of memory during runtime. To prevent the program
 from terminating early, it is suggested you configure `php.ini` to have no
 memory limit.

 `sudo vi /etc/php.ini`

 Find the line
 `memory_limit = 128M`

 And replace it with:
 `memory_limit = -1`

 If this is a concern, you can always change it back with ease.


 ### graphviz

 graphviz must be installed manually.

 To do so, run:

**Fedora:**
```
dnf install graphviz
```

**Ubuntu:**
```
apt-get install graphviz
```

**CentOS:**
```
yum install graphviz
```
