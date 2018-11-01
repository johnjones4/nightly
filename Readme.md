# Nightly

Nightly is a simple utility for executing a command every evening. Think of it as a poor person's Cron that only does one thing with a less-flexible scheduling system. I built this to handle kicking off automated scripts inside a few Docker projects.

## Requirements:

* Python 3.6+
* Python pip

## Installation:

```sh
pip install nightly
```

## Usage:

The following will run `/path/to/script.sh` every day at 4am:

```sh
# nightly --when 4:00 /path/to/script.sh
```
