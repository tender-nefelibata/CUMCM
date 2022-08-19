import numpy
import pygad

# find a solution of y = f(w1:w6) = w1x1 + w2x2 + w3x3 + w4x4 + w5x5 + 6wx6
# where (x1,x2,x3,x4,x5,x6)=(4,-2,3.5,5,-11,-4.7) and y=44


function_inputs = [4,-2,3.5,5,-11,-4.7]
desired_output = 44

def fitness_func(solution, solution_idx):
    output = numpy.sum(solution*function_inputs)
    fitness = 1.0 / numpy.abs(output - desired_output)
    return fitness

fitness_function = fitness_func

num_generations = 50
num_parents_mating = 4

sol_per_pop = 8
num_genes = len(function_inputs)

init_range_low = -2
init_range_high = 5

parent_selection_type = "sss"
keep_parents = 1

crossover_type = "single_point"

mutation_type = "random"
mutation_percent_genes = 20 

# Trace the execution of the genetic algorithm.
def callback_generation(ga_instance):
    global last_fitness
    print("Generation = {generation}".format(generation = ga_instance.generations_completed))
    print("Fitness    = {fitness}".format(fitness = ga_instance.best_solution()[1]))
    print("Change     = {change}".format(change = ga_instance.best_solution()[1] - last_fitness))
    last_fitness = ga_instance.best_solution()[1]

ga_instance = pygad.GA(num_generations = num_generations,
        num_parents_mating=num_parents_mating,
        fitness_func = fitness_function,
        sol_per_pop=sol_per_pop,
        num_genes=num_genes,
        init_range_low=init_range_low,
        init_range_high=init_range_high,
        parent_selection_type=parent_selection_type,
        keep_parents=keep_parents,
        crossover_type=crossover_type,
        mutation_type=mutation_type,
        mutation_percent_genes=mutation_percent_genes)


ga_instance.run()

# After the generations complete, some plots are showed that summarize how the outputs/fitenss values evolve over generations.
ga_instance.plot_fitness()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

prediction = numpy.sum(numpy.array(function_inputs)*solution)
print("Predicted output based on the best solution : {prediction}".format(prediction=prediction))
