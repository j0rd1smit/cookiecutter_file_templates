{%- if cookiecutter.type == "runable" -%}
#!/usr/bin/env python3
def main():
	pass

if __name__ == '__main__':
	main()

{%- elif cookiecutter.type == "class" -%}
class {{cookiecutter.name|replace("_", " ")|title|replace(" ", "")}}:
	def __init__(
		self,
	) -> None:
		super().__init__()

{%- elif cookiecutter.type == "empty" -%}
{% endif %}