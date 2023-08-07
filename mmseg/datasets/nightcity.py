from .builder import DATASETS
from .cityscapes import CityscapesDataset


@DATASETS.register_module()
class NightCityDataset(CityscapesDataset):

    def __init__(self, **kwargs):
        super(NightCityDataset, self).__init__(
            img_suffix='.png',
            seg_map_suffix='_labelTrainIds.png',
            **kwargs)