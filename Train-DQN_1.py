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
        self.save_path = os.path.join(log_dir, 'best_model_DQN')
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

# Ortamı oluştur 
env = CATastrophe()
env = Monitor(env, log_dir)
env._max_episode_steps = 5000
# Ajanı oluştur 
model = DQN('CnnPolicy', env, buffer_size=10000, learning_rate=1e-4, learning_starts=10000, 
train_freq=4, exploration_final_eps=0.01, exploration_fraction=0.1,tensorboard_log=log_path)
callback = SaveOnBestTrainingRewardCallback(check_freq=1000, log_dir=log_dir)
# Ajanı eğit 

model.learn(total_timesteps=1000000, callback=callback)

results_plotter.plot_results([log_dir], 100000, results_plotter.X_TIMESTEPS, "CATastrophe DQN")
plt.show()

# Save the agent
model.save("CATModelDQN")