BAKE_OPTIONS=--no-input

help:
	@echo "bake 	generate project using defaults"

bake:
	cookiecutter $(BAKE_OPTIONS) . --overwrite-if-exists
