from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView, Response

from parsears.serializers import DocumentsSerializer


class ViewUpload(APIView):
    parser_classes = [FileUploadParser]
    
    def post(self, request, filename, format=None):
        
        file = request.FILES["file"].read().decode().split("\n")
        getArrFile = []
        for item in file:
            print(item)
            
            serializer = DocumentsSerializer( 
                data={"type": item[0],  
                      "date": item[1:9], 
                      "value": item[9:19], 
                      "cpf": item[19:30], 
                      "card": item[30:42], 
                      "hour": item[42:48], 
                      "owner_store": item[48:62], 
                      "name_store": item[62:81]})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            
            getArrFile = [serializer.data] + getArrFile
            
            
        return Response(data=getArrFile, status=200)
