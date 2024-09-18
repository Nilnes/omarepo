import webbrowser
import random

lista = ["https://www.youtube.com/watch?v=dtER80sOjX4",
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "https://www.youtube.com/watch?v=PKQPey6L42M"]

url = (random.choice(lista))

webbrowser.open(url)