from mapplanner.mapplanner import MapPlanner

# This lib includes a small kit of test benchmarks. Use them like following:

import pkg_resources

if __name__ == '__main__':
    task_num = '1'

    path_spatial = 'benchmarks/spatial/'

    p_FILE = pkg_resources.resource_filename('mapplanner', path_spatial + 'task' + task_num + '.json')
    domain_load = pkg_resources.resource_filename('mapplanner', path_spatial + 'domain' + '.json')
    path = ''.join([p.strip() + '/' for p in p_FILE.split('/')[:-1]])
    planner = MapPlanner(path, task_num, gazebo=True, is_load=True,
                         agpath='gazeboplanner.CrumbAgent', agtype='GazeboAgent')
    solution = planner.searcher()