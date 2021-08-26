import torch
import torch.nn as nn


class BindingResiduesCNN(nn.Module):
    """ Convolutional neural network for prediction of 3 different types of binding residues (metal, nucleic acids,
    small molecules. Final output is determined by taking the average output probability from 5 different models from
    5 cross-validation runs """

    n_features = 1024
    bottleneck_dim = 128
    n_classes = 3
    dropout_rate = 0.7

    def __init__(self):
        super(BindingResiduesCNN, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv1d(in_channels=self.n_features, out_channels=self.bottleneck_dim, kernel_size=5, stride=1,
                      padding=2),
            nn.ELU(),
            nn.Dropout(self.dropout_rate),

            nn.Conv1d(in_channels=self.bottleneck_dim, out_channels=self.n_classes, kernel_size=5, stride=1,
                      padding=2),
        )

    def forward(self, x):
        # IN: 1024 x L --> 128 x L --> OUT: 3 x L
        x = self.conv1(x)
        return torch.squeeze(x)
