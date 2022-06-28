from django.shortcuts import render, get_object_or_404
from .models import Board

def index(request):
    """
    downloads 목록 출력
    """
    board_list = Board.objects.order_by('-create_date')
    context = {'board_list': board_list}
    return render(request, 'downloads/board_list.html', context)

def detail(request, board_id):
    """
    downloads 내용 출력
    """
    # board = Board.objects.get(id=board_id)
    board = get_object_or_404(Board, pk=board_id)
    context = {'board': board}
    return render(request, 'downloads/board_detail.html', context)