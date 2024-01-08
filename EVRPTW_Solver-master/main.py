import functools
import timeit
import numpy as np
import matplotlib.pyplot as plt
from os import listdir

from evrptw_meta import VariableNeighbourhoodSearch, SimulatedAnnealing
from evrptw_solver import EVRPTWSolver
from evrptw_utilities import load_problem_instance, load_solution, write_solution_to_file, write_solution_stats_to_file, \
    write_meta_heuristic_result_statistic_to_file
from heuristics.construction.beasley_heuristic import BeasleyHeuristic, k_nearest_neighbor_min_due_date, \
    k_nearest_neighbor_min_ready_time, nearest_neighbor_tolerance_min_due_date, \
    nearest_neighbor_tolerance_min_ready_time

RESULT_STATISTICS_FILENAME = 'ex1_result_1126205.csv'
RESULT_STATISTICS_LATEX_TABLE = 'ex1_result_1126205.tex'

MAX_ITERATIONS = 10


def main():
    # best_score, best_heuristic, best_param = find_best_heuristic_setting_experiment()

    # CACHING OF BEST RESULTS
    best_score = 0
    best_heuristic = nearest_neighbor_tolerance_min_ready_time
    best_param = 1.8

    print("The best score of {0} was achieved with {1} and parameter {2}".format(best_score, best_heuristic,
                                                                                 round(best_param, 2)))

    print()
    print("============================================")
    print("Generate initial solutions...")
    print("============================================")
    print()

    construction_heuristic = BeasleyHeuristic(best_heuristic, [best_param])
    test_case_statistics = []
    solver = EVRPTWSolver(construction_heuristic)
    for file in listdir('_problem_instances/exercise_instances/'):
        if file.endswith('.txt'):
            print('process file {0}'.format(file))
            print('load problem instance...')
            problem_instance = load_problem_instance('_problem_instances/exercise_instances/' + file)
            print('generate routes...')
            duration = timeit.timeit(functools.partial(solver.solve, problem_instance), number=1) * 1000
            distance, solution = solver.solve(problem_instance)
            test_case_statistics.append((file, distance, duration))
            print('write results to file ...')
            write_solution_to_file("_problem_solutions/solution_{0}".format(file), distance, solution)
            print()

            test_case_statistics.sort(key=lambda x: x[0])
            write_solution_stats_to_file(RESULT_STATISTICS_FILENAME, test_case_statistics)
            write_solution_stats_to_file(RESULT_STATISTICS_LATEX_TABLE, test_case_statistics, style='latex')

    print()
    print("============================================")
    print("Apply meta-heuristic to improve solutions...")
    print("============================================")
    print()

    dist_statistic = dict()
    time_statistic = dict()

    for file in listdir('_problem_instances/exercise_instances/'):
        if file.endswith('.txt'):

            print("process file {0}".format(file))
            problem_instance = load_problem_instance('_problem_instances/exercise_instances/' + file)
            distance, solution = load_solution('_problem_solutions/solution_{0}'.format(file))

            print('start to improve the routes...')

            dist_statistic[file] = []
            time_statistic[file] = []
            for i in range(0, MAX_ITERATIONS):
                meta_heuristic = SimulatedAnnealing(problem_instance, solution, distance, 0.5, 0.8, '{0}_{1}'.format(file,i))
                new_distance, new_solution = meta_heuristic.improve_solution()

                duration = timeit.timeit(meta_heuristic.improve_solution, number=1)

                time_statistic[file].append(duration)
                dist_statistic[file].append(new_distance)

                print('solution improved by {0}'.format(distance - new_distance))

            print("write results to file...")
            write_solution_to_file("_meta_solutions/solution_{0}_{1}".format(i, file), new_distance, new_solution)
            print()

    write_meta_heuristic_result_statistic_to_file('meta_heuristic_results.csv',dist_statistic,time_statistic)

    print("done")


def find_best_heuristic_setting_experiment():
    print('NN tolerance heuristic with min due date:')
    print('================================')
    print('tolerance; average score')
    best_param = -1
    best_heuristic = None
    best_score = 0

    nnt_deadline_results = []
    nnt_readytime_results = []
    knn_deadline_results = []
    knn_readytime_results = []

    for tolerance in np.arange(1, 3, 0.1):
        distances = []
        construction_heuristic = BeasleyHeuristic(nearest_neighbor_tolerance_min_due_date, [round(tolerance, 2)])
        test_case_statistics = []
        solver = EVRPTWSolver(construction_heuristic)

        for file in listdir('_problem_instances/exercise_instances/'):
            if file.endswith('.txt'):
                problem_instance = load_problem_instance('_problem_instances/exercise_instances/' + file)
                distance, solution = solver.solve(problem_instance)
                distances.append(distance)

        if best_score == 0 or best_score > np.mean(distances):
            best_score = np.mean(distances)
            best_heuristic = nearest_neighbor_tolerance_min_due_date
            best_param = round(tolerance, 2)

        nnt_deadline_results.append(np.mean(distances))
        print("{0:.2f}; {1:.2f}".format(tolerance, np.mean(distances)))

    print('NN tolerance heuristic with min ready time:')
    print('================================')
    print('tolerance; average score')

    for tolerance in np.arange(1, 3, 0.1):
        distances = []
        construction_heuristic = BeasleyHeuristic(nearest_neighbor_tolerance_min_ready_time, [round(tolerance, 2)])
        solver = EVRPTWSolver(construction_heuristic)

        for file in listdir('_problem_instances/exercise_instances/'):
            if file.endswith('.txt'):
                problem_instance = load_problem_instance('_problem_instances/exercise_instances/' + file)

                distance, solution = solver.solve(problem_instance)
                write_solution_to_file("_problem_solutions/solution_{0}".format(file), distance, solution)
                distances.append(distance)

        if best_score == 0 or best_score > np.mean(distances):
            best_score = np.mean(distances)
            best_heuristic = nearest_neighbor_tolerance_min_ready_time
            best_param = round(tolerance, 2)

        nnt_readytime_results.append(np.mean(distances))
        print("{0:.2f}; {1:.2f}".format(tolerance, np.mean(distances)))

    plt.title('NN heuristic with tolerance')
    deadline, = plt.plot(np.arange(1, 3, 0.1), nnt_deadline_results, label='deadline minimized')
    readytime, = plt.plot(np.arange(1, 3, 0.1), nnt_readytime_results, label='readytime minimized')
    plt.xlabel('tolerance')
    plt.ylabel('average score')
    plt.legend([deadline, readytime], ['deadline minimized', 'readytime minimized'])
    plt.show()

    print('kNN heuristic with min due date:')
    print('================================')
    print('k; average score')
    for k in range(1, 10):
        distances = []
        construction_heuristic = BeasleyHeuristic(k_nearest_neighbor_min_due_date, [round(k, 2)])
        solver = EVRPTWSolver(construction_heuristic)

        for file in listdir('_problem_instances/exercise_instances/'):
            if file.endswith('.txt'):
                problem_instance = load_problem_instance('_problem_instances/exercise_instances/' + file)

                distance, solution = solver.solve(problem_instance)
                write_solution_to_file("_problem_solutions/solution_{0}".format(file), distance, solution)
                distances.append(distance)

        if best_score == 0 or best_score > np.mean(distances):
            best_score = np.mean(distances)
            best_heuristic = k_nearest_neighbor_min_due_date
            best_param = k

        knn_deadline_results.append(np.mean(distances))
        print("{0:.2f}; {1:.2f}".format(k, np.mean(distances)))

    print('kNN heuristic with min ready time:')
    print('================================')
    print('k; average score')
    for k in range(1, 10):
        distances = []
        construction_heuristic = BeasleyHeuristic(k_nearest_neighbor_min_ready_time, [round(k, 2)])
        solver = EVRPTWSolver(construction_heuristic)

        for file in listdir('_problem_instances/exercise_instances/'):
            if file.endswith('.txt'):
                problem_instance = load_problem_instance('_problem_instances/exercise_instances/' + file)
                distance, solution = solver.solve(problem_instance)
                write_solution_to_file("_problem_solutions/solution_{0}".format(file), distance, solution)
                distances.append(distance)

        if best_score == 0 or best_score > np.mean(distances):
            best_score = np.mean(distances)
            best_heuristic = k_nearest_neighbor_min_ready_time
            best_param = k

        knn_readytime_results.append(np.mean(distances))
        print("{0:.2f}; {1:.2f}".format(k, np.mean(distances)))

    plt.title('kNN heuristic')
    deadline, = plt.plot(range(1, 10), knn_deadline_results, label='deadline minimized')
    readytime, = plt.plot(range(1, 10), knn_readytime_results, label='readytime minimized')
    plt.xlabel('k')
    plt.ylabel('average score')
    plt.legend([deadline, readytime], ['deadline minimized', 'readytime minimized'])
    plt.show()

    return best_score, best_heuristic, best_param


if __name__ == "__main__":
    main()
