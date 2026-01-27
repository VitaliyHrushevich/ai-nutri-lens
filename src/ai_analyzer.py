"""AI Analyzer for AI Nutri-Lens - Clean Architecture implementation."""

from typing import List
import requests
from requests.exceptions import RequestException


class NutriAnalyzer:
    """Professional AI nutrition analyst using local LLM."""

    def __init__(self, base_url: str = "http://localhost:11434", model: str = "llama3"):
        self.base_url = base_url
        self.model = model

    def analyze_ingredients(self, ingredients: List[str]) -> str:
        """Main analysis method - direct replacement."""
        print("🧠 AI is thinking (Context: Global & CIS Markets)...")

        ingredients_str = ", ".join(ingredients)
        prompt = f"""
        Ты — международный эксперт по питанию (Европа/США/СНГ). 
        ИНГРЕДИЕНТЫ: {ingredients_str}

        1. Тип продукта
        2. Сахар/специфика  
        3. Чистота состава
        4. Вердикт + оценка 1-10

        Отвечай на русском.
        """

        try:
            url = f"{self.base_url}/api/generate"
            payload = {"model": self.model, "prompt": prompt, "stream": False}

            resp = requests.post(url, json=payload, timeout=30)
            resp.raise_for_status()
            return resp.json()["response"].strip()

        except RequestException as e:
            return f"❌ Ollama недоступна: {e}"
        except Exception as e:
            return f"❌ Ошибка анализа: {e}"



def create_nutri_analyzer(base_url: str = "http://localhost:11434"):
    """Factory function"""
    return NutriAnalyzer(base_url)


def analyze_ingredients(ingredients: List[str]):
    analyzer = create_nutri_analyzer()
    return analyzer.analyze_ingredients(ingredients)
