{%- if cookiecutter.abstract|lower == "true" -%}
import abc 


{% endif -%}
class {{cookiecutter.file_name|replace("_", " ")|title|replace(" ", "")}}{% if cookiecutter.abstract|lower == "true" %}(abc.ABC){% endif %}:
	def __init__(
		self,
	) -> None:
		super().__init__()
