from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from wallet.helpers.send_notification_email import send_notification_email

from wallet.serializers import TransactionSerializer, WalletSerializer
from .models import Wallet, Transaction

class WalletBalanceView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    

    def get(self, request):
        wallet = request.user.wallet
        serializer = WalletSerializer(wallet)
        return Response(serializer.data)

class AddBalanceView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        amount = request.data.get('amount')
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Valor inválido.")
            wallet = request.user.wallet
            wallet.add_balance(amount)

            Transaction.objects.create(
                receiver=wallet,
                amount=amount,
                transaction_type=Transaction.TransactionType.ADD_FUNDS,
            )

            serialzer = WalletSerializer(wallet)

            send_notification_email(
                subject="Saldo Adicionado com Sucesso",
                message=f"Você adicionou {amount:.2f} à sua carteira. Saldo atual: {wallet.balance:.2f}.",
                recipient_email=request.user.email,
            )


            return Response({
                'message': 'Saldo adicionado com sucesso.',
                'data': serialzer.data
                })
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class TransferView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        receiver_id = request.data.get('receiver_id')
        amount = request.data.get('amount')
        try:
            receiver = Wallet.objects.get(user_id=receiver_id)
            sender = request.user.wallet
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Valor inválido.")

            sender.deduct_balance(amount)
            receiver.add_balance(amount)

            transaction = Transaction.objects.create(
                sender=sender,
                receiver=receiver,
                amount=amount,
                transaction_type=Transaction.TransactionType.TRANSFER,
            )

        
            # Enviar e-mail para o remetente
            send_notification_email(
                subject="Transferência Realizada",
                message=f"Você transferiu {amount:.2f} para {receiver.user.username}. Saldo atual: {sender.balance:.2f}.",
                recipient_email=request.user.email,
            )

            # Enviar e-mail para o destinatário
            send_notification_email(
                subject="Você Recebeu uma Transferência",
                message=f"Você recebeu {amount:.2f} de {sender.user.username}. Saldo atual: {receiver.balance:.2f}.",
                recipient_email=receiver.user.email,
            )
            serializer = TransactionSerializer(transaction)

            return Response({
                'message': 'Transferência realizada com sucesso.',
                'transaction': serializer.data,

                }
                )
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class TransactionHistoryView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    

    def get(self, request):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        transactions = Transaction.objects.filter(sender=request.user.wallet)
        if start_date and end_date:
            transactions = transactions.filter(timestamp__range=[start_date, end_date])
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)
