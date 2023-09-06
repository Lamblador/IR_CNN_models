IrResnet4(
  (conv1): Conv1d(3, 72, kernel_size=(3,), stride=(2,), padding=(1,))
  (bn1): BatchNorm1d(72, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
  (relu): ReLU()
  (layer1): Sequential(
    (0): BasicBlock(
      (conv1): Conv1d(72, 72, kernel_size=(3,), stride=(1,), padding=(1,))
      (bn1): BatchNorm1d(72, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      (relu): ReLU()
      (conv2): Conv1d(72, 72, kernel_size=(3,), stride=(1,), padding=(1,))
      (bn2): BatchNorm1d(72, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    )
    (1): BasicBlock(
      (conv1): Conv1d(72, 72, kernel_size=(3,), stride=(1,), padding=(1,))
      (bn1): BatchNorm1d(72, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      (relu): ReLU()
      (conv2): Conv1d(72, 72, kernel_size=(3,), stride=(1,), padding=(1,))
      (bn2): BatchNorm1d(72, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    )
    (2): BasicBlock(
      (conv1): Conv1d(72, 72, kernel_size=(3,), stride=(1,), padding=(1,))
      (bn1): BatchNorm1d(72, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      (relu): ReLU()
      (conv2): Conv1d(72, 72, kernel_size=(3,), stride=(1,), padding=(1,))
      (bn2): BatchNorm1d(72, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    )
  )
  (layer3): Sequential(
    (0): BasicBlock(
      (conv1): Conv1d(72, 144, kernel_size=(3,), stride=(2,), padding=(1,))
      (bn1): BatchNorm1d(144, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      (relu): ReLU()
      (conv2): Conv1d(144, 144, kernel_size=(3,), stride=(1,), padding=(1,))
      (bn2): BatchNorm1d(144, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      (downsample): Sequential(
        (0): Conv1d(72, 144, kernel_size=(1,), stride=(2,))
        (1): BatchNorm1d(144, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      )
    )
    (1): BasicBlock(
      (conv1): Conv1d(144, 144, kernel_size=(3,), stride=(1,), padding=(1,))
      (bn1): BatchNorm1d(144, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      (relu): ReLU()
      (conv2): Conv1d(144, 144, kernel_size=(3,), stride=(1,), padding=(1,))
      (bn2): BatchNorm1d(144, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    )
    (2): BasicBlock(
      (conv1): Conv1d(144, 144, kernel_size=(3,), stride=(1,), padding=(1,))
      (bn1): BatchNorm1d(144, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      (relu): ReLU()
      (conv2): Conv1d(144, 144, kernel_size=(3,), stride=(1,), padding=(1,))
      (bn2): BatchNorm1d(144, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    )
  )
  (layer5): Sequential(
    (0): BasicBlock(
      (conv1): Conv1d(144, 288, kernel_size=(3,), stride=(2,), padding=(1,))
      (bn1): BatchNorm1d(288, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      (relu): ReLU()
      (conv2): Conv1d(288, 288, kernel_size=(3,), stride=(1,), padding=(1,))
      (bn2): BatchNorm1d(288, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      (downsample): Sequential(
        (0): Conv1d(144, 288, kernel_size=(1,), stride=(2,))
        (1): BatchNorm1d(288, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      )
    )
    (1): BasicBlock(
      (conv1): Conv1d(288, 288, kernel_size=(3,), stride=(1,), padding=(1,))
      (bn1): BatchNorm1d(288, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      (relu): ReLU()
      (conv2): Conv1d(288, 288, kernel_size=(3,), stride=(1,), padding=(1,))
      (bn2): BatchNorm1d(288, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    )
    (2): BasicBlock(
      (conv1): Conv1d(288, 288, kernel_size=(3,), stride=(1,), padding=(1,))
      (bn1): BatchNorm1d(288, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      (relu): ReLU()
      (conv2): Conv1d(288, 288, kernel_size=(3,), stride=(1,), padding=(1,))
      (bn2): BatchNorm1d(288, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    )
  )
  (max3): MaxPool1d(kernel_size=3, stride=2, padding=0, dilation=1, ceil_mode=False)
  (layer7): Sequential(
    (0): BasicBlock(
      (conv1): Conv1d(288, 576, kernel_size=(3,), stride=(2,), padding=(1,))
      (bn1): BatchNorm1d(576, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      (relu): ReLU()
      (conv2): Conv1d(576, 576, kernel_size=(3,), stride=(1,), padding=(1,))
      (bn2): BatchNorm1d(576, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      (downsample): Sequential(
        (0): Conv1d(288, 576, kernel_size=(1,), stride=(2,))
        (1): BatchNorm1d(576, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      )
    )
    (1): BasicBlock(
      (conv1): Conv1d(576, 576, kernel_size=(3,), stride=(1,), padding=(1,))
      (bn1): BatchNorm1d(576, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      (relu): ReLU()
      (conv2): Conv1d(576, 576, kernel_size=(3,), stride=(1,), padding=(1,))
      (bn2): BatchNorm1d(576, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    )
    (2): BasicBlock(
      (conv1): Conv1d(576, 576, kernel_size=(3,), stride=(1,), padding=(1,))
      (bn1): BatchNorm1d(576, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      (relu): ReLU()
      (conv2): Conv1d(576, 576, kernel_size=(3,), stride=(1,), padding=(1,))
      (bn2): BatchNorm1d(576, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    )
  )
  (flatten): Flatten(start_dim=1, end_dim=-1)
  (do1): Dropout1d(p=0.5, inplace=False)
  (fc): Linear(in_features=32256, out_features=200, bias=True)
  (do2): Dropout1d(p=0.2, inplace=False)
  (relu1): ReLU()
  (fc1): Linear(in_features=200, out_features=72, bias=True)
)