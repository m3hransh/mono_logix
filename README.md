# Monologix

[![PyPI version](https://badge.fury.io/py/monologix.svg)](https://badge.fury.io/py/monologix)
![Python Versions](https://img.shields.io/pypi/pyversions/monologix)

**Monologix** is a Python library designed to enhance function execution with logging 
capabilities and result handling inspired by functional programming paradigms like monads 
and Rust's `Result` type.

## Features

- **Logging Decorator**: Wraps functions to log information about their execution, errors, 
        and results.
- **Result Type**: Implements a `Result` class for handling function outcomes,
        mimicking Rust's `Result` type or Haskell's `Maybe` type.
- **Monadic Logging**: Provides a decorator that can act like a monad for logging, 
    allowing for easy chaining of operations with built-in error handling and logging.

## Installation

### From PyPI

```bash
pip install monologix
```
## Usage
### Basic Logging with log_monad

### Result Handling

## Contributing
Contributions are welcome! Here's how you can contribute:

1. Fork the repository
2. Create your feature branch (git checkout -b feature/YourFeature)
3. Commit your changes (git commit -am 'Add some feature')
4. Push to the branch (git push origin feature/YourFeature)
5. Create a new Pull Request

Please ensure your code adheres to the project's style guide and includes tests.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
