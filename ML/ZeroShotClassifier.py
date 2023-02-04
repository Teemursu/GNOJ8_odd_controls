from godot import exposed, export
from godot import *

import json
import pickle
from transformers import DistilBertForSequenceClassification, pipeline


class ModelLoader:
	
	def __init__(self):
		
		model = DistilBertForSequenceClassification.from_pretrained(
			"distilbert-base-uncased", num_labels=2
		)
		try:
			with open('ML/DistilBertForSequenceClassificationModel.pkl', 'rb') as f:
				model = pickle.load(f)
		except Exception as e:
			model = DistilBertForSequenceClassification.from_pretrained(
				"distilbert-base-uncased", num_labels=2
			)
			with open('ML/DistilBertForSequenceClassificationModel.pkl', 'wb') as f:
				pickle.dump(model, f)
		
		self.pipe = pipeline(model="typeform/distilbert-base-uncased-mnli")


@exposed
class ZeroShotClassifier(Node2D):
	
	def check_result(self, player_input):
		player_input_string = str(player_input)
		print(player_input)
		keywords = {}
		result = self.zero_shot_classifier.pipe(player_input_string, candidate_labels=self.candidate_labels, multi_label=True)
		labels, scores = result["labels"], result["scores"]
		res_dict = {label: score for label, score in zip(labels, scores)}
		print("Action:", max(res_dict, key=res_dict.get))
		keywords['verb'] = max(res_dict, key=res_dict.get)
		if max(res_dict, key=res_dict.get) == "take something" or max(res_dict, key=res_dict.get) == "attack something":
			result = self.zero_shot_classifier.pipe(player_input_string, candidate_labels=self.take_labels, multi_label=True)
			labels, scores = result["labels"], result["scores"]
			take_dict = {label: score for label, score in zip(labels, scores)}
			object = max(take_dict, key=take_dict.get)
			print("that something is", max(take_dict, key=take_dict.get))
			keywords['object'] = object
		return json.dumps(keywords)


	def _ready(self):
		self.candidate_labels = [
			"attack something",
			"take something",
			"move somewhere",
		]

		self.take_labels = ["weapon", "document", "phone",]

		self.zero_shot_classifier = ModelLoader()
