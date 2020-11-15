from gym_miniworld.params import DEFAULT_PARAMS
from gym_miniworld.envs import Maze


class MazeS8(Maze):
    def __init__(self, forward_step=0.7, turn_step=45, max_steps=1500):
        # Parameters for larger movement steps, fast stepping
        params = DEFAULT_PARAMS.no_random()
        params.set('forward_step', forward_step)
        params.set('turn_step', turn_step)

        super().__init__(
            params=params,
            max_episode_steps=max_steps,
            domain_rand=False
        )
