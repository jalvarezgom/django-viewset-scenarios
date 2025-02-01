<h1 align="center">ViewSet Scenarios</h1>

<p align="center">
    <em>An elegant DRF library for managing and transforming serializers and paginators in your ViewSets based on defined scenarios</em>
</p>

<p align="center">
    <a href="https://github.com/jalvarezgom/drf-viewset-scenarios/blob/main/LICENSE">
        <img src="https://img.shields.io/github/license/jalvarezgom/drf-viewset-scenarios?style=flat-square&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="License">
    </a>
    <a href="https://github.com/jalvarezgom/drf-viewset-scenarios/commits">
        <img src="https://img.shields.io/github/last-commit/jalvarezgom/drf-viewset-scenarios?style=flat-square&logo=git&logoColor=white&color=0080ff" alt="Last commit">
    </a>
    <a href="https://pypi.org/project/drf-viewset-scenarios/">
        <img src="https://img.shields.io/pypi/v/drf-viewset-scenarios.svg?style=flat-square&logo=pypi&logoColor=white&color=0080ff" alt="PyPI Version">
    </a>
    <a href="https://pypi.org/project/drf-viewset-scenarios/">
        <img src="https://img.shields.io/pypi/pyversions/drf-viewset-scenarios?style=flat-square&logo=python&logoColor=white&color=0080ff" alt="Python Versions">
    </a>
</p>

## 🚀 Description

A Django REST Framework package that provides a flexible way to manage different serializers and paginators in your ViewSets based on defined scenarios.

## ✨ Key Features

ViewSet Scenarios allows you to:
- Define multiple scenarios for a single ViewSet
- Dynamically assign serializers based on actions or conditions
- Configure pagination settings per scenario
- Handle custom endpoints with specific serialization needs

## 🛠️ Installation

```bash
pip install drf-viewset-scenarios
```

## Quick Start

Here's a simple example of how to use ViewSet Scenarios:

```python
from viewset_scenarios import ViewSetScenarios, DRFScenario, DRFActionType
from rest_framework import viewsets

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    scenarios = ViewSetScenarios([
        DRFScenario(
            action=DRFActionType.LIST, 
            serializer=ProductListSerializer,
            pagination=StandardPagination
        ),
        DRFScenario(
            action=DRFActionType.RETRIEVE,
            serializer=ProductDetailSerializer
        ),
        DRFScenario(
            action=DRFActionType.DEFAULT,
            serializer=ProductBaseSerializer
        ),
    ])

    def get_serializer_class(self):
        return self.scenarios.get_serializer_class(self)

    @property
    def paginator(self):
        return self.scenarios.get_paginator(self)
```

## Features

### Action Types
Built-in support for common ViewSet actions:
- `LIST`: List view
- `RETRIEVE`: Detail view
- `CREATE`: Creation view
- `UPDATE`: Update view
- `DATATABLE`: Special handling for datatable requests
- `DEFAULT`: Fallback scenario

### Scenario Configuration
Each scenario can define:
- `action`: The ViewSet action or custom endpoint
- `serializer`: The serializer class to use
- `pagination`: Optional pagination class
- `condition`: Optional condition for more complex logic

### Custom Endpoints
Support for custom actions with specific serialization needs:

```python
class ProductViewSet(ViewSetScenarios, viewsets.ModelViewSet):
    scenarios = [
        DRFScenario(
            action="featured_products",
            serializer=FeaturedProductSerializer,
            pagination=None
        ),
    ]

    @action(detail=False, methods=["get"])
    def featured_products(self, request):
        products = self.get_queryset().filter(featured=True)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)
```

## Advanced Usage

### Conditional Scenarios
You can use conditions to determine which serializer to use:

```python
class OrderViewSet(viewsets.ModelViewSet):
    scenarios = ViewSetScenarios([
        DRFScenario(
            action=DRFActionType.RETRIEVE,
            serializer=OrderDetailSerializer,
            condition=lambda request: request.user.is_staff
        ),
        DRFScenario(
            action=DRFActionType.RETRIEVE,
            serializer=OrderBasicSerializer
        ),
    ])
```

### Custom Pagination
Configure different pagination per scenario:

```python
class ProductViewSet(viewsets.ModelViewSet):
    scenarios = ViewSetScenarios([
        DRFScenario(
            action=DRFActionType.LIST,
            serializer=ProductListSerializer,
            pagination=LargeResultsPagination
        ),
        DRFScenario(
            action="featured",
            serializer=ProductListSerializer,
            pagination=None  # Disable pagination for this endpoint
        ),
    ])
```

## 📁 Project Structure

```
└── viewset_scenarios/
    ├── LICENSE
    ├── pyproject.toml
    ├── README.md
    └── src/
        └── viewset_scenarios/
            ├── __init__.py
            ├── action_type.py
            └── scenarios.py
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📫 Contact

- GitHub: [@jalvarezgom](https://github.com/jalvarezgom)
- PyPI: [drf-viewset-scenarios](https://pypi.org/project//)

---

<p align="center">
    <em>Developed with ❤️ by Jancel</em>
</p>
