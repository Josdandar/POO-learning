from textblob import TextBlob

class AnalizadorDeSentimientos:
    def analizar_sentimiento(self, texto):
        analisis = TextBlob(texto)
        if analisis.sentiment.polarity > 0:
            return "Positive feeling"
        elif analisis.sentiment.polarity == 0:
            return "neutral"
        else:
            return "Negative feeling"

analizador = AnalizadorDeSentimientos()
resultado = analizador.analizar_sentimiento("bless u")
print(resultado)
