from domain.model import Model
from adapters.edx_adapter import EdxAdapter
from adapters.openai_adapter import OpenAiAdapter


class MyModel(Model):
    """
    Создание модели с подсоединением логики адаптеров
    """

    def completion(self, text: str) -> str:
        """
        :param completion: Логика подсоединения адаптеров и вывод нужного результата
        :return: Вывод результата от ChatGPT
        """

        # Получение данных с Edx API
        data_from_edx = self.edx_adapter.get_data(text)

        # Передача данных в OpenAI API
        processed_data_from_openai = self.openai_adapter.generate_response(data_from_edx)

        # Возврат результата
        return processed_data_from_openai


def main(text: str):
    """
    :param main: Запуск адаптеров и вывод результата с адаптеров
    :return: Результат обработки с ChatGPT
    """
    my_model = MyModel(edx_adapter=EdxAdapter(), openai_adapter=OpenAiAdapter())

    result = my_model.completion(text)
    print(result)


if __name__ == "__main__":
    """
    Запуск бесконечного запроса с получением ответа от ChatGPT
    """
    while True:
        word = input("Введите запрос: ")
        if word == "/q":
            break
        else:
            print(main(word))
