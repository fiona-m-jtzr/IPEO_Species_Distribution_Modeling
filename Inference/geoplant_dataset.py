import numpy as np
import torch
from sklearn.model_selection import train_test_split
from torch.utils.data import Dataset

class GeoPlantDataset(Dataset):
    def __init__(self, images, timeseries, tabular, labels, split='train', val_split=0.2, random_state=42):
        """
        Args:
            images: numpy array of satellite images
            timeseries: numpy array of time series data
            tabular: numpy array of environmental variables
            labels: numpy array of species labels
            split: 'train', 'val', or 'test'
            val_split: fraction of training data to use for validation (default 0.2)
            random_state: random seed for reproducibility
        """
        self.split = split

        if split == 'test' or split is None:
            self.images = images
            self.timeseries = timeseries
            self.tabular = tabular
            self.labels = labels
        else:
            indices = np.arange(len(labels))
            train_idx, val_idx = train_test_split(
                indices,
                test_size=val_split,
                random_state=random_state
            )

            if split == 'train':
                self.images = images[train_idx]
                self.timeseries = timeseries[train_idx]
                self.tabular = tabular[train_idx]
                self.labels = labels[train_idx]
            elif split == 'val':
                self.images = images[val_idx]
                self.timeseries = timeseries[val_idx]
                self.tabular = tabular[val_idx]
                self.labels = labels[val_idx]

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        img = torch.tensor(self.images[idx])
        ts  = torch.tensor(self.timeseries[idx])
        tab = torch.tensor(self.tabular[idx])
        y   = torch.tensor(self.labels[idx])
        return img, ts, tab, y
