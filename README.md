# CATastrophe
Kurulum için miniconda kullanılması tavsiye edilir.Ama zorunlu değildir 
miniconda kurulumu için linkten kullandığınız işletim sistemine uygun sürümü seçiniz ve kurunuz 

[MiniConda Latest Install](https://docs.conda.io/en/latest/miniconda.html)

## Eğer Miniconda kullanarak çalıştıracaksanız ilk 3 adımı uygulayınız: 

#### MiniConda kurulumundan sonra conda alanını oluşturunuz
```
conda create --name test1 
```

#### Oluşturduğunuz alanı aktive ediniz 
```
conda activate test1
```

#### Conda üzerinde GYM modülünü yükleyin Eğer Conda ile kuruluma devam etmiyorsanız pip ile yükleyiniz 
```
conda install -c conda-forge gym-all
pip install gym-all
```


### Stable-Baselines3'ü yükleyiniz 
```
pip install stable-baselines3[extra] 
```

### Pyglet'i yükleyiniz 
```
pip install pyglet 
```

### Tensorflow'u yükleyiniz 
```
pip install tensorflow
```

### Tensorflow-gpu yükleyiniz
```
pip install tensorflow-gpu
```

### Pygame'i yükleyiniz
```
pip install pygame 
``` 
