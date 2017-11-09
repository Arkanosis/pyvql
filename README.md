# pyvql [![License](http://img.shields.io/badge/license-ISC-blue.svg)](/LICENSE)

**pyvql** is a Python implementation of a VQL (Variant Query Language) parser.

## Usage

```python
import pyvql

selects, froms, wheres, ins = pyvql.parse('SELECT selects FROM froms WHERE wheres IN ins')
```
## Contributing and reporting bugs

Contributions are welcome through [GitHub pull requests](https://github.com/Arkanosis/pyvql/pulls).

Please report bugs and feature requests on [GitHub issues](https://github.com/Arkanosis/pyvql/issues).

## License

pyvql is copyright (C) 2017 Jérémie Roquet <jroquet@arkanosis.net> and
licensed under the ISC license.
