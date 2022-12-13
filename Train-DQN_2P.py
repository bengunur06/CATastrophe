from stable_baselines3 import DQN
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.callbacks import BaseCallback
from stable_baselines3.common.results_plotter import load_results, ts2xy
from stable_baselines3.common import results_plotter
import numpy as np
import matplotlib.pyplot as plt
from CATastrophe import CATastrophe
import os


"""
Bengünur Baş 
17290010 

Bu dosyayı DQN algoritması ile modeli eğitmek için lütfen çalıştırın 

"""


class SaveOnBestTrainingRewardCallback(BaseCallback):

    def __init__(self, check_freq: int, log_dir: str, verbose=1):
        super(SaveOnBestTrainingRewardCallback, self).__init__(verbose)
        self.check_freq = check_freq
        self.log_dir = log_dir
        self.save_path = os.path.join(log_dir, 'best_model_DQN2')
        self.best_mean_reward = -np.inf

    def _init_callback(self) -> None:
        if self.save_path is not None:
            os.makedirs(self.save_path, exist_ok=True)

    def _on_step(self) -> bool:
        if self.n_calls % self.check_freq == 0:

          # Eğitimdeki Ödülü topla
          x, y = ts2xy(load_results(self.log_dir), 'timesteps')
          if len(x) > 0:
              # Ortalama ödül miktarını hesapla her 100 bölüme bir 
              mean_reward = np.mean(y[-50:])
              if self.verbose > 0:
                print("Adım sayısı: {}".format(self.num_timesteps))
                print("En iyi ortalama ödül: {:.2f} - Son bölümün ortalama ödülü: {:.2f}".format(self.best_mean_reward, mean_reward))

              # En iyi modeli kaydet 
              if mean_reward > self.best_mean_reward:
                  self.best_mean_reward = mean_reward
                  if self.verbose > 0:
                    print("En iyi modeli kaydet {}".format(self.save_path))
                  self.model.save(self.save_path)

        return True

# Log için dizin oluştur en iyi modelin kaydı tutulacak 
log_dir = "tmp/"
os.makedirs(log_dir, exist_ok=True)
log_path =os.path.join('Training','Logs')

buffer_size = 100000 #kaydedilen eski bölümler 
learning_starts = 10000 # hafıza alıştırması
train_freq = 1 # prediction network gets an update each train_freq's step
batch_size = 25 # mini batch size drawn at each update step
policy_kwargs = {
        'net_arch': [64,64] # gizli MLP katmanı 
        }
exploration_fraction = 0.1 # Fraction of training steps the epsilon decays 
target_update_interval = 1000 # Target network gets updated each target_update_interval's step
gamma = 0.99
verbose = 1 # verbosity of stable-basline's prints

nb_steps = 500000
# Create environment
env = CATastrophe()
env = Monitor(env, log_dir)
env._max_episode_steps = 5000
# Ajanı oluştur

model = DQN('MlpPolicy', env, buffer_size=buffer_size, learning_starts=learning_starts ,train_freq=train_freq, 
            batch_size=batch_size, gamma=gamma, policy_kwargs=policy_kwargs, 
            exploration_fraction=exploration_fraction, target_update_interval=target_update_interval,
            verbose=verbose,tensorboard_log=log_path)

callback = SaveOnBestTrainingRewardCallback(check_freq=1000, log_dir=log_dir)
model.learn(total_timesteps=nb_steps,callback=callback)



results_plotter.plot_results([log_dir], 100000, results_plotter.X_TIMESTEPS, "CATastrophe DQN")
plt.show()

# Save the agent
model.save("CATModelDQN")