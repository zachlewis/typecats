import sys

if sys.version_info <= (3, 7):
    from typing_extensions import Literal  # noqa
else:
    from typing import Literal  # noqa
