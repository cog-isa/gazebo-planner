<h1>Gazebo visualization of mapplanner</h1>

To install this package you need:

1. Download mapplanner library: https://github.com/cog-isa/map-planner.git
2. Checkout to multiMAP branch
3. Install it
4. cd to folder on your PC with this project
5. python3 setup.py install
6. Install Crumb project: http://babel.isa.uma.es/crumb/index.php/category/work/ros-simulator/
7. Load in Gazebo crumb_pick_place.world
8. Start any GazeboAgent task


```python
from mapplanner.mapplanner import MapPlanner

#Example:
if __name__ == '__main__':
   planner = MapPlanner('src/benchmarks/spatial/', '2', gazebo = True,
                    agpath = 'gazeboplanner.CrumbAgent', agtype = 'GazeboAgent')
   solution = planner.searcher()
   
#This lib includes a small kit of test benchmarks. Use them like following:

import pkg_resources

if __name__ == '__main__':
    task_num = '1'
    path_spatial = 'benchmarks/spatial/'
    p_FILE = pkg_resources.resource_filename('mapplanner', path_simple+'task'+task_num+'.pddl')
    domain_load = pkg_resources.resource_filename('mapplanner', path_simple+'domain'+'.pddl')
    path = ''.join([p.strip() + '/' for p in p_FILE.split('/')[:-1]])
    planner = MapPlanner(path, task_num, gazebo = False, is_load=True, LogicType='classic',
                    agpath = 'mapplanner.agent.agent_search', agtype = 'Agent')
    solution = planner.searcher()
```

