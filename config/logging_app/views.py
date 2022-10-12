from django.shortcuts import render,HttpResponse
from datetime import datetime
# import logging
import logging
# get instance of logger
logger = logging.getLogger(__name__)

def home_view(request):
    logger.warning(f"home was accessed by {datetime.now().date()}")
    return HttpResponse("Hello World")