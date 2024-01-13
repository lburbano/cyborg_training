# Implementation of the red evaluation script
# This script is used to evaluate the performance of a red agent against a blue agent
# The blue agent is https://github.com/john-cardiff/-cyborg-cage-2.git
# Modified by Prof. H. Sasahara
import inspect
import time
from statistics import mean, stdev

from CybORG import CybORG, CYBORG_VERSION
from CybORG.Agents import B_lineAgent, SleepAgent
from CybORG.Agents.SimpleAgents.Meander import RedMeanderAgent
from Wrappers.ChallengeWrapper2 import ChallengeWrapper2
from Agents.WrappedAgent import WrappedBlueAgent
from Agents.MainAgent import MainAgent
import random

MAX_EPS = 100
agent_name = 'Red'
random.seed(153)


# changed to ChallengeWrapper2
def wrap(env):
    return ChallengeWrapper2(env=env, agent_name=agent_name)

if __name__ == "__main__":
    cyborg_version = CYBORG_VERSION
    scenario = 'Scenario2'
    # commit_hash = get_git_revision_hash()
    

    
    # Load scenario
    path = str(inspect.getfile(CybORG))
    path = path[:-10] + f'/Shared/Scenarios/{scenario}.yaml'
    # Load Red agent

    # Load blue agent
    blue_agent = lambda: WrappedBlueAgent(MainAgent())
    # Set up environment with blue agent running in the background and 
    # red agent as the main agent
    cyborg = CybORG(path, 'sim', agents={'Blue': blue_agent})
    env = ChallengeWrapper2(env=cyborg, agent_name="Red")
    # TODO: load red agent

    for num_steps in [30]:
        observation = env.reset()

        # action_space = wrapped_cyborg.get_action_space(agent_name)
        action_space = cyborg.get_action_space(agent_name)
        total_reward = []
        actions = []
        for i in range(MAX_EPS):
            r = []
            a = []
            # cyborg.env.env.tracker.render()
            for j in range(num_steps):
                action = 1 # TODO: get action from red agent
                observation, rew, done, info = env.step(action)
                # result = cyborg.step(agent_name, action)
                r.append(rew)
                a.append((str(cyborg.get_last_action('Blue')), str(cyborg.get_last_action('Red'))))
                print( str(cyborg.get_last_action('Red')) )
            total_reward.append(sum(r))
            actions.append(a)
            observation = env.reset()