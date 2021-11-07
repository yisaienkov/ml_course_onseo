"""
Simple ML Models.
"""

class HousePriceModel:
    def __init__(self) -> None:
        pass

    def __call__(self, *, n_floors: int, area: float, heating: str) -> float:
        heating_bonus_dict = {
            "A": 100,
            "B": 20,
            "C": 10,
            "D": 0,
        }

        return 100 * n_floors + 5 * area + heating_bonus_dict[heating]

class SentimentModel:
    def __init__(self) -> None:
        self.vocabulary = {
            "good": 2,
            "bad": -2,
            "nice": 5,
            "excelent": 10,
            "ugly": -5
        }

    def __call__(self, *, text: str) -> int:
        processed_text = text.lower()

        score = 0

        for item, val in self.vocabulary.items():
            if item in processed_text:
                score += val
        
        return 1 if score > 0 else 0 if score == 0 else -1
