import sys
from .cli.main import main

# allow running nameko-extras with `python -m nameko_extras <args>`
if __name__ == '__main__':
    sys.exit(main())
