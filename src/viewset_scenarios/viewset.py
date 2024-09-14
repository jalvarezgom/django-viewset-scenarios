from src.viewset_scenarios.exceptions import ViewSetScenarioException
from src.viewset_scenarios.scenarios import DRFDirectorScenarios


class ViewSetScenarios:
    director_class = DRFDirectorScenarios
    _pagination_scenarios_class = None
    _serializer_scenarios_class = None
    _action_scenarios_class = None
    scenarios = None

    def __init__(self, *args, **kwargs):
        self.director_class = self.director_class()
        self.director_class.set_scenarios(self.scenarios)

    @property
    def paginator(self):
        if self.pagination_class is not None:
            self._paginator = getattr(self, "_paginator", None) or self.pagination_class()
            return self._paginator
        _paginator = None
        if self.director_class.paginations is not None:
            scenario = self.director_class.get_action(self.action, self.request)
            _paginator = self.director_class.get_pagination(scenario)()
        return _paginator

    def get_serializer_class(self):
        if self.serializer_class:
            return self.serializer_class
        scenario = self.director_class.get_action(self.action, self.request)
        serializer_class = self.director_class.get_serializer(scenario, self.action)
        if serializer_class is None:
            raise ViewSetScenarioException(
                "'%s' should either include a `serializer_class` attribute, "
                "or override the `get_serializer_class()` method." % self.__class__.__name__
            )
        return serializer_class
