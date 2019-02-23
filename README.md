## TensorFlow-101

#### Docker Command

**Build docker image**

```bash
sudo docker build -t orozcohsu/tensorflow-101:v1 .
```

**Run container**

```bash
sudo docker run -i orozcohsu/tensorflow-101:v1 python src/main.py
```

#### Result

```
Training:
Epoch 000: Loss: 1.142, Accuracy: 29.167%
Epoch 050: Loss: 0.569, Accuracy: 78.333%
Epoch 100: Loss: 0.304, Accuracy: 95.833%
Epoch 150: Loss: 0.186, Accuracy: 97.500%
Epoch 200: Loss: 0.134, Accuracy: 98.333%

Testing:
Test set accuracy: 96.667%

Scoring:
Example 0 prediction: Iris setosa
Example 1 prediction: Iris versicolor
Example 2 prediction: Iris virginica
```
