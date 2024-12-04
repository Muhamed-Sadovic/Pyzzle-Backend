from rest_framework.views import APIView
from rest_framework.response import Response
from .algorithms.algorithms import bfs_puzzle, best_first_search, a_star_search
from .algorithms.heuristics import hamming_heuristic, manhattan_heuristic

class BFSAlgorithm(APIView):
    def post(self, request):
        try:
            start_state = request.data.get("start_state")
            goal_state = request.data.get("goal_state")

            print("Pocetno stanje:", start_state)
            print("Ciljno stanje:", goal_state)

            result = bfs_puzzle(start_state, goal_state)
            if result:
                print("Rešenje pronađeno:", result)
                return Response({"steps": result, "moves": len(result)}, status=200)
            else:
                print("Rešenje nije pronađeno.")
                return Response({"error": "Solution not found"}, status=404)
        except Exception as e:
            print("Greška:", str(e))
            return Response({"error": str(e)}, status=500)

class BestFirstSearchAlgorithm(APIView):
    def post(self, request):
        try:
            start_state = request.data.get("start_state")
            goal_state = request.data.get("goal_state")

            result = best_first_search(start_state, goal_state, hamming_heuristic)
            if result:
                return Response({"steps": result, "moves": len(result)}, status=200)
            else:
                return Response({"error": "Solution not found"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)

class AStarAlgorithm(APIView):
    def post(self, request):
        try:
            start_state = request.data.get("start_state")
            goal_state = request.data.get("goal_state")
            heuristic_name = request.data.get("heuristic", "hamming")

            heuristic = hamming_heuristic if heuristic_name == "hamming" else manhattan_heuristic
            result = a_star_search(start_state, goal_state, heuristic)
            if result:
                return Response({"steps": result, "moves": len(result)}, status=200)
            else:
                return Response({"error": "Solution not found"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)

