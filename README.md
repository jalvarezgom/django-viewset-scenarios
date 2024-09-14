## Overview
Package for DRF that acts as a wrapper on any ViewSet in order to manage different serializers and paginators based on defined rules.

## Features
- Ddefinition of scenarios for a viewset
- Dynamically assign the serializer used for the response
- Dynamically assign the pager used for the response

## Installation

```console
pip install temporis
```
## Usage

### Create a new datetime object
```python

class ThingViewSet(ViewSetScenarios, viewsets.ModelViewSet):
    queryset = Thing.objects.all()
    scenarios = [
        DRFScenario(action=DRFActionType.DATATABLE, serializer=DealDatatableSerializer, pagination=None),
        DRFScenario(action=DRFActionType.LIST, serializer=DealSerializer, pagination=None),
        DRFScenario(action=DRFActionType.RETRIEVE, serializer=DealGetSerializer, condition=DRFScenariosCondition.action),
        DRFScenario(action=DRFActionType.DEFAULT, serializer=DealSerializer),
        DRFScenario(action="test_endpoint", serializer=DealSerializer, pagination=StandardPagination),
    ]

    @action(detail=False, methods=["get"])
    def test_endpoint(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()
        return Response(data=serializer(self.queryset, many=True).data)
```

##  Repository Structure

```sh
└── viewset_scenarios/
    ├── LICENSE
    ├── pdm.lock
    ├── pyproject.toml
    ├── README.md
    ├── src
        └── viewset_scenarios
```

## License

`viewset_scenarios` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.