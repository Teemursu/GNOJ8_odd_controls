extends Node2D

onready var zero_shot_classifier = $ZeroShotClassifier


func _ready():
	var r = parse_json(zero_shot_classifier.check_result('Get the sword'))
	print(r)
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass
