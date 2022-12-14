# Test run of our enviroment by simply picking a random action.
from CATastrophe import CATastrophe
from stable_baselines3 import DQN
model = DQN.load("./Trained_Models/best_model_DQN")
from PIL import Image
import random
import csv

env = CATastrophe()
obs = env.reset()
env.render()

# Gets total number of actions available
action_length = env.action_space.n

# Test for 200 episodes
episodes = 1000
i = 1

scores = []
obs = env.reset()
while i <= episodes:
    action, _states = model.predict(obs)
    obs, reward, done, info = env.step(action)

    # Save our observation as an image
    # im = Image.fromarray(obs[:, :, 0] * 255)
    # im = im.convert("L")
    # im.save("your_file.jpeg")   

    env.render()

    if done:
        print(f"Episode {i}: {info['score']}")
        scores.append(info['score'])
        obs = env.reset()
        i += 1

print(f"\n-------\nBölümler: {episodes}\nOrtalama: {sum(scores)/len(scores)}\nMaksimum: {max(scores)}\nMinimum: {min(scores)}\n-------")

# Create a csv of scores
with open("scores.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(scores)
