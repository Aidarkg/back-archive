from datetime import date
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers.visitors import *


class VisitorsAPIView(APIView):
    def get(self, request):
        total_visits = request.session.get('total_visits', 0)
        today_visits = request.session.get('today_visits', 0)

        # Увеличение общего количества посещений и сегодняшних посещений
        request.session['total_visits'] = total_visits + 1

        # Проверка, были ли посещения сегодня, и обновление счетчика посещений за сегодня
        if 'last_visit_date' in request.session and request.session['last_visit_date'] == str(date.today()):
            request.session['today_visits'] = today_visits + 1
        else:
            request.session['today_visits'] = 1

        # Обновление последней даты посещения на сегодняшнюю
        request.session['last_visit_date'] = str(date.today())

        # Подготовка контекста для передачи в шаблон
        serializer = VisitSerializer(data={
            'total_visits': request.session['total_visits'],
            'today_visits': request.session['today_visits'],
        })
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
