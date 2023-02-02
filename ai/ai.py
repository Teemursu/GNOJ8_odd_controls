from transformers import DistilBertForSequenceClassification, pipeline

model = DistilBertForSequenceClassification.from_pretrained(
    "distilbert-base-uncased", num_labels=2
)
candidate_labels = [
    "attack",
    "grab",
    "move",
]
for i in range(5):
    player_input = input("Player input:")
    pipe = pipeline(model="typeform/distilbert-base-uncased-mnli")
    result = pipe(player_input, candidate_labels=candidate_labels, multi_label=True)
    labels = result["labels"]
    scores = result["scores"]  # extracting the scores associated with the labels
    res_dict = {label: score for label, score in zip(labels, scores)}
    print("Action:", res_dict)
