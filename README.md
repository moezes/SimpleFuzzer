# _SFUZZ_ - A Basic, SimpleFuzzer Program


## Description

Tool for fuzzing developed in Python.
The goal of this project is to have a simple fuzzer written in python that can easily be integrated and updated.

## Table of Contents

- [Pre-requisites](#Pre-requisites)
- [Installation](#installation)
    - [Venv](#virtualenv)
    - [Packages](#packages)
- [Usage](#usage)
- [Tests](#Tests)

---

## Pre-requisites

The project was test with Python 3.10. It should work with newer versions however, we cannot guarantee the results.

## Installation
0. Clone the project
```
$   git clone https://github.com/moezes/SimpleFuzzer.git
```

### Virtualenv
1. cd into the project

```
$   cd ./SimpleFuzzer
```
2. Create your venv
```
$   python -m venv vnv
```
3. Activate the new virtual environment _vnv_
```
$   source vnv/bin/activate
```

### Packages

Install required packages using
```
$	sudo apt-get install python-dev graphviz libgraphviz-dev pkg-config
```
then 
```
$   pip install -r requirements
```

## Usage

To run the program use
```
$   python -m sfuzz
```
The program will automatically test the binaries in the `tests/binaries/bin/` folder and return the details and the argument used to smash the stack

---

## Tests


