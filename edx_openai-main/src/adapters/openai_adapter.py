import openai


class OpenAiAdapter:
    """
    Адаптер OpenAI - отправка запроса и получение результата от ChatGPT
    """
    openai.api_key = 'API-KEY'  # Ключ OpenAI

    def generate_response(self, prompt):
        """
        :param prompt: Запрос, который был получен
        :return: Результат обработки запроса от ChatGPT
        """
        response = openai.Completion.create(
            engine='text-davinci-003',  # Движок можно менять
            prompt=prompt,
            max_tokens=3796,
            temperature=0.8,
            n=1,
            stop=None,
            timeout=50
        )
        return response.choices[0].text.strip()
