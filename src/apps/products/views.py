from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from loguru import logger

from services.scraper.runner import Runner
from apps.products.serializers import ProductModelSerializer
from apps.products.models import ProductsModel


# Create your views here.


class ScrapeView(APIView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        runner: Runner = Runner()
        try:
            keyword = request.data.get("keyword", "")
            page_number = request.data.get("page_number", "1")

            product_data = runner.search_product(
                keyword=keyword, page_number=page_number
            )
            for product in product_data:
                existed_data = ProductsModel.objects.filter(
                    product_link=product["product_link"]
                ).first()
                if existed_data:
                    logger.info("Data Is Existed return data from database")
                    serializer = ProductModelSerializer(data=existed_data)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    logger.info("Data Is Not In Database Saved Scraping data")
                    serializer = ProductModelSerializer(data=product)
                    if serializer.is_valid():
                        logger.info("Saved to database")
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    else:
                        return Response(
                            {"error": "Invalid data"},
                            status=status.HTTP_400_BAD_REQUEST,
                        )

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
