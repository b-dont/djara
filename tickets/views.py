from django.shortcuts import render, get_object_or_404

from .models import Ticket


def index(request):
    ticket_list = Ticket.objects.order_by("-reported_date")[:5]
    context = {"ticket_list": ticket_list}
    return render(request, "tickets/index.html", context)


def detail(reqest, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    return render(reqest, "tickets/detail.html", {"ticket": ticket})
