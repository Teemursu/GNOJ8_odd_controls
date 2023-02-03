from transformers import DistilBertForSequenceClassification, pipeline

model = DistilBertForSequenceClassification.from_pretrained(
    "distilbert-base-uncased", num_labels=2
)
candidate_labels = [
    "attack something",
    "take something",
    "move somewhere",
]

take_labels = ["cat", "dog", "car",]

pipe = pipeline(model="typeform/distilbert-base-uncased-mnli")

for i in range(5):
    import time
    player_input = input("Player input: ")
    start_time = time.time()
    result = pipe(player_input, candidate_labels=candidate_labels, multi_label=True)
    labels, scores = result["labels"], result["scores"]
    res_dict = {label: score for label, score in zip(labels, scores)}
    print("Action:", max(res_dict, key=res_dict.get))
    if max(res_dict, key=res_dict.get) == "take something" or max(res_dict, key=res_dict.get) == "attack something":
        result = pipe(player_input, candidate_labels=take_labels, multi_label=True)
        labels, scores = result["labels"], result["scores"]
        take_dict = {label: score for label, score in zip(labels, scores)}
        print("that something is", max(take_dict, key=take_dict.get))