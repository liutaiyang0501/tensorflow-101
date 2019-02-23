# -*- coding: utf-8 -*-

from train import train
from test import test
from predict import predict

# using training function
model = train()

# using testing function
test(model)

# using scoring function
predict(model)
  
