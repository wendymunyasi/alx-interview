# Project Name
**0x06. Star Wars API**

## Author's Details
Name: *Wendy Munyasi.*

Email: *wendymunyasi@gmail.com*

Tel: *+254707240068.*

##  Requirements

### JavaScript Scripts
*   Allowed editors: `vi`, `vim`, `emacs`, `Visual Studio Code`.
*   All your files will be interpreted on Ubuntu 20.04 LTS using `node` (version 14.x).
*   All your files should end with a new line.
*   The first line of all your files should be exactly `#!/usr/bin/node`.
*   Your code should be `semistandard` compliant.
*   All your files must be executable.
*   The length of your files will be tested using `wc`.
*   You are not allowed to use `var`.


## More Info
### Install Node 14
```
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Install semi-standard
```
$ sudo npm install semistandard --global
```

### Install request module
```
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

## Project Description

* **0. Star Wars Characters** - Write a script that prints all characters of a Star Wars movie. - `0-starwars_characters.js`.
    *   The first positional argument passed is the Movie ID - example: `3` = “Return of the Jedi”.
    *   Display one character name per line in the same order as the “characters” list in the `/films/` endpoint.
    *   You must use the [Star wars API](https://swapi-api.alx-tools.com/).
    *   You must use the `request` module.

    ```
    alexa@ubuntu:~/0x06$ ./0-starwars_characters.js 3
    Luke Skywalker
    C-3PO
    R2-D2
    Darth Vader
    Leia Organa
    Obi-Wan Kenobi
    Chewbacca
    Han Solo
    Jabba Desilijic Tiure
    Wedge Antilles
    Yoda
    Palpatine
    Boba Fett
    Lando Calrissian
    Ackbar
    Mon Mothma
    Arvel Crynyd
    Wicket Systri Warrick
    Nien Nunb
    Bib Fortuna
    alexa@ubuntu:~/0x06$
    ```

## Collaborate

To collaborate, reach me through my email address wendymunyasi@gmail.com.
