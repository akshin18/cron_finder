# Cron Expression Info Finder

## Overview
The Cron Expression Info Finder is a Python project designed to provide information about the different components of a cron expression. This tool parses a cron expression and breaks down its components, such as minute, hour, day of the month, month, and day of the week.

## Table of Contents
- [Installation](#installation)
- [Usage](#Usage)
- [Examples](#Examples)
- [Tests](#Tests)
## Installation
To use the Cron Expression Info Finder, you need to have Python installed on your machine. Follow these steps to set up the project:

1. **Clone the repository:**
```
git clone https://github.com/akshin18/cron_finder.git
```

3. **Navigate to the project directory:**
```
cd cron_finder
```

3. **Install the required dependencies:**
```
pip install -r requirements.txt
```

4. **Execute the command:**

```
python main.py "*/15 0 1,15 * 1-5"
```

## Tests
1. **Navigate to the project directory:**
```
cd cron_finder
```
2. **Run test:**
```
pytest
```

## Usage
To use the Cron Expression Info Finder, you can either import the Finder class into your own Python scripts or use it from the command line. Here's a basic example:

```
from cron_finder.src.finder import Finder
```

Instantiate the Finder class with a cron expression
```
cron_finder = Finder("*/15 * * * *", command="Your command here")
```

Find information about the cron expression
```
cron_finder.find_info()
```

Print the result
```
print(cron_finder)
```

## Examples
Here are a few examples of valid cron expressions that you can use with the Cron Expression Info Finder:

**Input:**
```
from cron_finder.src.finder import Finder


cron_finder = Finder("*/15 0 1,15 * 1-5")
cron_finder.find_info()
print(cron_finder)
```

**Output:**
```
minute              0 15 30 45
hour                0
day of month        1 15
month               1 2 3 4 5 6 7 8 9 10 11 12
day of week         1 2 3 4 5
command             main.py
```