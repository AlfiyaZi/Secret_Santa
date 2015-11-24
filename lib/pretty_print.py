from django.core import serializers

def pretty_print(model):
	data = serializers.serialize("json", model, indent=4)
	print(data)