BAKE_OPTIONS=--no-input

help:
	@echo "bake 	generate project using defaults"
	@echo "clean 	cleans out old generated files"

clean:
	rm -rf cmd2-example-plugin

bake: clean
	cookiecutter $(BAKE_OPTIONS) . --overwrite-if-exists

inst: bake
	pip install -e cmd2-example-plugin/cmd2_base_app
	pip install -e cmd2-example-plugin/sample_plugin
