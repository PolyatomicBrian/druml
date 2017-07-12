# druml

Unified Modeling Language (UML) Class Diagram generator for all Drupal projects
in a directory, written in Python 2.7.


## Usage

```
    $ python druml.py -p PATH/TO/PROJECTS
```

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

If you need a Class Diagram for each of your modules on a Drupal site, this is for you.

Class Diagrams are very useful in the evaluation of how a Drupal module was designed.

An example of usage would be if you're ever tasked with performing a security evaluation
of multiple Drupal Contributed modules, or even Drupal Core modules.

This program will spit out nicely made diagrams for each module.


## Dependencies

**druml will prompt the user to download any required dependencies during runtime.**

Those dependencies are:

 - [phUML](https://github.com/jakobwesthoff/phuml) (downloaded during runtime)
