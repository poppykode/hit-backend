import random
import string
import datetime
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    else:
        print(pdf.err)
    return None


def StudentNumber(stringLength=3):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    student_number = ''.join(random.choice(letters)
                               for i in range(stringLength))
    date = str(datetime.datetime.today().year)
    SN = 'H' + student_number.upper()+date
    print(date)
    return SN