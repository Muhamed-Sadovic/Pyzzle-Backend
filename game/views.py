from rest_framework.views import APIView
from rest_framework.response import Response
from .algorithms.algorithms import bfs_puzzle, best_first_search, a_star_search
from .algorithms.heuristics import hamming_heuristic, manhattan_heuristic

def solve_puzzle(solver_function, start_state, goal_state, *args):
    try:
        result = solver_function(start_state, goal_state, *args)
        return Response({"steps": result, "moves": len(result)}, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=500)

class BFSAlgorithm(APIView):
    def post(self, request):
        start_state = request.data.get("start_state")
        goal_state = request.data.get("goal_state")
        return solve_puzzle(bfs_puzzle, start_state, goal_state)

class BestFirstSearchAlgorithm(APIView):
    def post(self, request):
        start_state = request.data.get("start_state")
        goal_state = request.data.get("goal_state")
        return solve_puzzle(best_first_search, start_state, goal_state, hamming_heuristic)

class AStarAlgorithm(APIView):
    def post(self, request):
        start_state = request.data.get("start_state")
        goal_state = request.data.get("goal_state")
        heuristic_name = request.data.get("heuristic", "hamming")
        heuristic = hamming_heuristic if heuristic_name == "hamming" else manhattan_heuristic
        return solve_puzzle(a_star_search, start_state, goal_state, heuristic)
