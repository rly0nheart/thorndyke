![Python Version](https://img.shields.io/badge/python-3.x-blue?style=flat&logo=python)
![OS](https://img.shields.io/badge/OS-GNU%2FLinux-red?style=flat&logo=linux)
![GitHub](https://img.shields.io/github/license/rlyonheart/thorndyke?style=flat&logo=pypi)
![Lines of code](https://img.shields.io/tokei/lines/github/rlyonheart/thorndyke?style=flat&logo=github)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/rlyonheart/thorndyke?style=flat&logo=github)
[![CodeFactor](https://www.codefactor.io/repository/github/rlyonheart/thorndyke/badge)](https://www.codefactor.io/repository/github/rlyonheart/thorndyke)
![Snyk Vulnerabilities for GitHub Repo](https://img.shields.io/snyk/vulnerabilities/github/rlyonheart/thorndyke?style=flat&logo=pypi)
[![PyPI Downloads](https://pepy.tech/badge/thorndyke)](https://pepy.tech/project/thorndyke)
![PyPI](https://img.shields.io/pypi/v/thorndyke?style=flat&logo=pypi)

**Thorndyke**: *Username enumeration tool that checks the availability of a specified username on over 300 websites.*
[![asciicast](https://asciinema.org/a/449177.svg)](https://asciinema.org/a/449177)

# Clone from Github

```
git clone https://github.com/rlyonheart/thorndyke.git
```

```
cd thorndyke
```

```
pip install -r requirements.txt
```

```
python thorndyke -u [USERNAME]
```
[![asciicast](https://asciinema.org/a/rW2YwdTX8xMO00dNphttz2C6v.svg)](https://asciinema.org/a/rW2YwdTX8xMO00dNphttz2C6v)


# Install from Pypi

```
pip install thorndyke
```

```
thorndyke [USERNAME]
```

# Initialyzing the Bash alternative

```
python thorndyke --shell -u [USERNAME]
```
[![asciicast](https://asciinema.org/a/H53w6b1KRE7824xyO6VKUqF6c.svg)](https://asciinema.org/a/H53w6b1KRE7824xyO6VKUqF6c)

# Optional Args
| Flag |MetaVar|Usage|
| ------------- |:----------------------:|:---------:|
| <code>-u/--username</code>      |   **USERNAME** |  *target username (if username is not specified,Thorndyke will instead run tests on the site.json file*  |
| <code>-sh/--shell</code>      |   |  *run the Bash alternative of Thorndyke*  |
| <code>-d/--dictionary</code>  | **FILENAME**   |  *specify a custom file containing a list of websites to user for searching a username*  |
| <code>-v/--verbose</code>  |    |  *run thorndyke in verbose mode (show network logs and errors)*  |


# LICENSE
![license](https://user-images.githubusercontent.com/74001397/137917929-2f2cdb0c-4d1d-4e4b-9f0d-e01589e027b5.png)

# About author
* [About.me](https://about.me/rlyonheart)

# Contact author
* [Github](https://github.com/rlyonheart)

* [Twitter](https://twitter.com/rly0nheart)
