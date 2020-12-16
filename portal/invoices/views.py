from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
from .models import InvoicesList
from itertools import *
from django.db import connection


def index(request):
    return render(request, 'invoices_page.html')


# def invoices(request):
#     return render(request, 'invoices_page.html')


# def invoices(request):
#     with connection.cursor() as cursor:
#         # cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
#         cursor.execute("select  DocumentNumber,	DocumentDate ,TotalPayment ,PartnerName from vwInvoice where PartnerName like 'SUNMEDAIR TRAVEL  TOURISM SERVI'")
#         row = cursor.fetchall()
#         InvoicesList.objects.raw("select  DocumentNumber,	DocumentDate ,TotalPayment ,PartnerName from vwInvoice where PartnerName like 'SUNMEDAIR TRAVEL  TOURISM SERVI'")
#         columns = [col[0] for col in cursor.description]
#         print(columns)
#         print(row)
#         test = [
#             dict(zip(columns, row))
#             for row in cursor.fetchall()
#         ]
#         print(test)
#         return render(request, 'invoices_page.html', {'row': row})

def invoices(request):
    results = query_to_dicts("""
        select top 100  DocumentId,SiteId, DocumentNumber, DocumentDate, DocumentTypeId from Document
        """)
    return render(request, 'invoices_page.html', {'results': results})


def query_to_dicts(query_string, *query_args):
    cursor = connection.cursor()
    cursor.execute(query_string, query_args)
    col_names = [desc[0] for desc in cursor.description]
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        row_dict = dict(zip(col_names, row))
        print(row_dict)
        yield row_dict
    return
