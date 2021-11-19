import pprint

import pytorch_lightning as pl
from jsonargparse import ArgumentParser, namespace_to_dict
from pytorch_lightning import seed_everything
{%- if cookiecutter.lr_scheduler != "None" -%}
{""}
from pytorch_lightning.callbacks import LearningRateMonitor
{% endif %}


from .{{cookiecutter.model_file_name}} import {{cookiecutter.model_class_name}}
from .{{cookiecutter.data_module_file_name}} import {{cookiecutter.data_module_class_name}}


def main():
    parser = ArgumentParser()
    parser.add_class_arguments({{cookiecutter.model_class_name}}, "model", skip={})
    parser.add_class_arguments({{cookiecutter.data_module_class_name}}, "data")

    # General args
    parser.add_argument("--general.seed", type=int, default=0)
    parser.link_arguments("general.seed", "data.seed")

    # Training args
    parser.add_argument("--training.seed", type=int, default=0)
    parser.add_argument("--training.n_epochs", type=int, default=25)
    parser.add_argument("--training.fast_dev_run", type=bool, default=False)
    parser.add_argument("--training.gpus", type=int, default=1)

    cfg = parser.parse_args()

    seed_everything(cfg.general.seed, workers=True)

    data_module = {{cookiecutter.data_module_class_name}}(**namespace_to_dict(cfg.data))

    model = {{cookiecutter.model_class_name}}(
        **namespace_to_dict(cfg.model),
    )

    pprint.pprint(namespace_to_dict(cfg))

    callbacks = [
        {%- if cookiecutter.lr_scheduler != "None" -%}
        LearningRateMonitor(log_momentum=True),
        {% endif %}
    ]

    trainer = pl.Trainer(
        gpus=cfg.training.gpus,
        fast_dev_run=cfg.training.fast_dev_run,
        max_epochs=cfg.training.n_epochs,
        callbacks=callbacks,
        auto_lr_find=True,
        checkpoint_callback=True,
    )

    trainer.tune(model, data_module)
    trainer.fit(model, data_module)
    {%- if cookiecutter.test_loop == "True" -%}
    {""}
    trainer.test(model, data_module.test_dataloader())
    {% endif %}

    {%- if cookiecutter.prediction_loop == "True" -%}
    {""}
    if not cfg.training.fast_dev_run:
        predictions = trainer.predict(model, data_module.predict_dataloader(), return_predictions=True)
        # TODO
    {% endif %}


if __name__ == "__main__":
    main()
