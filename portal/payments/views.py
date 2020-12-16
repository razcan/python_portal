from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection


def index(request):
    return render(request, 'payments_page.html')


def payments(request):
    results = query_to_dicts("""        
select top 100 DocumentId, SiteId, DocumentNumber, PaymentValue, PaymentDate,PartnerName from vwPayment
        """)
    return render(request, 'payments_page.html', {'results': results})


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
