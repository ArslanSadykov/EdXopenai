import abc


class Model(abc.ABC):
    def __init__(self, edx_adapter, openai_adapter, *args, **kwargs):
        """
        :param edx_adapter: Адаптер, который отвечает за логику получения данных с EDX API
        :param openai_adapter: Адаптер, который отвечает за логику получения результата с запроса ChatGPT
        :param args: Вторичные данные
        :param kwargs: Остальные данные
        """
        self.edx_adapter = edx_adapter
        self.openai_adapter = openai_adapter

    @abc.abstractmethod
    def completion(self, text: str) -> str:
        pass
