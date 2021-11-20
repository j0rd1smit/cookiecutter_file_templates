import math
from typing import Any, Dict, List, Optional

import pytorch_lightning as pl
import torch
import torch.nn.functional as F
from torch.optim import Optimizer


class {{cookiecutter.model_class_name}}(pl.LightningModule):
    def __init__(
        self,
        *,
        # Network
        # Optimization
        lr: float = 5e-4,
    	{%- if cookiecutter.lr_scheduler == "OneCycleLR" -%}
    	{{""}}
        # LR schedule
        batch_size: int,
        dataset_size: int,
        n_epochs: int,
        {% endif %}
    ) -> None:
        super().__init__()
        self.save_hyperparameters()
        self.network = self._create_network()

	{%- if cookiecutter.automatic_optimization == "False" -%}
    {{""}}
    {{""}}
	@property
    def automatic_optimization(self) -> bool:
        return False
	{% endif %}

	def _create_network(self) -> torch.nn.Module:
        pass

    def training_step(
        self,
        batch: Any,
        batch_idx: int,
        optimizer_idx: Optional[int] = None,
        **kwargs: Dict[str, Any],
    ) -> Dict[str, torch.Tensor]:
    	{%- if cookiecutter.automatic_optimization == "False" -%}
    	{{""}}
    	optimizer1, *_ = self.optimizers()
    	{{""}}
    	{% endif %}
        loss = None  # TODO

        return {"loss": loss}

    {%- if cookiecutter.training_epoch_end == "True" -%}
    {{""}}
    {{""}}
    def training_epoch_end(
        self,
        outputs: Dict[str, torch.Tensor],
    ) -> None:
        loss = torch.stack([x["loss"] for x in outputs]).mean()
        # TODO
    {% endif %}

    {%- if cookiecutter.validation_loop == "True" -%}
    {{""}}
    {{""}}
    def validation_step(
        self,
        batch: Any,
        batch_idx: int,
        **kwargs: Dict[str, Any],
    ) -> Dict[str, torch.Tensor]:
        loss = None  # TODO

        return {"loss": loss}

    def validation_epoch_end(
        self,
        outputs: List[Dict[str, torch.Tensor]],
    ) -> None:
        loss = torch.stack([x["loss"] for x in outputs]).mean()
        # TODO
    {% endif %}

    {%- if cookiecutter.test_loop == "True" -%}
    {{""}}
    {{""}}
    def test_step(
        self,
        batch: Any,
        batch_idx: int,
        **kwargs: Dict[str, Any],
    ) -> Dict[str, torch.Tensor]:
        loss = None  # TODO

        return {"loss": loss}

    def test_epoch_end(
        self,
        outputs: List[Dict[str, torch.Tensor]],
    ) -> None:
        loss = torch.stack([x["loss"] for x in outputs]).mean()
        # TODO
    {% endif %}

    {%- if cookiecutter.prediction_loop == "True" -%}
    {{""}}
    {{""}}
    def predict_step(
        self,
        batch: Any,
        batch_idx: int,
        dataloader_idx: Optional[int] = None,
        **kwargs: Dict[str, Any],
    ) -> Dict[str, torch.Tensor]:
        prediction = None  # TODO

        return {"prediction": prediction}
    {% endif %}

    def configure_optimizers(self) -> Tuple[List[Optimizer], List[Any]]:
        optimizer = torch.optim.Adam(self.parameters(), lr=self.hparams.lr)

        {%- if cookiecutter.lr_scheduler == "OneCycleLR" -%}
		{{""}}
		{{""}}
        total_steps = math.ceil(self.hparams.dataset_size / self.hparams.batch_size) * self.hparams.n_epochs
        lr_scheduler = {
            "scheduler": torch.optim.lr_scheduler.OneCycleLR(
                optimizer,
                self.hparams.lr,
                total_steps=total_steps,
            ),
            "interval": "step",
            "frequency": 1,
        }
        return [optimizer], [lr_scheduler]
        {%- elif cookiecutter.lr_scheduler == "None" -%}
    {{""}}
    {{""}}
        return [optimizer], []
        {% endif %}
