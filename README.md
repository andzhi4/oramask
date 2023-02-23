[![build status](https://github.com/andzhi4/raws/actions/workflows/matrix-test.yml/badge.svg)](https://github.com/andzhi4/raws/actions/workflows/matrix-test.yml)
# ORAMASK

ORAMASK is a very simple converter of Oracle specific date/time masks to Python's strftime masks.

## Installation

You can install the oramask by cloning the repository and running pip install:
```shell
git clone git@github.com:andzhi4/oramask
cd oramask && pip install .
```

or using PyPi:
```shell
python3 -m pip install oramask
```

## Examples
Here are a few examples of how to use the AWS Profile Manager:

Show all available profiles:
```python
import oramask
from datetime import datetime

now = datetime.now()
now.strftime(ora_to_sft('DD-MON-YYYY HH24:MI:SS'))
print(now)
```

## Contributing

If you find a bug or have an idea for a new feature, feel free to create an issue or submit a pull request.

## License

RAWS is released under the MIT License.





