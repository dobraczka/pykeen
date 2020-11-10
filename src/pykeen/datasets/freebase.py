# -*- coding: utf-8 -*-

"""Freebase datasets.

* FB15k
* FB15k-237
"""

import pathlib
from typing import Optional

from .base import TarFileRemoteDataSet, ZipFileRemoteDataSet
from ..typing import Path

__all__ = [
    'FB15k',
    'FB15k237',
]


class FB15k(TarFileRemoteDataSet):
    """The FB15k data set."""

    def __init__(self, cache_root: Optional[Path] = None, **kwargs):
        super().__init__(
            url='https://everest.hds.utc.fr/lib/exe/fetch.php?media=en:fb15k.tgz',
            relative_training_path=pathlib.PurePath('FB15k', 'freebase_mtr100_mte100-train.txt'),
            relative_testing_path=pathlib.PurePath('FB15k', 'freebase_mtr100_mte100-test.txt'),
            relative_validation_path=pathlib.PurePath('FB15k', 'freebase_mtr100_mte100-valid.txt'),
            cache_root=cache_root,
            **kwargs,
        )


class FB15k237(ZipFileRemoteDataSet):
    """The FB15k-237 data set."""

    def __init__(self, cache_root: Optional[Path] = None, **kwargs):
        super().__init__(
            url='https://download.microsoft.com/download/8/7/0/8700516A-AB3D-4850-B4BB-805C515AECE1/FB15K-237.2.zip',
            relative_training_path=pathlib.PurePath('Release', 'train.txt'),
            relative_testing_path=pathlib.PurePath('Release', 'test.txt'),
            relative_validation_path=pathlib.PurePath('Release', 'valid.txt'),
            cache_root=cache_root,
            **kwargs,
        )
