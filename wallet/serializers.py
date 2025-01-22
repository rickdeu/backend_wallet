from rest_framework import serializers
from .models import User, Wallet, Transaction

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Wallet.objects.create(user=user)
        return user

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['id', 'user', 'balance']

class TransactionSerializer(serializers.ModelSerializer):
    sender = WalletSerializer()
    receiver = WalletSerializer()
    transaction_type = serializers.CharField(source="get_transaction_type_display") 
    
    class Meta:
        model = Transaction
        fields = ['id', 'sender', 'receiver', 'amount', 'transaction_type', 'timestamp']
