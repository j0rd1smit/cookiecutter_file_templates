from typing import Any, Dict, List, Optional, Union

import pytorch_lightning as pl
import torch
from torch.utils.data import DataLoader, Dataset

{%- if cookiecutter.custom_dataset == "True" -%}
{{""}}
{{""}}
class _Dataset(Dataset):
    def __init__(
        self,
    ):
        pass

    def __len__(self) -> int:
        pass

    def __getitem__(self, index) -> Dict[str, torch.Tensor]:
        pass


DatasetClass = _Dataset

{%- else -%}
{{""}}
{{""}}
DatasetClass = Any  # TODO
{% endif %}


class {{cookiecutter.name|replace("_", " ")|title|replace(" ", "")}}(pl.LightningDataModule):
    _train_dataset: DatasetClass
    _val_dataset: DatasetClass
    _test_dataset: DatasetClass
    _prediction_dataset: DatasetClass

    def __init__(
        self,
        *,
        batch_size: int,
        pin_memory: bool = True,
        num_workers: int = 0,
    ):
        super().__init__()
        self.batch_size = batch_size
        self.pin_memory = pin_memory
        self.num_workers = num_workers

    @property
    def dataset_size(self) -> int:
        assert self._train_dataset is not None, "setup(stage='fit') has not yet been called!"
        return len(self._train_dataset)

    def prepare_data(self) -> None:
        """
        Called from a single process (e.g. GPU 0).
        Do not use it to assign state (self.x = y).
        """
        pass

    def setup(self, stage: Optional[str] = None) -> None:
        """
        Called on every process separately.
        Use this to assign state.
        :param stage: Is either 'fit', 'validate', 'test' or None.
            If None, we assume all states have been set-up.
        """
        if stage in (None, "fit"):
            # TODO load data
            # TODO train/val split
            # TODO train/val transforms
            self._train_dataset = None  # TODO
            self._val_dataset = None  # TODO

        if stage in (None, "test"):
            # TODO load data
            # TODO test split
            # TODO test transforms
            self._test_dataset = None  # TODO
            self._prediction_dataset = None  # TODO

    def train_dataloader(self):
        return self._create_dataloader(self._train_dataset, shuffle=True)

    {%- if cookiecutter.validation_loop == "True" -%}
    {{""}}
    {{""}}
    def val_dataloader(self):
        return self._create_dataloader(self._val_dataset, shuffle=False)
    {{""}}
    {% endif %}

    {%- if cookiecutter.test_loop == "True" -%}
    {{""}}
    def test_dataloader(self):
        return self._create_dataloader(self._test_dataset, shuffle=False)
    {{""}}
    {% endif %}

    {%- if cookiecutter.custom_dataset == "True" -%}
    {{""}}
    def predict_dataloader(self) -> Union[DataLoader, List[DataLoader]]:
        return self._create_dataloader(self._prediction_dataset, shuffle=False)
    {{""}}
    {% endif %}

    def _create_dataloader(
        self,
        dataset: DatasetClass,
        *,
        shuffle: bool,
    ) -> torch.utils.data.DataLoader:
        return torch.utils.data.DataLoader(
            dataset,
            batch_size=self.batch_size,
            shuffle=shuffle,
            num_workers=self.num_workers,
            pin_memory=self.pin_memory,
        )
