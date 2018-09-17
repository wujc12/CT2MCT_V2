import os.path
from datasets.base_dataset import BaseDataset


class AlignedDataset(BaseDataset):
    def __init__(self):
        BaseDataset.__init__(self)
        self.dataset_name = 'AlignedDataset'
        self.opt = None
        self.root = None
        self.dir_AB = None

    def initialize(self, opt):
        self.opt = opt
        self.root = opt.dataroot
        self.dir_AB = os.path.join(opt.dataroot, opt.phase)
        assert (opt.resize_or_crop == 'resize_and_crop')

    def name(self):
        return self.dataset_name

    def __getitem__(self, index):
        return index

    def __len__(self):
        return len(self.AB_paths)
