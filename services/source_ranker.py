from urllib.parse import urlparse


class SourceRanker:

    PRIORITY = {

        "grindwellnorton.co.in": 100,

        "annual": 98,

        "investor": 96,

        "moneycontrol": 92,

        "economictimes": 91,

        "screener.in": 90,

        "yahoo": 88,

        "mca": 87,

        "gst": 86,

        "linkedin": 84,

        "indiamart": 75,

        "ambitionbox": 60

    }

    def score(self, url):

        url = url.lower()

        score = 10

        for keyword, value in self.PRIORITY.items():

            if keyword in url:

                score = max(score, value)

        return score