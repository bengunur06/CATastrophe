# CATastrophe
Pekiştirmeli öğrenme ile bir modelin oyunu çözmeye yönelik eğitilmesi hedeflenmektedir. Farklı algoritmaların bu model üzerinde test edilip farklarının ve
etkenlerinin tartışılması planlanmıştır.Günümüzde pek çok farkli alanda karşımıza çıkan yapay zeka uygulamalarından Pekiştirmeli Öğrenmenin nasıl gerçek hayata uygulanabileceği araştırılmıştır.Proje Python programlama dilinde yazılmış olup Pygame, StableBaselines3 gibi çeşitli
modüllerden destek alınarak geliştirilmiştir.

# Pekiştirmeli Öğrenme Uygulamaları
Pekiştirmeli Öğrenmenin temel kavramları şu şekildedir Ajan(agent), bulunduğu
çevre(enviroment) ile etkileşime geçer. Ajan eylemler(actions) gerçekleştirerek farklı
durumların(states) oluştuğu senaryolara gelir. Ajanın amacı aldığı ödül miktarını
arttırmaktır. Ajanın pekiştirmesini sağlayarak en iyi ödülü deneyimleyerek elde
etmesini sağlarız. Bu strateji poliçe(policy) olarak adlandırılır. Projede Tasarladığımız
oyundan örnek vererek kavramları eşleştirecek olursak. Ajan, Ana Karakterdir
Görselde Kedi ile temsil edilmektedir. Çevre ise oyunun içerisinde bulunan ve ajanın
etkileşime geçtiği her objedir. Eylemleri ise ajanın atış yapması, sağa, sola, çapraz
ilerleyerek engellerden kaçınmasıdır. Durumlar ise oyunda ajanın kara alması gereken
her andır.
Pekiştirmeli Öğrenme, Markov karar süreci model kullanmaktadır. Markov karar
süreçlerinin en önemli 3 özelliği; algılama (sensation), eylem (action) ve hedef (goal)[7]
Her bir durum sadece ve sadece bir önceki durumun sonucudur.


![Pekiştirmeli Öğrenme Kavramları Etkileşim Diyagramı](/readmeimg/S3-4-1.png)
Şekil 3.4.1 Pekiştirmeli Öğrenme Kavramları Etkileşim Diyagramı [8]
Bu projede iki ayrı Pekiştirmeli Öğrenme algoritmasının uygulaması gerçekleştirilmiştir.
Bunlar; Yakınsal Poliçe Optimizasyon Algoritmaları (Proximal Policy Optimization
Algorithms)(PPO) ve Derin Pekiştirmeli Q-Öğrenme(Deep Q-Learning)

# Oyun Tasarımı
Oyunu tasarlarken ana karakterin olması önündeki engellere atış yapabileceği ve bu
engellerin karaktere çarpması durumunda ana karakterin oyunu kaybetmesi ile oyunun
sonlanması planlanmıştır. Engellerin ise rastgele bir şekilde ana karaktere doğru
ilerleyerek hareket etmeleri hedeflenmiştir. Ana karakterin davranış seçenekleri
arasında yer değiştirmek ve engellere atış yapmak vardır.
Oyunun hikayesi ise bir Kedinin önüne çıkan balıklara karşı kendini koruması ve onları
gerekirse avlaması gerektiği. Projenin en son karar kılınan hikayesi bu şekildedir.

![Catastrophe](/readmeimg/S1-1-1.png "screenshot of the game")

# Oyunu oynamak ve Pekiştirmeli Öğrenme ile eğitmek 

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
