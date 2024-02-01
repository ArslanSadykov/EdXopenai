import requests

class EdxAdapter:
    """
    EDX адаптер - логика получения данных с EDX API
    """
    def get_data(self, question_text) -> str:
        """
        :param question_text: Текст вопроса, для которого нужно получить ответ
        :return: Ответ на вопрос (предположим, что это текстовый ответ)
        """
        # Используем API Open edX для получения ответа на вопрос
        # Предположим что API Open edX имеет метод get_answer, который принимает вопрос и возвращает ответ
        # Заменяем этот вызов на реальный метод из API Open edX
        answer_from_edx = self.call_edx_api(question_text)

        # Возвращаем полученный ответ
        return answer_from_edx

    def call_edx_api(self, question_text):
        """
        Вызов API Open edX для получения ответа на вопрос
        """
        # API Open edX имеет URL для получения ответа на вопрос
        edx_api_url = "https://apps.edx.bronzebeard.pro/ora-grading/block-v1:talent_hub+tl01+2024_C1+type@openassessment+block@7b7b608626b546ddb7acb23b5f4d8360"

        # Формируем запрос
        payload = {"question_text": question_text}
        headers = {"Content-Type": "application/json"}

        # Отправляем POST-запрос к API Open edX
        response = requests.post(edx_api_url, json=payload, headers=headers)

        # Проверяем успешность запроса
        if response.status_code == 200:
            return response.json().get("answer", "")
        else:
            return f"Ошибка при обращении к API Open edX. Код ошибки: {response.status_code}"

# Пример использования
edx_adapter = EdxAdapter()

# Предположим, у нас есть вопрос
question_text = "Какой язык программирования самый популярный?"

# Получаем ответ от Open edX с использованием нашего адаптера
answer_from_edx = edx_adapter.get_data(question_text)

# Выводим полученный ответ
print(answer_from_edx)

