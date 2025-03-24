def predict_sentiment(text):
	"""
	 Prédit le sentiment d'un texte donné.

	Cette fonction analyse le texte pour déterminer s'il est positif,
	négatif ou neutre en fonction de certains mots-clés comme 'happy', 
	'good', 'sad' et 'bad'.
	
	 Paramètres:
	text (str): Le texte à analyser.
	"""
	if not text:
		return "neutral"
	if "happy" in text.lower() or "good" in text.lower():
		return "positive"
	if "sad" in text.lower() or "bad" in text.lower():
		return "negative"
	return "neutral"
