from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import send_sms


class SendSMSView(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        text = data.get('text', '')
        recipients = data.get('recipients', [])

        # Вызываем функцию для отправки SMS
        result = send_sms(text, recipients)

        # Обрабатываем результат (возвращаем HTTP-ответ)
        if result.get('status') == 'success':
            return Response({'status': 'SMS sent successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status': 'Failed to send SMS'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





