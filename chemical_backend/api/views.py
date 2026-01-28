import pandas as pd
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import EquipmentData

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_history(request):
    try:
        # This filters the data so only the logged-in user (e.g., "ritika") sees their files
        history = EquipmentData.objects.filter(user=request.user).order_by('-uploaded_at')[:5]
        serializer = EquipmentDataSerializer(history, many=True)
        return Response(serializer.data)
    except Exception as e:
        # This prints the actual error in your terminal for debugging
        print(f"History Fetch Error: {e}")
        return Response({"error": "Failed to fetch history"}, status=500)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    
    if not username or not password:
        return Response({"error": "Username and password required"}, status=status.HTTP_400_BAD_REQUEST)
    
    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already taken"}, status=status.HTTP_400_BAD_REQUEST)
    
    user = User.objects.create_user(username=username, password=password, email=email)
    return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_csv(request):
    try:
        file = request.FILES['file']
        df = pd.read_csv(file)

        # Look for any column containing 'temp' or 'press' (case-insensitive)
        temp_col = next((c for c in df.columns if 'temp' in c.lower()), None)
        press_col = next((c for c in df.columns if 'press' in c.lower()), None)

        if not temp_col or not press_col:
            return Response({"error": "CSV must have Temperature and Pressure columns"}, status=400)

        summary = {
            "total_count": len(df),
            "avg_temp": round(df[temp_col].mean(), 2),
            "avg_pressure": round(df[press_col].mean(), 2),
            "rows": df.to_dict(orient='records') # Sends every row to your React table
        }

        # This saves the record specifically to the logged-in user
        EquipmentData.objects.create(user=request.user, filename=file.name)
        
        return Response(summary)
    except Exception as e:
        return Response({"error": str(e)}, status=500)