from wallflower.serializers import UserSerializer

# defining cutom JWT response payload handler that includes user's serialized data.
# this adds a new user field so that users can receive their data along with their token.

def my_jwt_response_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }