# Python Experiment Containers

[![miolab](https://circleci.com/gh/miolab/python_experiment_containers.svg?style=shield)](https://github.com/miolab/python_experiment_containers)

Python 試験実装用リポジトリ（主に機械学習用）

---

## :car: Usage

#### セットアップ

```
git clone https://github.com/miolab/python_experiment_containers.git

cd python_experiment_containers.git

docker-compose build
```

#### 起動

```
docker-compose up
```

- 自動化テスト起動

  ```
  docker-compose run --rm app ptw
  ```

- ターミナルで直接実行

  例

  ```
  docker-compose run --rm app python app_pytorch/pytorch_example.py
  ```

- JupyterLab をブラウザ起動実行

  ブラウザで `localhost:8889/lab`

---

## :book: Reference

#### PyTorch (Official) https://pytorch.org/

- Get Started https://pytorch.org/get-started/locally/

- Tutorial https://pytorch.org/tutorials/index.html

  - Deep Learning with PyTorch: A 60 Minute Blitz https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html

  - Learning PyTorch with Examples https://pytorch.org/tutorials/beginner/pytorch_with_examples.html

#### PyPl

- [torch (PyTorch)](https://pypi.org/project/torch/)

- [torchvision](https://pypi.org/project/torchvision/)

- [JupyterLab](https://pypi.org/project/jupyterlab/)

- [NumPy](https://pypi.org/project/numpy/)

- [Pandas](https://pypi.org/project/pandas/)

- [Matplotlib](https://pypi.org/project/matplotlib/)

- [Seaborn](https://pypi.org/project/seaborn/)

## :pen: Note

- 本リポジトリは、[miolab/jupyterlab_poetry](https://github.com/miolab/jupyterlab_poetry) をベースにしたスピンオフ版です（機械学習に特化）

- 検証ローカル環境: **MacOS**
