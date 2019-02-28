input_path = 'input/e_shiny_selfies.txt'
from simple_solutions import greedy_solution
import submission

def save_temp_result(slides):
    submission.save_result(input_path, slides)

submission.run_on_one(input_path, greedy_solution, all_horizontal=True, solution_func_kwargs={'callback': save_temp_result, 'callback_score_increment': 1000, 'thresh': 7})
