# Beerxml

## Description

The beerxml python package is a powerful tool designed to streamline the process of working with BeerXML files, ensuring that specific beer recipes adhere to the BeerXML standard. BeerXML is a widely adopted XML-based standard for representing brewing recipes, allowing brewers to share and exchange their recipes seamlessly.

## Installation

To install your package, use the following command:

```bash
pip install beerxml
```

## Code Generation

The models in this beerxml package have been generated from [this beerxml json schema](https://github.com/yourownbeer/beerxml-json-schema) with this command:

```
 datamodel-codegen  --input .\schemas\Recipe.json --input-file-type jsonschema --output output.py --snake-case-field --capitalise-enum-members --use-annotated  --use-non-positive-negative-number-constrained-types --output-model-type pydantic_v2.BaseModel
```

## Usage

Import the `BeerxmlParser` class and inject the file content into the class like in the following example:

```python
from beerxml import BeerxmlParser

# Example usage
parser: BeerxmlParser = BeerxmlParser()
with open("path/to/xml.file", "r") as file_content:
    recipe = parser.parse(file_content.read())

print(recipe.name)
print(recipe.hops)
print(recipe.fermentables)
print(recipe.yeasts)
```

## Contributing

We welcome contributions from the community! If you would like to contribute to this project, please follow these guidelines:

### Reporting Issues

If you encounter any issues or have suggestions, please [open an issue](https://github.com/lowmann15/beerxml/issues) on our GitHub repository.

### Pull Requests

1. Fork the repository and create a new branch for your contribution.
1. Write clear and concise commit messages.
1. Include unit tests for your changes
1. Submit a pull request, clearly describing the changes you've made and providing any necessary context.

### Linting and Code Style

We use the following linters to maintain code quality:

- [Ruff](https://github.com/astral-sh/ruff): for formatting.
- [Bandit](https://github.com/PyCQA/bandit): for security checks.
- [Mypy](https://github.com/python/mypy): for type checking.

Before submitting a pull request, ensure that your code passes these checks.

### Unit Testing

All contributions must be accompanied by unit tests using [pytest](https://github.com/pytest-dev/pytest). Test coverage is crucial to ensure the reliability of the codebase.

To run tests locally:

```bash
pytest .
```
