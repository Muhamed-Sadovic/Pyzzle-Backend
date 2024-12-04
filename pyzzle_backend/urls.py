from django.urls import path
from game.views import BestFirstSearchAlgorithm,BFSAlgorithm,AStarAlgorithm

urlpatterns = [
    path('bfs/', BFSAlgorithm.as_view(), name='bfs_algorithm'),
    path('best-first/', BestFirstSearchAlgorithm.as_view(), name='best_first_algorithm'),
    path('a-star/', AStarAlgorithm.as_view(), name='a_star_algorithm'),
]
