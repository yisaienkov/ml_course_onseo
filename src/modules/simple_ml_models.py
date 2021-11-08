"""
Simple ML Models.
"""


class HousePriceModel:
    def __init__(self) -> None:
        self.heating_map = {
            "A": 100,
            "B": 50,
            "C": 10,
        }

    def __call__(self, area: int, n_floors: int, heating: str):
        return 100 * n_floors + 5 * area + self.heating_ma.get(heating, 0)


class SentimentModel:
    def __init__(self) -> None:
        self.word_map = {
            "nice": 10,
            "bad": -5,
            "fine": 5,
            "good": 2,
            "disgusding": -8,
            "hate": -3,
        }

    def __call__(self, text: str):
        lower_text = text.lower()
        
        total_score = 0
        
        for key, val in self.word_map.items():
            if key in lower_text:
                total_score += val

        return 1 if total_score > 0 else 0 if total_score == 0 else -1