from typing import NamedTuple, Optional

from django.contrib.auth import get_user_model

from problem.models import ProblemInstance
from .score import calculate_problem_score

User = get_user_model()


class UserProblemInfo(NamedTuple):
    user: User
    problem_instance: ProblemInstance
    solved: bool
    first_solver: Optional[User]
    solver_count: int
    effective_points: int

    def display_first_solve(self):
        return self.first_solver is None or self.user == self.first_solver


def get_user_problem_info(user, problem_instance):
    solved_log = problem_instance.problemauthlog_set \
        .filter(auth_key=problem_instance.problem.auth_key) \
        .order_by('datetime')

    first_solver = solved_log.first().user if solved_log.exists() else None
    solved = solved_log.filter(user=user).exists()
    solve_count = solved_log.count()
    effective_solve_count = solve_count + (0 if solved else 1)
    first_blood = first_solver is None or user == first_solver
    points = calculate_problem_score(problem_instance, effective_solve_count, first_blood)

    return UserProblemInfo(user, problem_instance, solved, first_solver, solve_count, points)


def get_problem_list_info(problem_list, user):
    problem_instances = problem_list.probleminstance_set.all()
    problem_info = []
    user_score = 0
    for problem_instance in problem_instances:
        info = get_user_problem_info(user, problem_instance)
        if info.solved:
            user_score += info.effective_points
        problem_info.append(info)

    return problem_info, user_score