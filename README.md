[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![codecov](https://codecov.io/gh/fcbg-platforms/byte-triggers/graph/badge.svg?token=rSGaJehUMl)](https://codecov.io/gh/fcbg-platforms/byte-triggers)
[![tests](https://github.com/fcbg-platforms/byte-triggers/actions/workflows/pytest.yml/badge.svg?branch=main)](https://github.com/fcbg-platforms/byte-triggers/actions/workflows/pytest.yml)
[![doc](https://github.com/fcbg-platforms/byte-triggers/actions/workflows/doc.yml/badge.svg?branch=main)](https://github.com/fcbg-platforms/byte-triggers/actions/workflows/doc.yml)

# Byte-triggers

Delivers integer triggers between 0 and 255 on a parallel port or on an LSL marker
stream.

## Install

`byte_triggers` is available on [PyPI](https://pypi.org/project/byte_triggers/).

```
pip install byte_triggers
```

## Usage

For the API reference, see the online
[documentation](https://fcbg-platforms.github.io/byte-triggers).

```
from byte_triggers import LSLTrigger, MockTrigger, ParallelPortTrigger

trigger = MockTrigger()
trigger.signal(1)

trigger = LSLTrigger("MyTrigger")
trigger.signal(1)

# on-board parallel port on linux
trigger = ParallelPortTrigger("/dev/parport0")
trigger.signal(1)

# on-board parallel port on windows
trigger = ParallelPortTrigger(0x4FB8)
trigger.signal(1)

# arduino to parallel port converter
trigger = ParallelPortTrigger("arduino")
trigger.signal(1)
```

# Copyright and license

The code is released under the [MIT License](https://opensource.org/licenses/MIT).
