#!/usr/bin/env python3
{%- if cookiecutter.use_argparse|lower == "true" %}
from argparse import ArgumentParser


{% endif %}

def main():
	{%- if cookiecutter.use_argparse|lower == "true" %}
	parser = ArgumentParser()
	parser.add_argument("--seed", type=int, default=0, required=True)
	args = parser.parse_args()
	{% else %}
	pass
	{% endif %}

if __name__ == '__main__':
	main()
